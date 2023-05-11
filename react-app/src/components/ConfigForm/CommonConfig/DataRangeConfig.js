import { TextField, FormLabel } from "@mui/material";
import { Item } from "../../Item";

export const DataRangeInput = (props) => {
  const formik = props.formik;
  return (
    <>
      <Item>
        <FormLabel>Zakres zmiennych</FormLabel>
      </Item>
      <Item>
        <TextField
          type="number"
          label="Wartość minimalna zmiennej:"
          id="minValue"
          name="minValue"
          onChange={formik.handleChange}
          value={formik.values.minValue}
        />

        <TextField
          type="number"
          label="Wartość maksymalna zmiennej:"
          id="maxValue"
          name="maxValue"
          onChange={formik.handleChange}
          value={formik.values.maxValue}
        />
      </Item>
    </>
  );
};
