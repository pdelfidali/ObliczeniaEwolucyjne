import { DataRangeInput } from "./DataRangeConfig";
import { SizeEpochConfig } from "./SizeEpochConfig";

export const CommonConfig = (props) => {
  const formik = props.formik;
  return (
    <>
      <DataRangeInput formik={formik} />
      <SizeEpochConfig formik={formik} />
    </>
  );
};
