from datetime import datetime

import logs
from pysnmp.hlapi import *

import dbmanager


class SimpleSnmp ():
    def __init__(self, ip, community):
        self.ip = ip
        self.community = community

    def time_conversion(timestr):
        ''' Converte o tempo em segundos para horas e minutos '''
        if __name__ == '__main__':
            try:
                timesec = int(timestr)
                timemin = (timesec / 100) / 60
                m = timemin % 60.0
                h = (timemin - m) / 60
                return '{0} hora(s) e {1} minuto(s)'.format(int(h), int(m))
            except:
                return '0'

    def GetSNMP1(self):
        resultado = []
        resultado = errorIndication, errorStatus, errorIndex, varBindTable = next(
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
        if errorIndication:
            print(errorIndication)

        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBindTable[-1][int(errorIndex) - 1] or '?')
                      )
                logs.logsnmpget('FAIL: ID {0} - HOST {1} - {0}'.format( errorStatus.prettyPrint()))
            else:
                for varBindTableRow in varBindTable:
                    for name, val in varBindTableRow:
                        if str(name) == 'sysContact':
                            resultado.append(val)
                        if str(name) == 'sysUpTime':
                            resultado.append(self.time_conversion(val))
                        if str(name) == 'sysDescr':
                            resultado.append(val)
                        if str(name) == 'sysObjectID':
                            resultado.append(val)
                        if str(name) == 'sysLocation':
                            resultado.append(val)

            if len(resultado) == 5:
                resultado.insert(0, self.ip)
                resultado.append(datetime.today().strftime('%d/%m/%Y'))
                resultado.append(datetime.today().strftime('%H:%M:%S'))
                dbmanager.reg_group1_db('{0}{1}'.format(dbmanager.DB))
                logs.logsnmpget('SUCESSO: Dados do Grupo 1 do ID {0} e Host {1} coletados.'.format(logs.ID, logs.HOST))

        return resultado

    def GetSNMP2(self):
        resultado2 = []
        mem = ''
        resultado2 = errorIndication, errorStatus, errorIndex, varBindTable = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),

                   ObjectType(ObjectIdentity('HOST-RESOURCES-MIB', 'hrSWRunPerfCPU', 0)),
                   ObjectType(ObjectIdentity('HOST-RESOURCES-MIB', 'hrSWRunPerfMem', 0)),
                   )
        )


        if errorIndication:
            print(errorIndication)
            logs.logsnmpget('FAIL: ID {0} - HOST {1} - {0}'.format(logs.ID, logs.HOST, errorIndication))
        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBindTable[-1][int(errorIndex) - 1] or '?')
                        )
                logs.logsnmpget('FAIL: ID {0} - HOST {1} - {0}'.format(logs.ID, logs.HOST, errorStatus.prettyPrint()))
            else:
                for varBindTableRow in varBindTable:
                    for name, val in varBindTableRow:
                        if str(name) == 'hrSWRunPerfCPU':
                            mem = str(int(val) / 1024)
                        if str(name).find('hrSWRunPerfMem') >= 0:
                            resultado2.append(str(name).split('.')[-1])

        return varBindTable, resultado2, mem


    def GetSNMP3(self):
        resultado3 = []
        mem = ''
        resultado3 = errorIndication, errorStatus, errorIndex, varBindTable = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),

                   ObjectType(ObjectIdentity('SNMPv2-MIB', 'ipForwarding', 0)),
                   ObjectType(ObjectIdentity('SNMPv2-MIB', 'ipInHdrErrors', 0)),
                   )
        )


        if errorIndication:
            print(errorIndication)
            logs.logsnmpget('FAIL: ID {0} - HOST {1} - {0}'.format(logs.ID, logs.HOST, errorIndication))
        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBindTable[-1][int(errorIndex) - 1] or '?')
                        )
                logs.logsnmpget('FAIL: ID {0} - HOST {1} - {0}'.format(logs.ID, logs.HOST, errorStatus.prettyPrint()))
            else:
                for varBindTableRow in varBindTable:
                    for name, val in varBindTableRow:
                        if str(name) == 'hrSWRunPerfCPU':
                            mem = str(int(val) / 1024)
                        if str(name).find('hrSWRunPerfMem') >= 0:
                            resultado3.append(str(name).split('.')[-1])



if __name__ == '__main__':
    SimpleSnmp()

