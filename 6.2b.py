while True:
    ip = input('Введите ip адрес:')
    ip1 = ip.split('.')
    n = ip.count('.')
    if n == 3:
        if int(ip1[0]) in range(0,256) and int(ip1[1]) in range(0,256) and int(ip1[2]) in range(0,256) and int(ip1[3]) in range(0,256):
            if 1 <= int(ip1[0]) <= 223:
                print('unicast')
                break
            elif 239 <= int(ip1[0]) <= 244:
                print('multicast')
                break
            elif ip == '255.255.255.255':
                print('local broadcast')
                break
            elif ip == '0.0.0.0':
                print('unassigned')
                break
            else:
                print('unused')
                break
        else:
            print('Неправильный IP-адрес')
            continue
    else:
        print('Неправильный IP-адрес')
        continue