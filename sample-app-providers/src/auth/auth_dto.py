from dataclasses import dataclass


@dataclass
class LoginDto:
    username: str
    password: str


@dataclass
class RegisterDto:
    username: int
    email: str
    password: str
