import pyttsx3

class SpeakerControl:
    volume = 0
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()

    # Parameters:
    #     - volume is an int indicating the desired volume level for speakers
    #
    # Description:
    #     - Set the current volume of the RC car as specified
    #
    # Return:
    #     - Returns nothing
    def set_volume(self, volume):
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)
            self.engine.runAndWait()
        self.engine.stop()

    # Parameters:
    #     - None
    #
    # Description:
    #     - Return current volume level
    #
    # Return:
    #     - Returns volume as an int
    def get_volume(self):
        return self.engine.getProperty('volume')

    # Parameters:
    #     - message is the string which dictates the message the speakers will play
    #
    # Description:
    #     - Take in the message as a String and convert it to an audio file. Then speak the statement out loud
    #
    # Return:
    #     - Returns nothing
    def play_message(self, message):
        pass

