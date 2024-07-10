import React from "react";
import InfoRender from "./InfoRender.tsx";
import handleStepInformation from "../../../utils/playbook/stepInformation/handleStepInformation.ts";
import { Notes } from "@mui/icons-material";
import getNestedValue from "../../../utils/getNestedValue.ts";
import DeleteTaskButton from "../../Buttons/DeleteTaskButton/index.tsx";
import useCurrentTask from "../../../hooks/useCurrentTask.ts";
import useIsPrefetched from "../../../hooks/useIsPrefetched.ts";

type TaskInformationPropTypes = {
  taskId: string | undefined;
};

function TaskInformation({ taskId }: TaskInformationPropTypes) {
  const [task, , taskType] = useCurrentTask(taskId);
  const isPrefetched = useIsPrefetched();

  if (!task?.id) return;

  const taskData =
    task[task.source.toLowerCase() ?? ""][taskType?.toLowerCase()];

  return (
    <div
      className={`px-4 py-2 bg-white border-2 border-stone-400 w-full h-auto cursor-pointer transition-all hover:shadow-violet-500 flex justify-between`}>
      <div className="flex flex-col gap-2 flex-1 text-ellipsis overflow-hidden">
        {handleStepInformation(task.id).map((info, i) => (
          <div className="flex flex-col flex-1 text-ellipsis" key={i}>
            {getNestedValue(taskData, info.key) && (
              <>
                <p className="text-xs font-semibold">{info.label}</p>
                <InfoRender info={info} taskId={task?.id ?? ""} />
              </>
            )}
          </div>
        ))}

        {task.notes && (
          <div className="flex gap-1 items-center flex-wrap">
            <Notes fontSize="small" />
            <p className="line-clamp-2 text-xs">{task.notes}</p>
          </div>
        )}
      </div>
      {!isPrefetched && (
        <div className="flex-[0.1] self-end">
          <DeleteTaskButton taskId={task.id} />
        </div>
      )}
    </div>
  );
}

export default TaskInformation;
