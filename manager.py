#!/usr/bin/env python
#coding: utf-8
# Arquivo que executa tarefas simples e convoca programas externos.

import subprocess
from datetime import datetime
import re
import main
import dbmanager
from dbquery import sysusers_process_csv
import time
from threading import Timer
from get import SimpleSnmp

def opt2(self,ip, community):
    ''' Faz uma chamada no coletor manual de informacoes que ira coletar as informacoes dos Hosts.'''
    SimpleSnmp()


def opt3(self,ip, community, time1, time2):
    ''' Executa o agendamento do collector, que ira coletar informacoes de gerenciamento dos hosts cadastrados. '''
    if time1 < time2:
        resultado = 'O tempo digitado para execução é menor que o intervalo de tempo'
    else:
        while (time.time()< time2):
            t = Timer(30.0, dbmanager.reg_GetSNMP1_db())
            t.start()


def opt4(self, ip):
    sysusers_process_csv()


def opt5(self, ip):
    ''' Realiza a Exclusao de Hosts '''
    if (main.ip != ''):
        dbmanager.del_hosts_db(dbmanager.hosts)
    else:
        resultado = ('erro ao exluir dados!')


if __name__ == '__main__':

    opt2().run()
    opt3().run()
    opt4().run()
    opt5().run()



