class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class Pagina:
    def __init__(self, numero, conteudo=None):
        self.numero = numero
        self.conteudo = conteudo or f"Este é o conteúdo da página {numero}."

class LivroComPaginas:
    def __init__(self, titulo, num_paginas=200):
        self.titulo = titulo
        self.paginas = []
        self.adicionar_paginas(num_paginas)

    def adicionar_paginas(self, num_paginas):
        for i in range(num_paginas):
            self.paginas.append(Pagina(i + 1))

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

livro_agregado = Livro("Neuromancer", "William Gibson", 1984)
biblio_centro = Biblioteca("Biblioteca Central")
biblio_centro.adicionar_livro(livro_agregado)

meu_livro_com_paginas = LivroComPaginas("Duna", num_paginas=200)
