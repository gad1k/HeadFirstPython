from pprint import pprint
import requests


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content),  resp.status_code, resp.url


urls = ("http://github.com", "http://oreilly.com", "http://yandex.by")

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, "->", status, "->", url)

print()
urls_res = {url: size for size, _, url in gen_from_urls(urls)}
pprint(urls_res)
