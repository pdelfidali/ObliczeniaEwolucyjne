import { TextField, FormControl } from "@mui/material";
import { Item } from "../../Item";

export const SizeEpochConfig = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl fullWidth>
        <TextField
          inputProps={{ type: "number", min: 4, max: 1 }}
          label={"Wielkość populacji"}
          id="populationSize"
          name="populationSize"
          onChange={formik.handleChange}
          value={formik.values.populationSize}
        />
        <TextField
          inputProps={{ type: "number", min: 100, max: 100000 }}
          label={"Ilość epok"}
          id="epochsAmount"
          name="epochsAmount"
          onChange={formik.handleChange}
          value={formik.values.epochsAmount}
        />
      </FormControl>
    </Item>
  );
};
