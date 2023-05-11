import {
  TextField,
  FormControl,
  FormLabel,
  Select,
  MenuItem,
} from "@mui/material";
import { Item } from "../../Item";
export const RealCrossoverConfig = (props) => {
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
          <MenuItem value="arithmetic_crossover">Arytmetyczne</MenuItem>
          <MenuItem value="linear_crossover">Linearne</MenuItem>
          <MenuItem value="blend_crossover_alpha">
            Mieszającego typu alfa
          </MenuItem>
          <MenuItem value="blend_crossover_alpha_beta">
            Mieszającego typu alfa i beta
          </MenuItem>
          <MenuItem value="average_crossover">Uśredniające</MenuItem>
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
