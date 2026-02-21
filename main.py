from akordy import song

test = song()
i = input("url zadej: ")
if i:
    test.url = i
else:
    test.url = "https://pisnicky-akordy.cz/vypsana-fixa/schovana"
test.load()
test.curl()
test.save()
print (test.songtext)
