import React, {useState, useEffect} from "react";
import {Button} from '@mui/material';


export const History = (props) => {
    const [data, setData] = useState([]);
    useEffect(() => {
      fetch("https://obliczenia-ewolucyjne-default-rtdb.europe-west1.firebasedatabase.app/algoruns.json")
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      {Object.entries(data).map(([key]) => (
        <Button key={key} variant="contained" color="primary" onClick={() => {props.set_process_id(data[key].process_id)}}>{data[key].date}</Button>
      ))}
    </div>
  )
};
