from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete


engine = create_engine('sqlite3:///snmpdb.db')

base = declarative_base()

class hosts(base):
    __tablename__ = 'hosts'
    Column ='Ip'(String(15), primary_key = True),
    Column ='Comunidade' (String (8)),
    Column ='IdObject', (String),
    Column ='Contact', (String),
    Column ='Desc', (String),
    Column ='Uptime', (String),
    Column ='Location', (String),
    Column ='Data', (String),
    Column ='Hora', (String),


    def reg_hosts_bd(self):

        connection = engine.connect()
        ins = hosts.insert(


        )

        result = connection.execute(ins)
        connection.close()




    def del_hosts_db(self):
        connection = engine.connect()
        d = delete(hosts)
        connection.execute(d)
        connection.close()
