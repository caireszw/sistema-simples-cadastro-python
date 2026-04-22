temp = dict()
banco = list()
while True:
    print('1 -> CADASTRAR USUARIO')
    print('2 -> LISTA DE USUARIOS')
    print('3 -> BUSCAR USUARIO')
    print('4 -> SAIR')
    resp = int(input('Digite a opção desejada:'))
    if resp == 1:
        temp['Nome'] = str(input('Digite o nome do usuario:'))
        temp['Idade'] = int(input(f'Digite a idade de {temp["Nome"]}:'))
        temp['Cidade'] = str(input('Digite a cidade'))
        banco.append(temp.copy())
        temp.clear()
    elif resp == 2:
        if len(banco) == 0:
            print('ERRO NENHUM USUARIO CADASTRADO!')
            
        else:
            for p in banco:
                print(f' Nome: {p["Nome"]} | Idade: {p["Idade"]} | Cidade: {p["Cidade"]}')
    elif resp == 3:
        nome = str(input('Digite o nome do Usuario:')).lower()
        user = 'Usuario não encontrado!'  
        for p in banco:
            if nome in p['Nome'].lower():
                user =  'Usuario Encontrado na base de dados!'
        print(user)
    elif resp == 4:
        print('FIM DO PROGRAMA')
        break
    elif resp > 4:
        print('OPÇÃO INVALIDA')

