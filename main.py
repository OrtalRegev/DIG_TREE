import dns.resolver
import sys

res = dns.resolver.Resolver()

def get_domain_from_url(url):
    exts = ['co', 'net', 'org', 'ac']
    dots_list = str(url).split('.')
    if dots_list[-3] in exts:
        return dots_list[-4] + "." + dots_list[-3] + "." + dots_list[-2]
    return dots_list[-3] + "." + dots_list[-2]

def get_nameservers(domain):
    servers_arr = []
    for server in res.query(domain, 'NS'):
        servers_arr.append(get_domain_from_url(server.target))
    return set(servers_arr)

queue = []

domain = sys.argv[1] + "." # for our parsing
queue.append(get_domain_from_url(domain))
ns_ans = {}

while len(queue) > 0:
    this_domain = queue.pop()

    ns_ans[this_domain] = {'children': [], 'color': 'green'} # starts as in-bailiwick

    for server in get_nameservers(this_domain):
        if server not in ns_ans:
            queue.append(server)

        if server != this_domain:
            ns_ans[this_domain]['children'].append(server)
            ns_ans[this_domain]['color'] = 'red' # out-of-bailiwick

print ns_ans