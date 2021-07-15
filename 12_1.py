import subprocess


def ping_ip_addresses(ip_addresses):
    pinged = []
    notpinged = []

    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", "-c", "3", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            pinged.append(ip)
        else:
            notpinged.append(ip)

    return pinged, notpinged


if __name__ == "__main__":
    print(ping_ip_addresses(["1.2.3.4", "87.240.137.158"]))