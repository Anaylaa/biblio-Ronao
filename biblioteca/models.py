from datetime import date, timedelta

class Livro:
    def __init__(self, id, titulo, autor, categoria, quantidade):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.quantidade = quantidade  # total disponível na biblioteca

    def pode_emprestar(self):
        return self.quantidade > 1  # sempre deve sobrar 1


class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.emprestimos_ids = []  # empréstimos ativos


class Emprestimo:
    def __init__(self, id, livro, usuario):
        self.id = id
        self.livro = livro
        self.usuario = usuario
        self.data_inicio = date.today()
        self.data_fim = self.data_inicio + timedelta(days=30)
        self.renovacoes = 0
        self.ativo = True
