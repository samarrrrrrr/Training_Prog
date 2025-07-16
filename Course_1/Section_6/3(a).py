class Songs:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length

a = Songs('Back on 74','Jungle', 120)
b = Songs('Swiming','Flawed Mango', 60)

print(a.length+b.length)
