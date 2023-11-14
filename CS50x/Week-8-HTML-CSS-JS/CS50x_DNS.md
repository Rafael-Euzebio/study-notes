# DNS
DNS (Domain Name System) is a server that associates [IP](./CS50x_IP.md) addresses with [Domain Name](./CS50x_Domain-Name.md) (human readable strings)  
These servers know all the websites that exist on the internet and their IP addresses, so humans only have to remember the website names and not their IP addresses

## Example
| Domain Name| IP Address
|-------------- | -------------- 
| google.com | 142.251.39.110

```mermaid
flowchart LR
    Device--- 'google.com' --> DNS --> 142.251.39.110 
```
