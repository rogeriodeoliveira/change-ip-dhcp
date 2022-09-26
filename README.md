## Tool to set ip Static or DHCP


### Compile:
```python
nuitka --onefile .\main.py
```
### Usage:
Set default config in config.txt file

example:

```json
{
    "INTERFACE": "Ethernet",
    "IP": "192.168.0.20",
    "MASK": "255.255.255.0",
    "GATEWAY": "192.168.0.1",
    "DNS": "8.8.8.8"
}
```



Run as administrator
