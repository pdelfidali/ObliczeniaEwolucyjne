import React, { useState, useRef, useEffect } from "react";
import { CircularProgress, Box, Typography, Stack } from "@mui/material";
import { Item } from "./Item";

export const Plot = (props) => {
  return (
    <Box>
      <Box>
          <img
            src={
              process.env.PUBLIC_URL +
              `/plots/${props.process_id}/best_individuals_plot.jpg`
            }
            alt="Wartość funkcji celu dla najlepszego osobnika w kolejnych epokach"
          /></Box>
          <Box>
          <img
            src={
              process.env.PUBLIC_URL +
              `/plots/${props.process_id}/mean_plot.jpg`
            }
            alt="Średnia wartość funkcji celu dla populacji w kolejnych epokach"
          /></Box>
          <Box>
          <img
            src={
              process.env.PUBLIC_URL + `/plots/${props.process_id}/std_plot.jpg`
            }
            alt="Wartość odchylenia standardowego dla funkcji celu dla populacji w kolejnych epokach"
          /></Box>
    </Box>
  );
};
