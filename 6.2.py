print(6.2)
b = True
for i in range(5):
    ip = input('Введите ip адрес:')
    ip1 = ip.split('.')
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
