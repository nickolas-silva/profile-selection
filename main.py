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

    print('O melhor perfil selecionado foi: ')
    mp = ps.selecionar_melhor_perfil(list_perfis)
    mp.info()
    with open('db/output.txt', 'w') as file:
        file.write(f'Nome: {mp.nome}\n')
        file.write(f'Corda: {mp.corda}\n')
        file.write(f'Espessura: {mp.espessura}\n')
        file.write(f'Ângulo de Ataque: {mp.angulo_ataque}\n')
        file.write(f'Coeficiente de Lift: {mp.coeficiente_lift}\n')
        file.write(f'Coeficiente de Drag: {mp.coeficiente_drag}\n')
        file.write(f'Pontuação: {mp.coeficiente_lift / mp.coeficiente_drag}\n')

        file.write(f'\n\nOutros perfis da lista: \n')
        for perfil in list_perfis:
            if(perfil.nome == mp.nome):
                continue
            else:
                file.write(f'Nome: {perfil.nome}\n')
                file.write(f'Corda: {perfil.corda}\n')
                file.write(f'Espessura: {perfil.espessura}\n')
                file.write(f'Ângulo de Ataque: {perfil.angulo_ataque}\n')
                file.write(f'Coeficiente de Lift: {perfil.coeficiente_lift}\n')
                file.write(f'Coeficiente de Drag: {perfil.coeficiente_drag}\n')
                file.write(f'Pontuação: {perfil.coeficiente_lift / perfil.coeficiente_drag}\n')
                file.write(f'\n')


elif opcao == "2":
    print('Lendo arquivo de input... \n')
    list_perfis = profile_selector.Profile_Selector.read_profiles('db/input.txt')

    print('O melhor perfil selecionado foi: ')
    mp = ps.selecionar_melhor_perfil(list_perfis)
    mp.info()
    with open('db/output.txt', 'w') as file:
        file.write(f'O melhor perfil selecionado foi: \n')
        file.write(f'Nome: {mp.nome}\n')
        file.write(f'Corda: {mp.corda}\n')
        file.write(f'Espessura: {mp.espessura}\n')
        file.write(f'Ângulo de Ataque: {mp.angulo_ataque}\n')
        file.write(f'Coeficiente de Lift: {mp.coeficiente_lift}\n')
        file.write(f'Coeficiente de Drag: {mp.coeficiente_drag}\n')
        file.write(f'Pontuação: {mp.coeficiente_lift / mp.coeficiente_drag}\n')

        file.write(f'\n\nOutros perfis da lista: \n')
        for perfil in list_perfis:
            if(perfil.nome == mp.nome):
                continue
            else:
                file.write(f'Nome: {perfil.nome}\n')
                file.write(f'Corda: {perfil.corda}\n')
                file.write(f'Espessura: {perfil.espessura}\n')
                file.write(f'Ângulo de Ataque: {perfil.angulo_ataque}\n')
                file.write(f'Coeficiente de Lift: {perfil.coeficiente_lift}\n')
                file.write(f'Coeficiente de Drag: {perfil.coeficiente_drag}\n')
                file.write(f'Pontuação: {perfil.coeficiente_lift / perfil.coeficiente_drag}\n')
                file.write(f'\n')
        

        
        
else:
    print("Opção inválida!")