import random

def random_public_ip():
    while True:

        octet1 = random.randint(1, 223)
        octet2 = random.randint(0, 255)
        octet3 = random.randint(0, 255)
        octet4 = random.randint(1, 254)


        if (octet1 == 10 or
            (octet1 == 172 and 16 <= octet2 <= 31) or
            (octet1 == 192 and octet2 == 168)):
            continue

        return f"{octet1}.{octet2}.{octet3}.{octet4}"

def check_rules_of_firewall(ip, allowed_ips):

    return "allow" if ip in allowed_ips else "block"

def main():

    allowed_ips = [
        "8.8.8.8",
        "8.8.4.4",
        "10.1.10.1",
        "10.0.10.1",
        "198.51.100.1",
        "203.0.213.2",
        "192.11.2.1",
        "198.51.100.67",
        "203.0.3.68",
        "192.0.2.80"
    ]

    for _ in range(100):
        ip_address = random_public_ip()
        action = check_rules_of_firewall(ip_address, allowed_ips)
        print(f"IP ADDRESS: {ip_address} ACTION: {action}")

if __name__ == "__main__":
    main()
