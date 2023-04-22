import { TextField, FormControl } from "@mui/material";
import { Item } from "../../Item";

export const HillClimbingConfig = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl fullWidth>
        <TextField
          inputProps={{ type: "number", min: 100, max: 100000 }}
          label={"Dugość kroku"}
          id="formik_values_metaheuristics_assumptions_step_size"
          name="formik.values.metaheuristics.assumptions.step_size"
          onChange={formik.handleChange}
          value={formik.values.metaheuristics.assumptions.step_size}
        />
      </FormControl>
    </Item>
  );
};
