import { FormControl, Select, MenuItem, InputLabel } from "@mui/material";
import { Item } from "../../Item";

export const MetaheuristicsSelect = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl fullWidth>
        <InputLabel id="select-metaheuristics-label">
          Wybierz metodę:
        </InputLabel>
        <Select
          labelId="select-metaheuristics-label"
          id="method-select"
          name="metaheuristics.name"
          value={formik.values.metaheuristics.name}
          label=""
          onChange={formik.handleChange}
        >
          <MenuItem value="random_sampling">Losowe próbkowanie</MenuItem>
          <MenuItem value="random_walk">
            Alogrytm błądzenia przypadkowego
          </MenuItem>
          <MenuItem value="hill_climbing">Algorytm wspinaczki</MenuItem>
          <MenuItem value="simulated_annealing">Symulator wyżarzania</MenuItem>
        </Select>
      </FormControl>
    </Item>
  );
};
