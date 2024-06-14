import * as Types from "../types/index.ts";

export const handleActionsExtractor = (
  type: Types.WorkflowActionOptions,
  workflowAction: Types.WorkflowActionContractType,
) => {
  switch (type) {
    case Types.WorkflowActionOptions.SLACK_MESSAGE:
      return {};
    case Types.WorkflowActionOptions.SLACK_THREAD_REPLY:
      return {
        channel: {
          channel_id: workflowAction.slack_channel_id,
        },
        trigger: {
          channel: {
            channel_id: workflowAction.slack_channel_id,
          },
        },
      };

    default:
      return {};
  }
};
