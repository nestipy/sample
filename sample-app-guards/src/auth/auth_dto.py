from dataclasses import dataclass


@dataclass
class LoginDto:
    email: str
    password: str


@dataclass
class RegisterDto(LoginDto):
    name: str
