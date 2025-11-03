biblioteca_db = {
    "101": "O Iluminado",
    "102": "It: A Coisa"
}

def buscar_livro(id_livro):
    try:
        nome_livro = biblioteca_db[id_livro]
        print(f"Livro encontrado: {nome_livro}")
    except KeyError:
        print(f"Erro: Livro com ID '{id_livro}' não encontrado.")
    except TypeError:
        print("Erro: O ID deve ser uma string ou número.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("Busca finalizada.")

buscar_livro("101")
buscar_livro("999")
buscar_livro(None)
