import {
  FormControl,
  RadioGroup,
  Radio,
  FormControlLabel,
  FormLabel,
} from "@mui/material";
import { Item } from "../../Item";

export const EliteStrategyConfig = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl>
        <FormLabel>Strategia elitarna</FormLabel>
        <RadioGroup
          row
          name="eliteStrategy"
          onChange={formik.handleChange}
          value={formik.values.eliteStrategy}
        >
          <FormControlLabel
            value={false}
            control={<Radio />}
            label="Nie"
            labelPlacement="start"
          />
          <FormControlLabel
            value={true}
            control={<Radio />}
            label="Tak"
            labelPlacement="start"
          />
        </RadioGroup>
      </FormControl>
    </Item>
  );
};
