# TCP
TCP (Transmission Control Protocol) is a protocol that complements [IP](./CS50x_IP.md). Therefore the *IP Suite* is commonly called **TCP/IP**


## Ports
TCP ports are identifiers for internet services and media  
These ports allow packages received from IP addresses to be forwarded to specific applications, or treated in a special way  
For that to happen, every package transmitted must have an IP address as destination and a port assigned to it

### Well-Known Ports
Ports from 0 to 1023 are well-known ports, these are specifically assigned to applications and proccesses of widely used services

Example:

|     Port      | Description| 
|-------------- | ---------- | 
| 80            | HTTP, used by web browsers      |
| 443           | HTTPS, Encrypted version of HTTP|
| 194           | Internet Relay Chat (IRC)       |

## Segment Structure
TCP allows packages to be segmented and divided into chunks to send them in separately. Each part will have a header identifying it so it can be reassembled at the destination

## Flowchart

```mermaid
flowchart LR

Server1[Web Server]--- HTTP --> Device 
Server2[IRC Server]--- IRC --> Device 
Device --> TCP
TCP --- 80  --> Web[Web Browser]
TCP --- 194 --> Client[IRC Client]



