import MenuUploadForm from "../components/MenuUploadForm";

export default function AdminPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 flex items-center justify-center p-4">
      <div className="w-full max-w-lg bg-slate-900 rounded-2xl shadow-soft p-6">
        <h1 className="text-white text-xl font-semibold mb-1">
          🏪 Restaurant Admin
        </h1>
        <p className="text-slate-400 text-sm mb-6">
          Upload your menu so the AI can assist customers.
        </p>

        <MenuUploadForm />
      </div>
    </div>
  );
}
