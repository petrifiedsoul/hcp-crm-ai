import { useState } from "react";
import { TextField, Button, Paper, Typography } from "@mui/material";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { updateForm } from "../store/interactionSlice";

function Chat(){
  const dispatch = useDispatch();
  const formData = useSelector((state) => state.interaction.formData);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const newMessages = [...messages, { role: "user", text: message }];
    setMessages(newMessages);
    setMessage("");
    setIsLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message,
        current_state: formData
      });

      const output = res.data;

      // 🔥 THE FIX: Properly extract the 'structured' JSON from the backend tool 🔥
      if (output.data && output.data.structured) {
        dispatch(updateForm(output.data.structured));
      } else if (output.data) {
        dispatch(updateForm(output.data)); // Fallback just in case
      }

      setMessages([
        ...newMessages,
        { role: "ai", text: output.reply }
      ]);

    } catch (err) {
      console.error(err);
      setMessages([...newMessages, { role: "ai", text: "Error connecting to server." }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Paper elevation={2} style={{ padding: "20px", height: "100%", display: "flex", flexDirection: "column", borderRadius: "10px" }}>
      <Typography variant="h6" style={{ fontWeight: 600 }}>🌐 AI Assistant</Typography>

      <div style={{ flex: 1, overflowY: "auto", marginTop: "10px", paddingBottom: "10px" }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.role === "user" ? "right" : "left", margin: "8px 0" }}>
            <div style={{
                background: msg.role === "user" ? "#1976d2" : "#f1f3f5",
                color: msg.role === "user" ? "white" : "black",
                padding: "10px 14px", borderRadius: "12px", display: "inline-block", maxWidth: "85%",
                fontFamily: "inherit", fontSize: "0.95rem"
              }}>
              {msg.text}
            </div>
          </div>
        ))}
        {isLoading && <Typography variant="caption" style={{ color: "gray" }}>AI is thinking...</Typography>}
      </div>

      <div style={{ display: "flex", gap: "10px", marginTop: "auto" }}>
        <TextField fullWidth size="small" placeholder="Describe interaction..." value={message} onChange={(e) => setMessage(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && sendMessage()} />
        <Button variant="contained" onClick={sendMessage} style={{ textTransform: "none", background: "#1976d2" }}>Log</Button>
      </div>
    </Paper>
  );
}

export default Chat;