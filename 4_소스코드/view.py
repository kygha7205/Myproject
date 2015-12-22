# Reader

class Reader(object):
    @staticmethod
    def ox(message):
        response = input(message).lower()
        while not (response == 'o' or response == 'x'):
            response = input(message).lower()
        return response == 'o'

    @staticmethod
    def playmod(message):
        playmod = input(message)
        while (playmod.isdigit() != True) or ((playmod != "1") and (playmod != "2")):
            playmod = input(message)
        return playmod