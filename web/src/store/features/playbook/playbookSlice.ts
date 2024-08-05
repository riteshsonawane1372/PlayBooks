import { createSlice } from "@reduxjs/toolkit";
import * as Actions from "./slices/index.ts";
import { initialState } from "./initialState.ts";
export * from "./selectors";

export const playbookSlice = createSlice({
  name: "playbook",
  initialState: initialState,
  reducers: {
    setPlaybooks: Actions.setPlaybooks,
    setPlaybookData: Actions.setPlaybookData,
    copyPlaybook: Actions.copyPlaybook,
    setErrors: Actions.setErrors,
    addGlobalVariable: Actions.addGlobalVariable,
    deleteVariable: Actions.deleteVariable,
    updateGlobalVariable: Actions.updateGlobalVariable,
    setMeta: Actions.setMeta,
    setCurrentVisibleTask: Actions.setCurrentVisibleTask,
    setCurrentVisibleStep: Actions.setCurrentVisibleStep,
    showTaskConfig: Actions.showTaskConfig,
    createTaskWithSource: Actions.createTaskWithSource,
    addStep: Actions.addStep,
    deleteStep: Actions.deleteStep,
    deleteTask: Actions.deleteTask,
    updateTask: Actions.updateTask,
    updateStep: Actions.updateStep,
    updateSource: Actions.updateSource,
    updateTaskType: Actions.updateTaskType,
    setAssets: Actions.setAssets,
    addNotes: Actions.addNotes,
    addExternalLinks: Actions.addExternalLinks,
    toggleExternalLinkVisibility: Actions.toggleExternalLinkVisibility,
    toggleNotesVisibility: Actions.toggleNotesVisibility,
    resetState: Actions.resetState,
    resetExecutions: Actions.resetExecutions,
    setPlaybookKey: Actions.setPlaybookKey,
    setCurrentPlaybookKey: Actions.setCurrentPlaybookKey,
    pushToExecutionStack: Actions.pushToExecutionStack,
    popFromExecutionStack: Actions.popFromExecutionStack,
    addRule: Actions.addRule,
    duplicateTask: Actions.duplicateTask,
    removeRelation: Actions.removeRelation,
    addRelation: Actions.addRelation,
    addStepRule: Actions.addStepRule,
    createPlaybookForDynamicAlert: Actions.createPlaybookForDynamicAlert,
    addStepRuleSet: Actions.addStepRuleSet,
  },
});

export const {
  setPlaybooks,
  setPlaybookData,
  copyPlaybook,
  createTaskWithSource,
  setCurrentVisibleTask,
  showTaskConfig,
  updateTask,
  addGlobalVariable,
  deleteVariable,
  updateGlobalVariable,
  setMeta,
  deleteStep,
  setAssets,
  addNotes,
  addExternalLinks,
  resetState,
  setErrors,
  toggleExternalLinkVisibility,
  toggleNotesVisibility,
  setPlaybookKey,
  setCurrentPlaybookKey,
  resetExecutions,
  pushToExecutionStack,
  popFromExecutionStack,
  deleteTask,
  updateSource,
  updateTaskType,
  updateStep,
  setCurrentVisibleStep,
  addStep,
  addRule,
  duplicateTask,
  removeRelation,
  addRelation,
  addStepRule,
  createPlaybookForDynamicAlert,
} = playbookSlice.actions;

export default playbookSlice.reducer;
