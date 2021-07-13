trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = {}
    for port, vlans in intf_vlan_mapping.items():
        tmp = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlans_str = ",".join([str(vl) for vl in vlans])
                tmp.append(f"{command} {vlans_str}")
            else:
                tmp.append(command)
        result[port] = tmp
    return result

print(generate_trunk_config(trunk_config, trunk_mode_template))