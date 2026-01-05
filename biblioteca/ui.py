class UI:
    @staticmethod
    def menu():
        print("\n📚 Biblioteca")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Cadastrar usuário")
        print("5 - Emprestar livro")
        print("6 - Devolver livro")
        print("0 - Sair")

    @staticmethod
    def input_int(msg):
        try:
            return int(input(msg))
        except ValueError:
            return None
