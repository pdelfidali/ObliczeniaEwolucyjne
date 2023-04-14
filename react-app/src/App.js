import { Stack, Typography } from "@mui/material";
import { useState } from "react";
import "./App.css";
import { ConfigForm } from "./components/ConfigForm";
import { Plot } from "./components/Plot";
import { Progress } from "./components/Progress";

function App() {
  const [process_id, set_process_id] = useState(null);
  const [process_finished, set_process_finished] = useState(false);
  const [plot_path, set_plot_path] = useState(null);

  return (
    <Stack
      spacing={12}
      alignItems="center"
      justifyContent="center"
      style={{ minHeight: "100vh" }}
    >
      <Typography variant="h1">Obliczenia Ewolucyjne</Typography>
      {process_id === null && !process_finished && (
        <ConfigForm set_process_id={(id) => set_process_id(id)} />
      )}
      {process_id !== null && !process_finished && (
        <Progress
          process_id={process_id}
          set_process_finished={() => set_process_finished(true)}
        />
      )}
      {process_finished && <Plot filename={"68baa72c-ef2a-45d8-923b-8c8f5724b794.png"} />}
    </Stack>
  );
}

export default App;
