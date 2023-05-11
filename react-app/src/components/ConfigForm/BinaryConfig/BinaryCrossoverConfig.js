import {
  TextField,
  FormControl,
  FormLabel,
  Select,
  MenuItem,
} from "@mui/material";
import { Item } from "../../Item";
export const BinaryCrossoverConfig = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl fullWidth>
        <FormLabel id="select-crossover-label">Krzyżowanie</FormLabel>
        <Select
          labelId="select-crossover-label"
          id="select-crossover"
          name="crossoverType"
          value={formik.values.crossoverType}
          onChange={formik.handleChange}
        >
          <MenuItem value="one">Jednopunktowe</MenuItem>
          <MenuItem value="two">Dwupunktowe</MenuItem>
          <MenuItem value="three">Trzypunktowe</MenuItem>
          <MenuItem value="homo">Jednorodne</MenuItem>
        </Select>
        <TextField
          inputProps={{ type: "number", min: 0, max: 1 }}
          label={"Prawdopodobiestwo krzyowania"}
          id="crossoverProbability"
          name="crossoverProbability"
          onChange={formik.handleChange}
          value={formik.values.crossoverProbability}
        />
      </FormControl>
    </Item>
  );
};
