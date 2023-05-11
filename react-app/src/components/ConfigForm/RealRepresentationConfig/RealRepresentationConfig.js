import { RealCrossoverConfig } from "./RealCrossoverConfig";
import { RealMutationConfig } from "./RealMutationConfig";
import { EliteStrategyConfig } from "../CommonConfig/EliteStrategy";
import { Submit } from "../CommonConfig/Submit";
import { SelectionMethodConfig } from "../CommonConfig/SelectionMethodConfig";

export const RealRepresentationConfig = (props) => {
  const formik = props.formik;
  return (
    <>
      <RealCrossoverConfig formik={formik} />
      <RealMutationConfig formik={formik} />
      <SelectionMethodConfig formik={formik} />
      <EliteStrategyConfig formik={formik} />
      <Submit formik={formik} />
    </>
  );
};
