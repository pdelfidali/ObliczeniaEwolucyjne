import {Stack, Switch, TextField, Typography} from "@mui/material";

export const PrecisionInput = (props) => {
    return (<><Stack direction="row" spacing={2} alignItems="center">
        <Typography>Długość bitowa</Typography>
        <Switch value={props.precision} onChange={() => {props.updatePrecision()}}/>
        <Typography>Precyzja do n. miejsca po przecinku</Typography>
        <TextField inputProps={{ type: 'number', min: 1, max: 50}} />
    </Stack>
    <Stack direction="row" spacing={2} alignItems="center">
        <TextField inputProps={{ type: 'number'}} />
        <TextField inputProps={{ type: 'number'}} />
        <TextField inputProps={{ type: 'number'}} />
    </Stack></>)
}

