from classes import profile, profile_selector
import os

''' Modelo de criação de perfil manual
p1 = profile.Profile(
    nome="Exemplo1",
    corda=1.0,
    espessura=0.12,
    angulo_ataque=5.0,
    coeficiente_lift=1.2,
    coeficiente_drag=0.05
)
'''

ps = profile_selector.Profile_Selector()

list_perfis = []

print("Como deseja inserir os perfis?")
print("1 - Manualmente")
print("2 - A partir de um arquivo de input")
opcao = input("Digite a opção desejada: ")

os.system('clear')

if opcao == "1":
    qnt_perfis = int(input("Quantos perfis deseja inserir? "))
    for i in range(qnt_perfis):
        print(f"Insira os dados do perfil {i + 1}:")
        nome = input("Nome: ")
        corda = float(input("Corda: "))
        espessura = float(input("Espessura: "))
        angulo_ataque = float(input("Ângulo de Ataque: "))
        coeficiente_lift = float(input("Coeficiente de Lift: "))
        coeficiente_drag = float(input("Coeficiente de Drag: "))

        p = profile.Profile(
            nome=nome,
            corda=corda,
            espessura=espessura,
            angulo_ataque=angulo_ataque,
            coeficiente_lift=coeficiente_lift,
            coeficiente_drag=coeficiente_drag
        )

        list_perfis.append(p)

    ps.add_list(list_perfis)

    ps.print_list()


elif opcao == "2":
    print('Lendo arquivo de input...')
    list_perfis = profile_selector.Profile_Selector.read_profiles('input.txt')
    print(list_perfis[1].info())


        


