import re

def get_ip_from_cfg(config):
    with open(config) as f:
        regex = re.compile(
            r"interface (?P<intf>\S+)\n"
            r"( .*\n)*"
            r" ip address (?P<ip>\S+) (?P<mask>\S+)"
        )
        match = regex.finditer(f.read())

    result = {m.group("intf"): m.group("ip", "mask") for m in match}
    return result

print(get_ip_from_cfg("config_r1.txt"))