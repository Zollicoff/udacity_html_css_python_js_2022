pets = {
    'birds': {
        'parrot': 'Arthur',
        'canary': 'Ford'
    },
    'fish': {
        'goldfish': 'Zaphod',
        'koi': 'Trillium'
    }
}

for e in pets:
    print(e)

for e in pets['birds']:
    print(e)

for e in pets['birds'].values():
    print(e)
