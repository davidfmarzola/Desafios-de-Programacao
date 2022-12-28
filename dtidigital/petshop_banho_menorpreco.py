# 03/08/2018 3 5
# <data><quantidade de cães pequenos><quantidade de cães grandes>
def indicar_indice_do_dia(data):
    from datetime import date
    dia, mes, ano = data.split('/')
    try:
        data = date(year=int(ano), month=int(mes), day=int(dia))
    except ValueError:
        print('Dia esta fora do intervalo para o mes e/ou mes nao esta no intervalo (1, 12)')
        ler_entradas_arquivo()
    return data.weekday()

def estimar_custo_de_cada_canil(indice_da_semana, caes_pequenos, caes_grandes):
    custo = []
    meu_canino_feliz = 0
    vai_rex = 0
    # preço é o mesmo, independente do dia
    chow_chawgas = (caes_pequenos * 30) + (caes_grandes * 45)
    if indice_da_semana >= 0 and indice_da_semana <= 4:  # dia de semana
        meu_canino_feliz = (caes_pequenos*20)+(caes_grandes*40)
        vai_rex = (caes_pequenos*15)+(caes_grandes*50)
    else:  # final de semana
        meu_canino_feliz = (caes_pequenos*24)+(caes_grandes*48)
        vai_rex = (caes_pequenos*18)+(caes_grandes*60)
    custo.append(meu_canino_feliz)
    custo.append(vai_rex)
    custo.append(chow_chawgas)
    return custo

def escolher_petshop(custo):
    if custo[1] <= custo[0] and custo[1] < custo[2]:
        print('Vai Rex | R$'+str(custo[1]))
    elif custo[2] <= custo[1] and custo[2] <= custo[0]:
        print('ChowChawgas | R$'+str(custo[2]))
    else:
        print('Meu Canino Feliz | R$'+str(custo[0]))

def chamar_funcoes(data, *quantidade_de_caes):
    caes_pequenos = int(quantidade_de_caes[0])
    caes_grandes = int(quantidade_de_caes[1])
    indice_da_semana = indicar_indice_do_dia(data)  # 0-4: dia de semana; 5,6: final de semana
    custo = estimar_custo_de_cada_canil(indice_da_semana, caes_pequenos, caes_grandes)
    escolher_petshop(custo)

def ler_entradas_arquivo():
    manipulador = open('pub.in', 'r')
    for linha in manipulador:
        linha = linha.rstrip() 
        try:
            data, *quantidade_de_caes = input().split()
        except EOFError: 
            exit()
        chamar_funcoes(data, *quantidade_de_caes)
    manipulador.close() 

ler_entradas_arquivo()