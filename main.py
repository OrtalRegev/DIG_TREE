import socket
import dns.resolver

# Basic query
for rdata in dns.resolver.query('www.yahoo.com', 'CNAME'):
    print(rdata.target)

# Set the DNS Server
resolver = dns.resolver.Resolver()
resolver.nameservers=[socket.gethostbyname('ns1.cisco.com')]
for rdata in resolver.query('www.yahoo.com', 'CNAME'):
    print(rdata.target)
