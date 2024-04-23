from dataclasses import dataclass


@dataclass
class CreateUserDto:
    name: str
    email: str
    password: str


@dataclass
class UpdateUserDto(CreateUserDto):
    id: int
