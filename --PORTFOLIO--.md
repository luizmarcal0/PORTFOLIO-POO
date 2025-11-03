Aqui está um resumo dos conceitos de Programação Orientada a Objetos (POO) em Python abordados no texto:

1.  **Tipos de Dados:** Python tem tipagem dinâmica (o tipo é inferido em tempo de execução) e possui tipos embutidos como `int`, `str`, `list`, `dict`, etc.
2.  **Classe e Objeto:** A Classe é o "molde" (ex: `Livro`). O Objeto é a "instância" criada a partir do molde (ex: `livro1`).
3.  **Atributos e Métodos:** Atributos são as variáveis/dados da classe (ex: `self.titulo`). Métodos são as funções/comportamentos (ex: `emprestar()`). `__init__` é o método construtor.
4.  **Arrays e Coleções:** Python usa `list` (mutável), `tuple` (imutável), `dict` (chave-valor) e `set` (valores únicos) para agrupar dados.
5.  **Encapsulamento:** Proteção de atributos. Em Python, usa-se convenções como `_` (protegido) e `__` (privado). `@property` é a forma elegante de criar getters e setters.
6.  **Agregação e Composição:** Relacionamentos "Tem-um". **Agregação:** Objetos independentes (Biblioteca *tem* Livros). **Composição:** Objeto "parte" depende do "todo" (Livro *tem* Páginas).
7.  **Herança:** Relacionamento "É-um". Uma classe filha herda atributos e métodos de uma classe mãe (ex: `Livro` e `Revista` herdam de `ItemBiblioteca`).
8.  **Polimorfismo:** "Muitas formas". Objetos de classes diferentes respondem ao mesmo método (ex: `item.descrever()`) ou qualquer objeto com o método certo funciona (Duck Typing).
9.  **Enumeração (`Enum`):** Cria um conjunto de constantes nomeadas (ex: `Status.DISPONIVEL`), tornando o código mais legível e seguro.
10. **Estáticos/De Classe:** Atributos (`total_de_livros_criados`) e métodos (`@staticmethod`, `@classmethod`) que pertencem à Classe, não a uma instância específica.
11. **Tratamento de Exceção:** Uso de `try...except...finally` para capturar e lidar com erros (exceções) durante a execução.
12. **Generics (Type Hinting):** "Dicas" de tipo (ex: `nome: str`) que ajudam desenvolvedores e ferramentas de análise, mas não são forçadas em tempo de execução.
13. **Testes de Unidade (`unittest`):** Módulo usado para criar testes que verificam se pequenas partes do código (unidades) funcionam como esperado.
