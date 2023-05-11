import { BinaryCrossoverConfig } from "./BinaryCrossoverConfig";
import { BinaryMutationConfig } from "./BinaryMutationConfig";
import { SelectionMethodConfig } from "../CommonConfig/SelectionMethodConfig";
import { PrecisionConfig } from "./PrecisionConfig";
import { EliteStrategyConfig } from "../CommonConfig/EliteStrategy";
import { Submit } from "../CommonConfig/Submit";

export const BinaryConfig = (props) => {
  const formik = props.formik;
  return (
    <>
      <PrecisionConfig formik={formik} />
      <BinaryCrossoverConfig formik={formik} />
      <BinaryMutationConfig formik={formik} />
      <SelectionMethodConfig formik={formik} />
      <EliteStrategyConfig formik={formik} />
      <Submit formik={formik} />
    </>
  );
};
