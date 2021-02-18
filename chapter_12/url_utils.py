import requests

urls = ("http://github.com", "http://oreilly.com", "http://yandex.by")

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), "->", resp.status_code, "->", resp.url)
