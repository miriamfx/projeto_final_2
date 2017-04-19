from datetime import datetime
from settings import  LOG_FOLDER

def logdbquery(msg):
    ''' Registra o log do dbquery
    msg = mensagem do log '''
    with open('{0}{1}log_dbquery.log'.format(LOG_FOLDER), 'a') as flog:
        flog.writelines('{0}: {1}\n'.format(datetime.today().strftime('%d/%m/%Y %H:%M:%S'), msg))

def logdbmanager(msg):
    ''' Registra o log do dbmanager
        msg = mensagem do log '''
    with open('{0}{1}log_dbmanager.log'.format(LOG_FOLDER), 'a') as flog:
        flog.writelines('{0}: {1}\n'.format(datetime.today().strftime('%d/%m/%Y %H:%M:%S'), msg))


def logsnmpget(msg):
    ''' Registra o log do snmpget
        msg = mensagem do log '''
    with open('{0}{1}log_snmpget.log'.format(LOG_FOLDER), 'a') as flog:
        flog.writelines('{0}: {1}\n'.format(datetime.today().strftime('%d/%m/%Y %H:%M:%S'), msg))
