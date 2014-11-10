__author__ = 'Sergey'

class Human:
    def __init__(self, name, surname, weight):
        """

        @rtype : object
        """
        self.Name = name
        self.Surname = surname
        self.Weight = weight
        self.play_music = SonyWalkMan()

    def eat(self, food):
        self.Weight = self.Weight + food

    def run(self, km):
        self.Weight -= km * 0.1

    def __str__(self):
        return "%s \t%s \t%s kg" %(self.Name, self.Surname, self.Weight)

class SonyWalkMan:

    def Music_start(self):
        self.status = 'Playing now'

    def Music_Stop(self):
        self.status = 'Paused'

    def Music_show_track(self):
        self.status = 'The song name is %s' %random_track

    def __str__(self):
        return "%s" %self

random_track = 'Master of Puppets'

object = Human('Sergey', 'Chumak', 70)
print object

object.eat(15)
print object.Weight

object.run(160)
print int(object.Weight)

object.Weight = 90
print object.Weight

object.play_music.Music_start()

print object.play_music.status

object.play_music.Music_show_track()

print object.play_music.status

object.play_music.Music_Stop()

print object.play_music.status





if __name__ == "__main__":
    pass