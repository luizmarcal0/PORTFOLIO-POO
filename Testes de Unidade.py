class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.esta_emprestado = False

    def emprestar(self):
        if self.esta_emprestado:
            raise ValueError("Livro já emprestado")
        self.esta_emprestado = True
