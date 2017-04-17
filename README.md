# projeto_final_2
Programa de gerenciamento de rede atraves do protocolo SNMP

AUTOR: Míriam Félix Lemes da Silva
CONTATO: miriamfx2@gmail.com


RESUMO

	O programa utiliza o protocolo SNMP para pegar informacoes em determinado intervalo de tempos de Hosts na rede.
	Estas informacoes sao armazenadas em um banco de dados utilizando sqlite.

CONFIGURAÇÃO NECESSÁRIA
> Gerenciador
	Para gerenciar o programa e o banco de dados e necessario utilizar o Linux e seguir os seguintes passos para instalacao.
	1. Instalar o Python (pyenv install 3.5.1)
	2. Instalar o pysnmp (pip install pysnmp)
	3. Instalar o snmpd (no Ubuntu: apt-get install snmpd)


> Cliente Linux
	1. Instalar o snmpd
	2. Copiar o arquivo de configuracao snmpd.conf pre configurado do diretorio padrao do Gerenciador para o cliente.
	3. Reiniciar o snmpd

> Cliente Windows 7
	1. Iniciar
	2. Painel de Controle
	3. Programas
	4. Ativar ou desativar recursos do Windows
	5. Marcar Protocolo SNMP
	6. Clicar Ok.
	7. Acessar o gerenciador de servicos (services.msc)
	8. Abrir o servico Servico SNMP
	9. Na guia Agente, adicionar informacoes de contato e local e selecionar todos os servicos
	10. Na guia Intercalacoes, inserir a comunidade public
	11. Na guia Seguranca, adicionar em Nome de comunidades aceitas a comunidade public (somente leitura)
	12. Na guia Seguranca, definir se ira aceita pacotes SNMP de qualquer host ou definir o IP do host gerenciador


MODULOS DO PROGRAMA
>main.py

     >SnmpToolApp: responsavel pelos botões de ação, encaminha os atributos de entrada para o manager
    btn1 = cadastro
    btn2 = consulta (get)
    btn3 = agendar
    btn4 = gerar relatorio
    btn5 = limpar
    btn6 = sair

    >ponto de entrada
        ip
        comunidade
        tempo

    se entrada recebe 1 = btn1, 2 = btn2, 3 = btn3, 4 = btn4, 5 = btn5, 6 = btn6

>main.kv
      formata a parte grafica, funciona como uma pagina de estilos.

> manager.py
	  esse modulo é o responsavel por delegar as funções aos outros modulos
	  ele recebe os atributos de entrada do main.py que são as chaves para executar os demais modulos e gerencia qual modulo deve
	  ser executado.
	  para isso existem funções dentro de uma classe gerente, que executam com um repetidor while, e são executados a partir da condição


> get.py
	  Programa que recolhe as informacoes dos hosts.
	  Para chamar diretamente, deve ser passado por parametro o IP e a COMUNIDADE. Para obter estas informacoes, executar o dbquery.py

 > GetSNMP1: recebe informações da MIB system
    1.3.6.1.2.1.1.1 - sysDescr
    1.3.6.1.2.1.1.2 - sysObjectID
    1.3.6.1.2.1.1.3 - sysUpTime
    1.3.6.1.2.1.1.4 - sysContact
    1.3.6.1.2.1.1.6 - sysLocation

 >GetSNMP2: recebe informaçoes da MIB HOST-RESOURCES-MIB
    1.3.6.1.2.1.25.5.1.1.1 - hrSWRunPerfCPU
    "O número de centésimos-segundos da CPU do sistema total
    Recursos consumidos por este processo. Note que em um
    Sistema multi-processador, este valor pode
    Mais de um centi-segundo em um centi-segundo de real
    (Relógio de parede).

    1.3.6.1.2.1.25.5.1.1.2 - hrSWRunPerfMem'
    A quantidade total de memória do sistema real alocada para este processo.

 >GetSNMP3:
     1.3.6.1.2.1.4.1 - ipForwarding OBJECT-TYPE
     A indicação de se esta entidade está a actuar
     Como um gateway IP no que diz respeito ao encaminhamento de
     Datagramas recebidos por, mas não dirigidos a,
     entidade. IP gateways forward datagramas. Hosts IP
     Não (exceto aqueles fonte-roteados através do host).

     Note que para alguns nós gerenciados, este objeto pode
     Assumir apenas um subconjunto dos valores possíveis.
     Consequentemente, é apropriado que um agente
     Retornar uma resposta `badValue 'se um gerenciamento
     Estação tenta mudar este objeto para um
     Valor inadequado.


     1.3.6.1.2.1.4.4 -  ipInHdrErrors
     O número de datagramas de entrada descartados devido a
     Erros em seus cabeçalhos IP, incluindo
     Checksums, número de versão incompatível, outro formato
     Erros, tempo de vida excedido, erros descobertos
     No processamento de suas opções de IP, etc.


> dbmanager.py
	  Gerencia todas os cadastros, modificacoes e consultas no banco de dados.

> dbquery.py
	  Gera os relatorios das informacoes do banco de dados. Existem duas saidas: TXT e CSV.

> logs.py
	  Grava em arquivos de logs as operacoes dos programas.

> settings.py
	  Arquivo de configuracao
