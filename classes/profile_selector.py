from classes import profile
import os
class Profile_Selector:
    
    l_profiles = []
    def __init__(self):
        ...
    
    def add_list(self, lp):
        Profile_Selector.l_profiles = lp

    def print_list(self):
        os.system('clear')
        print(f"Lista de Perfis:")
        for profile in Profile_Selector.l_profiles:
            print(profile.info())
            print("\n")


    def read_profiles(file_name):
        lista_perfis = []
        with open(file_name, 'r') as file:
            linhas = file.readlines()

            for i in range(0, len(linhas), 6):
                nome = linhas[i].strip()
                corda = linhas[i + 1].strip()
                espessura = linhas[i + 2].strip()
                angulo_ataque = linhas[i + 3].strip()
                coeficiente_lift = linhas[i + 4].strip()
                coeficiente_drag = linhas[i + 5].strip()

                # Cria um objeto Profile e adiciona à lista
                perfil = profile.Profile(nome, corda, espessura, angulo_ataque, coeficiente_lift, coeficiente_drag)
                lista_perfis.append(perfil)

        Profile_Selector.l_profiles = lista_perfis
        return lista_perfis
    
    def pontuacao_desempenho(self):
        # Adapte a pontuação conforme necessário
        return self.coeficiente_lift / self.coeficiente_drag

    
    def selecionar_melhor_perfil(self, perfis):
        # Se não houver perfis, retorna None
        if not perfis:
            return None

        # Inicializa o melhor perfil como o primeiro da lista
        melhor_perfil = perfis[0]
        melhor_pontuacao = self.pontuacao_desempenho()

        # Itera sobre os perfis para encontrar o melhor
        for perfil in perfis[1:]:
            pontuacao_atual = self.pontuacao_desempenho()
            if pontuacao_atual > melhor_pontuacao:
                melhor_perfil = perfil
                melhor_pontuacao = pontuacao_atual

        return melhor_perfil