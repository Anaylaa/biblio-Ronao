from datetime import date, timedelta
from models import Livro, Usuario, Emprestimo

class BibliotecaService:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
        self._livro_id = 1
        self._usuario_id = 1
        self._emprestimo_id = 1

    # ---------- CADASTROS ----------
    def cadastrar_livro(self, titulo, autor, categoria, quantidade):
        livro = Livro(self._livro_id, titulo, autor, categoria, quantidade)
        self.livros.append(livro)
        self._livro_id += 1

    def cadastrar_usuario(self, nome):
        usuario = Usuario(self._usuario_id, nome)
        self.usuarios.append(usuario)
        self._usuario_id += 1

    # ---------- BUSCAS ----------
    def get_livro(self, livro_id):
        return next((l for l in self.livros if l.id == livro_id), None)

    def get_usuario(self, usuario_id):
        return next((u for u in self.usuarios if u.id == usuario_id), None)

    def get_emprestimo(self, emprestimo_id):
        return next((e for e in self.emprestimos if e.id == emprestimo_id), None)

    # ---------- EMPRÉSTIMOS ----------
    def emprestar_livro(self, livro_id, usuario_id):
        usuario = self.get_usuario(usuario_id)
        livro = self.get_livro(livro_id)

        if not usuario:
            return False, "Usuário não cadastrado."

        if not livro:
            return False, "Livro não encontrado."

        if len(usuario.emprestimos_ids) >= 7:
            return False, "Limite de 7 livros atingido."

        for emp_id in usuario.emprestimos_ids:
            emp = self.get_emprestimo(emp_id)
            if emp.livro.categoria == livro.categoria:
                return False, "Já existe um livro dessa categoria."

        if not livro.pode_emprestar():
            return False, "Não é possível emprestar o último exemplar."

        emprestimo = Emprestimo(self._emprestimo_id, livro, usuario)
        self.emprestimos.append(emprestimo)
        usuario.emprestimos_ids.append(emprestimo.id)
        livro.quantidade -= 1

        self._emprestimo_id += 1
        return True, "Livro emprestado com sucesso."

    def renovar_emprestimo(self, emprestimo_id):
        emprestimo = self.get_emprestimo(emprestimo_id)

        if not emprestimo or not emprestimo.ativo:
            return False, "Empréstimo inválido."

        emprestimo.data_fim += timedelta(days=30)
        emprestimo.renovacoes += 1
        return True, "Empréstimo renovado por mais 30 dias."

    def calcular_multa(self, emprestimo):
        hoje = date.today()
        if hoje <= emprestimo.data_fim:
            return 0
        return (hoje - emprestimo.data_fim).days * 1.0

    def devolver_livro(self, emprestimo_id):
        emprestimo = self.get_emprestimo(emprestimo_id)

        if not emprestimo or not emprestimo.ativo:
            return False, "Empréstimo inválido."

        multa = self.calcular_multa(emprestimo)

        emprestimo.ativo = False
        emprestimo.livro.quantidade += 1
        emprestimo.usuario.emprestimos_ids.remove(emprestimo.id)

        return True, f"Livro devolvido. Multa: R${multa:.2f}"
