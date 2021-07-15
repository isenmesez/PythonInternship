import re


def get_ip_from_cfg(config):
    regex = r"ip address (\S+) (\S+)"
    with open(config) as f:
        result = [m.groups() for m in re.finditer(regex, f.read())]
    return result

print(get_ip_from_cfg("config_r1.txt"))