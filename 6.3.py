access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access': {'0/12': '10', '0/14': '11',
                       '0/16': '17', '0/17': '150'},

            'trunk': {'0/1': ['add', '10', '20'],
                      '0/2': ['only', '11', '30'],
                      '0/4': ['del', '17']}}

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
print('_' * 30)
for intf, vlan in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for trunk_command in trunk_template:
        if trunk_command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                print(' {} {} {}'.format(trunk_command, vlan[0], ','.join(vlan[1:])))
            elif vlan[0] == 'only':
                print(' {} {}'.format(trunk_command, ','.join(vlan[1:])))
            elif vlan[0] == 'del':
                vlan[0] = 'remove'
                print(' {} {} {}'.format(trunk_command, vlan[0], ','.join(vlan[1:])))
        else:
            print(' {}'.format(trunk_command))