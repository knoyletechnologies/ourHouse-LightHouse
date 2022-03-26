import os


class Ping:

    def pingHost(self, host):
        response = os.system("ping -c 1 " + self)

        if response == 0:
            return True
        else:
            return False

