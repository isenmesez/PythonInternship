access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    for inter, vlan in intf_vlan_mapping.items():
        result.append(f"interface {inter}")
        for template in access_template:
            if template.endswith("access vlan"):
                result.append(f"{template} {vlan}")
            else:
                result.append(template)
    return result


print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config_2, access_mode_template))