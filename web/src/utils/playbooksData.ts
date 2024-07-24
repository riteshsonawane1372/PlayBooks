import { playbookSelector } from "../store/features/playbook/playbookSlice.ts";
import { store } from "../store/index.ts";
import { FormFields } from "../types/inputs/formFields.ts";
import { Sources } from "../types/sources.ts";
import { TaskDetails } from "../types/taskDetails.ts";
import extractOptions from "./extractOptions.ts";
import getCurrentTask from "./getCurrentTask.ts";
import { KeyType } from "./playbook/key.ts";

export const constructBuilder = (id?: string) => {
  const [task] = getCurrentTask(id);
  if (!task) return [];
  const { supportedTaskTypes } = playbookSelector(store.getState());
  const source: Sources = task.source.toLowerCase() as Sources;
  const taskType = ((task as any)[source] as TaskDetails).type;
  const type = supportedTaskTypes?.find(
    (e: any) => e.source === source.toUpperCase() && e.task_type === taskType,
  );

  return type.form_fields.map((field: FormFields) => ({
    key: field.key_name,
    label: field.display_name,
    placeholder: field.description,
    options:
      field.valid_values?.map((v) => ({
        id: v[v.type.toLowerCase()],
        label: v[v.type.toLowerCase()],
      })) ?? extractOptions(task, field.key_name as KeyType),
    inputType: field.form_field_type,
    isOptional: field.is_optional,
    default: field.default_value?.[field.default_value.type.toLowerCase()],
  }));
};
