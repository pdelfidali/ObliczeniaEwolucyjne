import { useFormik } from "formik";
import {
  Stack,
  TextField,
  Paper,
  FormControl,
  RadioGroup,
  Radio,
  FormControlLabel,
  FormLabel,
  Select,
  MenuItem,
  Button,
} from "@mui/material";
import { styled } from "@mui/material/styles";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));

export const ConfigForm = () => {
  const formik = useFormik({
    initialValues: {
      x1MaxVal: 4,
      x1MinVal: 0,
      x2MaxVal: 5,
      x2MinVal: 1,
      precisionType: "bitsLength",
      precisionVal: 7,
      populationSize: 150,
      epochsAmount: 1000,
      crossover: {
        type: "one",
        probability: 0.5,
      },
      mutation: {
        type: "one",
        probability: 0.5,
      },
      inversion: {
        probability: 0.5,
      },
      eliteStrategy: {
        type: "percent",
        value: 25,
      },
      selection: {
        type: "rank",
        value: 0.3,
      },
    },
    onSubmit: (values) => {
      alert(JSON.stringify(values, null, 2));
    },
  });

  return (
    <Stack
      spacing={12}
      alignItems="center"
      justifyContent="space-evenly"
      style={{ minHeight: "100%" }}
    >
      <form onSubmit={formik.handleSubmit}>
        <Item>
          <FormLabel>Zakres zmiennych</FormLabel>
        </Item>
        <Item>
          <TextField
            type="number"
            label="Wartość minimalna zmiennej x1:"
            id="x1MinVal"
            name="x1MinVal"
            onChange={formik.handleChange}
            value={formik.values.x1MinVal}
          />

          <TextField
            type="number"
            label="Wartość maksymalna zmiennej x1:"
            id="x1MaxVal"
            name="x1MaxVal"
            onChange={formik.handleChange}
            value={formik.values.x1MaxVal}
          />
        </Item>
        <Item>
          <TextField
            type="number"
            label="Wartość minimalna zmiennej x2:"
            id="x2MinVal"
            name="x2MinVal"
            onChange={formik.handleChange}
            value={formik.values.x2MinVal}
          />

          <TextField
            type="number"
            label="Wartość maksymalna zmiennej x2:"
            id="x2MaxVal"
            name="x2MaxVal"
            onChange={formik.handleChange}
            value={formik.values.x2MaxVal}
          />
        </Item>
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
                value={"bitsLength"}
                control={<Radio />}
                label="Długość ciągu bitowego"
                labelPlacement="start"
              />
              <FormControlLabel
                value={"comaPrecision"}
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
              formik.values.precisionType === "comaPrecision"
                ? "Dokładność do n: miejsca po przecinku:"
                : "Długość ciągu bitowego:"
            }
            id="precisionVal"
            name="precisionVal"
            onChange={formik.handleChange}
            value={formik.values.precisionVal}
          />
        </Item>
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
        <Item>
          <FormControl fullWidth>
            <FormLabel id="select-crossover-label">Krzyżowanie</FormLabel>
            <Select
              labelId="select-crossover-label"
              id="select-crossover"
              value={formik.values.crossover.type}
              onChange={formik.handleChange}
            >
              <MenuItem value="one">Jedno punktowe</MenuItem>
              <MenuItem value="two">Dwu punktowe</MenuItem>
              <MenuItem value="three">Trzy punktowe</MenuItem>
              <MenuItem value="homogeneous">Jednorodne</MenuItem>
            </Select>
            <TextField
              inputProps={{ type: "number", min: 0, max: 1 }}
              label={"Prawdopodobiestwo krzyowania"}
              id="crossover-probability"
              name="crossover.probability"
              onChange={formik.handleChange}
              value={formik.values.crossover.probability}
            />
          </FormControl>
        </Item>
        <Item>
          <FormControl fullWidth>
            <FormLabel id="select-mutation-label">Mutacja</FormLabel>
            <Select
              labelId="select-mutation-label"
              id="select-mutation"
              value={formik.values.mutation.type}
              onChange={formik.handleChange}
            >
              <MenuItem value="one">Jednopunktowa</MenuItem>
              <MenuItem value="two">Dwupunktowa</MenuItem>
              <MenuItem value="border">Brzegowa</MenuItem>
            </Select>
            <TextField
              inputProps={{ type: "number", min: 0, max: 1 }}
              label={"Prawdopodobiestwo mutacji"}
              id="mutation-probability"
              name="mutation.probability"
              onChange={formik.handleChange}
              value={formik.values.mutation.probability}
            />
          </FormControl>
        </Item>
        <Item>
          <TextField
            fullWidth
            inputProps={{ type: "number", min: 0, max: 1 }}
            label={"Prawdopodobiestwo inwersji"}
            id="inversion-probability"
            name="inversion.probability"
            onChange={formik.handleChange}
            value={formik.values.inversion.probability}
          />
        </Item>
        <Item>
          <FormControl>
            <FormLabel>Strategia elitarna</FormLabel>
            <RadioGroup
              row
              name="eliteStrategy.type"
              onChange={formik.handleChange}
              value={formik.values.eliteStrategy.type}
            >
              <FormControlLabel
                value={"percent"}
                control={<Radio />}
                label="Procent najlepszych osobników"
                labelPlacement="start"
              />
              <FormControlLabel
                value={"n-best"}
                control={<Radio />}
                label="N. najlepszych osobników"
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
              formik.values.eliteStrategy.type === "percent"
                ? "Procent najlepszych osobników:"
                : "N. najlepszych osobników:"
            }
            id="eliteStrategy.value"
            name="eliteStrategy.value"
            onChange={formik.handleChange}
            value={formik.values.eliteStrategy.value}
          />
        </Item>
        <Item>
          <FormControl>
            <FormLabel>Metoda selekcji</FormLabel>
            <RadioGroup
              row
              name="selection.type"
              onChange={formik.handleChange}
              value={formik.values.selection.type}
            >
              <FormControlLabel
                value={"rank"}
                control={<Radio />}
                label="Selekcja rankingowa"
                labelPlacement="start"
              />
              <FormControlLabel
                value={"tournament"}
                control={<Radio />}
                label="Selekcja turniejowa"
                labelPlacement="start"
              />
              <FormControlLabel
                value={"roulette_wheel"}
                control={<Radio />}
                label="Selekcja kołem ruletki"
                labelPlacement="start"
              />
            </RadioGroup>
            {formik.values.selection.type !== "roulette_wheel" && (
              <TextField
                fullWidth
                inputProps={{ type: "number", min: 0, max: 50 }}
                label={
                  formik.values.selection.type === "rank"
                    ? "Procent najlepszych osobników:"
                    : "N. najlepszych osobników:"
                }
                id="selection.value"
                name="selection.value"
                onChange={formik.handleChange}
                value={formik.values.selection.value}
              />
            )}
          </FormControl>
        </Item>
        <Item>
          <Button
            size="large"
            variant="contained"
            onClick={formik.handleSubmit}
          >
            Rozpocznij
          </Button>
        </Item>
      </form>
    </Stack>
  );
};
