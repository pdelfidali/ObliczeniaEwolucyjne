import { MetaheuristicsSelect } from "./MetahueristicsSelect";
import { Submit } from "../CommonConfig/Submit";
import { HillClimbingConfig } from "./HillClimbingConfig";
import { SimulatedAnnealingConfig } from "./SimulatedAnnealingConfig";

const renderFieldsForMetaheuristic = (formik) => {
  switch (formik.values.metaheuristics.name) {
    case "hill_climbing":
      return <HillClimbingConfig formik={formik} />;
    case "simulated_annealing":
      return <SimulatedAnnealingConfig formik={formik} />;
    default:
      return <></>;
  }
};

export const MetaheuristicsConfig = (props) => {
  const formik = props.formik;
  return (
    <>
      <MetaheuristicsSelect formik={formik} />
      {renderFieldsForMetaheuristic(formik)}
      <Submit formik={formik} />
    </>
  );
};
