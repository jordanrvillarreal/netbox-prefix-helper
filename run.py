import ipaddress, easysnmp, re

from easysnmp import Session

session = Session(hostname='192.168.86.85',version=2, community='public')

output = session.walk(oids='.1.3.6.1.2.1.4.20.1.3')

for addy in output:
    foundIP = re.search('.*3\.6\.1\.2\.1\.4\.20\.1\.3\.(.+?)\'', str(addy)).group(1)
    foundSubnet = re.search('.*value=\'(.+?)\'',str(addy)).group(1)
    foundIPandSubnet = (str(foundIP) + "/" + str(foundSubnet))

    prefix = ipaddress.ip_interface(foundIPandSubnet)

    print (str(prefix.network.network_address) + "/" + str(foundSubnet))

