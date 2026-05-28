# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chefe do Departamento")
define e = Character("Estagiario")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fenda

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "Voce foi escolhido para ser um estagiario do Departamento Tecnico de Informatica (DTI) da FCT - UNESP."

    "Suas tarefas serao voltadas para o suporte tecnico no geral, realizando manutencao, formatacao e diagnostico de computadores."

    "Voce está na sala aguardando para ser chamado pelo chefe geral do departamento"

    show chefe
    
    c "Ola, serei seu chefe durante o seu tempo de estágio aqui no departamento"

    c "Me chamo §§§§§§§§§§, e serei responsável por acompanhar seu desenvolvimento. "
    
    c "Antes de assinarmos o contrato, gostaria de entender mais sobre as suas habilidades."

    c "Por isso, vou te colocar em algumas situações reais que acontecem aqui no setor. Assim poderei ver como você se sai."

    c "Considere estas situações como pequenos testes. Se você acertar, estará pronto para atuar como estagiário de verdade."

    c "Vamos começar:"

    c "Mesmo com o computador desligado, o sistema operacional e os programas permanecem guardados em um recurso essencial de armazenamento permanente. Identifique este importante recurso."
    jump questao1 

    label questao1:
        menu:
            "HD/SSD":
                "Correto! O item que armazena o sistema e os demais programas é o SSD ou HD."
                c "Muito bom!! Falando agora das atividades internas de um computador, explique quais atividades acontecem quando se liga o computador."
                jump questao2
            "Memoria RAM":
                "Incorreto! A RAM guarda dados temporários e perde tudo quando o computador é desligado."
                jump questao1
            "Processador":
                "Incorreto! O processador executa instruções, mas não é responsável por armazenar permanentemente o sistema."
                jump questao1
    
    label questao2:
        menu:
            "Ao ser ligado, o computador executa o POST para verificar os componentes básicos, em seguida a BIOS/UEFI localiza o dispositivo de boot, carrega o bootloader e inicializa o sistema operacional na memória RAM.":
                c "Muito bom! De fato ocorre a execução do POST e a verificação dos demais componentes"
                jump questao3
            "Quando o computador é ligado, o sistema operacional é executado diretamente a partir da CPU, sem necessidade de verificação do hardware ou de carregamento na memória.":
                "Incorreto! A CPU não inicia o sistema sozinha, primeiro é necessário passar pelo POST, BIOS/UEFI e bootloader."
                jump questao2
            "Ao ser ligado, o computador carrega todos os programas de usuário diretamente do HD/SSD para a RAM, antes mesmo do sistema operacional ser iniciado.":
                "Incorreto! O sistema operacional precisa ser carregado primeiro, só depois os programas de usuário podem ser executados."
                jump questao2

    label questao3:

    # This ends the game.
