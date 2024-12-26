# Network-Traffic-Check
This Python project generates random public IP addresses and checks them against predefined firewall rules. It simulates network traffic, determining whether each IP should be allowed or blocked based on a list of allowed IPs, providing a basic demonstration of network security practices.

## Purpose

The purpose of this script is to:

- Generate random public IP addresses, ensuring that the generated IPs are not part of private IP address ranges.
- Simulate network traffic by checking if each IP address should be allowed or blocked based on a set of firewall rules.
- Provide a simple demonstration of how a firewall might allow or block traffic based on IP addresses.

## Features

- **Random IP Generation**: Generates random public IP addresses while avoiding private IP ranges (like `10.x.x.x`, `172.16.x.x`, and `192.168.x.x`).
- **Firewall Rule Checking**: Compares each generated IP address to a list of allowed IPs and determines whether the traffic is allowed or blocked.
- **Simulated Network Traffic**: Simulates 100 network traffic checks and outputs the result for each check.

## How It Works

### 1. Random Public IP Generation
The `random_public_ip()` function generates random IP addresses by selecting values for each of the four octets. The first octet is chosen between 1 and 223 to ensure it falls within the public IP range. Private IPs (defined by certain ranges) are excluded to simulate only public IP traffic.

Private IP ranges:
- `10.0.0.0` to `10.255.255.255`
- `172.16.0.0` to `172.31.255.255`
- `192.168.0.0` to `192.168.255.255`

### 2. Firewall Rule Checking
The `check_rules_of_firewall()` function takes a randomly generated IP address and compares it against a list of allowed IPs. If the IP is in the allowed list, it returns "allow", otherwise it returns "block".

### 3. Main Simulation
The `main()` function initializes a predefined list of allowed IPs and simulates 100 random IP checks, printing the result (either "allow" or "block") for each IP address.

## Installation

1. Clone the repository or download the script file.
2. No additional libraries or dependencies are required other than Python's built-in `random` module.

## Usage

1. Save the Python script to a `.py` file, e.g., `firewall_checker.py`.
2. Run the script in your terminal


