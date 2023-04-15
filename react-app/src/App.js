import { Stack, Typography } from "@mui/material";
import { useState } from "react";
import "./App.css";
import { ConfigForm } from "./components/ConfigForm";
import { Plot } from "./components/Plot";

function App() {
  const [process_id, set_process_id] = useState(null);

  return (
    <Stack
      spacing={12}
      alignItems="center"
      justifyContent="center"
      style={{ minHeight: "100vh" }}
    >
      <Typography variant="h1">Obliczenia Ewolucyjne</Typography>
      {process_id === null && (
        <ConfigForm set_process_id={(id) => set_process_id(id)} />
      )}
      {process_id !== null && <Plot process_id={process_id} />}
    </Stack>
  );
}

export default App;
