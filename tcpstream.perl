
### 3. Memory Forensics Using Volatility
Example command to list running processes from a memory dump:
```bash
volatility -f memory.dmp --profile=Win7SP1x64 pslist
