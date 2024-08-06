n, game = map(str, input().split())
players = []

for _ in range(int(n)):
    players.append(input())

player_count = len(set(players))


if game == 'Y':
    print(player_count)
elif game == 'F':
    print(player_count // 2)
else:
    print(player_count // 3)