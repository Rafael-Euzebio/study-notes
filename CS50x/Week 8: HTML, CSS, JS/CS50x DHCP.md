# DHCP
DHCP (Dynamic Host Configuration Protocol) is a protocol to assign unique [[CS50x IP]] addresses to every device that connects to the internet. The protocol is implemented by a DHCP server

The protocol is standardized worldwide so there are no conflicts

## Server
The DHCP server can have authority on a designed range, from residential networks to large campus networks. Some routers also have their own DHCP servers

```mermaid
flowchart LR
    Device --> DHCP[DHCP Server] --> ... --> Internet
```
