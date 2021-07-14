print(6.2)
ip = input('Введите ip адрес:')
ip1 = ip.split('.')
n = ip.count('.')
if n == 3:
    if int(ip1[0]) in range(0,256) and int(ip1[1]) in range(0,256) and int(ip1[2]) in range(0,256) and int(ip1[3]) in range(0,256):
        if 1 <= int(ip1[0]) <= 223:
            print('unicast')
        elif 239 <= int(ip1[0]) <= 244:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
    else:
        print('Неправильный IP-адрес', n)
else:
    print('Неправильный IP-адрес',n)