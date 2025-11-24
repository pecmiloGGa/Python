class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__saved_volume = self.__volume  

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__saved_volume = self.__volume
                self.__volume = 0
            else:
                self.__muted = False
                self.__volume = self.__saved_volume

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__saved_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__saved_volume = self.__volume

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__saved_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__saved_volume = self.__volume

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
