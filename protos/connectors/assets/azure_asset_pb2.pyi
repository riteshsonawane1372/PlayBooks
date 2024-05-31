"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import protos.base_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AzureWorkspaceAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKSPACE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def workspace(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        workspace: google.protobuf.wrappers_pb2.StringValue | None = ...,
        name: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["name", b"name", "workspace", b"workspace"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "workspace", b"workspace"]) -> None: ...

global___AzureWorkspaceAssetModel = AzureWorkspaceAssetModel

@typing_extensions.final
class AzureWorkspaceAssetOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKSPACES_FIELD_NUMBER: builtins.int
    @property
    def workspaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AzureWorkspaceAssetModel]: ...
    def __init__(
        self,
        *,
        workspaces: collections.abc.Iterable[global___AzureWorkspaceAssetModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["workspaces", b"workspaces"]) -> None: ...

global___AzureWorkspaceAssetOptions = AzureWorkspaceAssetOptions

@typing_extensions.final
class AzureAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LAST_UPDATED_FIELD_NUMBER: builtins.int
    AZURE_WORKSPACE_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    connector_type: protos.base_pb2.Source.ValueType
    type: protos.base_pb2.SourceModelType.ValueType
    last_updated: builtins.int
    @property
    def azure_workspace(self) -> global___AzureWorkspaceAssetModel: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        type: protos.base_pb2.SourceModelType.ValueType = ...,
        last_updated: builtins.int = ...,
        azure_workspace: global___AzureWorkspaceAssetModel | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asset", b"asset", "azure_workspace", b"azure_workspace", "id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset", b"asset", "azure_workspace", b"azure_workspace", "connector_type", b"connector_type", "id", b"id", "last_updated", b"last_updated", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["asset", b"asset"]) -> typing_extensions.Literal["azure_workspace"] | None: ...

global___AzureAssetModel = AzureAssetModel

@typing_extensions.final
class AzureAssets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AzureAssetModel]: ...
    def __init__(
        self,
        *,
        assets: collections.abc.Iterable[global___AzureAssetModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets"]) -> None: ...

global___AzureAssets = AzureAssets
