import { useEffect, useState } from "react";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
  const [txt, setTxt] = useState("cargando…");

  useEffect(() => {
    fetch(`${API}/api/avance`)
      .then((r) => r.json())
      .then((j) => setTxt(JSON.stringify(j, null, 2)))
      .catch((e) => setTxt("error: " + String(e)));
  }, []);

  return (
    <div style={{ fontFamily: "monospace", padding: 16 }}>
      <p>GET {API}/api/avance</p>
      <pre style={{ whiteSpace: "pre-wrap" }}>{txt}</pre>
    </div>
  );
}
