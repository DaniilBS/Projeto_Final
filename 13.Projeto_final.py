Tamanho = input('Bom tarde, que T1/2/3 vai escolher: ')
Dinheiro = input('Quanto dinheiro tem: ')
if Tamanho == 'T1':
    local = input('Quer que a casa seija onde Porto(0),Vila de Conde(1),Maia(2),Braga(3): ')
if Tamanho == 'T2':
    local = input('Quer que a casa seija onde Porto(0),Vila de Conde(1),Maia(2),Braga(3): ')
if Tamanho == 'T3':
    local = input('Quer que a casa seija onde Porto(0),Vila de Conde(1),Maia(2),Braga(3): ')
Local = ['Porto','Vila de Conde','Maia','Braga']

T1PMin = '1000'
T1PMax = '1500'
T2PMin = '2000'
T2PMax = '2650'
T3PMin = '2850'
T3PMax = '3350'

if Dinheiro < T1PMin:
    print('O senhor/a não tem dinheiro para uma casa')
    n1 = Dinheiro-1000
else:
    print('O senhor/a comprou a casa com sucesso')