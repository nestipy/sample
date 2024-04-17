from dataclasses import dataclass


@dataclass
class CreateUserDto:
    name: str


@dataclass
class UpdateUserDto(CreateUserDto):
    id: int