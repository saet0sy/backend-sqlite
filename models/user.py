from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email: str

@dataclass
class UserInput:
    username: str
    email: str