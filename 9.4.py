ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    config = {}
    with open(config_filename) as file:
        for line in file:
            line = line.rstrip()
            if line and not (line.startswith("!") or ignore_command(line, ignore)):
                if line[0].isalnum():
                    section = line
                    config[section] = []
                else:
                    config[section].append(line.strip())
    return config

print(convert_config_to_dict("config_sw1.txt"))