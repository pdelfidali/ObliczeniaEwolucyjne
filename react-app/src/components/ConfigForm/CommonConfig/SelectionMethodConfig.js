import {
  TextField,
  FormControl,
  RadioGroup,
  Radio,
  FormControlLabel,
  FormLabel,
} from "@mui/material";
import { Item } from "../../Item";

export const SelectionMethodConfig = (props) => {
  const formik = props.formik;
  let selectionLabel;
  switch (formik.values.selectionType) {
    case "rank":
      selectionLabel = "Procent najlepszych osobników:";
      break;
    case "roulette":
      selectionLabel = "Ilość losowań:";
      break;
    default:
      selectionLabel = "Wielkość turnieju:";
      break;
  }
  return (
    <Item>
      <FormControl>
        <FormLabel>Metoda selekcji</FormLabel>
        <RadioGroup
          row
          name="selectionType"
          onChange={formik.handleChange}
          value={formik.values.selectionType}
        >
          <FormControlLabel
            value={"rank"}
            control={<Radio />}
            label="Selekcja rankingowa"
            labelPlacement="start"
          />
          <FormControlLabel
            value={"tournament"}
            control={<Radio />}
            label="Selekcja turniejowa"
            labelPlacement="start"
          />
          <FormControlLabel
            value={"roulette"}
            control={<Radio />}
            label="Selekcja kołem ruletki"
            labelPlacement="start"
          />
        </RadioGroup>
        <TextField
          inputProps={{ type: "number", min: 0, max: 50 }}
          label={selectionLabel}
          id="selectionValue"
          name="selectionValue"
          onChange={formik.handleChange}
          value={formik.values.selectionValue}
        />
      </FormControl>
    </Item>
  );
};
