print('4.1')
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
n1 = "GigabitEthernet"
n2 = nat[0:40]  # с помощью .index узанала индекс части строки, которую надо заменить и срезала строку
n3 = nat[52:len(nat)]  # нужную часть записала в другую переменную
n4 = n2 + n1 + n3  # сложили необходимые строки
print(n4)
print(nat.replace('FastEthernet','GigabitEthernet'))  # пример более оптимального решения

print('4.2')
mac = "AAAA:BBBB:CCCC"
print(mac[0:4] + '.' + mac[5:9] + '.' + mac[10:len(mac)])
print(mac.replace(':','.')) # пример более оптимального решения

print('4.3')
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
c = (config[30:len(config)])
print(c.split(','))

print('4.4')
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(set(vlans)))

print('4.5')
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
v1 = (command1[30:len(command1)]).split(',')
v2 = (command2[30:len(command2)]).split(',')
print(sorted(list(set(v1) & set(v2))))

print('4.6')
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
l = list(ospf_route.split(' '))
print("%-20s %-15s" % ('Prefix', l[7]))
print("%-20s %-15s" % ('AD/Metric', l[8].strip('[]')))
print("%-20s %-15s" % ('Next-Hop ', l[9]))
print("%-20s %-15s" % ('Last update', l[10].replace(',','')))
print("%-20s %-15s" % ('Outbound Interface', l[11].replace(',','')))

print('4.7')
mac = "AAAA:BBBB:CCCC"
print(bin(int((mac.replace(':','')),16)).strip('0b'))

print('4.8')
ip = "192.168.3.1"
i1 = bin(int(ip[0:3])).replace('0b','',1)
i2 = bin(int(ip[4:7])).replace('0b','',1)
i3 = bin(int(ip[8])).strip('0b').zfill(6)
i4 = bin(int(ip[10])).strip('0b').zfill(7)
print(ip[0:3],' '*4, ip[4:7], ' '*4, ip[8], ' '*4, ip[10])
print(i1,i2,i3,i4)