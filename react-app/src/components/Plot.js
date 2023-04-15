import React, { useState, useRef, useEffect } from "react";
import { CircularProgress, Box, Typography, Stack } from "@mui/material";
import { Item } from "./Item";

export const Plot = (props) => {
  const [plot, setPlot] = useState(null);
  const [time, setTime] = useState(0);

  const ref = useRef(null);

  const callApi = () => {
    fetch(`http://127.0.0.1:8000/epoch/${props.process_id}`)
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data.filename);
        if (data.filename !== undefined) {
          setPlot(data.filename);
        } else {
          setTime(time + 1);
        }
      })
      .catch((err) => console.warn(err));
  };

  useEffect(() => {
    ref.current = setInterval(() => setTime(time + 1), 1000);

    return () => {
      if (ref.current) {
        clearInterval(ref.current);
      }
    };
  }, [time]);

  return (
    <Box>
      {plot === null && (
        <>
          <Item>
            <CircularProgress />
          </Item>
          <Item>
            <Typography variant="h3">{`Czas wykonywania algorytmu: ${time}s`}</Typography>
          </Item>
        </>
      )}
      {plot !== null && (
        <>
          <img
            src={
              process.env.PUBLIC_URL +
              `/plots/${props.process_id}/best_individuals_plot.jpg`
            }
            alt="Wartość funkcji celu dla najlepszego osobnika w kolejnych epokach"
          />
          <img
            src={
              process.env.PUBLIC_URL +
              `/plots/${props.process_id}/mean_plot.jpg`
            }
            alt="Średnia wartość funkcji celu dla populacji w kolejnych epokach"
          />
          <img
            src={
              process.env.PUBLIC_URL + `/plots/${props.process_id}/std_plot.jpg`
            }
            alt="Wartość odchylenia standardowego dla funkcji celu dla populacji w kolejnych epokach"
          />
        </>
      )}
    </Box>
  );
};
