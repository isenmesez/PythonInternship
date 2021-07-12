access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]
conf = {'access': access_template, 'trunk': trunk_template,
        'vlanaccess': 'Введите номер VLAN:', 'vlantrunk': 'Введите разрешенные VLANы:'}
mode = input('Введите режим работы интерфейса (access/trunk):')
interface = input('Введите тип и номер интерфейса:')
vlan = input(conf['vlan' + mode])
print(('interface {}').format(interface))
print(('\n'.join(conf[mode])).format(vlan))
