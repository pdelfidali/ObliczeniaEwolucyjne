import { Button } from "@mui/material";
import { Item } from "../../Item";
export const Submit = (props) => {
  const formik = props.formik;
  return (
    <Item>
      <Button size="large" variant="contained" onClick={formik.handleSubmit}>
        Rozpocznij
      </Button>
    </Item>
  );
};
