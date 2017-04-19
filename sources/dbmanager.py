import sqlite3
import manager
import dbquery
from settings import DB
import logs

def create_db(db):
    ''' Cria o arquivo do Banco de Dados vazio (sem tabelas).
        E utilizado por padrao o caminho do Banco de Dados definidos no settings.py
        As operacaoes de sucesso e falha sao inseridas no arquivo de log log_dbmanager '''
    try:
        # Apenas cria o arquivo do Banco de Dados vazio (sem tabelas)
        with open(db, 'a') as arq:
            pass

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, arquivo {0} do Banco de Dados criado.'.format(db))
    except:
        #Insere falha no log
        logs.logdbmanager('FALHA, nao e possivel criar o arquivo {0} do Banco de Dados.'.format(db))
        print ('Erro ao criar o arquivo do Banco de Dados.')


def create_tables_db(db):

    try:
        con = sqlite3.connect(db)
        c = con.cursor()

        # Inicia a criacao das tabelas no Banco de Dados.
        c.execute("CREATE TABLE Hosts(id INTEGER PRIMARY KEY, ip TEXT, community TEXT)")
        c.execute("CREATE TABLE GetSNMP1(id INTEGER PRIMARY KEY, Comunidade TEXT, sysObjectID TEXT, sysContact TEXT, sysDescr TEXT, sysLocation TEXT, sysUpTime TEXT, data DATETIME, hora TEXT)")
        c.execute("CREATE TABLE GetSNMP2(id INTEGER PRIMARY KEY, hrSWRunPerfCPU TEXT, hhrSWRunPerfMem TEXT)")
        c.execute("CREATE TABLE GetSNMP3(id INTEGER PRIMARY KEY, ipForwarding TEXT, ipInHdrErrors TEXT)")
        resultado = ('Tabelas criadas com sucesso.')
        con.commit()
        c.close
        con.close

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Tabelas criadas no Banco de Dados {0}.'.format(db))
    except:
        # Insere falha no log
        logs.logdbmanager('FALHA, nao e possivel criar as tabelas no Banco de Dados {0}.'.format(db))
        print ('Erro ao criar tabelas no Banco de Dados.')


def drop_tables_db(db):
    ''' Exclui as tabelas do Banco de Dados.
        O Banco de Dados utilizando e o definido no settings.py.
         '''
    try:
        con = sqlite3.connect(db)
        c = con.cursor()

        # Comandos de exclusao de tabela
        c.execute("DROP TABLE Hosts")
        c.execute("DROP TABLE GetSNMP1")
        c.execute("DROP TABLE GetSNMP2")
        c.execute("DROP TABLE GetSNMP3")

        con.commit()
        print ('Tabelas do Banco de dados deletadas com sucesso.')
        c.close
        con.close

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Tabelas excluidas do Banco de Dados {0}.'.format(db))
    except:
        # Insere falha no log
        logs.logdbmanager('FALHA, nao e possivel excluir tabelas do Banco de Dados {0}.'.format(db))
        print ('Erro ao deletar tabelas do Banco de Dados.')

def reg_GetSNMP1_db(db, hosts_list):
    ''' Grava do Dados do GetSNMP1 no Banco de Dados.
        O Banco de Dados utilizando e o definido no settings.py.
        hosts_list contem uma lista com idhost, sysDescr, sysUpTime, sysContact, sysLocation.
        '''
    try:
        con = sqlite3.connect(db)
        c = con.cursor()

        # Executa o INSERT na tabela GetSNMP1
        # {0}ip,{1} Comunidade,{2} sysObjectID,{3}sysContact,{4}sysDescr,{5}sysUpTime,{6}sysLocation,{7}data, {8}hora
        c.execute("INSERT INTO GetSNMP1 VALUES(NULL, {0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(hosts_list[0], hosts_list[2], hosts_list[3], hosts_list[4], hosts_list[5], hosts_list[6], hosts_list[7], hosts_list[8]))

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, GetSNMP1 do Host id {0}, ip {1} inserido no Banco de Dados {2}.'.format(hosts_list[0], hosts_list[1], db))
        print ('GetSNMP1 do Host IP {0}, Comunidade {1} inserido no Banco de Dados com sucesso.'.format(hosts_list[0], hosts_list[1]))
        con.commit()
        c.close
        con.close
    except:
        # Insere falha no log
        logs.logdbmanager('FALHA, nao e possivel inserir dados no Grupo 1 no Banco de Dados {0}.'.format(db))
        print ('Erro ao inserir hosts no Banco de Dados.')


def query_GetSNMP1_db(db, idhost):
    ''' Executa um SELECT na tabela de Group1 e retorna todos os dados das consulta automatica do ID fornecido.
        O Banco de Dados utilizando e o definido no settings.py.
        idhost contem o ID do host consultado.
        '''
    try:
        con = sqlite3.connect(db)
        c = con.cursor()

        # Executa um SELECT na tabela Group1 para o host idhost
        query = c.execute("SELECT * FROM Group1 WHERE idhost = {0} ORDER BY id DESC".format(ip))

        # Percorre todos os resultados da consulta e armazena em uma lista no formato de tupla
        for i in query:
            l = (i[2], i[3], i[4], i[5], i[6], i[7], i[8])

            # Sai do for, para o Grupo 1, somente a ultima informacao e relevante
            break
        con.commit()
        c.close
        con.close

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Listagem do Grupo 1 gerada.')
        return l
    except:
       # Insere falha no log
        logs.logdbmanager('FALHA ao gerar dados do Grupo 1 para o ID {0}.'.format(idhost))
        print ('Falha ao gerar dados do Grupo 1 para o ID {0}.'.format(idhost))


def reg_GetSNMP2_db(db, hosts_list2):
    ''' Grava do Dados do Grupo 2 no Banco de Dados.
        O Banco de Dados utilizando e o definido no settings.py.
        hosts_list conte uma lista com idhost, hrSystemUsers, hrSystemProcess, data e hora.
        '''
    try:
        con = sqlite3.connect(db)
        c = con.cursor()

        # Executa um INSERT na tabela Group2
        # {0}idhost, {2}hrSystemUsers, {3}hrSystemProcess, {4}data, {5}hora
        c.execute("INSERT INTO GetSNMP2 VALUES(NULL, {0}, '{1}', '{2}', '{3}', '{4}')".format(hosts_list2[0], hosts_list2[2], hosts_list2[3], hosts_list2[4], hosts_list2[5]))

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Grupo 2 do Host id {0}, ip {1} inserido no Banco de Dados {2}.'.format(hosts_list2[0], hosts_list2[1], db))
        print ('Grupo 2 do Host id {0}, ip {1} inserido no Banco de Dados com sucesso.'.format(hosts_list2[0], hosts_list2[1]))
        con.commit()
        c.close
        con.close
    except:
        # Insere falha no log
        logs.logdbmanager('FALHA, nao e possivel inserir dados no Grupo 2 no Banco de Dados {0}.'.format(db))
        print ('Erro ao inserir hosts no Banco de Dados.')


def query_GetSNMP2_db(db, idhost):
    ''' Executa um SELECT na tabela de Group2 e retorna uma lista com todos os dados das consulta automatica do ID fornecido.
        O Banco de Dados utilizando e o definido no settings.py.
        idhost contem o ID do host consultado.
        '''
    try:
        l = []
        con = sqlite3.connect(db)
        c = con.cursor()

        # Executa um SELECT na tabela Group2 para o host idhost
        query = c.execute("SELECT * FROM GetSNMP2 WHERE idhost = {0} ORDER BY data, hora".format(idhost))

        # Percorre todos os resultados da consulta e armazena em uma lista no formato de tupla
        for i in query:
            l.append(i)
        con.commit()
        c.close
        con.close

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Listagem do Grupo 2 gerada.')
        return l
    except:
       # Insere falha no log
        logs.logdbmanager('FALHA ao gerar dados do Grupo 2 para o ID {0}.'.format(idhost))
        print ('Falha ao gerar dados do Grupo 2 para o ID {0}.'.format(idhost))


def reg_group3_db(db, hosts_list3):
    ''' Grava do Dados do Grupo 3 no Banco de Dados.
        O Banco de Dados utilizando e o definido no settings.py.
        hosts_list contem a lista com idhost, Memory, hrStorageDescr, hrStorageSize, hrStorageUsed, data e hora '''
    try:
        con = sqlite3.connect(db)
        c = con.cursor()

        # Executa um INSERT na tabela Group3
        # {0}idhost, {2}Memory, {3}hrStorageDescr, {4}hrStorageSize, {5}hrStorageUsed, {6}data, {7}hora
        c.execute("INSERT INTO Group3 VALUES(NULL, {0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(hosts_list3[0], hosts_list3[2], hosts_list3[3], hosts_list3[4], hosts_list3[5], hosts_list3[6], hosts_list3[7]))

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Grupo 3 do Host id {0}, ip {1} inserido no Banco de Dados {2}.'.format(hosts_list3[0], hosts_list3[1], db))
        print ('Grupo 3 do Host id {0}, ip {1} inserido no Banco de Dados com sucesso.'.format(hosts_list3[0], hosts_list3[1]))
        con.commit()
        c.close
        con.close
    except:
        # Insere falha no log
        logs.logdbmanager('FALHA, nao e possivel inserir dados no Grupo 3 no Banco de Dados {0}.'.format(db))
        print ('Erro ao inserir hosts no Banco de Dados.')


def query_GetSNMP3_db(db, idhost):
    ''' Executa um select na tabela de Group3 e retorna uma lista com todos os dados da consulta automatica do ID fornecido
        O Banco de Dados utilizando e o definido no settings.py.
        idhost contem o ID do host consultado. '''
    try:
        l = []
        con = sqlite3.connect(db)
        c = con.cursor()

        # Executa um SELECT na tabela Group3 para o host idhost
        query = c.execute("SELECT * FROM GetSNMP3 WHERE idhost = {0} ORDER BY data, hora".format(idhost))

        # Percorre todos os resultados da consulta e armazena em uma lista no formato de tupla
        for i in query:
            l.append(i)
        con.commit()
        c.close
        con.close

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, Listagem do Grupo 3 gerada.')
        return l
    except:
        # Insere falha no log
        logs.logdbmanager('FALHA ao gerar dados do Grupo 3 para o ID {0}.'.format(idhost))
        print ('Falha ao gerar dados do Grupo 3 para o ID {0}.'.format(idhost))



if __name__ == '__main__':
    l = query_hosts_db('{0}{1}'.format(DB))
    if len(l) > 0:
        print ('ID\tIP\tHOST')
        for i in l:
            print ('{0}\t{1}\t{2}'.format(i[0], i[1], i[2]))
