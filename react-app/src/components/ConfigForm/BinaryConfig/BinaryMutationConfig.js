import {
  TextField,
  FormControl,
  FormLabel,
  Select,
  MenuItem,
} from "@mui/material";
import { Item } from "../../Item";
export const BinaryMutationConfig = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <FormControl fullWidth>
        <FormLabel id="select-mutation-label">Mutacja</FormLabel>
        <Select
          labelId="select-mutation-label"
          id="select-mutation"
          value={formik.values.mutationType}
          onChange={formik.handleChange}
          name="mutationType"
        >
          <MenuItem value="one">Jednopunktowa</MenuItem>
          <MenuItem value="two">Dwupunktowa</MenuItem>
          <MenuItem value="edge">Brzegowa</MenuItem>
          <MenuItem value="inv">Inwersja</MenuItem>
        </Select>
        <TextField
          inputProps={{ type: "number", min: 0, max: 1 }}
          label={"Prawdopodobiestwo mutacji"}
          id="mutationProbability"
          name="mutationProbability"
          onChange={formik.handleChange}
          value={formik.values.mutationProbability}
        />
      </FormControl>
    </Item>
  );
};
