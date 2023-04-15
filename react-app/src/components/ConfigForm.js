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
 import { Item } from "./Item";

export const ConfigForm = (props) => {
  const formik = useFormik({
    initialValues: {
      minValue: 0,
      maxValue: 4,
      precisionType: "bitsLength",
      precisionVal: 7,
      populationSize: 150,
      epochsAmount: 1000,
      crossoverType: "one",
    crossoverProbability: 0.5,
    mutationType: "one",
    mutationProbability: 0.5,
    inversionProbability: 0.5,
    eliteStrategy: true,
    selectionType: "rank",
    selectionValue: 0.3,
    optimizationMode: "min"
    },
    onSubmit: (values) => { 
      const requestOptions = {
      method: 'POST',
      headers: { 
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(values, null, 2)
  };
  fetch('http://127.0.0.1:8000/assumptions/', requestOptions)
      .then(response => response.json())
      .then(data => props.set_process_id(data.process_id));
    },
  });

  let selectionLabel;
  switch(formik.values.selectionType){
    case "rank":
      selectionLabel = "Procent najlepszych osobników:"
      break;
    case "roulette":
      selectionLabel = "Ilość losowań:"
      break;
    default:
      selectionLabel = "Wielkość turnieju:"
      break;
  }

  return (
      <form onSubmit={formik.handleSubmit}>
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
              value={formik.values.crossoverType}
              onChange={formik.handleChange}
            >
              <MenuItem value="one">Jednopunktowe</MenuItem>
              <MenuItem value="two">Dwupunktowe</MenuItem>
              <MenuItem value="three">Trzypunktowe</MenuItem>
              <MenuItem value="homo">Jednorodne</MenuItem>
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
        <Item>
          <FormControl fullWidth>
            <FormLabel id="select-mutation-label">Mutacja</FormLabel>
            <Select
              labelId="select-mutation-label"
              id="select-mutation"
              value={formik.values.mutationType}
              onChange={formik.handleChange}
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
        <Item>
          <FormControl>
            <FormLabel>Strategia elitarna</FormLabel>
            <RadioGroup
              row
              name="eliteStrategy"
              onChange={formik.handleChange}
              value={formik.values.eliteStrategy}
            >
              <FormControlLabel
                value={false}
                control={<Radio />}
                label="Nie"
                labelPlacement="start"
              />
              <FormControlLabel
                value={true}
                control={<Radio />}
                label="Tak"
                labelPlacement="start"
              />
            </RadioGroup>
          </FormControl>
        </Item>
        <Item>
          <FormControl>
            <FormLabel>Metoda selekcji</FormLabel>
            <RadioGroup
              row
              name="selectionType"
              onChange={formik.handleChange}
              value={formik.values.selectionType}
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
                value={"roulette"}
                control={<Radio />}
                label="Selekcja kołem ruletki"
                labelPlacement="start"
              />
            </RadioGroup>
              <TextField
                fullWidth
                inputProps={{ type: "number", min: 0, max: 50 }}
                label={selectionLabel}
                id="selection.value"
                name="selection.value"
                onChange={formik.handleChange}
                value={formik.values.selectionValue}
              />
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
  );
};
