_## 📚 Portfólio de Conceitos POO em Python

Aqui está uma demonstração de como Python implementa cada um dos conceitos fundamentais de POO.

### 1. Tipos de Dados

Python é uma linguagem de **tipagem dinâmica**, o que significa que você não precisa declarar o tipo de uma variável. O próprio interpretador infere o tipo em tempo de execução.

Principais tipos de dados embutidos:

- **Numéricos:** `int` (inteiro), `float` (ponto flutuante), `complex` (complexo)
- **Texto:** `str` (string)
- **Booleano:** `bool` (True, False)
- **Sequências:** `list`, `tuple`
- **Mapeamento:** `dict` (dicionário)
- **Conjuntos:** `set`
- **Nulo:** `NoneType` (valor `None`)

Python

[]()

# 

### 2. Classe e Objeto

- **Classe:** É o "molde" ou a planta baixa para criar objetos. Define propriedades (atributos) e comportamentos (métodos).
- **Objeto:** É uma "instância" de uma classe. É a coisa real que você constrói a partir do molde, com seus próprios dados.

### 3. Atributos e Métodos

- **Atributos:** São as variáveis dentro de uma classe; representam os dados ou o "estado" do objeto.
- **Métodos:** São as funções dentro de uma classe; representam o "comportamento" do objeto.

O método `__init__` é um método especial (construtor) chamado automaticamente quando um novo objeto é criado. `self` é uma referência ao próprio objeto.

Python

# 

`class Livro:
    # Método Construtor (inicializa os atributos)
    def __init__(self, titulo, autor, ano):
        # --- Atributos ---
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.esta_emprestado = False

    # --- Métodos ---
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

# Criando objetos e usando seus métodos
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)

# Acessando atributos
print(f"Livro 1: {livro1.titulo} ({livro1.ano})")

# Usando métodos
livro1.emprestar()
livro1.emprestar() # Tenta emprestar de novo
livro1.devolver()`

### 4. Arrays e Coleções

Python não tem "arrays" nativos no mesmo sentido que C++ ou Java. A estrutura de dados mais comum e flexível que cumpre esse papel é a **Lista** (`list`).

- **List (`list`):** Coleção ordenada e mutável. (Equivalente ao `ArrayList` do Java).
- **Tuple (`tuple`):** Coleção ordenada e **imutável**.
- **Dictionary (`dict`):** Coleção não ordenada de pares chave-valor.
- **Set (`set`):** Coleção não ordenada de itens únicos.

Python

# 

`# List (mutável)
autores_favoritos = ["J.R.R. Tolkien", "George Orwell", "Isaac Asimov"]
autores_favoritos.append("Ursula K. Le Guin")
print(autores_favoritos[0]) # Acessa por índice

# Tuple (imutável) - usado para dados que não devem mudar
coordenadas_biblioteca = (-7.22, -35.88)

# Dict (chave-valor) - ótimo para representar objetos complexos
membro = {
    "id": 101,
    "nome": "Ana Silva",
    "livros_emprestados": [livro1, livro2]
}
print(membro["nome"])

# Set (valores únicos)
generos = {"Ficção", "Fantasia", "Ficção"}
print(generos) # Saída: {'Fantasia', 'Ficção'} (duplicata removida)`

### 5. Encapsulamento

Encapsulamento é a ideia de proteger os atributos internos de uma classe. Em Python, não há `private` ou `public` estritos. Em vez disso, usa-se **convenções**:

- **`_` (Um underscore):** "Protegido". Um aviso a outros desenvolvedores para não acessarem diretamente.
- **`__` (Dois underscores):** "Privado". O Python "mutila" o nome (ex: `__saldo` vira `_Conta__saldo`) para evitar que subclasses o sobrescrevam acidentalmente.

A forma "Pythonica" de fazer encapsulamento é usar **Propriedades** (`@property`), que criam "getters" e "setters" de forma elegante.

Python

# 

`class ContaBancaria:
    def __init__(self, saldo_inicial):
        # "Privado" - não deve ser acessado diretamente
        self.__saldo = saldo_inicial

    # Getter (Usando @property)
    @property
    def saldo(self):
        """Este método 'get' permite ler o saldo."""
        if self.__saldo < 0:
            return 0
        return self.__saldo

    # Setter (Usando @<nome_da_property>.setter)
    @saldo.setter
    def saldo(self, novo_valor):
        """Este método 'set' valida antes de alterar."""
        if novo_valor < 0:
            print("Erro: O saldo não pode ser negativo.")
        else:
            self.__saldo = novo_valor

# --- Usando a classe ---
conta = ContaBancaria(100)

# Acessamos como se fosse um atributo, mas o getter é chamado
print(f"Saldo atual: R${conta.saldo}")

# Alteramos como se fosse um atributo, mas o setter é chamado
conta.saldo = 150
print(f"Novo saldo: R${conta.saldo}")

# O setter vai bloquear esta operação
conta.saldo = -50
print(f"Saldo após tentativa negativa: R${conta.saldo}")`

### 6. Agregação e Composição

Ambos são tipos de relacionamento "Tem-um" (um objeto possui outro).

- **Agregação:** Os objetos têm vidas independentes. Se o "container" for destruído, o outro objeto continua existindo. (Ex: Uma `Biblioteca` *tem* `Livros`).
- **Composição:** O objeto "parte" não existe sem o "todo". Se o "todo" for destruído, a "parte" também é. (Ex: Um `Livro` *tem* `Paginas`).

Python

# 

`# --- Agregação ---
# O Livro existe independentemente da Biblioteca
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = [] # Agrega objetos Livro

    def adicionar_livro(self, livro):
        self.livros.append(livro)

livro_agregado = Livro("Neuromancer", "William Gibson", 1984)
biblio_centro = Biblioteca("Biblioteca Central")

biblio_centro.adicionar_livro(livro_agregado)
# Se 'biblio_centro' for deletada, 'livro_agregado' ainda existe.

# --- Composição ---
# A Página é criada *dentro* do Livro e não faz sentido sem ele.
class LivroComPaginas:
    def __init__(self, titulo):
        self.titulo = titulo
        self.paginas = [] # Composição
        self.adicionar_paginas(200) # O próprio livro gerencia suas páginas

    def adicionar_paginas(self, num_paginas):
        for i in range(num_paginas):
            # O objeto Pagina é criado e pertence ao Livro
            self.paginas.append(Pagina(i + 1))

class Pagina:
    def __init__(self, numero):
        self.numero = numero
        self.conteudo = f"Este é o conteúdo da página {numero}."

meu_livro_com_paginas = LivroComPaginas("Duna")
# Se 'meu_livro_com_paginas' for deletado, suas 200 páginas
# serão coletadas pelo garbage collector, pois não fazem sentido sozinhas.`

### 7. Herança

É um relacionamento "É-um". Uma classe (filha) herda atributos e métodos de outra classe (mãe), permitindo o reuso de código.

Python

# 

`# Classe Mãe (Superclasse)
class ItemBiblioteca:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def descrever(self):
        print(f"Item: {self.titulo} ({self.ano})")

# Classe Filha (Subclasse) - herda de ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self, titulo, ano, autor):
        # super() chama o construtor da classe mãe
        super().__init__(titulo, ano)
        self.autor = autor

# Outra Classe Filha
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano, edicao):
        super().__init__(titulo, ano)
        self.edicao = edicao

meu_livro_heranca = Livro("Fundação", "Isaac Asimov", 1951)
minha_revista = Revista("Scientific American", 2023, 10)

meu_livro_heranca.descrever() # Método herdado
minha_revista.descrever() # Método herdado`

### 8. Polimorfismo

"Muitas formas". É a capacidade de objetos de classes diferentes responderem ao mesmo método (com a mesma assinatura) de formas diferentes. Em Python, isso acontece de duas formas principais:

1. **Polimorfismo de Herança (Overriding):** Classes filhas podem reescrever (overriding) métodos da classe mãe.
2. **Polimorfismo "Duck Typing":** "Se anda como um pato e faz quack como um pato, então é um pato." Python não se importa com a *classe* do objeto, apenas se ele *possui o método* que você quer chamar.

Python

# 

`# 1. Polimorfismo com Herança (Method Overriding)

class ItemBiblioteca:
    def __init__(self, titulo):
        self.titulo = titulo

    def descrever(self):
        # Método genérico
        print(f"Item: {self.titulo}")

class Livro(ItemBiblioteca):
    # Reescrevendo (overriding) o método da classe mãe
    def descrever(self):
        print(f"LIVRO: {self.titulo}")

class Revista(ItemBiblioteca):
    # Reescrevendo de outra forma
    def descrever(self):
        print(f"REVISTA: {self.titulo}")

# ---
itens = [Livro("Dom Casmurro"), Revista("Veja")]

# Polimorfismo em ação:
# O loop não se importa se o item é Livro ou Revista,
# ele apenas chama o método .descrever() de cada um.
for item in itens:
    item.descrever()
# Saída:
# LIVRO: Dom Casmurro
# REVISTA: Veja

# 2. Polimorfismo com Duck Typing
class Pato:
    def fazer_quack(self):
        print("Quack!")

class PessoaFantasiada:
    def fazer_quack(self):
        print("Eu sou uma pessoa fazendo Quack!")

def no_lago(animal):
    # Esta função não pede um Pato.
    # Pede qualquer coisa que tenha o método .fazer_quack()
    animal.fazer_quack()

pato_real = Pato()
pessoa = PessoaFantasiada()

no_lago(pato_real)   # Funciona
no_lago(pessoa)      # Funciona também!`

### 9. Enumeração

Usado para criar um conjunto de constantes nomeadas (membros). Torna o código mais legível e seguro do que usar strings ou números mágicos.

Python

# 

`from enum import Enum, auto

class Status(Enum):
    DISPONIVEL = auto() # auto() atribui valores automaticamente (1, 2, 3...)
    EMPRESTADO = auto()
    EM_MANUTENCAO = auto()

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.status = Status.DISPONIVEL # Usando a enum

    def emprestar(self):
        if self.status == Status.DISPONIVEL:
            self.status = Status.EMPRESTADO
            print(f"'{self.titulo}' emprestado. Status: {self.status.name}")
        else:
            print(f"Não é possível emprestar. Status: {self.status.name}")

livro_enum = Livro("A Guerra dos Mundos")
livro_enum.emprestar()
livro_enum.emprestar()`

### 10. Atributos e Métodos Estáticos (de Classe)

- **Atributo de Classe (Estático):** É um atributo que pertence à *classe*, e não a uma instância (objeto). É compartilhado por todas as instâncias.
- **Método Estático (`@staticmethod`):** Um método que pertence à classe, mas não tem acesso nem à instância (`self`) nem à classe (`cls`). É basicamente uma função utilitária que faz sentido estar dentro da classe.
- **Método de Classe (`@classmethod`):** Similar ao estático, mas recebe a própria classe (`cls`) como primeiro argumento. Útil para criar "construtores alternativos".

Python

# 

`class Livro:
    # Atributo de Classe (Estático)
    # Contador compartilhado por todos os objetos Livro
    total_de_livros_criados = 0

    def __init__(self, titulo):
        self.titulo = titulo
        Livro.total_de_livros_criados += 1 # Incrementa o contador da CLASSE

    # Método Estático (Utilitário)
    @staticmethod
    def is_isbn_valido(isbn):
        """Verifica se um ISBN (formato simples) é válido."""
        isbn = isbn.replace("-", "")
        return len(isbn) == 13 and isbn.isdigit()

    # Método de Classe (Construtor Alternativo)
    @classmethod
    def criar_livro_csv(cls, string_csv):
        """Cria um livro a partir de uma linha de CSV (ex: 'Titulo,Autor')"""
        titulo, autor = string_csv.split(",")
        # 'cls' aqui é a própria classe Livro
        return cls(titulo) # É o mesmo que chamar Livro(titulo)

# --- Usando métodos estáticos e de classe ---
print(f"ISBN '123-456-789012-3' é válido? {Livro.is_isbn_valido('123-456-789012-3')}")
# Note que chamamos o método a partir da CLASSE, não do objeto.

# --- Usando atributos estáticos ---
print(f"Total de livros antes: {Livro.total_de_livros_criados}") # Saída: 0
l1 = Livro("O Hobbit")
l2 = Livro("O Silmarillion")
print(f"Total de livros depois: {Livro.total_de_livros_criados}") # Saída: 2
# l1.total_de_livros_criados também é 2!

# --- Usando método de classe ---
livro_csv = Livro.criar_livro_csv("O Nome do Vento,Patrick Rothfuss")
print(f"Livro criado do CSV: {livro_csv.titulo}")`

### 11. Tratamento de Exceção

Python usa blocos `try...except` para lidar com erros (exceções) que podem ocorrer durante a execução do programa.

Python

# 

`biblioteca_db = {
    "101": "O Iluminado",
    "102": "It: A Coisa"
}

def buscar_livro(id_livro):
    try:
        # Tenta executar este bloco
        nome_livro = biblioteca_db[id_livro]
        print(f"Livro encontrado: {nome_livro}")

    except KeyError:
        # Executa se um KeyError ocorrer (ID não encontrado no dict)
        print(f"Erro: Livro com ID '{id_livro}' não encontrado.")

    except TypeError:
        # Executa se um TypeError ocorrer (ex: ID foi None)
        print("Erro: O ID deve ser uma string ou número.")

    except Exception as e:
        # Captura qualquer outra exceção inesperada
        print(f"Ocorreu um erro inesperado: {e}")

    finally:
        # Executa SEMPRE, ocorrendo erro ou não (bom para fechar arquivos/conexões)
        print("Busca finalizada.")

buscar_livro("101")  # Sucesso
buscar_livro("999")  # Causa KeyError
buscar_livro(None)   # Causa TypeError`

### 12. Generics (Type Hinting)

Python é dinamicamente tipado, mas introduziu "Type Hints" (dicas de tipo) para ajudar desenvolvedores e ferramentas de análise estática (como o `mypy`). *Generics* permitem criar funções e classes que funcionam com *vários tipos* de forma segura.

O módulo `typing` é usado para isso.

Python

# 

`from typing import List, Dict, TypeVar, Any

# 1. Dicas de tipo básicas
def saudar(nome: str) -> str:
    return f"Olá, {nome}"

def listar_titulos(livros: List[Livro]) -> None:
    for livro in livros:
        print(livro.titulo)

# 2. Generics
# 'T' pode ser qualquer tipo (int, str, Livro, etc.)
T = TypeVar('T')

def obter_primeiro_item(lista: List[T]) -> T:
    """Retorna o primeiro item de qualquer lista."""
    return lista[0]

# O 'mypy' (um verificador de tipos) entenderia isso:
numeros: List[int] = [1, 2, 3]
primeiro_num = obter_primeiro_item(numeros) # mypy infere que primeiro_num é 'int'

strings: List[str] = ["a", "b", "c"]
primeira_str = obter_primeiro_item(strings) # mypy infere que primeira_str é 'str'`

*Nota: Essas dicas são ignoradas pelo interpretador Python em tempo de execução; elas são apenas "dicas".*

### 13. Testes de Unidade

Testes de unidade verificam se pequenas "unidades" de código (como um método ou uma função) funcionam como esperado. O módulo `unittest` já vem com o Python.

Suponha que temos nossa classe `Livro` salva em um arquivo chamado `biblioteca.py`:

Python

# 

---_
