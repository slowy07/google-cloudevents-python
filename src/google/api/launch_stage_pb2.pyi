from typing import ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

ALPHA: LaunchStage
BETA: LaunchStage
DEPRECATED: LaunchStage
DESCRIPTOR: _descriptor.FileDescriptor
EARLY_ACCESS: LaunchStage
GA: LaunchStage
LAUNCH_STAGE_UNSPECIFIED: LaunchStage
PRELAUNCH: LaunchStage
UNIMPLEMENTED: LaunchStage

class LaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
