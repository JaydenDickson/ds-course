def binary_search_strings(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return "Not found"

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"(self.album_name, self.number_of_songs, self.album_artist)"
    
album_1 = Album("Hellbound", 12, "feast for crows")
album_2 = Album("Abbey Road", 17, "The Beatles")
album_3 = Album("Thriller", 9, "Michael Jackson")
album_4 = Album("Back in Black", 10, "AC/DC")
album_5 = Album("Rumours", 11, "Fleetwood Mac")

albums1 = [album_1, album_2, album_3, album_4, album_5]
for album in albums1:
    print(album.album_name)

albums1.sort(key=lambda x: x.number_of_songs)
print([album.number_of_songs for album in albums1])

albums1[0],albums1[1] = albums1[1], albums1[0]

album_6 = Album("Hotel California", 9, "Eagles")
album_7 = Album("Led Zeppelin IV", 8, "Led Zeppelin")
album_8 = Album("The Wall", 26, "Pink Floyd")
album_9 = Album("Sgt. Pepper's Lonely Hearts Club Band", 13, "The Beatles") 
album_10 = Album("Born to Run", 8, "Bruce Springsteen")
albums2 = [album_6, album_7, album_8, album_9, album_10]

for album in albums2:
    print(album.album_name)

print("--------------------------------------")

for album in albums1:
    albums2.append(album)
albums2.append(Album("dark side of the moon", 10, "pink floyd"))
albums2.append(Album("oops!... I did it again", 16, "britney spears"))

albums2.sort(key=lambda x: x.album_name)
print("\n".join([album.album_name for album in albums2]))

print(binary_search_strings([album.album_name for album in albums2], "dark side of the moon"))



