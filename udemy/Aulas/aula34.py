def generator(n=0, maximum =10):
    while True:
        yield n

        n += 1

        if n > maximum:
            return

gen = generator(n=0, maximum=8)
for n in gen:
    print(n)

