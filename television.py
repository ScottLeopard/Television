
class Television:
    '''
    Sets up class
    sets up class variables for mins and maxes of volume variable
    sets up class variables for mins and maxes of channel variable
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        sets tv status to False
        sets muted to False
        sets volume to minimum
        sets channel to minimum
        """
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        """
        switches the status from True to False
        and False to True
        :return: None
        """
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def mute(self):
        """
        checks if status is True
        if so then switches muted to True from False
        or False to True
        :return: None
        """
        if self.status:
            if self.muted == False:
                self.muted = True
            else:
                self.muted = False

    def channel_up(self):
        """
        checks if status is true if so
        checks if channel is at max
        if so then sets to channel min
        else increases channel by 1
        :return: None
        """
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        """
        checks if status is true if so
        checks if channel is at min
        if so then sets to channel max
        else decreases channel by 1
        :return: None
        """
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        """
        checks if status is true if so
        checks if volume is not at max
        if so increases volume by 1
        :return: None
        """
        if self.status:
            if self.volume != Television.MAX_VOLUME:
                self.volume += 1
                self.muted = False

    def volume_down(self):
        """
        checks if status is true if so
        checks if volume is not at min
        if so decreases volume by 1
        :return: None
        """
        if self.status:
            if self.volume != Television.MIN_VOLUME:
                self.volume -= 1
                self.muted = False

    def __str__(self):
        """
        checks if muted
        if so returns tv variables with volume set as min
        else returns volume as its value
        :return: tv variables
        """
        if self.muted:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {Television.MIN_CHANNEL}'
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'