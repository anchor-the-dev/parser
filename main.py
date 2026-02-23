from akordy import song

test = song()
test.url = "https://pisnicky-akordy.cz/traband/lovci-lebek"
test.load()
test.curl()
test.save()
print(test.songtext)
