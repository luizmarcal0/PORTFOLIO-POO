class Livro:
    total_de_livros_criados = 0

    def __init__(self, titulo):
        self.titulo = titulo
        Livro.total_de_livros_criados += 1

    @staticmethod
    def is_isbn_valido(isbn):
        """Verifica se um ISBN (formato simples) é válido."""
        isbn = isbn.replace("-", "")
        return len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def criar_livro_csv(cls, string_csv):
        titulo, autor = string_csv.split(",")
        return cls(titulo)


print(f"ISBN '123-456-789012-3' é válido? {Livro.is_isbn_valido('123-456-789012-3')}")
print(f"Total de livros antes: {Livro.total_de_livros_criados}")
l1 = Livro("O Hobbit")
l2 = Livro("O Silmarillion")
print(f"Total de livros depois: {Livro.total_de_livros_criados}")
livro_csv = Livro.criar_livro_csv("O Nome do Vento,Patrick Rothfuss")
print(f"Livro criado do CSV: {livro_csv.titulo}")
