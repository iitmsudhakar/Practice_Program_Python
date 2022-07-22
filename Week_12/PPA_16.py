players = {
    'Karthik': {
        'Tennis': True,
        'Badminton': False,
        'Cricket': True
    },
    'Rahul': {
        'Tennis': True,
        'Badminton': True,
        'Cricket': False
    },
    'Tina': {
        'Tennis': False,
        'Badminton': True,
        'Cricket': True
    }
}


def loop(players, game):
    name = set()
    L = []
    for x in players:
        for g in game:
            if players[x][g]:
                L.append(players[x][g])
                # print(players[x][g])
                if L.count(True) == 2:
                    name.add(x)
                return name


game = ['Tennis', 'Badminton', 'Cricket']

print(loop(players, game))
