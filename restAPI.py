import requests

baseURL = "https://data.knoyletechnologies.co.uk/api/our-house"


class API:
    def setupHouseCheck(self, data):
        response = requests.get(baseURL + "/v1" + "/house/check", data)
        if response.status_code == 200:
            return response.content
        else:
            return response.content

    def setupLightHouse(self, house, data):
        response = requests.post(baseURL + "/v1" + "/house/" + house + "/lightHouse/setup", data)
        if response.status_code == 200:
            return response.content
        else:
            return {}

    def house(self, house, key):
        headers = {'light-house-key': key, 'light-house-house': house}
        response = requests.get(baseURL + "/v1" + "/house/" + house, headers)
        if response.status_code == 200:
            return response.content
        else:
            return {}

    def presenceHosts(self, house, key):
        headers = {'light-house-key': key, 'light-house-house': house}
        response = requests.get(baseURL + "/v1" + "/house/" + house + "/lightHouse/presence/hosts", headers)
        if response.status_code == 200:
            return response.content
        else:
            return {}

    def presenceUpdate(self, house, key, data):
        headers = {'light-house-key': key, 'light-house-house': house}
        response = requests.post(baseURL + "/v1" + "/house/" + house + "/lightHouse/presence/update", headers, data)
        if response.status_code == 200:
            return response.content
        else:
            return {}
