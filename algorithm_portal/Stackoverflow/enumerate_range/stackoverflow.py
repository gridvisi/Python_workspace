# https://stackoverflow.com/questions/62090327/is-there-more-to-enumerate-than-just-ziprangelen
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

for i in enumerate(seasons):
    print(i)

for i in zip(range(len(seasons)), seasons):
    print(i)

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1