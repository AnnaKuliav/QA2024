import re

with open('/Users/annakuliavets/Documents/pythonQA2024/wiki_page.txt', 'r') as file:
    content = file.read()

pattern = r'<a[^>]+href="([^"]+)"'
href_values = re.findall(pattern, content)

print(href_values)