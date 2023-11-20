# HTTP/HTTPS
HTTP or HTTPS is a protocol built on top of [IP](./CS50x_IP.md) to exchange hypermedia information commonly in the form of [HTML](./CS50x_HTML.md) documents  
A common http/https connection consists of [HTTP Request](./CS50x_HTTP-Request.md) and [HTTP Response](./CS50x_HTTP-Response.md)

## Addresses
A HTTP/HTTPS address has the following format:
`https://www.example.com/`  
`https://www.example.com/file.html`  
`https://www.example.com/folder/file.html`  

It can be divided in 3 parts:

- Protocol:
    - *http/https://* is the protocol
    - Other protocols for exchange of hypermedia exist
        - *gopher://* is an example

- Fully Qualified Domain name
    - Prefix
        - *www.* was commonly used as a prefix to indicate *World Wide Web* pages. 
        - *mail.* was common for email services. It's mostly in disuse nowadays and can be omitted   
    - [Domain Name](./CS50x_Domain-Name.md)
        - *example* is the domain name. This is converted to [IP](./CS50x_IP.md) addresses  through a DNS  

    - Top Level Domain
        - *.com* is the [TLD](./CS50x_TLD.md). It indicates what kind of organization owns the website being accessed and is the last part of the domain name

- Path
    - The domain name is converted to a ip address which is the unique address of a computer. That computer has folders and files. The path portion indicates what folder and what files to retrieve
        - *...example.com/* Is the the very root of the folder. If there's a *index.html* file it is automatically retrieved
        - *...example.com/file.html* is specifically the file *file.html*
        - *...example.com/folder/file.html* is specifically the file *file.html* under the folder *folder*


