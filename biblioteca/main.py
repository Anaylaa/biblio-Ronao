from service import BibliotecaService
from ui import UI

service = BibliotecaService()

while True:
    UI.menu()
    opcao = UI.input_int("Escolha: ")

    if opcao == 1:
        t = input("Título: ")
        a = input("Autor: ")
        ano = input("Ano: ")
        c = input("Categoria: ")
        service.cadastrar_livro(t, a, ano, c)

    elif opcao == 2:
        for l in service.listar_livros():
            status = "Disponível" if l.disponivel else "Emprestado"
            print(f"{l.id} - {l.titulo} ({status})")

    elif opcao == 3:
        termo = input("Buscar: ")
        for l in service.buscar_livro(termo):
            print(f"{l.id} - {l.titulo}")

    elif opcao == 4:
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        service.cadastrar_usuario(nome, tipo)

    elif opcao == 5:
        livro_id = UI.input_int("ID do livro: ")
        usuario_id = UI.input_int("ID do usuário: ")
        ok, msg = service.emprestar_livro(livro_id, usuario_id)
        print(msg)

    elif opcao == 6:
        livro_id = UI.input_int("ID do livro: ")
        ok, msg = service.devolver_livro(livro_id)
        print(msg)

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
