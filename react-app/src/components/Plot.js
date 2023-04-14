import React from "react";
export const Plot = (props) => {
    alert(props.filename)
  return (
      <img src={process.env.PUBLIC_URL + '/plots/' + props.filename} alt="Wykres przedstawiajacy blad w kolejnych epokach."/>
  );
};
