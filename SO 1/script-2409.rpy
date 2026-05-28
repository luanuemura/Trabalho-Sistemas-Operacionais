# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chefe do Departamento")
define e = Character("Estagiario")
define pg = Character("Professor de Geografia")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    scene sala with dissolve

    "Você foi escolhido para ser um estagiário do Departamento Técnico de Informática (DTI) da FCT - UNESP."

    "Suas tarefas serão voltadas para o suporte técnico no geral, realizando manutenção, formatação e diagnóstico de computadores."

    "Você está na sala aguardando para ser chamado pelo chefe geral do departamento"

    # show chefe
    
    c "Olá, serei seu chefe durante o seu tempo de estágio aqui no departamento"

    c "Me chamo §§§§§§§§§§, e serei responsável por acompanhar seu desenvolvimento."
    
    c "Antes de assinarmos o contrato, gostaria de entender mais sobre as suas habilidades."

    c "Por isso, vou te colocar em algumas situações reais que acontecem aqui no setor. Assim poderei ver como você se sai."

    c "Considere estas situações como pequenos testes. Se você acertar, estará pronto para atuar como estagiário de verdade."

    c "Vamos começar:"

    c "Mesmo com o computador desligado, o sistema operacional e os programas permanecem guardados em um recurso essencial de armazenamento permanente. Identifique este importante recurso."
    jump questao1 

    label questao1:
        menu:
            "Memoria RAM":
                "Incorreto! A RAM guarda dados temporários e perde tudo quando o computador é desligado."
                jump questao1
            "Processador":
                "Incorreto! O processador executa instruções, mas não é responsável por armazenar permanentemente o sistema."
                jump questao1
            "HD/SSD":
                "Correto! O item que armazena o sistema e os demais programas é o SSD ou HD."
                c "Muito bom!! Falando agora das atividades internas de um computador, explique quais atividades acontecem quando se liga o computador."
                jump questao2
    
    label questao2:
        menu:
            "Quando o computador é ligado, o sistema operacional é executado diretamente a partir da CPU, sem necessidade de verificação do hardware ou de carregamento na memória.":
                "Incorreto! A CPU não inicia o sistema sozinha, primeiro é necessário passar pelo POST, BIOS/UEFI e bootloader."
                jump questao2
            "Ao ser ligado, o computador executa o POST para verificar os componentes básicos, em seguida a BIOS/UEFI localiza o dispositivo de boot, carrega o bootloader e inicializa o sistema operacional na memória RAM.":
                c "Muito bom! De fato ocorre a execução do POST e a verificação dos demais componentes"
                c "Agora falando em questão das atividades finais do BIOS. Fale quais são as duas ultimas: "
                jump questao3
            "Ao ser ligado, o computador carrega todos os programas de usuário diretamente do HD/SSD para a RAM, antes mesmo do sistema operacional ser iniciado.":
                "Incorreto! O sistema operacional precisa ser carregado primeiro, só depois os programas de usuário podem ser executados."
                jump questao2

    label questao3:
        menu:
            "Transfere todos os programas de usuário do HD/SSD diretamente para a memória RAM, iniciando-os automaticamente junto com o sistema.":
                "Incorreto! O BIOS não carrega programas de usuario"
                jump questao3
            "Carrega o núcleo do sistema operacional do HD/SSD para a RAM e entrega ao processador o ponto inicial de execução, permitindo que o sistema assuma o controle.":
                c "Isso mesmo! Voce está sabendo muito bem sobre o BIOS!!"
            "Antes de encerrar, o BIOS realiza novamente o POST e reconfigura os parâmetros de hardware, garantindo que o sistema operacional seja iniciado sem erros.":
                "Incorreto! O POST ocorre logo no início da inicialização do BIOS"
                jump questao3

    "Após responder corretamente todas as perguntas, o chefe do departamento fica muito satisfeito com o seu conhecimento."

    "Assim, você assina os termos de estágio e consequentemente está com a vaga"

    "Um pouco mais tarde naquele dia..."

    # scene dti-sala

    "O primeiro problema real aparece. Um professor do curso de Geografia te traz um computador."  

    pg "Meu computador tem estado muito lento ultimamente, gostaria da sua ajuda para entender o porquê, e o que fazer."  

    pg "Ainda não sei se é o processador, a memória, ou talvez os programas que uso ao mesmo tempo."  

    pg "Quando abro vários aplicativos de uma vez — navegador, editor de texto, planilhas — parece que todos brigam pela atenção do computador."    

    "Olhando para todo o contexto dado pelo professor, você chega na conclusão de que deve explicar como funciona o subsistema denominado de escalonamento para o professor de maneira simples"

    "Se tratando do tema voltado para escalonamento, explique de maneira simples com um exemplo do cotidiano o que o escalonamento faz:"  
    jump questao4

    label questao4:
        menu:
            "O escalonamento é como uma corrida, onde todos os corredores largam ao mesmo tempo e só quem for mais rápido consegue chegar ao final.":
                "Incorreto! Pense em algo mais organizado, onde as tarefas precisam esperar sua vez."
                jump questao4
            "O escalonamento é como um caderno de anotações, em que várias pessoas escrevem ao mesmo tempo na mesma página sem qualquer organização.":
                "Incorreto! O escalonamento não é bagunça — ele existe justamente para organizar a ordem de execução."
                jump questao4
            "O escalonamento pode ser comparado a uma fila de banco, onde cada cliente deve aguardar sua vez para ser atendido, e o gerente decide a ordem do atendimento."
                
    pg "Entendi! Eu sei que tenho vários programas instalados, mas fico pensando: como o sistema operacional lida com tudo isso ao mesmo tempo?"  

    pg "Será que o sistema só entrega o processador para um programa até ele acabar, e só depois passa para o próximo?"  

    pg "Ou será que existe algum jeito de equilibrar o uso, para que todos os programas rodem juntos sem travar?" 

    pg "Você pode me explicar essa relação entre o sistema operacional, os programas de usuário e o processo de escalonamento?" 
    jump questao5

    label questao5:
        menu:
            "Na verdade, professor, os programas rodam todos ao mesmo tempo, cada um usando 100% do processador. O sistema operacional não interfere nesse processo.":
                "Incorreto! Imagine só várias pessoas tentando falar ao telefone ao mesmo tempo na mesma linha: não dá pra entender nada."
                jump questao5
            "O sistema operacional funciona como um organizador. Ele recebe todos os pedidos dos programas de usuário e, através do escalonamento, decide a ordem em que cada um vai usar a CPU."
                
            "O sistema operacional só abre os programas, mas depois que eles estão rodando, cada programa decide sozinho quando usar o processador e por quanto tempo.":
                "Incorreto! Os programas não têm controle sobre o processador. Quem organiza o acesso é o sistema operacional, que distribui o tempo de uso de forma controlada."
                jump questao5

    pg "Eu costumo deixar vários programas abertos ao mesmo tempo: navegador, planilhas, editor de texto e até o software de mapas. Mas percebo que o computador parece ficar dividido entre eles, nunca atendendo só um de cada vez. Isso me deixa curioso."

    pg "Como é que o sistema operacional consegue lidar com tantos programas rodando ao mesmo tempo, sem travar completamente?"
    
    label questao6:
        menu:
            "Multitarefa significa que todos os programas utilizam 100% do processador ao mesmo tempo, sem necessidade de organização pelo sistema operacional.":
                "Incorreto! O processador não consegue atender vários programas exatamente no mesmo instante."
                jump questao6
            "Multitarefa é quando o sistema operacional executa apenas um programa por vez, impedindo que outros rodem ao mesmo tempo, sem relação com escalonamento.":
                "Incorreto! Pense em como você consegue ouvir música enquanto escreve um texto no computador. Se fosse apenas um programa por vez, isso não seria possível."
                jump questao6
            "Multitarefa é a capacidade do sistema operacional de executar vários programas aparentemente ao mesmo tempo. Para isso, ele usa o escalonamento, que organiza a ordem em que cada programa acessa a CPU."

    pg "Entendi melhor a ideia de multitarefa, mas fiquei com outra dúvida... Quando abro vários programas, como navegador, planilhas e mapas, o sistema vê cada um deles como um todo único?"

    pg "Mas afinal, como ele enxerga cada programa que está rodando? Será que existe um nome específico para isso?"

    label questao7:
        menu:
            "Damos o nome de processo, que é um programa em execução, reunindo o código, os dados e os recursos que o sistema operacional reservou para ele."
            "Damos o nome de arquivo executável, que é o instalador ou o ícone do programa que você clica. Quando ele está aberto, o sistema apenas monitora o uso de memória desse arquivo original.":
                "Incorreto! O arquivo executável é o programa no disco, antes de ser carregado na memória."
                jump questao7
            "Chamamos de sessão do usuário, que é como um pacote contendo todos os programas abertos por você. O sistema controla tudo como um bloco único, sem separar cada aplicação.":
                "Incorreto! Cada programa dentro dessa sessão é uma instância de execução independente, e o sistema operacional os gerencia de forma individual, não como um bloco único."
                jump questao7
    
    # This ends the game.
