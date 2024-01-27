Guia de Usuário:

Esse é um projeto de seleção de perfis aerodinâmicos! Este programa foi desenvolvido para auxiliar na análise e seleção de perfis aerodinâmicos com base em critérios específicos, como coeficientes de sustentação e arrasto.

Utilidade de Cada Função:

    Profile Class:
        A classe Profile representa um perfil aerodinâmico e inclui atributos como nome, corda, espessura, ângulo de ataque, coeficiente de sustentação e coeficiente de arrasto.
    
    Profile.info() Method:
        Esse método exibie todos os atributos de um perfil no terminal.

    Profile_Selector:
        Essa classe representa um seletor de perfil, tem como objetivo recer uma lista de perfis para realizar a seleção de qual o melhor.

    Profile_Selector.pontuacao_desempenho() Method:
        Este método calcula uma pontuação de desempenho com base na relação entre o coeficiente de sustentação e o coeficiente de arrasto de um perfil.

    Profile_Selector.selecionar_melhor_perfil() Method:
        O método estático selecionar_melhor_perfil() compara os perfis fornecidos e retorna o perfil com o melhor desempenho aerodinâmico com base na pontuação calculada.

    Profile_Selector.read_profiles() Method:
        Esta função lê um arquivo de texto contendo informações de vários perfis e retorna uma lista de objetos Profile com esses dados.

    Profile_Selector.print_list() Method:
        Exibe todos o perfis presentes na lista atual do objeto Profile_Selector no terminal

Inputs:
    Estrutura do arquivo input.txt:

    NomePerfil1
    Corda1
    Espessura1
    AnguloAtaque1
    CoefLift1
    CoefDrag1
    --------------------------
    NomePerfil2
    Corda2
    Espessura2
    AnguloAtaque2
    CoefLift2
    CoefDrag2
    --------------------------

Outputs:
    Exemplo de saida do arquivo output.txt:
    O melhor perfil selecionado foi: 
    Nome: Selig S1223
    Corda: 1.1
    Espessura: 0.15
    Ângulo de Ataque: 5.3
    Coeficiente de Lift: 1.1
    Coeficiente de Drag: 0.03
    Pontuação: 36.66666666666667


    Outros perfis da lista: 
    Nome: NACA 2412
    Corda: 1.0
    Espessura: 0.12
    Ângulo de Ataque: 5.0
    Coeficiente de Lift: 0.9
    Coeficiente de Drag: 0.03
    Pontuação: 30.000000000000004

    Nome: Eppler E423
    Corda: 1.1
    Espessura: 0.15
    Ângulo de Ataque: 5.3
    Coeficiente de Lift: 1.2
    Coeficiente de Drag: 0.05
    Pontuação: 23.999999999999996

    Nome: Clark Y
    Corda: 1.1
    Espessura: 0.15
    Ângulo de Ataque: 5.3
    Coeficiente de Lift: 1.0
    Coeficiente de Drag: 0.04
    Pontuação: 25.0

Exemplo de utilização:

1- Copie o conteudo abaixo no arquivo input.txt;

NACA 2412
1.0
0.12
5.0
0.9
0.03
--------------------------
Eppler E423
1.1
0.15
5.3
1.2
0.05
--------------------------
Clark Y
1.1
0.15
5.3
1.0
0.04
--------------------------
Selig S1223
1.1
0.15
5.3
1.1
0.03

2- Rode o arquivo main selecione a opção 2;

3- Verifique a sáida no terminal e no arquivo db/output.txt