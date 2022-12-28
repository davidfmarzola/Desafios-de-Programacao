# 03/08/2018 3 5
# <data><quantidade de cães pequenos><quantidade de cães grandes>
def indicedodia(data):
    from datetime import date
    dia, mes, ano = data.split('/')
    data = date(year=int(ano), month=int(mes), day=int(dia))
    return data.weekday()


def custototaldecadacanil(indicedasemana, caespequenos, caesgrandes):
    custo = []
    meucaninofeliz = 0
    vairex = 0
    # preço é o mesmo, independente do dia
    chowchawgas = (caespequenos * 30) + (caesgrandes * 45)
    if indicedasemana >= 0 and indicedasemana <= 4:  # dia de semana
        meucaninofeliz = (caespequenos*20)+(caesgrandes*40)
        vairex = (caespequenos*15)+(caesgrandes*50)
    else:  # final de semana
        meucaninofeliz = (caespequenos*24)+(caesgrandes*48)
        vairex = (caespequenos*18)+(caesgrandes*60)
    custo.append(meucaninofeliz)
    custo.append(vairex)
    custo.append(chowchawgas)
    return custo


def petshopescolhido(custo):
    if custo[1] <= custo[0] and custo[1] < custo[2]:
        print('Vai Rex | R$'+str(custo[1]))
    elif custo[2] <= custo[1] and custo[2] <= custo[0]:
        print('ChowChawgas | R$'+str(custo[2]))
    else:
        print('Meu Canino Feliz | R$'+str(custo[0]))

def leitura(data, *quantidadedecaes):
    caespequenos = int(quantidadedecaes[0])
    caesgrandes = int(quantidadedecaes[1])
    indicedasemana = indicedodia(data)  # 0-4: dia de semana; 5,6: final de semana
    custo = custototaldecadacanil(indicedasemana, caespequenos, caesgrandes)
    petshopescolhido(custo)

manipulador = open('pub.in', 'r')
for linha in manipulador:
    linha = linha.rstrip() 
    data, *quantidadedecaes = input().split()
    leitura(data, *quantidadedecaes)
manipulador.close() 