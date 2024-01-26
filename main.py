from classes import profile, profile_selector
# with open('db/output.txt', 'w') as file:
#     file.write('teste')

p1 = profile.Profile(
    nome="Exemplo1",
    corda=1.0,
    espessura=0.12,
    angulo_ataque=5.0,
    coeficiente_lift=1.2,
    coeficiente_drag=0.05
)

p2 = profile.Profile(
    nome="Exemplo2",
    corda=1.0,
    espessura=0.12,
    angulo_ataque=5.0,
    coeficiente_lift=1.2,
    coeficiente_drag=0.05
)

p3 = profile.Profile(
    nome="Exemplo3",
    corda=1.0,
    espessura=0.12,
    angulo_ataque=5.0,
    coeficiente_lift=1.2,
    coeficiente_drag=0.05
)

p4 = profile.Profile(
    nome="Exemplo4",
    corda=1.0,
    espessura=0.12,
    angulo_ataque=5.0,
    coeficiente_lift=1.2,
    coeficiente_drag=0.05
)

#p1.info()

lista = [p1, p2, p3, p4]

list_test = []

ps = profile_selector.Profile_Selector(lista)
#ps.print_list()

vari = ps.read_profiles('input.txt')

print(vari[1].nome)
