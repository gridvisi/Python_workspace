def greet(language):
    database = {'english': 'Welcome','czech': 'Vitejte','danish': 'Velkomst','dutch': 'Welkom','estonian': 'Tere tulemast',
'finnish': 'Tervetuloa','flemish': 'Welgekomen','french': 'Bienvenue','german': 'Willkommen','irish': 'Failte','italian': 'Benvenuto',
'latvian': 'Gaidits','lithuanian': 'Laukiamas','polish': 'Witamy','spanish': 'Bienvenido','swedish': 'Valkommen','welsh': 'Croeso'}
    try:
        return database[language]
    except KeyError:
        return database['english']
print(greet('IP_ADDRESS_INVALID'))