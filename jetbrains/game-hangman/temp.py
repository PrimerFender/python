n = int(input())
results = [input() for x in range(n)]
winners = [player.split()[0] for player in results if player.split()[1] == "win"]

print(winners)
print(len(winners))