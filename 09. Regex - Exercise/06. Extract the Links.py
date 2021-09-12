import re

links_found = []
pattern = r"w{3}\.[a-zA-Z0-9-]+(?P<domainblock>\.[a-z]+)+"


while True:
    text = input()
    if not text:
        break

    valid_domains = re.finditer(pattern, text)
    if valid_domains:
        domains = [domain.group() for domain in valid_domains]
        for d in domains:
            links_found.append(d)

print("\n".join(links_found))


