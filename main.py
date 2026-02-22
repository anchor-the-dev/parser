from akordy import song

test = song()
i = input("url zadej: ")
test.url = "https://pisnicky-akordy.cz/vypsana-fixa/schovana"
test.load()
test.curl()
test.save()
print(test.songtext)
