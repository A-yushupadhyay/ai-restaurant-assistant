import { useState } from "react";

export default function MenuUploadForm() {
  const [menuJson, setMenuJson] = useState("");
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const restaurantId = "spice-garden-001"; // static for now

  // 🔹 Existing JSON upload (UNCHANGED)
  async function handleUploadJson() {
    try {
      setLoading(true);
      setStatus(null);

      let parsed = JSON.parse(menuJson);
       if (!Array.isArray(parsed)) {
          parsed = [parsed];
        }

      const res = await fetch(
        `http://localhost:8000/restaurant/${restaurantId}/menu`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(parsed),
        }
      );

      if (!res.ok) throw new Error("Upload failed");

      setStatus("✅ Menu uploaded successfully (JSON)");
      setMenuJson("");
    } catch (err) {
      console.error("Error uploading menu:", err);
      setStatus("❌ Invalid JSON or server error");
    } finally {
      setLoading(false);
    }
  }

  // 🔹 NEW: PDF / Image upload via OCR (SAFE ADDITION)
  async function handleFileUpload(file) {
    if (!file) return;

    try {
      setLoading(true);
      setStatus(null);

      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch(
        `http://localhost:8000/restaurant/${restaurantId}/menu/ocr`,
        {
          method: "POST",
          body: formData,
        }
      );

      if (!res.ok) throw new Error("OCR upload failed");

      setStatus("✅ Menu uploaded successfully (PDF / Image)");
    } catch (err) {
      console.error("Error uploading file:", err);
      setStatus("❌ Failed to process menu file");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-5">
      {/* JSON UPLOAD (EXISTING) */}
      <div className="space-y-2">
        <label className="block text-slate-300 text-sm">
          Paste Menu JSON
        </label>

        <textarea
          rows={10}
          value={menuJson}
          onChange={(e) => setMenuJson(e.target.value)}
          placeholder={`[
  {
    "id": 1,
    "name": "Paneer Tikka",
    "price": 220,
    "diet": "vegetarian",
    "taste": ["spicy"],
    "health_flags": ["diabetic-friendly"],
    "ingredients": ["paneer", "spices"]
  }
]`}
          className="w-full bg-slate-800 text-slate-100 rounded-xl p-3 text-sm outline-none
                     focus:ring-2 focus:ring-green-500 transition"
        />

        <button
          onClick={handleUploadJson}
          disabled={loading}
          className="w-full bg-green-500 text-black font-semibold py-2 rounded-xl
                     hover:opacity-90 transition disabled:opacity-50"
        >
          {loading ? "Uploading..." : "Upload Menu (JSON)"}
        </button>
      </div>

      {/* 🔥 NEW: FILE UPLOAD (PDF / IMAGE) */}
      <div className="border-t border-slate-700 pt-4 space-y-2">
        <label className="block text-slate-300 text-sm">
          Upload Menu PDF / Image
        </label>

        <input
          type="file"
          accept=".pdf,image/*"
          onChange={(e) => handleFileUpload(e.target.files[0])}
          className="w-full text-slate-300 text-sm
                     file:bg-slate-700 file:text-white
                     file:border-0 file:rounded-lg
                     file:px-4 file:py-2
                     file:cursor-pointer
                     hover:file:bg-slate-600 transition"
        />
      </div>

      {status && (
        <p className="text-sm text-slate-300 mt-2">
          {status}
        </p>
      )}
    </div>
  );
}
