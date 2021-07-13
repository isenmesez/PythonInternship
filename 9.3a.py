def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    with open(config_filename) as file:
        for line in file:
            if "interface FastEthernet" in line:
                current_interface = line.split()[-1]
                access[current_interface] = 1
            elif "switchport access vlan" in line:
                access[current_interface] = int(line.split()[-1])
            elif "switchport trunk allowed vlan" in line:
                vlans = [int(i) for i in line.split()[-1].split(",")]
                trunk[current_interface] = vlans
                del access[current_interface]
    return access, trunk

print(get_int_vlan_map("config_sw2.txt"))