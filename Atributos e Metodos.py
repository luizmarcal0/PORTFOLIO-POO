class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.esta_emprestado = False

    def emprestar(self):
        if not self.esta_emprestado:
            self.esta_emprestado = True
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if self.esta_emprestado:
            self.esta_emprestado = False
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print("Este livro já está na biblioteca.")

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)

print(f"Livro 1: {livro1.titulo} ({livro1.ano})")

livro1.emprestar()
livro1.emprestar()
livro1.devolver()
