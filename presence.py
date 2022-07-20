import json
import os

import lightHouse
import ping
import restAPI
import time
import datetime

localHostList = "hosts.json"
pingInternal = 60
hosts = []


class Presence:

    def load_hosts(self):
        # function to get and load configuration from file.
        if os.path.isfile(localHostList):  # check if file exists
            with open(localHostList, "r") as read_file:  # open config file with read permissions
                global hosts  # import appConfig global var
                hosts = json.load(read_file)  # json decode config and set app config var
            return True
        else:
            # config file does not exists
            return False

    def save_hosts(self):
        with open(localHostList, "w") as write_file:
            # open contacts file with write permissions
            json.dump(hosts, write_file, default=str) # json encode loaded app config to config file using json dump
        return True

    def pingHost(self, host):
        response = os.system("ping -c 1 " + host)

        if response == 0:
            return True
        else:
            return False

    def runCycle(self):
        if hosts:
            for host in hosts:
                if host['localIP'] != "":
                    detected = self.pingHost(host['localIP'])
                    if detected:
                        host['detected'] = True
                        host['lastDetected'] = datetime.datetime.now().isoformat()
                    else:
                        host['detected'] = False
                else:
                    host['detected'] = False

        else:
            print("Hosts Empty -- check with api")
            dtGetHosts = restAPI.API.presenceHosts(self, lightHouse.appConfig['houseID'],
                                                   lightHouse.appConfig['lightHouseKey'],
                                                   lightHouse.appConfig['lightHouseNode'])
            getHosts = json.loads(dtGetHosts)
            print(getHosts)
            if getHosts['status'] == "ok":
                hosts[:] = getHosts['data']
            else:
                print("API Error: "+getHosts['error'])

        self.save_hosts()

    def loopCycle(self):
        self.runCycle()

    def __init__(self):
        self.load_hosts()
        self.loopCycle()

