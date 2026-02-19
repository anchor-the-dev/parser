from bs4 import BeautifulSoup as bs 
import requests as rr
import sqlite3


class song:
    def __init__(self):
        self.name = ""
        self.author = ""
        self.raw = None
        self.polivka = None
        self._url = None
        self.songtext = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        if self.url:
            response = rr.get(value)
            self.raw = response.text
            self.polivka = bs(self.raw, "html.parser")
            self.author = self.polivka.title.text.split("-")[0].strip()
            self.name = self.polivka.title.text.split("-")[1].strip()
            self.songtext = self.polivka.find_all("div", id="songtext")
    def load(self):
        pass  
    def save(self):
        pass
    

    def save(self, db_path="dat.db"):
        if not self.author or not self.name:
            print("Song není naparsovaný.")
            return

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("""
            INSERT INTO songs (author, title, lyrics, url)
            VALUES (?, ?, ?, ?)
        """, (self.author, self.name, self.songtext, self.url))
