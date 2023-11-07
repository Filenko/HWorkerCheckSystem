from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CodeWithTests(_message.Message):
    __slots__ = ["id", "program_code", "tests"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_CODE_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    program_code: bytes
    tests: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., program_code: _Optional[bytes] = ..., tests: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckResults(_message.Message):
    __slots__ = ["id", "result"]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., result: _Optional[_Iterable[str]] = ...) -> None: ...
