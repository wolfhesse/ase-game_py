links = [
    'https://www.semiosis.at/2017/10/16/viel-spricht-fuer-rot-blau/',
    'https://www.google.com/',

]


def http_fetch(link):
    return len(link)


print('====')
sizes = [[link, http_fetch(link)] for link in links]
print(sizes)

print('====')
sizes_m = [{'link': link,
            'size': http_fetch(link)}
           for link in links]
print(sizes_m)
print('====')

for link in links:
    print(link)

print('====')
