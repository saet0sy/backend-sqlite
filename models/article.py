from dataclasses import dataclass

@dataclass
class Article:
    id: int
    title: str
    author: str

@dataclass
class ArticleInput:
    title: str
    author: str
