import { useState, useRef, useEffect } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import TypingIndicator from "./TypingIndicator";
import DishCard from "./DishCard";
import QuickActions from "./QuickActions";
import { sendMessage } from "../services/chatApi";

export default function ChatWindow() {
  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      text: "Hi 👋 Welcome! What are you in the mood for today?",
      type: "message",
    },
  ]);

  const [sessionId, setSessionId] = useState(null);
  const [isTyping, setIsTyping] = useState(false);
  const [quickActions, setQuickActions] = useState([
    { label: "🍃 Vegetarian", value: "vegetarian" },
    { label: "🍗 Non-Vegetarian", value: "non-vegetarian" },
  ]);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isTyping, quickActions]);

  async function handleSend(text) {
    // Remove buttons once user responds
    setQuickActions([]);

    setMessages((prev) => [...prev, { sender: "user", text }]);
    setIsTyping(true);

    try {
      const res = await sendMessage({
        message: text,
        sessionId,
      });

      if (!sessionId) setSessionId(res.session_id);

      // ✅ KEY FIX: Replace old recommendations
      setMessages((prev) => {
        const cleaned =
          res.type === "recommendation"
            ? prev.filter((m) => m.type !== "recommendation")
            : prev;

        return [
          ...cleaned,
          {
            sender: "assistant",
            text: res.reply,
            type: res.type,
          },
        ];
      });

      // 🎯 Decide next buttons (UI-only logic)
      if (res.type === "message") {
        if (res.reply.includes("vegetarian or non-veg")) {
          setQuickActions([
            { label: "🍃 Vegetarian", value: "vegetarian" },
            { label: "🍗 Non-Vegetarian", value: "non-vegetarian" },
          ]);
        } else if (
          res.reply.includes("spice") ||
          res.reply.includes("budget")
        ) {
          setQuickActions([
            { label: "🌶 Spicy", value: "spicy" },
            { label: "😌 Mild", value: "mild" },
            { label: "💸 Under ₹250", value: "under 250" },
          ]);
        }
      }
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: "⚠️ Sorry, something went wrong. Please try again.",
          type: "message",
        },
      ]);
    } finally {
      setIsTyping(false);
    }
  }

  return (
    <>
      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {messages.map((msg, idx) => {
          if (msg.sender === "assistant" && msg.type === "recommendation") {
            const dishes = msg.text
              .split("\n")
              .filter((l) => l.includes("₹"))
              .map((line) => {
                const [name, price] = line.split("₹");
                return {
                  name: name.replace("-", "").trim(),
                  price: price.trim(),
                  tags: ["recommended"],
                };
              });

            return (
              <div key={idx} className="space-y-2">
                {dishes.map((d, i) => (
                  <DishCard key={i} {...d} />
                ))}
              </div>
            );
          }

          return (
            <MessageBubble
              key={idx}
              sender={msg.sender}
              text={msg.text}
            />
          );
        })}

        <QuickActions actions={quickActions} onSelect={handleSend} />

        {isTyping && <TypingIndicator />}
        <div ref={bottomRef} />
      </div>

      <ChatInput onSend={handleSend} disabled={isTyping} />
    </>
  );
}
