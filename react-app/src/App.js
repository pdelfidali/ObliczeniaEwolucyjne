import { Button, Stack, Typography } from "@mui/material";
import { useState } from "react";
import "./App.css";
import { ConfigForm } from "./components/ConfigForm/ConfigForm";
import { History } from "./components/History";
import { Plot } from "./components/Plot";

function App() {
  const [new_algo, set_new_algo] = useState(false);
  const [history, set_history] = useState(false);
  const [process_id, set_process_id] = useState(null);

  const startProcess = (values) => {
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(values, null, 2),
    };
    set_new_algo(false);
    fetch("http://localhost:8000/assumptions", requestOptions);
  };

  return (
    <Stack
      spacing={12}
      alignItems="center"
      justifyContent="center"
      style={{ minHeight: "100vh" }}
    >
      <Typography variant="h1">Obliczenia Ewolucyjne</Typography>
      {process_id === null && !new_algo && !history && (
        <>
          <Button
            variant="contained"
            size="large"
            onClick={() => set_new_algo(true)}
          >
            Nowe obliczenia
          </Button>
          <Button
            variant="contained"
            size="large"
            onClick={() => set_history(true)}
          >
            Pokaż historię
          </Button>
        </>
      )}
      {new_algo && (
        <ConfigForm startProcess={(values) => startProcess(values)} />
      )}
      {history && <History set_process_id={(val)=>{set_process_id(val)}}/>}
      {process_id != null && <Plot process_id={process_id} />}
      {(history || new_algo || process_id != null) && (
          <Button
            variant="contained"
            size="large"
            onClick={() => {
              set_history(false);
              set_new_algo(false);
              set_process_id(null);
            }}
          >Wróć</Button>
        )}
    </Stack>
  );
}

export default App;
