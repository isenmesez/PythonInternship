def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    with open(config_filename) as file:
        for line in file:
            line = line.rstrip()
            if line.startswith("interface"):
                inter = line.split()[1]
            elif "access vlan" in line:
                access[inter] = int(line.split()[-1])
            elif "trunk allowed" in line:
                trunk[inter] = [int(v) for v in line.split()[-1].split(",")]
        return access, trunk

print(get_int_vlan_map("config_sw1.txt"))