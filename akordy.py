from bs4 import BeautifulSoup
import requests as rr

class song:
    def __init__(self):
        self.name = ""
        self.author = ""
        self.raw = None
        self.sp = None
        self._url = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        if self.url:
            response = rr.get(value)
            self.raw = response.text
            self.sp = BeautifulSoup(self.raw, "html.parser")
            self.author = self.sp.title.text.split("-")[0].strip()
            self.name = self.sp.title.text.split("-")[1].strip()
