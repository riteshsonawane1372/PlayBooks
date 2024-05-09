"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ConnectorType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ConnectorTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ConnectorType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _ConnectorType.ValueType  # 0
    SENTRY: _ConnectorType.ValueType  # 1
    SEGMENT: _ConnectorType.ValueType  # 2
    ELASTIC_SEARCH: _ConnectorType.ValueType  # 3
    AMPLITUDE: _ConnectorType.ValueType  # 4
    AWS_KINESIS: _ConnectorType.ValueType  # 5
    CLOUDWATCH: _ConnectorType.ValueType  # 6
    CLEVERTAP: _ConnectorType.ValueType  # 7
    RUDDERSTACK: _ConnectorType.ValueType  # 8
    MOENGAGE: _ConnectorType.ValueType  # 9
    CRIBL: _ConnectorType.ValueType  # 10
    KAFKA: _ConnectorType.ValueType  # 11
    DATADOG: _ConnectorType.ValueType  # 12
    FILEBEAT: _ConnectorType.ValueType  # 13
    LOGSTASH: _ConnectorType.ValueType  # 14
    FLUENTD: _ConnectorType.ValueType  # 15
    FLUENTBIT: _ConnectorType.ValueType  # 16
    PAGER_DUTY: _ConnectorType.ValueType  # 17
    NEW_RELIC: _ConnectorType.ValueType  # 18
    SLACK: _ConnectorType.ValueType  # 19
    HONEYBADGER: _ConnectorType.ValueType  # 20
    GOOGLE_CHAT: _ConnectorType.ValueType  # 21
    DATADOG_OAUTH: _ConnectorType.ValueType  # 22
    GCM: _ConnectorType.ValueType  # 23
    PROMETHEUS: _ConnectorType.ValueType  # 24
    ELASTIC_APM: _ConnectorType.ValueType  # 25
    VICTORIA_METRICS: _ConnectorType.ValueType  # 26
    SLACK_CONNECT: _ConnectorType.ValueType  # 27
    GRAFANA: _ConnectorType.ValueType  # 28
    CLICKHOUSE: _ConnectorType.ValueType  # 29
    DOCUMENTATION: _ConnectorType.ValueType  # 30
    POSTGRES: _ConnectorType.ValueType  # 31
    OPS_GENIE: _ConnectorType.ValueType  # 32
    EKS: _ConnectorType.ValueType  # 33
    AGENT_PROXY: _ConnectorType.ValueType  # 34
    GRAFANA_VPC: _ConnectorType.ValueType  # 35
    GITHUB_ACTIONS: _ConnectorType.ValueType  # 36
    SQL_DATABASE_CONNECTION: _ConnectorType.ValueType  # 37
    OPEN_AI: _ConnectorType.ValueType  # 38
    REMOTE_SERVER: _ConnectorType.ValueType  # 39

class ConnectorType(_ConnectorType, metaclass=_ConnectorTypeEnumTypeWrapper): ...

UNKNOWN: ConnectorType.ValueType  # 0
SENTRY: ConnectorType.ValueType  # 1
SEGMENT: ConnectorType.ValueType  # 2
ELASTIC_SEARCH: ConnectorType.ValueType  # 3
AMPLITUDE: ConnectorType.ValueType  # 4
AWS_KINESIS: ConnectorType.ValueType  # 5
CLOUDWATCH: ConnectorType.ValueType  # 6
CLEVERTAP: ConnectorType.ValueType  # 7
RUDDERSTACK: ConnectorType.ValueType  # 8
MOENGAGE: ConnectorType.ValueType  # 9
CRIBL: ConnectorType.ValueType  # 10
KAFKA: ConnectorType.ValueType  # 11
DATADOG: ConnectorType.ValueType  # 12
FILEBEAT: ConnectorType.ValueType  # 13
LOGSTASH: ConnectorType.ValueType  # 14
FLUENTD: ConnectorType.ValueType  # 15
FLUENTBIT: ConnectorType.ValueType  # 16
PAGER_DUTY: ConnectorType.ValueType  # 17
NEW_RELIC: ConnectorType.ValueType  # 18
SLACK: ConnectorType.ValueType  # 19
HONEYBADGER: ConnectorType.ValueType  # 20
GOOGLE_CHAT: ConnectorType.ValueType  # 21
DATADOG_OAUTH: ConnectorType.ValueType  # 22
GCM: ConnectorType.ValueType  # 23
PROMETHEUS: ConnectorType.ValueType  # 24
ELASTIC_APM: ConnectorType.ValueType  # 25
VICTORIA_METRICS: ConnectorType.ValueType  # 26
SLACK_CONNECT: ConnectorType.ValueType  # 27
GRAFANA: ConnectorType.ValueType  # 28
CLICKHOUSE: ConnectorType.ValueType  # 29
DOCUMENTATION: ConnectorType.ValueType  # 30
POSTGRES: ConnectorType.ValueType  # 31
OPS_GENIE: ConnectorType.ValueType  # 32
EKS: ConnectorType.ValueType  # 33
AGENT_PROXY: ConnectorType.ValueType  # 34
GRAFANA_VPC: ConnectorType.ValueType  # 35
GITHUB_ACTIONS: ConnectorType.ValueType  # 36
SQL_DATABASE_CONNECTION: ConnectorType.ValueType  # 37
OPEN_AI: ConnectorType.ValueType  # 38
REMOTE_SERVER: ConnectorType.ValueType  # 39
global___ConnectorType = ConnectorType

class _ConnectorMetadataModelType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ConnectorMetadataModelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ConnectorMetadataModelType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_MT: _ConnectorMetadataModelType.ValueType  # 0
    NEW_RELIC_POLICY: _ConnectorMetadataModelType.ValueType  # 1
    """New Relic Models"""
    NEW_RELIC_CONDITION: _ConnectorMetadataModelType.ValueType  # 2
    NEW_RELIC_ENTITY: _ConnectorMetadataModelType.ValueType  # 3
    NEW_RELIC_ENTITY_DASHBOARD: _ConnectorMetadataModelType.ValueType  # 4
    NEW_RELIC_ENTITY_APPLICATION: _ConnectorMetadataModelType.ValueType  # 5
    NEW_RELIC_NRQL: _ConnectorMetadataModelType.ValueType  # 6
    DATADOG_MONITOR: _ConnectorMetadataModelType.ValueType  # 101
    """Datadog Models"""
    DATADOG_DASHBOARD: _ConnectorMetadataModelType.ValueType  # 102
    DATADOG_LIVE_INTEGRATION_AWS: _ConnectorMetadataModelType.ValueType  # 103
    DATADOG_LIVE_INTEGRATION_AWS_LOG: _ConnectorMetadataModelType.ValueType  # 104
    DATADOG_LIVE_INTEGRATION_AZURE: _ConnectorMetadataModelType.ValueType  # 105
    DATADOG_LIVE_INTEGRATION_CLOUDFLARE: _ConnectorMetadataModelType.ValueType  # 106
    DATADOG_LIVE_INTEGRATION_FASTLY: _ConnectorMetadataModelType.ValueType  # 107
    DATADOG_LIVE_INTEGRATION_GCP: _ConnectorMetadataModelType.ValueType  # 108
    DATADOG_LIVE_INTEGRATION_CONFLUENT: _ConnectorMetadataModelType.ValueType  # 109
    DATADOG_SERVICE: _ConnectorMetadataModelType.ValueType  # 110
    DATADOG_METRIC: _ConnectorMetadataModelType.ValueType  # 111
    DATADOG_QUERY: _ConnectorMetadataModelType.ValueType  # 112
    CLOUDWATCH_METRIC: _ConnectorMetadataModelType.ValueType  # 201
    """Cloudwatch Models"""
    CLOUDWATCH_LOG_GROUP: _ConnectorMetadataModelType.ValueType  # 202
    GRAFANA_DATASOURCE: _ConnectorMetadataModelType.ValueType  # 301
    """Grafana Models"""
    GRAFANA_DASHBOARD: _ConnectorMetadataModelType.ValueType  # 302
    GRAFANA_TARGET_METRIC_PROMQL: _ConnectorMetadataModelType.ValueType  # 303
    CLICKHOUSE_DATABASE: _ConnectorMetadataModelType.ValueType  # 401
    """Clickhouse Models"""
    SLACK_CHANNEL: _ConnectorMetadataModelType.ValueType  # 501
    """Slack Models"""
    MARKDOWN: _ConnectorMetadataModelType.ValueType  # 601
    """Documentation Models"""
    POSTGRES_DATABASE: _ConnectorMetadataModelType.ValueType  # 701
    """Postgres Models"""
    EKS_CLUSTER: _ConnectorMetadataModelType.ValueType  # 801
    """EKS Models"""
    SQL_DATABASE_CONNECTION_RAW_QUERY: _ConnectorMetadataModelType.ValueType  # 901
    """Sql Database Connection Models"""
    SSH_SERVER: _ConnectorMetadataModelType.ValueType  # 1100
    """Remote Server Models"""

class ConnectorMetadataModelType(_ConnectorMetadataModelType, metaclass=_ConnectorMetadataModelTypeEnumTypeWrapper): ...

UNKNOWN_MT: ConnectorMetadataModelType.ValueType  # 0
NEW_RELIC_POLICY: ConnectorMetadataModelType.ValueType  # 1
"""New Relic Models"""
NEW_RELIC_CONDITION: ConnectorMetadataModelType.ValueType  # 2
NEW_RELIC_ENTITY: ConnectorMetadataModelType.ValueType  # 3
NEW_RELIC_ENTITY_DASHBOARD: ConnectorMetadataModelType.ValueType  # 4
NEW_RELIC_ENTITY_APPLICATION: ConnectorMetadataModelType.ValueType  # 5
NEW_RELIC_NRQL: ConnectorMetadataModelType.ValueType  # 6
DATADOG_MONITOR: ConnectorMetadataModelType.ValueType  # 101
"""Datadog Models"""
DATADOG_DASHBOARD: ConnectorMetadataModelType.ValueType  # 102
DATADOG_LIVE_INTEGRATION_AWS: ConnectorMetadataModelType.ValueType  # 103
DATADOG_LIVE_INTEGRATION_AWS_LOG: ConnectorMetadataModelType.ValueType  # 104
DATADOG_LIVE_INTEGRATION_AZURE: ConnectorMetadataModelType.ValueType  # 105
DATADOG_LIVE_INTEGRATION_CLOUDFLARE: ConnectorMetadataModelType.ValueType  # 106
DATADOG_LIVE_INTEGRATION_FASTLY: ConnectorMetadataModelType.ValueType  # 107
DATADOG_LIVE_INTEGRATION_GCP: ConnectorMetadataModelType.ValueType  # 108
DATADOG_LIVE_INTEGRATION_CONFLUENT: ConnectorMetadataModelType.ValueType  # 109
DATADOG_SERVICE: ConnectorMetadataModelType.ValueType  # 110
DATADOG_METRIC: ConnectorMetadataModelType.ValueType  # 111
DATADOG_QUERY: ConnectorMetadataModelType.ValueType  # 112
CLOUDWATCH_METRIC: ConnectorMetadataModelType.ValueType  # 201
"""Cloudwatch Models"""
CLOUDWATCH_LOG_GROUP: ConnectorMetadataModelType.ValueType  # 202
GRAFANA_DATASOURCE: ConnectorMetadataModelType.ValueType  # 301
"""Grafana Models"""
GRAFANA_DASHBOARD: ConnectorMetadataModelType.ValueType  # 302
GRAFANA_TARGET_METRIC_PROMQL: ConnectorMetadataModelType.ValueType  # 303
CLICKHOUSE_DATABASE: ConnectorMetadataModelType.ValueType  # 401
"""Clickhouse Models"""
SLACK_CHANNEL: ConnectorMetadataModelType.ValueType  # 501
"""Slack Models"""
MARKDOWN: ConnectorMetadataModelType.ValueType  # 601
"""Documentation Models"""
POSTGRES_DATABASE: ConnectorMetadataModelType.ValueType  # 701
"""Postgres Models"""
EKS_CLUSTER: ConnectorMetadataModelType.ValueType  # 801
"""EKS Models"""
SQL_DATABASE_CONNECTION_RAW_QUERY: ConnectorMetadataModelType.ValueType  # 901
"""Sql Database Connection Models"""
SSH_SERVER: ConnectorMetadataModelType.ValueType  # 1100
"""Remote Server Models"""
global___ConnectorMetadataModelType = ConnectorMetadataModelType

class _TransformerType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TransformerTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TransformerType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_TT: _TransformerType.ValueType  # 0
    SEGMENT_DFAULT_TRANSFORMER: _TransformerType.ValueType  # 2
    AMPLITUDE_DEFAULT_TRANSFORMER: _TransformerType.ValueType  # 3
    PRODIGAL_CLOUDWATCH_LOG_TRANSFORMER: _TransformerType.ValueType  # 4
    CLOUDWATCH_JSON_LOG_TRANSFORMER: _TransformerType.ValueType  # 5

class TransformerType(_TransformerType, metaclass=_TransformerTypeEnumTypeWrapper): ...

UNKNOWN_TT: TransformerType.ValueType  # 0
SEGMENT_DFAULT_TRANSFORMER: TransformerType.ValueType  # 2
AMPLITUDE_DEFAULT_TRANSFORMER: TransformerType.ValueType  # 3
PRODIGAL_CLOUDWATCH_LOG_TRANSFORMER: TransformerType.ValueType  # 4
CLOUDWATCH_JSON_LOG_TRANSFORMER: TransformerType.ValueType  # 5
global___TransformerType = TransformerType

class _DecoderType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DecoderTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DecoderType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_DT: _DecoderType.ValueType  # 0
    AWS_KINESIS_DECODER: _DecoderType.ValueType  # 1
    AWS_CLOUDWATCH_KINESIS_DECODER: _DecoderType.ValueType  # 2

class DecoderType(_DecoderType, metaclass=_DecoderTypeEnumTypeWrapper): ...

UNKNOWN_DT: DecoderType.ValueType  # 0
AWS_KINESIS_DECODER: DecoderType.ValueType  # 1
AWS_CLOUDWATCH_KINESIS_DECODER: DecoderType.ValueType  # 2
global___DecoderType = DecoderType

class _ReportType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReportTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReportType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_RT: _ReportType.ValueType  # 0
    INITIAL: _ReportType.ValueType  # 1
    FINAL: _ReportType.ValueType  # 2

class ReportType(_ReportType, metaclass=_ReportTypeEnumTypeWrapper): ...

UNKNOWN_RT: ReportType.ValueType  # 0
INITIAL: ReportType.ValueType  # 1
FINAL: ReportType.ValueType  # 2
global___ReportType = ReportType

@typing_extensions.final
class PeriodicRunStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _StatusType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PeriodicRunStatus._StatusType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: PeriodicRunStatus._StatusType.ValueType  # 0
        STARTED: PeriodicRunStatus._StatusType.ValueType  # 1
        FINISHED: PeriodicRunStatus._StatusType.ValueType  # 2
        ERROR: PeriodicRunStatus._StatusType.ValueType  # 3

    class StatusType(_StatusType, metaclass=_StatusTypeEnumTypeWrapper): ...
    UNKNOWN: PeriodicRunStatus.StatusType.ValueType  # 0
    STARTED: PeriodicRunStatus.StatusType.ValueType  # 1
    FINISHED: PeriodicRunStatus.StatusType.ValueType  # 2
    ERROR: PeriodicRunStatus.StatusType.ValueType  # 3

    def __init__(
        self,
    ) -> None: ...

global___PeriodicRunStatus = PeriodicRunStatus

@typing_extensions.final
class Connector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    SENTRY_CONFIG_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    type: global___ConnectorType.ValueType
    @property
    def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    created_at: builtins.int
    updated_at: builtins.int
    @property
    def display_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def category(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def sentry_config(self) -> global___SentryConnectorConfig: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        type: global___ConnectorType.ValueType = ...,
        is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_by: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_at: builtins.int = ...,
        updated_at: builtins.int = ...,
        display_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        category: google.protobuf.wrappers_pb2.StringValue | None = ...,
        sentry_config: global___SentryConnectorConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["category", b"category", "config", b"config", "created_by", b"created_by", "display_name", b"display_name", "id", b"id", "is_active", b"is_active", "name", b"name", "sentry_config", b"sentry_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["category", b"category", "config", b"config", "created_at", b"created_at", "created_by", b"created_by", "display_name", b"display_name", "id", b"id", "is_active", b"is_active", "name", b"name", "sentry_config", b"sentry_config", "type", b"type", "updated_at", b"updated_at"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["sentry_config"] | None: ...

global___Connector = Connector

@typing_extensions.final
class SentryConnectorConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLLING_FREQUENCY_FIELD_NUMBER: builtins.int
    @property
    def polling_frequency(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    def __init__(
        self,
        *,
        polling_frequency: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["polling_frequency", b"polling_frequency"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["polling_frequency", b"polling_frequency"]) -> None: ...

global___SentryConnectorConfig = SentryConnectorConfig

@typing_extensions.final
class ConnectorKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _KeyType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _KeyTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ConnectorKey._KeyType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: ConnectorKey._KeyType.ValueType  # 0
        SENTRY_API_KEY: ConnectorKey._KeyType.ValueType  # 1
        SENTRY_ORG_SLUG: ConnectorKey._KeyType.ValueType  # 6
        DATADOG_APP_KEY: ConnectorKey._KeyType.ValueType  # 2
        DATADOG_API_KEY: ConnectorKey._KeyType.ValueType  # 3
        DATADOG_AUTH_TOKEN: ConnectorKey._KeyType.ValueType  # 15
        DATADOG_API_DOMAIN: ConnectorKey._KeyType.ValueType  # 18
        NEWRELIC_API_KEY: ConnectorKey._KeyType.ValueType  # 4
        NEWRELIC_APP_ID: ConnectorKey._KeyType.ValueType  # 5
        NEWRELIC_QUERY_KEY: ConnectorKey._KeyType.ValueType  # 7
        NEWRELIC_API_DOMAIN: ConnectorKey._KeyType.ValueType  # 19
        SLACK_BOT_AUTH_TOKEN: ConnectorKey._KeyType.ValueType  # 8
        SLACK_CHANNEL: ConnectorKey._KeyType.ValueType  # 9
        HONEYBADGER_USERNAME: ConnectorKey._KeyType.ValueType  # 10
        HONEYBADGER_PASSWORD: ConnectorKey._KeyType.ValueType  # 11
        HONEYBADGER_PROJECT_ID: ConnectorKey._KeyType.ValueType  # 12
        AWS_ACCESS_KEY: ConnectorKey._KeyType.ValueType  # 13
        AWS_SECRET_KEY: ConnectorKey._KeyType.ValueType  # 14
        AWS_REGION: ConnectorKey._KeyType.ValueType  # 20
        AWS_ASSUMED_ROLE_ARN: ConnectorKey._KeyType.ValueType  # 23
        EKS_ROLE_ARN: ConnectorKey._KeyType.ValueType  # 40
        GOOGLE_CHAT_BOT_OAUTH_TOKEN: ConnectorKey._KeyType.ValueType  # 16
        GOOGLE_CHAT_BOT_SPACES: ConnectorKey._KeyType.ValueType  # 17
        GRAFANA_HOST: ConnectorKey._KeyType.ValueType  # 21
        GRAFANA_API_KEY: ConnectorKey._KeyType.ValueType  # 22
        CLICKHOUSE_INTERFACE: ConnectorKey._KeyType.ValueType  # 24
        CLICKHOUSE_HOST: ConnectorKey._KeyType.ValueType  # 25
        CLICKHOUSE_PORT: ConnectorKey._KeyType.ValueType  # 26
        CLICKHOUSE_USER: ConnectorKey._KeyType.ValueType  # 27
        CLICKHOUSE_PASSWORD: ConnectorKey._KeyType.ValueType  # 28
        GCM_PROJECT_ID: ConnectorKey._KeyType.ValueType  # 29
        GCM_PRIVATE_KEY: ConnectorKey._KeyType.ValueType  # 30
        GCM_CLIENT_EMAIL: ConnectorKey._KeyType.ValueType  # 31
        GCM_TOKEN_URI: ConnectorKey._KeyType.ValueType  # 32
        POSTGRES_HOST: ConnectorKey._KeyType.ValueType  # 33
        POSTGRES_USER: ConnectorKey._KeyType.ValueType  # 34
        POSTGRES_PASSWORD: ConnectorKey._KeyType.ValueType  # 35
        POSTGRES_PORT: ConnectorKey._KeyType.ValueType  # 36
        POSTGRES_DATABASE: ConnectorKey._KeyType.ValueType  # 37
        POSTGRES_OPTIONS: ConnectorKey._KeyType.ValueType  # 38
        SQL_DATABASE_CONNECTION_STRING_URI: ConnectorKey._KeyType.ValueType  # 39
        PAGER_DUTY_API_KEY: ConnectorKey._KeyType.ValueType  # 41
        OPS_GENIE_API_KEY: ConnectorKey._KeyType.ValueType  # 42
        AGENT_PROXY_HOST: ConnectorKey._KeyType.ValueType  # 43
        AGENT_PROXY_API_KEY: ConnectorKey._KeyType.ValueType  # 44
        GITHUB_ACTIONS_TOKEN: ConnectorKey._KeyType.ValueType  # 45
        SLACK_APP_ID: ConnectorKey._KeyType.ValueType  # 46
        OPEN_AI_API_KEY: ConnectorKey._KeyType.ValueType  # 47
        REMOTE_SERVER_PEM: ConnectorKey._KeyType.ValueType  # 49
        REMOTE_SERVER_USER: ConnectorKey._KeyType.ValueType  # 50
        REMOTE_SERVER_HOST: ConnectorKey._KeyType.ValueType  # 51
        REMOTE_SERVER_PASSWORD: ConnectorKey._KeyType.ValueType  # 52

    class KeyType(_KeyType, metaclass=_KeyTypeEnumTypeWrapper): ...
    UNKNOWN: ConnectorKey.KeyType.ValueType  # 0
    SENTRY_API_KEY: ConnectorKey.KeyType.ValueType  # 1
    SENTRY_ORG_SLUG: ConnectorKey.KeyType.ValueType  # 6
    DATADOG_APP_KEY: ConnectorKey.KeyType.ValueType  # 2
    DATADOG_API_KEY: ConnectorKey.KeyType.ValueType  # 3
    DATADOG_AUTH_TOKEN: ConnectorKey.KeyType.ValueType  # 15
    DATADOG_API_DOMAIN: ConnectorKey.KeyType.ValueType  # 18
    NEWRELIC_API_KEY: ConnectorKey.KeyType.ValueType  # 4
    NEWRELIC_APP_ID: ConnectorKey.KeyType.ValueType  # 5
    NEWRELIC_QUERY_KEY: ConnectorKey.KeyType.ValueType  # 7
    NEWRELIC_API_DOMAIN: ConnectorKey.KeyType.ValueType  # 19
    SLACK_BOT_AUTH_TOKEN: ConnectorKey.KeyType.ValueType  # 8
    SLACK_CHANNEL: ConnectorKey.KeyType.ValueType  # 9
    HONEYBADGER_USERNAME: ConnectorKey.KeyType.ValueType  # 10
    HONEYBADGER_PASSWORD: ConnectorKey.KeyType.ValueType  # 11
    HONEYBADGER_PROJECT_ID: ConnectorKey.KeyType.ValueType  # 12
    AWS_ACCESS_KEY: ConnectorKey.KeyType.ValueType  # 13
    AWS_SECRET_KEY: ConnectorKey.KeyType.ValueType  # 14
    AWS_REGION: ConnectorKey.KeyType.ValueType  # 20
    AWS_ASSUMED_ROLE_ARN: ConnectorKey.KeyType.ValueType  # 23
    EKS_ROLE_ARN: ConnectorKey.KeyType.ValueType  # 40
    GOOGLE_CHAT_BOT_OAUTH_TOKEN: ConnectorKey.KeyType.ValueType  # 16
    GOOGLE_CHAT_BOT_SPACES: ConnectorKey.KeyType.ValueType  # 17
    GRAFANA_HOST: ConnectorKey.KeyType.ValueType  # 21
    GRAFANA_API_KEY: ConnectorKey.KeyType.ValueType  # 22
    CLICKHOUSE_INTERFACE: ConnectorKey.KeyType.ValueType  # 24
    CLICKHOUSE_HOST: ConnectorKey.KeyType.ValueType  # 25
    CLICKHOUSE_PORT: ConnectorKey.KeyType.ValueType  # 26
    CLICKHOUSE_USER: ConnectorKey.KeyType.ValueType  # 27
    CLICKHOUSE_PASSWORD: ConnectorKey.KeyType.ValueType  # 28
    GCM_PROJECT_ID: ConnectorKey.KeyType.ValueType  # 29
    GCM_PRIVATE_KEY: ConnectorKey.KeyType.ValueType  # 30
    GCM_CLIENT_EMAIL: ConnectorKey.KeyType.ValueType  # 31
    GCM_TOKEN_URI: ConnectorKey.KeyType.ValueType  # 32
    POSTGRES_HOST: ConnectorKey.KeyType.ValueType  # 33
    POSTGRES_USER: ConnectorKey.KeyType.ValueType  # 34
    POSTGRES_PASSWORD: ConnectorKey.KeyType.ValueType  # 35
    POSTGRES_PORT: ConnectorKey.KeyType.ValueType  # 36
    POSTGRES_DATABASE: ConnectorKey.KeyType.ValueType  # 37
    POSTGRES_OPTIONS: ConnectorKey.KeyType.ValueType  # 38
    SQL_DATABASE_CONNECTION_STRING_URI: ConnectorKey.KeyType.ValueType  # 39
    PAGER_DUTY_API_KEY: ConnectorKey.KeyType.ValueType  # 41
    OPS_GENIE_API_KEY: ConnectorKey.KeyType.ValueType  # 42
    AGENT_PROXY_HOST: ConnectorKey.KeyType.ValueType  # 43
    AGENT_PROXY_API_KEY: ConnectorKey.KeyType.ValueType  # 44
    GITHUB_ACTIONS_TOKEN: ConnectorKey.KeyType.ValueType  # 45
    SLACK_APP_ID: ConnectorKey.KeyType.ValueType  # 46
    OPEN_AI_API_KEY: ConnectorKey.KeyType.ValueType  # 47
    REMOTE_SERVER_PEM: ConnectorKey.KeyType.ValueType  # 49
    REMOTE_SERVER_USER: ConnectorKey.KeyType.ValueType  # 50
    REMOTE_SERVER_HOST: ConnectorKey.KeyType.ValueType  # 51
    REMOTE_SERVER_PASSWORD: ConnectorKey.KeyType.ValueType  # 52

    ID_FIELD_NUMBER: builtins.int
    KEY_TYPE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    key_type: global___ConnectorKey.KeyType.ValueType
    @property
    def key(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def connector_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    created_at: builtins.int
    updated_at: builtins.int
    @property
    def display_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        key_type: global___ConnectorKey.KeyType.ValueType = ...,
        key: google.protobuf.wrappers_pb2.StringValue | None = ...,
        is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        connector_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        created_at: builtins.int = ...,
        updated_at: builtins.int = ...,
        display_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id", "display_name", b"display_name", "id", b"id", "is_active", b"is_active", "key", b"key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id", "created_at", b"created_at", "display_name", b"display_name", "id", b"id", "is_active", b"is_active", "key", b"key", "key_type", b"key_type", "updated_at", b"updated_at"]) -> None: ...

global___ConnectorKey = ConnectorKey

@typing_extensions.final
class UpdateConnectorOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Op:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OpEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[UpdateConnectorOp._Op.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: UpdateConnectorOp._Op.ValueType  # 0
        UPDATE_CONNECTOR_NAME: UpdateConnectorOp._Op.ValueType  # 1
        UPDATE_CONNECTOR_STATUS: UpdateConnectorOp._Op.ValueType  # 2
        UPDATE_CONNECTOR_KEYS: UpdateConnectorOp._Op.ValueType  # 3

    class Op(_Op, metaclass=_OpEnumTypeWrapper): ...
    UNKNOWN: UpdateConnectorOp.Op.ValueType  # 0
    UPDATE_CONNECTOR_NAME: UpdateConnectorOp.Op.ValueType  # 1
    UPDATE_CONNECTOR_STATUS: UpdateConnectorOp.Op.ValueType  # 2
    UPDATE_CONNECTOR_KEYS: UpdateConnectorOp.Op.ValueType  # 3

    @typing_extensions.final
    class UpdateConnectorName(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        @property
        def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["name", b"name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

    @typing_extensions.final
    class UpdateConnectorStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateConnectorKeys(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CONNECTOR_KEYS_FIELD_NUMBER: builtins.int
        @property
        def connector_keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ConnectorKey]: ...
        def __init__(
            self,
            *,
            connector_keys: collections.abc.Iterable[global___ConnectorKey] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["connector_keys", b"connector_keys"]) -> None: ...

    OP_FIELD_NUMBER: builtins.int
    UPDATE_CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    UPDATE_CONNECTOR_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_CONNECTOR_KEYS_FIELD_NUMBER: builtins.int
    op: global___UpdateConnectorOp.Op.ValueType
    @property
    def update_connector_name(self) -> global___UpdateConnectorOp.UpdateConnectorName: ...
    @property
    def update_connector_status(self) -> global___UpdateConnectorOp.UpdateConnectorStatus: ...
    @property
    def update_connector_keys(self) -> global___UpdateConnectorOp.UpdateConnectorKeys: ...
    def __init__(
        self,
        *,
        op: global___UpdateConnectorOp.Op.ValueType = ...,
        update_connector_name: global___UpdateConnectorOp.UpdateConnectorName | None = ...,
        update_connector_status: global___UpdateConnectorOp.UpdateConnectorStatus | None = ...,
        update_connector_keys: global___UpdateConnectorOp.UpdateConnectorKeys | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update", b"update", "update_connector_keys", b"update_connector_keys", "update_connector_name", b"update_connector_name", "update_connector_status", b"update_connector_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["op", b"op", "update", b"update", "update_connector_keys", b"update_connector_keys", "update_connector_name", b"update_connector_name", "update_connector_status", b"update_connector_status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["update", b"update"]) -> typing_extensions.Literal["update_connector_name", "update_connector_status", "update_connector_keys"] | None: ...

global___UpdateConnectorOp = UpdateConnectorOp

@typing_extensions.final
class AccountActiveConnectorModelTypes(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConnectorMetadataModelTypeMap(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MODEL_TYPE_FIELD_NUMBER: builtins.int
        DISPLAY_NAME_FIELD_NUMBER: builtins.int
        model_type: global___ConnectorMetadataModelType.ValueType
        @property
        def display_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            model_type: global___ConnectorMetadataModelType.ValueType = ...,
            display_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["display_name", b"display_name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["display_name", b"display_name", "model_type", b"model_type"]) -> None: ...

    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    MODEL_TYPES_MAP_FIELD_NUMBER: builtins.int
    connector_type: global___ConnectorType.ValueType
    @property
    def model_types_map(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AccountActiveConnectorModelTypes.ConnectorMetadataModelTypeMap]: ...
    def __init__(
        self,
        *,
        connector_type: global___ConnectorType.ValueType = ...,
        model_types_map: collections.abc.Iterable[global___AccountActiveConnectorModelTypes.ConnectorMetadataModelTypeMap] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_type", b"connector_type", "model_types_map", b"model_types_map"]) -> None: ...

global___AccountActiveConnectorModelTypes = AccountActiveConnectorModelTypes
