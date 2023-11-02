# Local Networks
Devices don't connect directly to each other. Local Networks do this job, acting as an intermediary between devices.  
A local network is a combination of routers, ISPs (Internet Service Providers), DNSs, DHCPs on a local level.  
These networks connect between themselvs so none of them has to know the IP addresses of every device and server in the world. Instead they only need to know what network has that information  

```mermaid
flowchart TD 
    subgraph Network One
        Device1((Device)) <--> Router1[Router]
        Device2((Device)) <--> Router1[Router]
        Router1 --- Network1
    end

    subgraph Network two
        Device3((Device)) <--> Router2[Router]
        Device4((Device)) <--> Router2[Router]
        Router2 <--> Network2[Network]
    end

    subgraph Network three
        Device5((Device)) <--> Router3[Router]
        Device6((Device)) <--> Router3[Router]
        Router3 <--> Network3[Network]
    end

    Network1 <--> Network2
    Network1 <--> Network3
    Network2 <--> Network3
```

Every device can connect to each other through their networks
