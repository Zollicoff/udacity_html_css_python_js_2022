weather = [
    {
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for e in weather[0]:
    print(e)

for e in weather[1].values():
    print(e)

for e in weather:
    print(e['date'])
    print(e['state'])
    print(e['temp'])

