import { PageKeys } from "./pageKeys";

export const routes = {
  [PageKeys.LOGIN]: "/login",
  [PageKeys.SIGNUP]: "/signup",
  [PageKeys.RESET_PASSWORD]: "/reset-password",
  [PageKeys.OAUTH_CALLBACK]: "/oauth/callback/:oauthId",
  [PageKeys.PLAYBOOKS_CREATE]: "/playbooks/create",
  [PageKeys.PLAYBOOK_VIEW]: "/playbooks/:playbook_id",
  [PageKeys.PLAYBOOK_LOGS]: "/playbooks/logs/:playbook_run_id",
  [PageKeys.PLAYBOOK_EDIT]: "/playbooks/edit/:playbook_id",
  [PageKeys.HOME]: "/",
  [PageKeys.SETTINGS]: "/settings",
  [PageKeys.PLAYBOOKS]: "/playbooks",
  [PageKeys.PLAYBOOK_EXECUTIONS_LIST]: "/playbooks/executions/list",
  [PageKeys.PLAYBOOK_EXECUTIONS]: "/playbooks/executions/:id",
  [PageKeys.WORKFLOWS_CREATE]: "/workflows/create",
  [PageKeys.WORKFLOWS]: "/workflows",
  [PageKeys.WORKFLOW_VIEW]: "/workflows/:id",
  [PageKeys.WORKFLOW_EXECUTIONS]: "/workflows/executions/:id",
  [PageKeys.WORKFLOW_EXECUTIONS_LIST]: "/executions/list",
  [PageKeys.WORKFLOW_EXECUTION_LOGS]: "/workflows/logs/:workflow_run_id",
  [PageKeys.PLAYGROUND]: "/playgrounds",
  [PageKeys.INTEGRATIONS_ADD]: "/data-sources/add",
  [PageKeys.DATA_SOURCES]: "/data-sources",
  [PageKeys.CONNECTOR_PAGE]: "/data-sources/:connectorEnum",
  [PageKeys.CONNECTOR_PAGE_ID]: "/data-sources/:connectorEnum/:id",
  [PageKeys.API_TOKENS]: "/settings/api-keys",
  [PageKeys.INVITE_TEAM]: "/settings/invite-team",
  [PageKeys.SUPPORT]: "/support",
  [PageKeys.NOT_FOUND]: "*",
};
