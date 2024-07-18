"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
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

@typing_extensions.final
class Gke(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _TaskType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TaskTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Gke._TaskType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Gke._TaskType.ValueType  # 0
        GET_PODS: Gke._TaskType.ValueType  # 1
        GET_DEPLOYMENTS: Gke._TaskType.ValueType  # 2
        GET_EVENTS: Gke._TaskType.ValueType  # 3
        GET_SERVICES: Gke._TaskType.ValueType  # 4
        KUBECTL_COMMAND: Gke._TaskType.ValueType  # 5

    class TaskType(_TaskType, metaclass=_TaskTypeEnumTypeWrapper): ...
    UNKNOWN: Gke.TaskType.ValueType  # 0
    GET_PODS: Gke.TaskType.ValueType  # 1
    GET_DEPLOYMENTS: Gke.TaskType.ValueType  # 2
    GET_EVENTS: Gke.TaskType.ValueType  # 3
    GET_SERVICES: Gke.TaskType.ValueType  # 4
    KUBECTL_COMMAND: Gke.TaskType.ValueType  # 5

    @typing_extensions.final
    class Command(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DESCRIPTION_FIELD_NUMBER: builtins.int
        ZONE_FIELD_NUMBER: builtins.int
        CLUSTER_FIELD_NUMBER: builtins.int
        NAMESPACE_FIELD_NUMBER: builtins.int
        @property
        def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def zone(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def cluster(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def namespace(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            description: google.protobuf.wrappers_pb2.StringValue | None = ...,
            zone: google.protobuf.wrappers_pb2.StringValue | None = ...,
            cluster: google.protobuf.wrappers_pb2.StringValue | None = ...,
            namespace: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["cluster", b"cluster", "description", b"description", "namespace", b"namespace", "zone", b"zone"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["cluster", b"cluster", "description", b"description", "namespace", b"namespace", "zone", b"zone"]) -> None: ...

    @typing_extensions.final
    class KubectlCommand(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ZONE_FIELD_NUMBER: builtins.int
        CLUSTER_FIELD_NUMBER: builtins.int
        COMMAND_FIELD_NUMBER: builtins.int
        @property
        def zone(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def cluster(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def command(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            zone: google.protobuf.wrappers_pb2.StringValue | None = ...,
            cluster: google.protobuf.wrappers_pb2.StringValue | None = ...,
            command: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["cluster", b"cluster", "command", b"command", "zone", b"zone"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["cluster", b"cluster", "command", b"command", "zone", b"zone"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    GET_PODS_FIELD_NUMBER: builtins.int
    GET_DEPLOYMENTS_FIELD_NUMBER: builtins.int
    GET_EVENTS_FIELD_NUMBER: builtins.int
    GET_SERVICES_FIELD_NUMBER: builtins.int
    KUBECTL_COMMAND_FIELD_NUMBER: builtins.int
    type: global___Gke.TaskType.ValueType
    @property
    def get_pods(self) -> global___Gke.Command: ...
    @property
    def get_deployments(self) -> global___Gke.Command: ...
    @property
    def get_events(self) -> global___Gke.Command: ...
    @property
    def get_services(self) -> global___Gke.Command: ...
    @property
    def kubectl_command(self) -> global___Gke.KubectlCommand: ...
    def __init__(
        self,
        *,
        type: global___Gke.TaskType.ValueType = ...,
        get_pods: global___Gke.Command | None = ...,
        get_deployments: global___Gke.Command | None = ...,
        get_events: global___Gke.Command | None = ...,
        get_services: global___Gke.Command | None = ...,
        kubectl_command: global___Gke.KubectlCommand | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["get_deployments", b"get_deployments", "get_events", b"get_events", "get_pods", b"get_pods", "get_services", b"get_services", "kubectl_command", b"kubectl_command", "task", b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["get_deployments", b"get_deployments", "get_events", b"get_events", "get_pods", b"get_pods", "get_services", b"get_services", "kubectl_command", b"kubectl_command", "task", b"task", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["task", b"task"]) -> typing_extensions.Literal["get_pods", "get_deployments", "get_events", "get_services", "kubectl_command"] | None: ...

global___Gke = Gke
