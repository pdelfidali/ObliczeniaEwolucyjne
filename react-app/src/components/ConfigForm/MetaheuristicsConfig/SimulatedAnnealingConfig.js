import { TextField, FormControl } from "@mui/material";
import { Item } from "../../Item";

export const SimulatedAnnealingConfig = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl fullWidth>
        <TextField
          inputProps={{ type: "number", min: 0, max: 1 }}
          label={"Dugość kroku"}
          id="formik_values_metaheuristics_assumptions_step_size"
          name="formik.values.metaheuristics.assumptions.step_size"
          onChange={formik.handleChange}
          value={formik.values.metaheuristics.assumptions.step_size}
        />
        <TextField
          inputProps={{ type: "number", min: 0, max: 10 }}
          label={"Temperatura początkowa"}
          id="formik_values_metaheuristics_assumptions_temperature"
          name="formik.values.metaheuristics.assumptions.temperature"
          onChange={formik.handleChange}
          value={formik.values.metaheuristics.assumptions.temperature}
        />
      </FormControl>
    </Item>
  );
};
