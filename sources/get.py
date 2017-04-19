from datetime import datetime
import logs
from pysnmp.hlapi import *
import dbmanager


class SimpleSnmp ():
    def __init__(self, ip, community):
        ip = self.ip
        community = self.community

    def GetSNMP1(self,ip, community):
        hosts_list = []
        hosts_list = errorIndication, errorStatus, errorIndex, varBindTable = next(
            getCmd(SnmpEngine(),
                   CommunityData(community),
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
                        if str(name) == self.ip:
                            hosts_list.append(val)
                        if str(name) == self.community:
                            hosts_list.append(val)
                        if str(name) == 'sysObjectID':
                            hosts_list.append(val)
                        if str(name) == 'sysContact':
                            hosts_list.append(val)
                        if str(name) == 'sysUpTime':
                            hosts_list.append(val)
                        if str(name) == 'sysDescr':
                            hosts_list.append(val)
                        if str(name) == 'sysLocation':
                            hosts_list.append(val)

            if len(hosts_list) == 7:
                hosts_list.append(datetime.today().strftime('%d/%m/%Y'))
                hosts_list.append(datetime.today().strftime('%H:%M:%S'))
                dbmanager.reg_group1_db('{0}{1}'.format(dbmanager.DB))
                logs.logsnmpget('SUCESSO: Dados do GetSNMP1 do IP {0} e Comunidade {1} coletados.'.format(logs.ID, logs.HOST))

        return hosts_list

    def GetSNMP2(ip,community):
        resultado2 = []
        mem = ''
        resultado2 = errorIndication, errorStatus, errorIndex, varBindTable = next(
            getCmd(SnmpEngine(),
                   CommunityData(community),
                   UdpTransportTarget((ip, 161)),
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


    def GetSNMP3(ip, community):
        resultado3 = []
        mem = ''
        resultado3 = errorIndication, errorStatus, errorIndex, varBindTable = next(
            getCmd(SnmpEngine(),
                   CommunityData(community),
                   UdpTransportTarget((ip, 161)),
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

