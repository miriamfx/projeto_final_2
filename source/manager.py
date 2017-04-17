#!/usr/bin/env python
#coding: utf-8
# Arquivo que executa tarefas simples e convoca programas externos.

import subprocess
from datetime import datetime
import re
import main
import dbmanager
import dbquery
import time
import datetime
from get import SimpleSnmp


def opt1(ip, community):
    ''' Cadastro manual de Hosts. '''
    l = []
    if (main.ip != '') and (main.community != ''):
        l.append((main.ip, main.comnunity))
        laux = dbmanager.reg_query_db('{0}{1}'.format(dbmanager.DB), l)
        dbmanager.reg_hosts_db('{0}{1}'.format(dbmanager.DB), laux)
    else:
        main.resultado = ('IP ou Comunidade vazio nao sao validos')


def opt2(self, ip, community):
    ''' Faz uma chamada no coletor manual de informacoes que ira coletar as informacoes dos Hosts.'''
    SimpleSnmp()


def opt3(ip, community, time1, time2):
    ''' Executa o agendamento do collector, que ira coletar informacoes de gerenciamento dos hosts cadastrados. '''
    if time1 < time2:
        resultado = 'O tempo digitado para execução é menor que o intervalo de tempo'
    else:
        if (time.time < time1):
            time.sleep(time2)
            dbmanager.reg_hosts_db()




def opt4(self, ip):
    pass


def opt5(self, ip):
    ''' Realiza a Exclusao de Hosts '''
    if (main.ip != ''):
        dbmanager.del_hosts_db('{0}{1}'.format(dbmanager.DB), dbmanager.l)
    else:

        dbmanager.drop_tables_db
        dbmanager.create_tables_db


if __name__ == '__main__':
   gerente()

