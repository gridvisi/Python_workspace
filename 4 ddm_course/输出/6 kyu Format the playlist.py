'''
https://www.codewars.com/kata/61a87854b4ae0b000fe4f36b/train/python

+----------------------------+------+-----------------+
| Name                       | Time | Artist          |
+----------------------------+------+-----------------+
| Candy Shop                 | 3:45 | 50 Cent         |
| In Da Club                 | 3:13 | 50 Cent         |
| What Up Gangsta            | 2:58 | 50 Cent         |
| In The Night Of Wilderness | 5:26 | Blackmill       |
| Wicked                     | 2:53 | Future          |
| Cudi Montage               | 3:16 | KIDS SEE GHOSTS |
| Cellular                   | 2:58 | King Krule      |
| Pull Up                    | 3:35 | Playboi Carti   |
| The Birthday Party         | 4:45 | The 1975        |
| One                        | 4:36 | U2              |
+----------------------------+------+-----------------+
'''

songs = [
    ('In Da Club', '3:13', '50 Cent'),
    ('Candy Shop', '3:45', '50 Cent'),
    ('One', '4:36', 'U2'),
    ('Wicked', '2:53', 'Future'),
    ('Cellular', '2:58', 'King Krule'),
    ('The Birthday Party', '4:45', 'The 1975'),
    ('In The Night Of Wilderness', '5:26', 'Blackmill'),
    ('Pull Up', '3:35', 'Playboi Carti'),
    ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
    ('What Up Gangsta', '2:58', '50 Cent')
]
def format_playlist(songs):
    width = len(max([''.join(c) for c in songs],key=len))
    namewid = len(max([c[0] for c in songs],key=len))
    timewid = len(max([c[1] for c in songs],key=len))
    artwid = len(max([c[2] for c in songs],key=len))

    print("+"+"-"*namewid+"+"+"-"*timewid+"+"+"-"*artwid+"+")
    print("| "+"Name"+" "*(namewid-4)+"| "+"Time"+ " "*(timewid-6))
    for c in songs:
        print("|"+f"{c[0]}")
    return width,namewid,artwid,timewid




#1st
# Just cleaned it a bit
def format_playlist(songs):
    size1 = max((4, *(len(s[0]) for s in songs)))
    size2 = max((6, *(len(s[2]) for s in songs)))
    border = f"+-{'-' * size1}-+------+-{'-' * size2}-+"
    line = lambda a, b, c: f"| {a.ljust(size1)} | {b.ljust(4)} | {c.ljust(size2)} |"

    res = []
    res.append(border)
    res.append(line("Name", "Time", "Artist"))
    res.append(border)

    for name, duration, artist in sorted(songs, key=lambda k: (k[2], k[0])):
        res.append(line(name, duration, artist))
    if songs:
        res.append(border)

    return '\n'.join(res)


#2nd
def format_playlist(songs):
    ln = max([4] + [len(s[0]) for s in songs])
    la = max([6] + [len(s[2]) for s in songs])
    row = f"+-{'-' * ln}-+------+-{'-' * la}-+\n"
    res = row + f"| {'Name'.ljust(ln)} | Time | {'Artist'.ljust(la)} |\n" + row
    if songs:
        for n, t, a in sorted(songs, key=lambda c:(c[2], c[0])):
            res += f"| {n.ljust(ln)} | {t} | {a.ljust(la)} |\n"
        res += row
    return res[:-1]

print(format_playlist(songs))