import requests
import re


r = requests.get(
    'https://www.zscaler.com/blogs/security-research/return-emotet-malware-analysis')

# print the response
html = r.text.encode("utf-8")
# print(html)
# print(type(html))


# html = html.decode('utf-8')

# print(html.encode('utf-8'))

result1 = re.search("[0-9a-fA-F]{64}", html.decode('utf-8'))
# print(result1.string.encode("utf-8"))

sha256 = re.compile("[0-9a-fA-F]{64}", re.IGNORECASE)
md5 = re.compile("[0-9a-fA-F]{32}", re.IGNORECASE)
result2 = re.findall(sha256, html.decode('utf-8'))
print(result2)

unique_hash = [*set(result2)]

print(type(result2))
print(len(unique_hash))
print(unique_hash)
