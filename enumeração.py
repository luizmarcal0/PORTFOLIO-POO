class ItemBiblioteca:
    def __init__(self, titulo):
        self.titulo = titulo

    def descrever(self):
        print(f"Item: {self.titulo}")

class Livro(ItemBiblioteca):
    def descrever(self):
        print(f"LIVRO: {self.titulo}")

class Revista(ItemBiblioteca):
    def descrever(self):
        print(f"REVISTA: {self.titulo}")

itens = [Livro("Dom Casmurro"), Revista("Veja")]

for item in itens:
    item.descrever()

class Pato:
    def fazer_quack(self):
        print("Quack!")

class PessoaFantasiada:
    def fazer_quack(self):
        print("Eu sou uma pessoa fazendo Quack!")

def no_lago(animal):
    animal.fazer_quack()

pato_real = Pato()
pessoa = PessoaFantasiada()

no_lago(pato_real)
no_lago(pessoa)
