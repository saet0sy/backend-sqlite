from dataclasses import dataclass

@dataclass
class Product:
    id: int
    title: str
    price: int

@dataclass
class ProductInput:
    title: str
    price: int