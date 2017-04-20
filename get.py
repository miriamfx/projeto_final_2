from pysnmp.hlapi import *
from kivy.properties import ObjectProperty
from os import *
import dbmanager
import logs
from datetime import datetime


class SimpleSnmp():
    def __init__(self, ip, community):
        self.ip = ip
        self.community = community



    def GetSNMP(self):

        resultado = errorIndication, errorStatus, errorIndex, varBinds,varBindTable = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),

                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysObjectID', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)),


                      ),
        )
        print (resultado)
        host = dbmanager.Host()
        if errorIndication:
            print(errorIndication)

        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBindTable[-1][int(errorIndex) - 1] or '?')
                      )
                logs.logsnmpget('FAIL: ID {0} - HOST {1} - {0}'.format(errorStatus.prettyPrint()))
            else:
                for varBindTableRow in varBindTable:
                    for name, val in varBindTableRow:
                        if str(name) == 'sysObjectID':
                            resultado.append(val)
                            host.idObject = str(val)
                        if str(name) == 'sysContact':
                            resultado.append(val)
                            host.contact = str(val)
                        if str(name) == 'sysUpTime':
                            resultado.append(val)
                            host.uptime = str(val)
                        if str(name) == 'sysDescr':
                            resultado.append(val)
                            host.desc = str(val)
                        if str(name) == 'sysLocation':
                            resultado.append(val)
                            host.location = str(val)

            if len(resultado) == 5:
                host.ip = str(val)
                host.Comunidade = str(val)
                host.data = str (datetime.today().strftime('%d/%m/%Y'))
                host.hora = str(datetime.today().strftime('%H:%M:%S'))


                dbmanager.reg_group1_db('{0}{1}'.format(dbmanager.DB))
                logs.logsnmpget(
                    'SUCESSO: Dados do GetSNMP1 do IP {0} e Comunidade {1} coletados.'.format(logs.ID, logs.HOST))
        host.save()

        return str(resultado)