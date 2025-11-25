class DVDPlayer:
    @staticmethod
    def on():
        print("DVD player is on")

    @staticmethod
    def off():
        print("DVD player is off")


    @staticmethod
    def insert_disc():
        print("DVDPlayer inserted disc")

    @staticmethod
    def remove_disc():
        print("DVDPlayer removed disc")



class Television:
    def on(self):
        print("Television is on")

    def off(self):
        print("Television is off")

    def connect_dvd(self):
        print("DVD connected")

    def diconnect_dvd(self):
        print("DVD disconnected")

    def play(self):
        print("TV playing")




class TVDVDFacade:
    def __init__(self, t, v):
        self.tv = t
        self.dvd = v

    def watch_movie(self):
        self.tv.on()
        self.dvd.on()
        self.tv.connect_dvd()
        self.dvd.insert_disc()
        self.tv.play()

    def end_movie(self):
        self.dvd.remove_disc()
        self.tv.diconnect_dvd()
        self.dvd.off()
        self.tv.off()


if __name__ == "__main__":
    facade = TVDVDFacade(Television(), DVDPlayer())
    facade.watch_movie()
    facade.end_movie()


