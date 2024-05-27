with open('wiki_page.txt', 'r') as file:
    content = file.read()
href_values = []
start = 0

while True:
    start_link = content.find('<a ', start)
    if start_link == -1:
        break

    end_link = content.find('>', start_link)
    if end_link == -1:
        break

    start_href = content.find('href="', start_link, end_link)
    if start_href == -1:
        start = end_link
        continue

    start_quote = start_href + len('href="')
    end_quote = content.find('"', start_quote)
    href_value = content[start_quote:end_quote]

    href_values.append(href_value)

    start = end_quote

print(href_values)