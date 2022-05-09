import os
import json
import time

import restAPI

configPath = "appConfig.json"  # global define config file path
appConfig = {}  # global set app config


class LightHouse:
    def load_config(self):
        # function to get and load configuration from file.
        if os.path.isfile(configPath):  # check if file exists
            with open(configPath, "r") as read_file:  # open config file with read permissions
                global appConfig  # import appConfig global var
                appConfig = json.load(read_file)  # json decode config and set app config var
            return True
        else:
            # config file does not exists
            return False

    def save_config(self):
        with open(configPath, "w") as write_file:
            # open contacts file with write permissions
            json.dump(appConfig, write_file) # json encode loaded app config to config file using json dump
        return True

    def mnu_setup_lightHouse(self):
        print("\n\n--LightHouse Setup --\n")
        print("To set up Lighthouse, please open OurHouse and turn on LightHouse for your house.\n You should be given a 'LightHouse Key', you will need to enter this.")
        entLightHouseKey = ""
        while(entLightHouseKey == ""):
            entLightHouseKey = input("Enter LightHouse Key: ")

        print("Thanks! We now need your house code, you can find this in house settings.")
        entHouseCode = ""
        while (entHouseCode == ""):
            entHouseCode = input("Enter House code: ")

        dtCheckCode = restAPI.API.setupHouseCheck(self, {"houseCode": entHouseCode})
        if dtCheckCode != {}:
            # ran successfully
            print("ran successfully")
            print(dtCheckCode)
        else:
            print(dtCheckCode)

        print("Thanks! \nTo confirm:\nLightHouse Key: "+entLightHouseKey+"\nHouse Code: "+entHouseCode)

    def __init__(self):
        if self.load_config():
            print("Welcome to OurHouse LightHouse!\nProgram loading...\n")
            time.sleep(2)
            print("LightHouse Version: "+appConfig['version'])
            if appConfig['houseID'] != "":
                print("LightHouse is set up.")
                print("Initialising...")
            else:
                print("LightHouse is not set up. need to run set up")
                prmpt = ""
                while (prmpt == ""):
                    print("\nPlease choose one of the following options and enter the prompt:\n1. Run LightHouse setup wizard - 'run'\n2. Exit program 'exit'\n")
                    prmpt = input("")
                if prmpt.upper() == "RUN":
                    self.mnu_setup_lightHouse()
                elif prmpt.upper() == "EXIT":
                    exit()
                else:
                    exit()

        else:
            print("Failed to load config")