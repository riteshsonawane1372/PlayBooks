# Generated by Django 4.1.13 on 2024-06-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectors', '0015_migrate_remote_servers_to_metadata_model_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connector',
            name='connector_type',
            field=models.IntegerField(blank=True, choices=[(0, 'UNKNOWN'), (1, 'SENTRY'), (2, 'SEGMENT'), (3, 'ELASTIC_SEARCH'), (4, 'AMPLITUDE'), (5, 'AWS_KINESIS'), (6, 'CLOUDWATCH'), (7, 'CLEVERTAP'), (8, 'RUDDERSTACK'), (9, 'MOENGAGE'), (10, 'CRIBL'), (11, 'KAFKA'), (12, 'DATADOG'), (13, 'FILEBEAT'), (14, 'LOGSTASH'), (15, 'FLUENTD'), (16, 'FLUENTBIT'), (17, 'PAGER_DUTY'), (18, 'NEW_RELIC'), (19, 'SLACK'), (20, 'HONEYBADGER'), (21, 'GOOGLE_CHAT'), (22, 'DATADOG_OAUTH'), (23, 'GCM'), (24, 'PROMETHEUS'), (25, 'ELASTIC_APM'), (26, 'VICTORIA_METRICS'), (27, 'SLACK_CONNECT'), (28, 'GRAFANA'), (29, 'CLICKHOUSE'), (30, 'DOCUMENTATION'), (31, 'POSTGRES'), (32, 'OPS_GENIE'), (33, 'EKS'), (34, 'AGENT_PROXY'), (35, 'GRAFANA_VPC'), (36, 'GITHUB_ACTIONS'), (37, 'SQL_DATABASE_CONNECTION'), (38, 'OPEN_AI'), (39, 'REMOTE_SERVER'), (40, 'API'), (41, 'BASH'), (42, 'AZURE'), (43, 'GRAFANA_MIMIR'), (44, 'GKE'), (45, 'MS_TEAMS')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='connectorkey',
            name='key_type',
            field=models.IntegerField(blank=True, choices=[(0, 'UNKNOWN_SKT'), (1, 'SENTRY_API_KEY'), (6, 'SENTRY_ORG_SLUG'), (2, 'DATADOG_APP_KEY'), (3, 'DATADOG_API_KEY'), (15, 'DATADOG_AUTH_TOKEN'), (18, 'DATADOG_API_DOMAIN'), (4, 'NEWRELIC_API_KEY'), (5, 'NEWRELIC_APP_ID'), (7, 'NEWRELIC_QUERY_KEY'), (19, 'NEWRELIC_API_DOMAIN'), (8, 'SLACK_BOT_AUTH_TOKEN'), (9, 'SLACK_CHANNEL_ID'), (46, 'SLACK_APP_ID'), (10, 'HONEYBADGER_USERNAME'), (11, 'HONEYBADGER_PASSWORD'), (12, 'HONEYBADGER_PROJECT_ID'), (13, 'AWS_ACCESS_KEY'), (14, 'AWS_SECRET_KEY'), (20, 'AWS_REGION'), (23, 'AWS_ASSUMED_ROLE_ARN'), (40, 'EKS_ROLE_ARN'), (16, 'GOOGLE_CHAT_BOT_OAUTH_TOKEN'), (17, 'GOOGLE_CHAT_BOT_SPACES'), (21, 'GRAFANA_HOST'), (22, 'GRAFANA_API_KEY'), (24, 'CLICKHOUSE_INTERFACE'), (25, 'CLICKHOUSE_HOST'), (26, 'CLICKHOUSE_PORT'), (27, 'CLICKHOUSE_USER'), (28, 'CLICKHOUSE_PASSWORD'), (29, 'GCM_PROJECT_ID'), (30, 'GCM_PRIVATE_KEY'), (31, 'GCM_CLIENT_EMAIL'), (32, 'GCM_TOKEN_URI'), (33, 'POSTGRES_HOST'), (34, 'POSTGRES_USER'), (35, 'POSTGRES_PASSWORD'), (36, 'POSTGRES_PORT'), (37, 'POSTGRES_DATABASE'), (38, 'POSTGRES_OPTIONS'), (39, 'SQL_DATABASE_CONNECTION_STRING_URI'), (41, 'PAGER_DUTY_API_KEY'), (42, 'OPS_GENIE_API_KEY'), (43, 'AGENT_PROXY_HOST'), (44, 'AGENT_PROXY_API_KEY'), (45, 'GITHUB_ACTIONS_TOKEN'), (47, 'OPEN_AI_API_KEY'), (49, 'REMOTE_SERVER_PEM'), (50, 'REMOTE_SERVER_USER'), (51, 'REMOTE_SERVER_HOST'), (52, 'REMOTE_SERVER_PASSWORD'), (53, 'MIMIR_HOST'), (54, 'X_SCOPE_ORG_ID'), (55, 'SSL_VERIFY'), (56, 'AZURE_SUBSCRIPTION_ID'), (57, 'AZURE_TENANT_ID'), (58, 'AZURE_CLIENT_ID'), (59, 'AZURE_CLIENT_SECRET'), (60, 'GKE_PROJECT_ID'), (61, 'GKE_SERVICE_ACCOUNT_JSON'), (62, 'MS_TEAMS_CONNECTOR_WEBHOOK_URL')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='connectormetadatamodelstore',
            name='connector_type',
            field=models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'SENTRY'), (2, 'SEGMENT'), (3, 'ELASTIC_SEARCH'), (4, 'AMPLITUDE'), (5, 'AWS_KINESIS'), (6, 'CLOUDWATCH'), (7, 'CLEVERTAP'), (8, 'RUDDERSTACK'), (9, 'MOENGAGE'), (10, 'CRIBL'), (11, 'KAFKA'), (12, 'DATADOG'), (13, 'FILEBEAT'), (14, 'LOGSTASH'), (15, 'FLUENTD'), (16, 'FLUENTBIT'), (17, 'PAGER_DUTY'), (18, 'NEW_RELIC'), (19, 'SLACK'), (20, 'HONEYBADGER'), (21, 'GOOGLE_CHAT'), (22, 'DATADOG_OAUTH'), (23, 'GCM'), (24, 'PROMETHEUS'), (25, 'ELASTIC_APM'), (26, 'VICTORIA_METRICS'), (27, 'SLACK_CONNECT'), (28, 'GRAFANA'), (29, 'CLICKHOUSE'), (30, 'DOCUMENTATION'), (31, 'POSTGRES'), (32, 'OPS_GENIE'), (33, 'EKS'), (34, 'AGENT_PROXY'), (35, 'GRAFANA_VPC'), (36, 'GITHUB_ACTIONS'), (37, 'SQL_DATABASE_CONNECTION'), (38, 'OPEN_AI'), (39, 'REMOTE_SERVER'), (40, 'API'), (41, 'BASH'), (42, 'AZURE'), (43, 'GRAFANA_MIMIR'), (44, 'GKE'), (45, 'MS_TEAMS')], db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='connectormetadatamodelstore',
            name='model_type',
            field=models.IntegerField(choices=[(0, 'UNKNOWN_MT'), (1, 'NEW_RELIC_POLICY'), (2, 'NEW_RELIC_CONDITION'), (3, 'NEW_RELIC_ENTITY'), (4, 'NEW_RELIC_ENTITY_DASHBOARD'), (5, 'NEW_RELIC_ENTITY_APPLICATION'), (6, 'NEW_RELIC_NRQL'), (101, 'DATADOG_MONITOR'), (102, 'DATADOG_DASHBOARD'), (103, 'DATADOG_LIVE_INTEGRATION_AWS'), (104, 'DATADOG_LIVE_INTEGRATION_AWS_LOG'), (105, 'DATADOG_LIVE_INTEGRATION_AZURE'), (106, 'DATADOG_LIVE_INTEGRATION_CLOUDFLARE'), (107, 'DATADOG_LIVE_INTEGRATION_FASTLY'), (108, 'DATADOG_LIVE_INTEGRATION_GCP'), (109, 'DATADOG_LIVE_INTEGRATION_CONFLUENT'), (110, 'DATADOG_SERVICE'), (111, 'DATADOG_METRIC'), (112, 'DATADOG_QUERY'), (201, 'CLOUDWATCH_METRIC'), (202, 'CLOUDWATCH_LOG_GROUP'), (301, 'GRAFANA_DATASOURCE'), (302, 'GRAFANA_DASHBOARD'), (303, 'GRAFANA_TARGET_METRIC_PROMQL'), (304, 'GRAFANA_PROMETHEUS_DATASOURCE'), (401, 'CLICKHOUSE_DATABASE'), (501, 'SLACK_CHANNEL'), (601, 'MARKDOWN'), (602, 'IFRAME'), (701, 'POSTGRES_QUERY'), (801, 'EKS_CLUSTER'), (901, 'SQL_DATABASE_CONNECTION_RAW_QUERY'), (1001, 'AZURE_WORKSPACE'), (1100, 'SSH_SERVER'), (1201, 'GRAFANA_MIMIR_PROMQL'), (1301, 'GKE_CLUSTER'), (1401, 'MS_TEAMS_CHANNEL')], db_index=True, default=0),
        ),
    ]
