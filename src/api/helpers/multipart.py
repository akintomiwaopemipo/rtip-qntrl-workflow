from typing import BinaryIO, TypeAlias


MultipartField: TypeAlias = (
    tuple[None, str] |
    tuple[str, BinaryIO, str]
)

MultipartFiles: TypeAlias = dict[
    str,
    MultipartField
]