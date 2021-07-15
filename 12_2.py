import ipaddress


def convert_ranges_to_ip_list(ip_addresses):
    result = []
    for ip_address in ip_addresses:
        if "-" in ip_address:
            start_ip, stop_ip = ip_address.split("-")
            if "." not in stop_ip:
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                result.append(str(ipaddress.ip_address(ip)))
        else:
            result.append(str(ip_address))
    return result

print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))