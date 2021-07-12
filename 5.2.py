network = input('Введите адрес сети: ')
ip, mask = network.split('/')
mask = int(mask)
oct1, oct2, oct3, oct4 = [int(i) for i in ip.split('.')]
bin_mask = '1' * mask + '0' * (32 - mask)
m1, m2, m3, m4 = [int(bin_mask[i:i + 8], 2) for i in [0, 8, 16, 24]]
ip_output = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''

mask_output = '''
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask, m1, m2, m3, m4))