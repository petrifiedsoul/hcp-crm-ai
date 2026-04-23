import Chat from "./components/Chat";
import LogForm from "./components/LogForm";

function App() {
  return (
    <div style={{ display: "flex", height: "100vh", padding: "10px" }}>
      {/* LEFT FORM */}
      <div style={{ flex: 2, padding: "10px" }}>
        <LogForm />
      </div>

      {/* RIGHT CHAT */}
      <div style={{ flex: 1, padding: "10px" }}>
        <Chat />
      </div>
    </div>
  );
}

export default App;