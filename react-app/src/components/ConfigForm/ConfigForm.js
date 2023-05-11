import { useFormik } from "formik";
import { MethodModeConfig } from "./MethodModeConfig";
import { BinaryConfig } from "./BinaryConfig/BinaryConfig";
import { RealRepresentationConfig } from "./RealRepresentationConfig/RealRepresentationConfig";
import { MetaheuristicsConfig } from "./MetaheuristicsConfig/MetaheuristicsConfig";
import { CommonConfig } from "./CommonConfig/CommonConfig";

const renderFieldsForMethod = (formik) => {
  formik.values.useMetaheuristics = false;
  switch (formik.values.method) {
    case "binary_representation":
      if (["uniform", "gaussian"].includes(formik.values.mutationType)) {
        formik.values.crossoverType = "one";
        formik.values.mutationType = "one";
      }
      return <BinaryConfig formik={formik} />;
    case "real_representation":
      if (!["uniform", "gaussian"].includes(formik.values.mutationType)) {
        formik.values.crossoverType = "arithmetic_crossover";
        formik.values.mutationType = "uniform";
      }
      return <RealRepresentationConfig formik={formik} />;
    case "metaheuristics":
      formik.values.useMetaheuristics = true;
      return <MetaheuristicsConfig formik={formik} />;
    default:
      return <></>;
  }
};

export const ConfigForm = (props) => {
  const formik = useFormik({
    initialValues: {
      method: "binary_representation",
      minValue: -5,
      maxValue: 5,
      precisionType: "bits_length",
      precisionVal: 20,
      populationSize: 150,
      epochsAmount: 1000,
      crossoverType: "one",
      crossoverProbability: 0.75,
      mutationType: "one",
      mutationProbability: 0.15,
      eliteStrategy: true,
      selectionType: "rank",
      selectionValue: 0.3,
      optimizationMode: "min",
      useMetaheuristics: false,
      metaheuristics: {
        name: "random_walk",
        assumptions: {
          step_size: 0.5,
          temperature: 1,
        },
      },
    },
    onSubmit: (values) => {
      props.startProcess(values);
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <MethodModeConfig formik={formik} />
      <CommonConfig formik={formik} />
      {renderFieldsForMethod(formik)}
    </form>
  );
};
