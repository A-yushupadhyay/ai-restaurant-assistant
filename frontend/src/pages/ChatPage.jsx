import ChatWindow from "../components/ChatWindow";
import RestaurantHeader from "../components/RestaurantHeader";

export default function ChatPage() {
  return (
    <div className="h-screen w-full bg-gradient-to-br from-slate-900 to-slate-800 flex items-center justify-center">
      <div className="w-full max-w-md h-full md:h-[90vh] bg-slate-900 rounded-none md:rounded-2xl shadow-soft flex flex-col">
        {/* ✅ Restaurant identity header */}
        <RestaurantHeader />

        {/* ✅ Chat remains unchanged */}
        <ChatWindow />
      </div>
    </div>
  );
}
