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
        response = requests.post(baseURL + "/v1" + "/house/" + house + "/lightHouse/setup", json=data)
        if response.status_code == 201:
            return response.content
        else:
            return response.content

    def house(self, house, key, node):
        headers = {'X-LIGHT-HOUSE-KEY': key, 'X-LIGHT-HOUSE-NODE': node}
        response = requests.get(baseURL + "/v1" + "/house/" + house, headers)
        if response.status_code == 200:
            return response.content
        else:
            return {}

    def presenceHosts(self, house, key, node):
        headers = {'X-LIGHT-HOUSE-KEY': key, 'X-LIGHT-HOUSE-NODE': node}
        response = requests.get(baseURL + "/v1" + "/house/" + house + "/lightHouse/presence/hosts", headers=headers)
        return response.content

    def presenceUpdate(self, house, key, node, data):
        headers = {'X-LIGHT-HOUSE-KEY': key, 'X-LIGHT-HOUSE-NODE': node}
        response = requests.post(baseURL + "/v1" + "/house/" + house + "/lightHouse/presence/update", headers=headers, json=data)
        return response.content
