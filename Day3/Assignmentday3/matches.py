players = ['sehwag', 'virat', 'saloni']
runs = [100,120,200]
matches =  [20,10,30]

print(players, runs, matches)
name = input("Enter the name of the player")

for i in range(len(players)):
    if name==players[i]:
        print(runs[i]/matches[i])
    else:
        print("No player found")
