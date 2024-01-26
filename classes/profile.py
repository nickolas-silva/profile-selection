class Profile:
    def __init__(self, nome, corda, espessura, angulo_ataque, coeficiente_lift, coeficiente_drag):
        self.nome = nome
        self.corda = corda
        self.espessura = espessura
        self.angulo_ataque = angulo_ataque
        self.coeficiente_lift = coeficiente_lift
        self.coeficiente_drag = coeficiente_drag

    def info(self):
        print(f"Perfil Aerodinâmico: {self.nome}")
        print(f"Corda: {self.corda}")
        print(f"Espessura: {self.espessura}")
        print(f"Ângulo de Ataque: {self.angulo_ataque}")
        print(f"Coeficiente de Lift: {self.coeficiente_lift}")
        print(f"Coeficiente de Drag: {self.coeficiente_drag}")