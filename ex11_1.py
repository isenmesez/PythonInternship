def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде
    будет получен вывод команды с оборудования. Принимая как аргумент вывод
    команды, вместо имени файла, мы делаем функцию более универсальной: она может
    работать и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
    command_output = command_output.split('\n')
    for line in command_output:
        main = []
        second = []
        if line.find('>') != -1:
            main_machine = line[:line.find('>')]
        elif line.find('Eth') != -1:
            second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
            main.append(main_machine)
            second.append(second_machine)
            main_interface = main_eth + main_inter
            second_interface = second_eth + second_inter
            main.append(main_interface)
            second.append(second_interface)
            main_tuple = tuple(main)
            second_tuple = tuple(second)
            result[main_tuple] = second_tuple
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))