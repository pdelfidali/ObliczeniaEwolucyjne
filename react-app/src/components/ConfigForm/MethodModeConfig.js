import {
  FormControl,
  RadioGroup,
  Radio,
  FormControlLabel,
  FormLabel,
  Select,
  MenuItem,
  InputLabel,
} from "@mui/material";
import { Item } from "../Item";

export const MethodModeConfig = (props) => {
  const formik = props.formik;
  return (
    <>
      {" "}
      <Item>
        <FormControl fullWidth>
          <InputLabel id="select-method-label">Wybierz metodę:</InputLabel>
          <Select
            labelId="select-method-label"
            id="method-select"
            name="method"
            value={formik.values.method}
            label=""
            onChange={formik.handleChange}
          >
            <MenuItem value="binary_representation">
              Reprezentacja binarna
            </MenuItem>
            <MenuItem value="real_representation">
              Reprezentacja rzeczywista
            </MenuItem>
            <MenuItem value="metaheuristics">Metaheurystyki</MenuItem>
          </Select>
        </FormControl>
      </Item>
      <Item>
        <FormControl>
          <FormLabel>Typ optymalizacji</FormLabel>
          <RadioGroup
            row
            name="optimizationMode"
            onChange={formik.handleChange}
            value={formik.values.optimizationMode}
          >
            <FormControlLabel
              value={"min"}
              control={<Radio />}
              label="Minimalizowanie"
              labelPlacement="start"
            />
            <FormControlLabel
              value={"max"}
              control={<Radio />}
              label="Maksymalizowanie"
              labelPlacement="start"
            />
          </RadioGroup>
        </FormControl>
      </Item>
    </>
  );
};
