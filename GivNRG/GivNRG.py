
import json
import requests
from datetime import datetime, timedelta, date

import logging
_LOGGER = logging.getLogger("GivNRG")

class GivNRG:
    baseURL = None
    session = requests.Session()

    def __init__(self):
        self.baseURL = 'http://www.givenergy.cloud/GivManage/api/'

    def login(self,username,password):
        data = {"account":username, "password":password}
        url = f"{self.baseURL}/login"
        r = self.session.post(url, data=data)
        return r.status_code

    # Plant API    
    def getPlantList(self):
        url = f"{self.baseURL}/plant/getPlantList"
        r = self.session.post(url)
        return r.json()

    def getPlantInfo(self,plantId):
        url = f"{self.baseURL}/plant/getPlantInfo"
        params = {'plantId': plantId}
        r = self.session.post(url, params=params)
        return r.json()

    def getPlantSummary(self):
        url = f"{self.baseURL}/plant/getPlantSummary"
        r = self.session.post(url)
        return r.json()

    def getPlantRuntime(self,plantId):
        url = f"{self.baseURL}/plant/getPlantRuntime"
        params = {'plantId': plantId}
        r = self.session.post(url, params=params)
        return r.json()

    def getPlantDevices(self,plantId):
        url = f"{self.baseURL}/plant/getPlantDevices"
        params = {'plantId': plantId}
        r = self.session.post(url, params=params)
        return r.json()

    def getPlantEnergy(self):
        url = f"{self.baseURL}/plant/getPlantEnergy"
        r = self.session.post(url)
        return r.json()

    def getPlantEvents(self,plantId):
        url = f"{self.baseURL}/plant/getPlantEvents"
        params = {'plantId': plantId}
        r = self.session.post(url, params=params)
        return r.json()