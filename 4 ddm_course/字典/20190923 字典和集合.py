
dial_codes = [
    (86,'china'),
    (91,'india'),
    (1,'United states'),
    (62,'Indonesia'),
    (55,'Brazil'),
    (92,'Pakistan'),
    (880,'Bangladesh'),
    (234,'Nigera'),
    (7,'Russia'),
    (81,'Japan'),
    ]
d1 = dict(dial_codes)
d2 = dict(sorted(dial_codes))
d3 = dict(sorted(dial_codes,key=lambda x:x[1]))
assert d1 == d2 and d2 == d3

print('d1:',d1.keys())
print('d2:',d2.keys())
print('d3:',d3.keys())