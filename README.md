# netbox-prefix-helper
A simple script to extract prefixes from production equipment for easy import into netbox

This code will allow you to point to a networked device and it will extract all of the entries under OID iso.3.6.1.2.1.4.20.1.3 alongside their subnet masks.  The output will be in a format friendly for import into import module in netbox.  There are probably better ways of extracting this information, but I opted to go right at the SNMP OID since Cisco, Arista, and other manufuctures will store this same information in the same place.  Haven't tested Juniper yet. 

## Configuration
---
There isn't much to configure here, outside of SNMP connectivity methods.  Both v2 and v3 are commented out at the top of the file.  Uncomment the method you need.


## Examples 
---
### *Cisco IOS*

Showing only the interfaces that have IPs associated with them.
```
Cisco-Switch#show ip interface brief | include \.
GigabitEthernet0/0     192.168.86.74   YES DHCP   up                    up      
Vlan10                 10.10.10.1      YES manual administratively down down    
Vlan20                 10.10.20.1      YES manual administratively down down    
Vlan30                 10.10.30.39     YES manual administratively down down    
Vlan40                 10.10.40.125    YES manual administratively down down    
Cisco-Switch#
```
Truncated `show run` output that keys in on just interfaces.
```
Cisco-Switch#show running-config | inc Ethernet|Vlan|address
interface GigabitEthernet0/0
 ip address dhcp
interface Vlan10
 ip address 10.10.10.1 255.255.255.0
interface Vlan20
 ip address 10.10.20.1 255.255.255.0
interface Vlan30
 ip address 10.10.30.39 255.255.255.128
interface Vlan40
 ip address 10.10.40.125 255.255.255.192
Cisco-Switch#
```
Then the output from running against our example device.
```
10.10.10.0/255.255.255.0
10.10.20.0/255.255.255.0
10.10.30.0/255.255.255.128
10.10.40.64/255.255.255.192
192.168.86.0/255.255.255.0
```
