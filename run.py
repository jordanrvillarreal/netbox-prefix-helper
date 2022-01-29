import ipaddress, easysnmp, re

from easysnmp import Session

#SNMP v2
#session = Session(hostname='192.168.86.74',version=2, community='public')

#SNMP v3
#session = Session(hostname='192.168.86.74', version=3, security_level='auth_with_privacy', security_username='SNMPv3User', privacy_protocol='AES', privacy_password='PrivPass2', auth_protocol='SHA', auth_password='AuthPass1')

output = session.walk(oids='.1.3.6.1.2.1.4.20.1.3')

for addy in output:
    foundIP = re.search('.*3\.6\.1\.2\.1\.4\.20\.1\.3\.(.+?)\'', str(addy)).group(1)
    foundSubnet = re.search('.*value=\'(.+?)\'',str(addy)).group(1)
    foundIPandSubnet = (str(foundIP) + "/" + str(foundSubnet))

    prefix = ipaddress.ip_interface(foundIPandSubnet)

    print (str(prefix.network.network_address) + "/" + str(foundSubnet))

