from classes import profile
class Profile_Selector:
    
    def __init__(self, lista):
        self.list_profiles = lista
        

    def print_list(self):
        print(f"Lista de Perfis:")
        for profile in self.list_profiles:
            print(profile.info())

    def read_profiles(self, file_name):
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

        return lista_perfis