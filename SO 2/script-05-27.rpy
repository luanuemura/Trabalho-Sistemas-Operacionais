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

    scene dti-inicio

    "Você foi escolhido para ser um estagiário do Departamento Técnico de Informática (DTI) da FCT - UNESP."

    "Suas tarefas serão voltadas para o suporte técnico no geral, realizando manutenção, formatação e diagnóstico de computadores."

    "Você está na sala aguardando para ser chamado pelo chefe geral do departamento"

    show chefe
    
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

    scene dti
    
    label problema1:
        "O primeiro problema real aparece. Um professor do curso de Geografia chega até você com uma cara confusa."  
        show professor
        pg "Meu computador tem estado muito lento ultimamente. Gostaria da sua ajuda para entender o porquê e o que posso fazer."  
        pg "Ainda não sei se é o processador, a memória, ou talvez os programas que uso ao mesmo tempo."  
        pg "Quando abro o navegador, o editor de texto e as planilhas, por exemplo, parece que todos brigam pela atenção do computador."    
        "Analisando o contexto, você percebe que deve explicar como funciona o subsistema chamado de escalonamento, para que o professor compreenda melhor a situação." 
        jump questao4

    label questao4:
        menu:
            "É o processo pelo qual o sistema operacional decide a ordem e o tempo de execução dos processos na CPU, garantindo que todos recebam acesso de forma controlada e eficiente.":
                "Após responder, o professor ainda parece meio confuso"
                "Pensando nisso, explique de maneira simples, com um exemplo do cotidiano, o que o escalonamento faz:" 
                jump questao5
            "É o método usado pelo sistema operacional para organizar os arquivos dentro do disco rígido ou SSD, melhorando o espaço de armazenamento.":
                "Incorreto! Pense em algo mais relacionado à forma como o sistema distribui o uso da CPU, e não ao armazenamento de arquivos."
                jump questao4
            "É o processo de aumentar a velocidade do processador para executar tarefas mais rapidamente, independentemente do número de programas em execução.":
                "Incorreto! O escalonamento não muda a velocidade do processador, ele organiza quem o vai usar e por quanto tempo."
                jump questao4

    label questao5:
        menu:
            "O escalonamento é como uma corrida, onde todos os corredores largam ao mesmo tempo e só quem for mais rápido consegue chegar ao final.":
                "Incorreto! Pense em algo mais organizado, onde as tarefas precisam esperar sua vez."
                jump questao5
            "O escalonamento é como um caderno de anotações, em que várias pessoas escrevem ao mesmo tempo na mesma página sem qualquer organização.":
                "Incorreto! O escalonamento não é bagunça — ele existe justamente para organizar a ordem de execução."
                jump questao5
            "O escalonamento pode ser comparado a uma fila de banco, onde cada cliente aguarda sua vez para ser atendido, e o gerente decide a ordem do atendimento.":
                pg "Entendi! Eu sei que tenho vários programas instalados, mas fico pensando: como o sistema operacional lida com tudo isso ao mesmo tempo?"  
                pg "Será que o sistema só entrega o processador para um programa até ele terminar, e só depois passa para o próximo?"  
                pg "Ou será que existe algum jeito de equilibrar o uso, para que todos os programas rodem juntos sem travar?" 
                pg "Você pode me explicar essa relação entre o sistema operacional, os programas de usuário e o processo de escalonamento?"    
                jump questao6

    label questao6:
        menu:
            "Na verdade, professor, os programas rodam todos ao mesmo tempo, cada um usando 100%% do processador. O sistema operacional não interfere nesse processo.":
                "Incorreto! Imagine várias pessoas tentando falar ao telefone na mesma linha: não dá pra entender nada."
                jump questao6
            "O sistema operacional funciona como um organizador. Ele recebe todos os pedidos dos programas de usuário e, através do escalonamento, decide a ordem em que cada um vai usar a CPU.":
                pg "Ah, entendi! Eu costumo deixar vários programas abertos ao mesmo tempo: navegador, planilhas, editor de texto e até o software de mapas." 
                pg "Mas percebo que o computador parece se dividir entre os programas, nunca atendendo só um de cada vez. Isso me deixa curioso."
                pg "Como é que o sistema operacional consegue lidar com tantos programas rodando ao mesmo tempo, sem travar completamente?"
                jump questao7
            "O sistema operacional só abre os programas, mas depois que eles estão rodando, cada um decide sozinho quando usar o processador e por quanto tempo.":
                "Incorreto! Os programas não têm controle sobre o processador. Quem organiza o acesso é o sistema operacional, que distribui o tempo de uso de forma controlada."
                jump questao6

    label questao7:
        menu:
            "Multitarefa significa que todos os programas utilizam 100%% do processador ao mesmo tempo, sem necessidade de organização pelo sistema operacional.":
                "Incorreto! O processador não consegue atender vários programas exatamente no mesmo instante."
                jump questao7
            "Multitarefa é quando o sistema operacional executa apenas um programa por vez, impedindo que outros rodem simultaneamente.":
                "Incorreto! Pense em como você consegue ouvir música enquanto escreve um texto no computador. Se fosse apenas um programa por vez, isso não seria possível."
                jump questao7
            "Multitarefa é a capacidade do sistema operacional de executar vários programas aparentemente ao mesmo tempo. Para isso, ele usa o escalonamento, que organiza a ordem em que cada programa acessa a CPU.":
                pg "Entendi melhor a ideia de multitarefa, mas fiquei com outra dúvida..." 
                pg "Quando abro vários programas, como navegador, planilhas e mapas, o sistema vê cada um deles como um todo único?"
                pg "Como o sistema operacional enxerga cada programa que está rodando? Existe um nome específico para isso?"
                jump questao8

    label questao8:
        menu:
            "Chamamos de processo, que é um programa em execução, reunindo o código, os dados e os recursos que o sistema operacional reservou para ele.":
                pg "Ah, então cada programa aberto é um processo diferente... isso explica porque o sistema precisa organizar e controlar tudo isso."
                pg "Você comentou antes sobre o papel do sistema operacional e dos programas de usuário, mas acho que ainda não entendi completamente como isso se conecta."  
                pg "Será que essa lentidão tem a ver com a memória RAM? O pessoal sempre diz que, quando o computador fica devagar, é por falta de memória."  
                pg "No caso em que se precisa de vários programas funcionando ao mesmo tempo, como exatamente a memória RAM, o sistema operacional e os programas de usuário trabalham juntos?"
                jump questao9
            "Chamamos de arquivo executável, que é o instalador ou o ícone do programa que você clica. Quando ele está aberto, o sistema apenas monitora o uso de memória desse arquivo original.":
                "Incorreto! O arquivo executável é o programa no disco, antes de ser carregado na memória."
                jump questao8
            "Chamamos de sessão do usuário, que é como um pacote contendo todos os programas abertos por você. O sistema controla tudo como um bloco único, sem separar cada aplicação.":
                "Incorreto! Cada programa dentro dessa sessão é uma instância de execução independente, e o sistema operacional os gerencia individualmente, não como um bloco único."
                jump questao8

    label questao9:
        menu:
            "A memória RAM é responsável apenas por armazenar arquivos de forma permanente, como se fosse um HD.":
                "Incorreto! A memória RAM não guarda arquivos de forma permanente — ela só mantém dados enquanto o computador está ligado."
                jump questao9
            "O sistema operacional e os programas de usuário funcionam de forma independente da memória RAM, usando apenas o processador.":
                "Incorreto! O processador depende da memória RAM para acessar rapidamente as instruções e dados em uso."
                jump questao9
            "A memória RAM armazena temporariamente o sistema operacional e os programas de usuário, permitindo acesso rápido e uma execução mais eficiente das tarefas e processos.":
                pg "Depois de entender melhor o papel do escalonamento e da memória RAM, fiquei com outra dúvida."
                pg "Quando o computador liga, o que acontece dentro da memória RAM? Ela já vem organizada ou o sistema operacional precisa dividir o espaço?"
                pg "E como exatamente o sistema operacional e os programas de usuário compartilham essa memória sem se misturar?"
                "Pensando no problema apresentado, proponha uma forma de organizar o armazenamento do sistema operacional e dos programas de usuário na memória RAM."
                jump questao10
                
    label questao10:
        menu:
            "A melhor forma é permitir que o sistema operacional e os programas de usuário usem toda a RAM livremente, sem separação. Assim, o espaço é aproveitado ao máximo.":
                "Incorreto! Se não houver separação, um programa pode sobrescrever partes do sistema operacional, causando travamentos ou falhas graves."
                jump questao10
            "O ideal é que a memória RAM seja particionada em áreas distintas: uma reservada ao sistema operacional e outra destinada aos programas de usuário.":
                pg "Então o sistema operacional mantém uma parte só para si e o restante é usado pelos programas que o usuário executa, certo?"
                pg "Entendi... então o sistema operacional separa a memória em partes. Mas quando isso acontece?"
                pg "Será que essa divisão acontece toda vez que eu abro um programa, ou já no momento em que o computador é ligado?"
                "Tendo em mente o funcionamento da memória RAM e o gerenciamento do sistema, responda: em que momento e como a memória deve ser particionada entre o sistema operacional e os programas de usuário?"
                jump questao11
            "A organização da RAM é feita apenas pelos programas de usuário, que decidem onde armazenar suas informações temporárias, sem interferência do sistema operacional.":
                "Incorreto! O sistema operacional é quem gerencia a memória, garantindo que cada programa use apenas o espaço que lhe foi concedido."
                jump questao10

    label questao11:
        menu:
            "A RAM deve ser particionada apenas quando o usuário abre um programa, pois antes disso não há necessidade de separação. O sistema operacional ocupa a memória conforme for precisando.":
                "Incorreto! Parte da memória já é reservada ao sistema operacional assim que o computador é iniciado."
                jump questao11
            "A memória RAM é dividida logo na inicialização do sistema: o sistema operacional ocupa uma parte fixa, enquanto o restante fica disponível para os programas de usuário conforme forem abertos.":
                jump continuacao
            "A RAM é particionada aleatoriamente, conforme o processador escolhe qual programa deve rodar primeiro, sem relação com o sistema operacional.":
                "Incorreto! O processador não gerencia a memória dessa forma — quem define e controla o uso da RAM é o sistema operacional."
                jump questao11
                
    label continuacao:
        "Após explicar todos os conceitos, você fornece formas para resolver o problema do professor, como por exemplo fechar alguns programas que estão ociosos e aumentar a memória RAM."  
        pg "Agora tudo faz sentido! Então o sistema operacional é quem organiza o uso do processador entre os programas, e não eles mesmos que decidem quando usar."  
        pg "Quer dizer que, se eu estiver com muitos programas abertos, o sistema vai tentar dividir o tempo da CPU entre todos, mas isso pode deixar tudo mais lento"  
        pg "Então, para melhorar o desempenho, eu poderia fechar os programas que não estou usando e priorizar os mais importantes"  
        pg "Acho que agora entendo por que meu computador estava tão lento. Vou tentar liberar memória e, se possível, aumentar a RAM. Obrigado pela ajuda!"  
        hide professor
        "Você resolve então o primeiro problema real, explicando ao professor como o escalonamento e a memória RAM influenciam o desempenho do computador."
        

# a partir da questão 22 -> SO 2

    "Mais tarde naquele dia..."
    "Um novo problema surge no seu primeiro dia de trabalho"
    "Alguns alunos do curso de Ciência da Computação estão com problemas em relação ao armazenamento interno de um computador"
    "Eles então começam a falar sobre as diferentes estratégias de alocação, porém não entendem como funciona"
    "Sua próxima tarefa então é descrever de maneira resumida como cada estratégia funciona"
    
    label blocos:
        "Um sistema de arquivos armazena dados em ______ de disco."
        menu:
            "Cluster":
                "Incorreto! Pense em um termo mais geral utilizado na teoria de sistemas operacionais para representar as unidades em que os arquivos são divididos no disco."
                jump blocos
            "Partições":
                "Incorreto! Partições são grandes divisões, reflita sobre qual unidade pode ser menor para armazenar partes de um arquivo dentro dessas divisões."
                jump blocos
            "Blocos":    
                jump contigua1
    
    label contigua1:
        "Cada arquivo ocupa vários blocos ______, e o sistema operacional guarda apenas o endereço do ______ bloco."
        menu:
            "Consecutivos/Primeiro":
                jump contigua2
            "Aleatórios/Último":
                "Incorreto! Nesse método os blocos não ficam espalhados pelo disco. Pense em como eles são organizados fisicamente."
                jump contigua1
            "Independentes/Maior":
                "Incorreto! O sistema precisa de um ponto de referência que permita localizar todos os outros blocos do arquivo."
                jump contigua1

    label contigua2:
        "Os outros blocos são encontrados a partir ______________________________."
        menu:
            "de uma busca completa por todo o disco":
                "Incorreto! O sistema operacional tenta evitar percorrer todo o disco sempre que precisa localizar partes de um arquivo."
                jump contigua2
            "desse primeiro endereço e da posição do bloco no arquivo":
                jump encadeada1
            "de uma tabela global contendo todos os blocos do sistema":
                "Incorreto! Embora existam estruturas auxiliares, nesse método os blocos podem ser localizados diretamente a partir de uma referência inicial."
                jump contigua2

    label encadeada1:
        "Nesse sistema de arquivos, cada arquivo é formado por vários blocos que podem estar ______ no disco."
        menu:
            "aleatórios":
                "Incorreto! Nesse método os blocos do arquivo não são escolhidos de forma totalmente aleatória. Existe uma forma específica de localizar o próximo bloco do arquivo."
                jump encadeada1
            "contíguos":
                "Incorreto! Blocos contíguos significam que eles ficam um ao lado do outro no disco. Porém, nesse sistema os blocos de um mesmo arquivo não precisam estar em sequência."
                jump encadeada1
            "dispersos":
                jump encadeada2

    label encadeada2:
        "Cada bloco armazena o endereço do ______ bloco do mesmo arquivo."
        menu:
            "primeiro":
                "Incorreto! O primeiro bloco serve apenas como ponto inicial para acessar o arquivo. Pense em qual bloco precisa ser encontrado depois que o atual é lido."
                jump encadeada2
            "próximo":
                jump indexada1
            "último":
                "Incorreto! O último bloco representa o final do arquivo, então ele não ajuda a continuar a leitura do restante dos blocos."
                jump encadeada2
    
    label indexada1:
        "Nesse sistema de arquivos, os endereços de todos os blocos de um arquivo são armazenados em uma estrutura chamada ______."
        menu:
            "nó-i":
                jump indexada2
            "diretório":
                "Incorreto! Diretórios servem para organizar arquivos dentro do sistema de arquivos. Pense em qual estrutura é usada especificamente para guardar os endereços dos blocos de um arquivo."
                jump indexada1
            "partição":
                "Incorreto! Partições são divisões maiores do disco usadas para separar áreas de armazenamento. A estrutura procurada é utilizada para localizar blocos específicos de um arquivo."
                jump indexada1
    
    label indexada2:
        "Essas estruturas podem ser organizadas em diferentes ______ para facilitar a localização dos blocos."
        menu:
            "setores":
                "Incorreto! Setores fazem parte da estrutura física do disco, não da organização lógica usada para localizar blocos."
                jump indexada2 
            "níveis":
                jump contexto
            "registros físicos":
                "Incorreto! Diretórios servem para organizar arquivos, não para armazenar os endereços de seus blocos."
                jump indexada2

    label contexto:
        "Quando o sistema operacional interrompe a execução de um processo para executar outro, ele precisa salvar o ______ do processador, que contém informações como valores dos registradores e o contador de programa."    
        menu:
            "contexto":
                jump trocacontexto
            "clock":
                "Incorreto! O clock está relacionado à velocidade de funcionamento do processador, não às informações necessárias para continuar a execução de um processo."
                jump contexto
            "cache":
                "Incorreto! A cache armazena dados frequentemente utilizados pelo processador, mas não guarda o estado de execução de um processo."
                jump contexto

    label trocacontexto:
        "Em um sistema operacional multitarefa, vários processos podem estar ativos ao mesmo tempo. No entanto, o processador só consegue executar um processo por vez."
        "O momento em que o sistema interrompe a execução de um processo e passa a executar outro é chamado de ______ de processo."
        menu:
            "troca":
                jump tabelaprocesso
            "replicação":
                "Incorreto! Nesse caso o sistema não cria cópias do processo, apenas alterna qual processo está sendo executado."
                jump trocacontexto
            "fragmentação":
                "Incorreto! Fragmentação está relacionada ao uso da memória ou do disco, não à alternância de execução entre processos."
                jump trocacontexto

    label tabelaprocesso:
        "Ainda falando sobre o termo contexto, explique onde ele fica salvo no processador"
        "Esse armazenamento é feito na ______, uma estrutura mantida pelo sistema operacional para cada processo."
        menu:
            "cache do processador":
                "Incorreto! A cache armazena dados frequentemente acessados para acelerar o processamento, mas não mantém informações completas sobre o estado de um processo."
                jump tabelaprocesso
            "PCB (Process Control Block)":
                jump armzprocesso
            "memória secundária":
                "Incorreto! A memória secundária é usada para armazenamento permanente. Pense em uma estrutura mantida pelo sistema operacional especificamente para gerenciar processos ativos."
                jump tabelaprocesso

    label armzprocesso:
        "O contexto de um processo é armazenado em uma estrutura chamada PCB, que fica localizada na ______, sendo acessada diretamente pelo sistema operacional durante a troca de processos."
        menu:
            "disco rígido":
                "Incorreto! O acesso ao disco é muito lento para armazenar informações que precisam ser recuperadas rapidamente durante a execução dos processos."
                jump armzprocesso
            "registradores do usuário":
                "Incorreto! Os registradores fazem parte do contexto, mas não são onde ele é armazenado de forma persistente pelo sistema operacional."
                jump armzprocesso
            "memória principal (RAM)":
                jump mutex
    
    #podemos dar exemplo de um dispositivo que pode ser usado por dois processos ou mais (impresora, braço robotico, placa de som)
    label mutex:
        "Para evitar que dois processos enviem comandos simultaneamente para a impressora, o sistema operacional deve utilizar um mecanismo de ______."
        menu:
            "exclusão mútua(Mutex)":
                jump monopolio
            "multiprogramação":
                "Incorreto! Multiprogramação permite executar vários processos, mas não controla o acesso simultâneo a um mesmo recurso."
                jump mutex
            "paginação":
                "Incorreto! Paginação está relacionada ao gerenciamento de memória, não ao controle de acesso a dispositivos."
                jump mutex

    label monopolio:
        "Considere que o controle de acesso ao braço robótico foi deixado sob responsabilidade dos próprios processos de usuário."
        "Um desses processos decide não liberar o recurso após utilizá-lo, impedindo que outros processos tenham acesso ao dispositivo."
        "Esse tipo de problema pode ser caracterizado como um ______ do recurso."
        menu:
            "compartilhamento":
                "Incorreto! Nesse caso o recurso não está sendo dividido entre os processos, mas sim mantido por apenas um deles."
                jump monopolio
            "paralelismo":
                "Incorreto! Paralelismo envolve execução simultânea de tarefas, não a retenção indevida de um recurso."
                jump monopolio
            "monopólio":
                jump chamada_sistema
        
    label chamada_sistema:
        "Para evitar que um processo egoísta cause um monopólio, o dispositivo agora é gerenciado pelo Sistema Operacional. Sempre que um processo de usuário precisa mover o dispositivo, ele deve solicitar essa operação através de uma _________."
        menu:
            "variável global":
                "Incorreto! Variáveis globais no espaço do usuário ainda permitiriam que um processo ignorasse os outros ou travasse o recurso."
                jump chamada_sistema
            "instrução de loop":
                "Incorreto! Isso apenas manteria a CPU ocupada, mas não daria ao processo o direito de acessar o hardware de forma segura."
                jump chamada_sistema
            "chamada de sistema":
                "Correto! A chamada de sistema (system call) transfere o controle para o Kernel, garantindo que o SO gerencie o braço e evite abusos dos processos."
                jump envio_com
    
    label envio_com:
        "Durante a execução de um sistema, chamadas de sistema ocorrem quando um processo precisa interagir com o sistema operacional, como ao ______ ou ao encerrar sua execução."
        menu:
            "iniciar o computador":
                "Incorreto! Chamadas de sistema ocorrem durante a execução dos programas, não apenas na inicialização."
                jump envio_com
            "esperar um tempo fixo":
                "Incorreto! O uso de chamadas de sistema não depende de intervalos de tempo, mas de necessidades dos processos."
                jump envio_com
            "enviar comandos a um dispositivo":
                jump chamada_procedimento
    
    label chamada_procedimento:
        "No código de um programa, o uso de uma chamada de sistema para acessar um dispositivo é feito por meio de uma ______."
        menu: 
            "chamada a procedimento":
                jump interrupcao
            "acesso direto ao hardware":
                "Incorreto! Programas de usuário não acessam diretamente o hardware por questões de segurança."
                jump chamada_procedimento
            "interrupção manual":
                "Incorreto! Interrupções são tratadas pelo sistema, não chamadas diretamente pelo programador dessa forma."
                jump chamada_procedimento

    label interrupcao:
        "Uma interrupção pode ser entendida como um evento que faz com que uma atividade em execução seja temporariamente interrompida para tratar outra situação."
        "Um exemplo do cotidiano que representa esse conceito é ______."
        menu:
            "luz visível":
                "Incorreto! Esse exemplo não representa algo que interrompe uma atividade em andamento."
                jump interrupcao
            "rastros de inseto":
                "Incorreto! Esse exemplo não envolve uma interrupção imediata de uma ação em execução."
                jump interrupcao
            "campainha do telefone":
                jump rotina_tratamento

    label rotina_tratamento:
        "Quando ocorre uma interrupção, o sistema operacional precisa executar uma ação específica para tratar o evento antes de continuar a execução normal. Essa ação é realizada por uma ______."
        menu:
            "interrupção pró-ativa":
                "Incorreto! Esse não é um termo utilizado para descrever como o sistema trata interrupções."
                jump rotina_tratamento
            "rotina de tratamento de interrupção"
                jump vetores_interrupcao
            "método de índice sistólico":
                "Incorreto! Esse conceito não está relacionado ao tratamento de interrupções em sistemas operacionais."
                jump rotina_tratamento

    label vetores_interrupcao:
        "Para que o processador saiba exatamente qual função executar quando um dispositivo de hardware dispara um sinal, ele consulta uma tabela de ponteiros na memória. A quantidade de vetores de interrupção nessa tabela deve ser ______."
        menu:
            "o mesmo número de interrupções geradas pelos processos":
                "Incorreto! Os processos disparam milhares de interrupções repetidas ao longo do tempo. A tabela mapeia os tipos de eventos, não a frequência com que ocorrem."
                jump vetores_interrupcao
            "sempre fixa em vinte e sete":
                "Incorreto! O tamanho da tabela depende exclusivamente da arquitetura do processador e do hardware integrado, não sendo um número fixo universal."
                jump vetores_interrupcao
            "o mesmo número de rotinas de tratamento de interrupção":
                jump driver

    label driver:
        "Sistemas operacionais comerciais modernos não possuem controle nativo para todos os periféricos existentes no mercado. Para que o SO aprenda a se comunicar e controlar as especificidades de um novo hardware, é obrigatório instalar um ______."
        menu:
            "driver":
                jump analogia_driver
            "programa adaptador robótico":
                "Incorreto! Esse termo não existe na literatura técnica de sistemas operacionais para descrever a interface de controle de hardware genérico."
                jump driver
            "simulador em modo de segurança":
                "Incorreto! O modo de segurança serve para diagnóstico e costuma desativar componentes extras, em vez de adicionar suporte a novos hardwares."
                jump driver

    label analogia_driver:
        "Como supervisor da equipe, você precisa explicar para um novo estagiário o que um driver faz, usando uma metáfora do cotidiano. No fundo, o driver funciona como um _________."
        menu:
            "Gerador de pulsos":
                "Incorreto! O gerador de pulsos lida com a parte elétrica física dos motores, enquanto o driver é um componente de software."
                jump analogia_driver
            "Linkeditor":
                "Incorreto! O linkeditor (linker) junta pedaços de código compilados para formar um programa executável, não tem relação com comunicação de hardware."
                jump analogia_driver
            "Tradutor":
                jump atomicidade

    label atomicidade:
        "Quando uma sequência de instruções ou uma operação de entrada/saída é executada do início ao fim sem a possibilidade de ser interrompida por outro processo, garantindo que ela seja indivisível, dizemos em sistemas operacionais que esse comportamento possui ______."
        menu:
            "Preempção":
                "Incorreto! Preempção é o exato oposto: a capacidade do sistema operacional de interromper uma tarefa no meio da execução para dar prioridade a outra."
                jump atomicidade
            "Convolução":
                "Incorreto! Convolução é um conceito matemático e de processamento de sinais, sem relação com a indivisibilidade de execução no SO."
                jump atomicidade
            "Atomicidade":
                jump ciclo_vida_processo

    label ciclo_vida_processo:
        "Ao longo de sua existência no sistema, desde o momento em que é criado até o encerramento de suas instruções, um programa passa por diferentes estados que definem o seu ciclo de vida completo. Esses estados são conhecidos como ______."
        menu:
            "Ausente, intermitente e fechado":
                "Incorreto! Esses termos não representam o modelo de estados de processos utilizado pelos gerenciadores de tarefas dos sistemas operacionais."
                jump ciclo_vida_processo
            "Alocado, transmutado, particionado e escalonado":
                "Incorreto! Embora termos como 'alocado' e 'escalonado' existam no contexto do SO, eles se referem a recursos e algoritmos, não aos estados do ciclo de vida do processo."
                jump ciclo_vida_processo
            "Rodando, bloqueado, pronto e concluído":
                jump thread_processo

    label thread_processo:
        "Em sistemas operacionais, uma ______ pode ser entendida como uma unidade de execução que existe dentro de um ______."
        menu:
            "partição/registrador":
                "Incorreto! Partições estão relacionadas à divisão de armazenamento em disco, e registradores são componentes do processador, não unidades de execução."
                jump thread_processo
            "thread/processo":
                jump modos_execucao
            "tarefa/serviço":
                "Incorreto! Tarefas e serviços são conceitos mais amplos e não descrevem a relação específica entre unidades de execução e seus contêineres no SO."
                jump thread_processo

    label modos_execucao:
        "O acesso direto a instruções privilegiadas ocorre no modo ______, enquanto o acesso restrito e seguro ao hardware ocorre no modo ______."
        menu:
            "secundário e kernel":
                "Incorreto! O modo secundário não é um termo utilizado para descrever os modos de privilégio da CPU. O kernel é outro nome utilizado sendo responsável pelo controle do hardware."
                jump modos_execucao
            "núcleo e usuário":
                jump multi_nucleo
            "físico e virtual":
                "Incorreto! Esses termos referem-se à organização da memória (memória física e memória virtual), não aos modos de privilégio da CPU."
                jump modos_execucao
            

    label multi_nucleo:
        "Programas podem ser executados realmente ao mesmo tempo quando a arquitetura do computador possui múltiplos ______ de processamento."
        menu:
            "núcleos":
                jump prioridade
            "threads":
                "Incorreto! Threads são unidades de execução dentro de um processo, mas não garantem execução simultânea."
                jump multi_nucleo
            "partições":
                "Incorreto! Partições são divisões de armazenamento em disco, não unidades de processamento."
                jump multi_nucleo

    label prioridade:
        "Quando um sistema operacional decide que um programa deve receber mais tempo de execução por ser mais importante que outro, ele está utilizando um algoritmo de escalonamento por ______."
        menu:
            "prioridade":
                jump condicao_corrida
            "round-robin":
                "Incorreto! O round-robin é um algoritmo de escalonamento que distribui o tempo de CPU de forma igual entre os processos."
                jump prioridade
            "fragmentação":
                "Incorreto! A fragmentação é um problema relacionado à gestão de memória, não a algoritmos de escalonamento."
                jump prioridade

    label condicao_corrida:
        "Uma condição de corrida ocorre quando dois ou mais processos ou threads acessam um mesmo recurso compartilhado ao mesmo tempo, causando resultados ______ ou inesperados."
        menu:
            "sequenciais":
                "Incorreto! Condições de corrida levam a resultados incoerentes e instáveis, não previsíveis."
                jump condicao_corrida
            "determinísticos":
                "Incorreto! O comportamento de uma condição de corrida é justamente o oposto de determinístico, pois depende do timing de execução dos processos."
                jump condicao_corrida
            "inconsistentes":
                jump regiao_critica

    label regiao_critica:
        "Para evitar condições de corrida, os sistemas operacionais utilizam mecanismos de sincronização que garantem que apenas um processo ou thread acesse um recurso compartilhado por vez. O código que manipula esse recurso é chamado de ______."
        menu:
            "zona de exclusão":
                "Incorreto! Embora o termo 'exclusão' esteja relacionado, ainda assim não é o nome correto para descrever o código que controla o acesso a recursos compartilhados."
                jump regiao_critica
            "região crítica":
                jump problemas_classicos
            "área de bloqueio":
                "Incorreto! Esse termo não é utilizado para descrever o código que acessa recursos compartilhados em sistemas operacionais."
                jump regiao_critica

    label problemas_classicos:
        "Os problemas clássicos de comunicação entre processos são utilizados para estudar situações de concorrência, sincronização e compartilhamento de ______ entre processos."
        menu:
            "recursos":
                jump deadlock
            "pixels":
                "Incorreto! Os pixels são elementos de imagem, não à comunicação de processos."
                jump problemas_classicos
            "partições":
                "Incorreto! As partições são divisões de armazenamento em disco."
                jump problemas_classicos

    label deadlock:
        "Deadlock ocorre quando dois ou mais processos ficam esperando indefinidamente por recursos que estão sendo utilizados uns pelos outros, impedindo a ______ da execução."
        menu:
            "continuidade":
                jump comparacao
            "segmentação":
                "Incorreto! Segmentação é um método de gerenciamento de memória, não está relacionada ao bloqueio de processos."
                jump deadlock
            "inicialização":
                "Incorreto! O deadlock ocorre durante a execução, não na inicialização dos processos."
                jump deadlock

    label comparacao:
        "Na memória virtual, a ______ divide a memória em partes de tamanho fixo chamadas páginas, que são armazenadas na memória principal em estruturas chamadas ______."
        menu:
            "paginação/molduras":
                jump mmu
            "segmentação/partições":
                "Incorreto! A segmentação é um método diferente de gerenciamento de memória, e as partições são divisões de armazenamento em disco, não estruturas de memória principal."
                jump comparacao
            "interrupção/blocos":
                "Incorreto! Interrupção é um evento que interrompe a execução de um processo, e blocos são unidades de armazenamento, não estruturas de memória principal."
                jump comparacao

    label mmu:
        "A MMU (Unidade de Gerência de Memória) é responsável por realizar a tradução de endereços ______ para endereços físicos da memória."
        menu:
            "mecânicos":
                "Incorreto! A MMU trabalha com endereços de memória, não com componentes físicos mecânicos."
                jump mmu
            "virtuais":
                jump fim
            "virtuais extremos":
                "Incorreto! A tradução realizada pela MMU envolve os endereços usados pelos programas e os endereços reais da RAM."
                jump mmu