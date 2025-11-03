class ItemBiblioteca:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def descrever(self):
        print(f"Item: {self.titulo} ({self.ano})")

class Livro(ItemBiblioteca):
    def __init__(self, titulo, ano, autor):
        super().__init__(titulo, ano)
        self.autor = autor

class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano, edicao):
        super().__init__(titulo, ano)
        self.edicao = edicao
        class ItemBiblioteca:
            def __init__(self, titulo, ano):
                self.titulo = titulo
                self.ano = ano

            def descrever(self):
                print(f"Item: {self.titulo} ({self.ano})")

        class Livro(ItemBiblioteca):
            def __init__(self, titulo, ano, autor):
                super().__init__(titulo, ano)
                self.autor = autor

        class Revista(ItemBiblioteca):
            def __init__(self, titulo, ano, edicao):
                super().__init__(titulo, ano)
                self.edicao = edicao

        meu_livro_heranca = Livro("Fundação", "Isaac Asimov", 1951)
        minha_revista = Revista("Scientific American", 2023, 10)

        meu_livro_heranca.descrever()
        minha_revista.descrever()
meu_livro_heranca = Livro("Fundação", "Isaac Asimov", 1951)
minha_revista = Revista("Scientific American", 2023, 10)

meu_livro_heranca.descrever()
minha_revista.descrever()
