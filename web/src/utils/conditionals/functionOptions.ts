import { Step } from "../../types.ts";

enum ResultTypeTypes {
  TIMESERIES = "TIMESERIES",
  TABLE = "TABLE",
  OTHERS = "others",
}

export const functionOptions = (step: Step) => {
  const type = step.resultType;

  switch (type) {
    case ResultTypeTypes.TIMESERIES:
      return [
        {
          id: "AVG_F",
          label: "Average",
        },
        {
          id: "MAX_F",
          label: "Max",
        },
        {
          id: "MIN_F",
          label: "Min",
        },
        {
          id: "LAST_F",
          label: "Latest",
        },
      ];
    case ResultTypeTypes.TABLE:
      return [
        {
          id: "count",
          label: "Count of results",
        },
        {
          id: "result",
          label: "Query result Value",
        },
        {
          id: "list",
          label: "Query result List of values",
        },
      ];
    default:
      return [];
  }
};
