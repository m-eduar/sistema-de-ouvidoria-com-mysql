#Tópicos a serem feitos:
#1) Listagem das Manifestações - ok
#2) Listagem de manifestações por tipo - ok
#3) Criar uma nova Manifestação por tipo - ok
#4) Exibir quantidade de manifestações - ok
#5) Pesquisar uma manifestação por código - ok
#6) Excluir uma manifestação pelo codigo - ok
#7) Sair do sistema - ok

from operacoesbd import *

opcao = 0
conn = criarConexao("localhost","root","2007Mes#","ouvidoria_tipo")
tipoManifestacao = 0

print("Seja bem vindo(a) ao sistema de ouvidoria da Universidade XYZ")

while opcao != 7:
    print("\n1) Listagem de manifestações  \n2) Listagem de manifestações por tipo \n3) Criar uma nova manifestação \n4) Exibir quantidade de manifestações   \n5) Pesquisar uma manifestação por código \n6) Excluir uma manifestação por código \n7) Sair")
    opcao = int(input("Digite sua opção: "))

#Listagem manifestações geral
    if opcao == 1:
        consultaManifestacoes = "select * from Ouvidoria_Por_Tipo"
        manifestacoes = listarBancoDados(conn, consultaManifestacoes)
        if len(manifestacoes) > 0:
            print()
            print("Lista de manifestações")
            for item in manifestacoes:
                print("\nCódigo: ", item[0], "\nAutor: ", item[3], "\nManifestação: ", item[1], "\nTipo: ", item[2])
        else:
            print("Não existe manifestações cadastrados no sistema.")

#Listagem de manifestações por tipo
    elif opcao == 2:
        print("Qual lista de manifestações você deseja ver? \n1) Elogio \n2) Sugestão \n3) Reclamação")
        tipoManifestacaoListagem = int(input("Digite a sua opção: "))

#TipoElogioListagem
        if tipoManifestacaoListagem == 1:
            consultaManifestacoes = "select * from Ouvidoria_Por_Tipo where tipo='Elogio'"
            manifestacoes = listarBancoDados(conn, consultaManifestacoes)
            if len(manifestacoes) > 0:
                print()
                print("Lista de manifestações")
                for item in manifestacoes:
                    print("\nCódigo: ", item[0], "\nAutor: ", item[3], "\nManifestação: ", item[1], "\nTipo: ", item[2])
#TipoSugestaoListagem
        elif tipoManifestacaoListagem == 2:
            consultaManifestacoes = "select * from Ouvidoria_Por_Tipo where tipo='Sugestao'"
            manifestacoes = listarBancoDados(conn, consultaManifestacoes)
            if len(manifestacoes) > 0:
                print()
                print("Lista de manifestações")
                for item in manifestacoes:
                    print("\nCódigo: ", item[0], "\nAutor: ", item[3], "\nManifestação: ", item[1], "\nTipo: ", item[2])

#TipoReclamacaoListagem
        elif tipoManifestacaoListagem == 3:
            consultaManifestacoes = "select * from Ouvidoria_Por_Tipo where tipo='Reclamacao'"
            manifestacoes = listarBancoDados(conn, consultaManifestacoes)
            if len(manifestacoes) > 0:
                print()
                print("Lista de manifestações")
                for item in manifestacoes:
                    print("\nCódigo: ", item[0], "\nAutor: ", item[3], "\nManifestação: ", item[1], "\nTipo: ", item[2])

#Criar uma nova manifestação
    elif opcao == 3:
        print("Qual tipo de manifestação você deseja criar? \n1) Elogio \n2) Sugestão \n3) Reclamação")
        tipoManifestacao = int(input("Digite a sua opção: "))

#TipoElogio
        if tipoManifestacao == 1:
                autorElogio = input("Digite seu nome: ")
                elogio = input("Digite seu elogio: ")
                tipoElogio = "Elogio"

                sql = "insert into Ouvidoria_Por_Tipo(conteudo,tipo,autor) values(%s, %s, %s)"
                dadosInsert = [elogio,tipoElogio,autorElogio]
                insertNoBancoDados(conn, sql, dadosInsert)
                print("Manifestação criada com sucesso!")

#TipoSugestao
        elif tipoManifestacao == 2:
                autorSugestao = input("Digite seu nome: ")
                sugestao = input("Digite sua sugestão: ")
                tipoSugestao = "Sugestão"

                sql = "insert into Ouvidoria_Por_Tipo(conteudo,tipo,autor) values(%s, %s, %s)"
                dadosInsert = [sugestao,tipoSugestao,autorSugestao]
                insertNoBancoDados(conn, sql, dadosInsert)
                print("Manifestação criada com sucesso!")

#TipoReclamacao
        elif tipoManifestacao == 3:
                autorReclamacao = input("Digite seu nome: ")
                reclamacao = input("Digite sua reclamação: ")
                tipoReclamacao = "Reclamação"

                sql = "insert into Ouvidoria_Por_Tipo(conteudo,tipo,autor) values(%s, %s, %s)"
                dadosInsert = [reclamacao,tipoReclamacao,autorReclamacao]
                insertNoBancoDados(conn, sql, dadosInsert)
                print("Manifestação criada com sucesso!")


#Quantidade de manifestações
    elif opcao == 4:
        consultaListagemManifestacoes = "select count(*) from Ouvidoria_Por_Tipo"
        manifestacoesContagem = listarBancoDados(conn, consultaListagemManifestacoes)

        for item in manifestacoesContagem:
            print("O sistema possui", item[0], "manifestações")

#Pesquisar por código
    elif opcao == 5:
        codigoPesquisa = int(input("Digite o código: "))
        consultaPesquisaFilme = "select * from Ouvidoria_Por_Tipo where cod = %s"
        dados = [codigoPesquisa]

        manifestacoes = listarBancoDados(conn, consultaPesquisaFilme, dados)

        if len(manifestacoes) > 0:
            for item in manifestacoes:
                print("\nCódigo: ", item[0], "\nAutor: ", item[3], "\nManifestação: ", item[1], "\nTipo: ", item[2])
        else:
            print()
            print("Não existe manifestação cadastrada para o código informado.")


#Excluir por código
    elif opcao == 6:
        codigoRemocao = int(input("Digite o código: "))
        consultaRemocaoManifestacao = "delete from Ouvidoria_Por_Tipo where cod = %s"
        dados = [codigoRemocao]

        linhasApagadas = excluirBancoDados(conn, consultaRemocaoManifestacao, dados)

        if linhasApagadas > 0:
            print()
            print("Manifestação removida com sucesso!")
        else:
            print()
            print("Nenhuma manifestação foi removida.")

print("Obrigado(a) por utilizar nosso sistema!")

encerrarConexao(conn)
