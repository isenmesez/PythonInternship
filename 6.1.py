print('6.1')
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
mac1 = []
for i in mac:
    mac1.append(i.replace(':','.'))
print(mac1)

