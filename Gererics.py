from dataclasses import dataclass
from typing import List, TypeVar

@dataclass
class Livro:
    titulo: str

def saudar(nome: str) -> str:
    return f"Olá, {nome}"

def listar_titulos(livros: List[Livro]) -> None:
    for livro in livros:
        print(livro.titulo)

T = TypeVar('T')

def obter_primeiro_item(lista: List[T]) -> T:
    return lista[0]

numeros: List[int] = [1, 2, 3]
primeiro_num = obter_primeiro_item(numeros)

strings: List[str] = ["a", "b", "c"]
primeira_str = obter_primeiro_item(strings)
