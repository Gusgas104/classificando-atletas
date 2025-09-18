from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
if idade == 10:
    print('''O atleta tem {} anos
Classificação: MIRIM '''.format(idade))
elif idade in (11, 12):
    print('''O atleta tem {} anos
Classificação: PETIZ'''.format(idade))
elif idade in (13, 14):
    print('''O atleta tem {} anos
Classificado: INFÂNTIL'''.format(idade))
elif idade in (15,16):
    print('''O atleta tem {} anos
Classificação: JUVENIL'''.format(idade))
elif idade in (17,18):
    print('''O atleta tem {} anos
Classificação: JUNIOR'''.format(idade))
elif idade >= 19:
    print('''O atleta tem {} anos
Classificação: SÊNIOR'''.format(idade))

