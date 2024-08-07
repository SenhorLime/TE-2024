import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.contagem.cefetmg.br/category/noticias/")
soup = BeautifulSoup(page.content, "html.parser")

main_tag = soup.select("div#lista-conteudo")

for noticia in main_tag:
    for info in noticia.select("h4#titulo"):
        titulo = info.select_one("a").text
        link = info.select_one("a").get("href")

        print(f"{titulo} - {link}")
