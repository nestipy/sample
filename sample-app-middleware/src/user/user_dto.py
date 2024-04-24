from dataclasses import dataclass

from nestipy.common import UploadFile


@dataclass
class CreateUserDto:
    name: str
    file: UploadFile
    files: list[UploadFile]


@dataclass
class UpdateUserDto(CreateUserDto):
    id: int
