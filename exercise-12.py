persons = int(input())
playlist = []
number = []

songs = set()
selected_songs = []

for i in range(persons):
    number.append(int(input()))
    playlist.append(set(input().split()))

songs = playlist[0]
for i in range(1, persons):
    songs.intersection_update(playlist[i])

selected_songs = list(songs)
selected_songs.sort()

print(len(selected_songs))
print(' '.join(selected_songs))