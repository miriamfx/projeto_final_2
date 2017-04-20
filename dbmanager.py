from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
import csv
import settings
import subprocess
import logs

engine = create_engine('sqlite:///snmpdb.db')

base = declarative_base()


class Host(base):
    __tablename__ = 'hosts'
    ip = Column(String(15), primary_key=True)
    comunidade = Column(String(8))
    idObject = Column(String)
    contact = Column(String)
    desc = Column(String)
    uptime = Column(String)
    location = Column(String)
    data = Column(String)
    hora = Column(String)
    qtd_mem = Column(String)
    qtd_mem_proc = Column(String)
    ip_Errors = Column(String)

    def save(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(self)
        session.commit()


    def create_db(self):
        base.metadata.create_all(engine)


        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, arquivo {0} do Banco de Dados criado.')

    def gera_rel(self):

        cursor = hosts.cursor()
        cursor.execute(hosts)
        row = cursor.fetchall()
        with open('snmp.csv', 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            for line in row:
                a.writerows(line)
        cursor.close()
        subprocess.call(['Calc', 'snmp.csv'.format(settings.CSV)])

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, relatorio {0} do Banco de Dados criado.')

    def del_hosts_db(self):
        connection = engine.connect()
        d = delete(hosts)
        connection.execute(d)
        connection.close()

        # Insere sucesso no log
        logs.logdbmanager('SUCESSO, excluido Banco de Dados.')