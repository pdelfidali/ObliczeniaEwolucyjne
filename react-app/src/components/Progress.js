import { useState, useEffect } from "react";
import { CircularProgress, Box, Typography, Stack } from "@mui/material";

const CircularProgressWithLabel = (props) => {
  return (
    <Box sx={{ position: "relative", display: "inline-flex" }}>
      <CircularProgress variant="determinate" {...props} />
      <Box
        sx={{
          top: 0,
          left: 0,
          bottom: 0,
          right: 0,
          position: "absolute",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography variant="caption" component="div" color="text.secondary">
          {`${Math.round(props.value)}%`}
        </Typography>
      </Box>
    </Box>
  );
};
export const Progress = (props) => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    function getProgress() {
      fetch("http://127.0.0.1:8000/epoch/" + props.process_id)
        .then((result) => result.json())
        .then((result) => {
          setProgress(result.progress);
          if (result.progress === 1) {
            props.set_process_finished();
          }
        });
    }
    getProgress();
    const interval = setInterval(() => getProgress(), 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  return <CircularProgressWithLabel value={progress * 100} />;
};
