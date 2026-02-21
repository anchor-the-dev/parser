from akordy import song

test = song()
i = input("url zadej: ")
if i:
    test.url = i
else:
    test.url = "https://pisnicky-akordy.cz/spiritual-kvintet/batalion"
test.load()
test.curl()
test.save()
