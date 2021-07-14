from ex11_1 import parse_cdp_neighbors

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    result = {}

    for filename in filenames:
        with open(filename) as show_command:
            parsed = parse_cdp_neighbors(show_command.read())
            result.update(parsed)
    return result


if __name__ == "__main__":
    topology = create_network_map(infiles)
    print(topology)