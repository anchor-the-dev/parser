from bs4 import BeautifulSoup as bs
import requests as rr
import os

## name nazev unicode z tittle
## author author unicode taky z tittle
## raw cely html stranky
## polivka BeautifulSoup parser
## asau asciiauthor autor z url pasnuty nazev filesystem
## asnm asciiname nazev pisnicky parsnuty z url zaroven nazev soboru
##
class song:
    def __init__(self):
        self.name = ""
        self.author = ""
        self.raw = None
        self.polivka = None
        self.url = None
        self.songtext = None

    def parse_url(self):
        parts = self.url.strip("/").split("/")
        self.asau = parts[-2]
        self.asnm = parts[-1]
        self.path = f"data/{self.asau}/{self.asnm}"

    def parse(self):
        self.polivka = bs(self.raw, "html.parser")
        self.author = self.polivka.title.text.split("-")[0].strip()
        self.name = self.polivka.title.text.split("-")[1].strip()

    def curl(self):
        if self.url:
            if not self.raw:
                self.parse_url()

                self.response = rr.get(self.url)
                self.raw = response.text
                self.parse()
        #        divs = self.polivka.find_all("div", id="songtext")
        #        self.songtext = "\n".join(div.get_text(strip=True) for div in divs)

    def load(self):
        self.parse_url()
        if os.path.exists(f"{self.path}/raw.html"):
            with open(f"{self.path}/raw.html", "r", encoding="utf-8") as f:
                self.raw = f.read()
                self.parse()

    def save(self):
        if self.url:
            os.makedirs(f"{self.path}", exist_ok=True)
            with open(f"{self.path}/raw.html", "w", encoding="utf-8") as f:
                f.write(self.raw)

