import { Stack, Typography } from "@mui/material";
import { useState } from "react";
import "./App.css";
import { ConfigForm } from "./components/ConfigForm";
import { Plot } from "./components/Plot";

function App() {
  const [process_id, set_process_id] = useState(null);
  const [loading, set_loading] = useState(false);

  const startProcess = (values) =>       {
    set_loading(true)
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(values, null, 2),
  };
  fetch("http://localhost:8000/assumptions", requestOptions)
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
    }).catch((err) => console.warn(err));}

  return (
    <Stack
      spacing={12}
      alignItems="center"
      justifyContent="center"
      style={{ minHeight: "100vh" }}
    >
      <Typography variant="h1">Obliczenia Ewolucyjne</Typography>
      {!loading && (
        <ConfigForm startProcess={(values) => startProcess(values)}/>
      )}
      {loading && <Plot process_id={process_id} />}
    </Stack>
  );
}

export default App;
