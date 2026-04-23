import { TextField, Typography, Paper, Divider } from "@mui/material";
import { useSelector } from "react-redux";

function LogForm() {
  // Pulling formData from Redux instead of props
  const formData = useSelector((state) => state.interaction.formData);

  return (
    <Paper elevation={2} style={{ padding: "25px", borderRadius: "10px", height: "100%" }}>
      <Typography variant="h5" style={{ fontWeight: 600 }}>
        Log HCP Interaction
      </Typography>

      <Divider style={{ margin: "20px 0" }} />

      <Typography variant="subtitle1">Interaction Details</Typography>
      <TextField label="HCP Name" value={formData.hcpName || ""} fullWidth margin="normal" size="small" />
      
      {/* Changed product to topics to match backend JSON */}
      <TextField label="Topics Discussed" value={formData.topics || ""} fullWidth multiline rows={3} margin="normal" size="small" />

      <Divider style={{ margin: "20px 0" }} />

      <Typography variant="subtitle1">HCP Sentiment</Typography>
      <TextField label="Sentiment" value={formData.sentiment || ""} fullWidth margin="normal" size="small" />

      <Divider style={{ margin: "20px 0" }} />

      <Typography variant="subtitle1">Additional Info</Typography>
      <TextField label="Date" value={formData.date || ""} fullWidth margin="normal" size="small" />
      <TextField label="Materials Shared" value={formData.materials || ""} fullWidth margin="normal" size="small" />
    </Paper>
  );
}

export default LogForm;