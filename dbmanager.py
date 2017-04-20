from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
import csv
import settings
import subprocess
import get
from get import SimpleSnmp

engine = create_engine('sqlite3:///snmpdb.db')

base = declarative_base()

class hosts(base):
    __tablename__ = 'hosts'
    Column('Ip',String(15), primary_key = True),
    Column('Comunidade', String (8)),
    Column('IdObject', String),
    Column('Contact', String),
    Column('Desc', String),
    Column('Uptime', String),
    Column('Location', String),
    Column('Data', String),
    Column('Hora', String),
    Column('hrSWRunPerfCPU', String)
    Column('hrSWRunPerfMem', String)
    Column('ipForwarding', String)
    Column('ipInHdrErrors', String)



    def reg_hosts_bd(self):
        connection = engine.connect()
        Insert = sessionmaker(bind=engine)
        session = Insert()
        session.add_all([ hosts(Ip=SimpleSnmp.hosts_list[0],
                                    Comunidade=SimpleSnmp.hosts_list[1],
                                    Contact=SimpleSnmp.hosts_list[2],
                                    Desc=SimpleSnmp.hosts_list[3],
                                    UpTime=SimpleSnmp.hosts_list[4],
                                    Location=SimpleSnmp.hosts_list[5],
                                    Data=SimpleSnmp.hosts_list[6],
                                    Hora=SimpleSnmp.hosts_list[7],
                                    hrSWRunPerfCPU=SimpleSnmp.hosts_list2[0],
                                    hrSWRunPerfMem=SimpleSnmp.hosts_list2[1],
                                    ipForwarding=SimpleSnmp.hosts_list3[0],
                                    ipInHdrErrors=SimpleSnmp.hosts_list3[1],
                                )
                          ])
        session.add(hosts)
        connection.close()

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

    def del_hosts_db(self):
        connection = engine.connect()
        d = delete(hosts)
        connection.execute(d)
        connection.close()
