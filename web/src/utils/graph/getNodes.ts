import { currentPlaybookSelector } from "../../store/features/playbook/playbookSlice.ts";
import { store } from "../../store/index.ts";
import { Step } from "../../types/index.ts";

const initialPlaybookNode = {
  id: "playbook",
  position: { x: 0, y: 0 },
  data: {
    label: "Playbook",
    index: 0,
  },
  type: "parent",
};

export const getNodes = () => {
  const playbook = currentPlaybookSelector(store.getState());
  const steps: Step[] = playbook?.steps ?? [];
  const nodes = steps.map((step, index) => {
    return {
      id: `node-${step.id}`,
      data: {
        step,
        index,
      },
      type: "step",
    };
  });

  return [initialPlaybookNode, ...nodes];
};
