# Incident Response: Wireshark and Volatility Analysis

## 1. Preparation

- Ensure Wireshark is installed and available.
- Familiarize yourself with common filters, such as:
  - `ip.addr == <target_ip>`
  - `tcp.port == <port_number>`
  
## 2. Detection and Analysis

- Use Wireshark to filter specific traffic:
  ```plaintext
  ip.addr == 192.168.1.100 && tcp
