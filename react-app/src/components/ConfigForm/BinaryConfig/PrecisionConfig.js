import {
  FormControl,
  RadioGroup,
  Radio,
  FormControlLabel,
  FormLabel,
  TextField,
} from "@mui/material";
import { Item } from "../../Item";

export const PrecisionConfig = (props) => {
  const formik = props.formik;
  return (
    <>
      <Item>
        <FormControl>
          <FormLabel id="demo-form-control-label-placement">
            Dokładność
          </FormLabel>
          <RadioGroup
            row
            aria-labelledby="demo-form-control-label-placement"
            name="precisionType"
            onChange={formik.handleChange}
            value={formik.values.precisionType}
          >
            <FormControlLabel
              value={"bits_length"}
              control={<Radio />}
              label="Długość ciągu bitowego"
              labelPlacement="start"
            />
            <FormControlLabel
              value={"precision"}
              control={<Radio />}
              label="Do n. miejsca po przecinku"
              labelPlacement="start"
            />
          </RadioGroup>
        </FormControl>
      </Item>
      <Item>
        <TextField
          fullWidth
          inputProps={{ type: "number", min: 0, max: 50 }}
          label={
            formik.values.precisionType === "precision"
              ? "Dokładność do n: miejsca po przecinku:"
              : "Długość ciągu bitowego:"
          }
          id="precisionVal"
          name="precisionVal"
          onChange={formik.handleChange}
          value={formik.values.precisionVal}
        />
      </Item>
    </>
  );
};
