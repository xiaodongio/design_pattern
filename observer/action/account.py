import time
import sys
sys.path.append("..")
from observer import Observable


class Account(Observable):

    def __init__(self):
        super().__init__()
        self.__latest_ip = {}
        self.__lastest_region = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip" : ip, "region": region, "time":time})
        self.__latest_ip[name] = ip
        self.__lastest_region[name] = region

    def __getRegion(self, ip):
        ip_regions = {
            "127.0.0.1": "localhost",
            "112.10.69.91": "Hangzhou"
        }
        region = ip_regions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        latest_region = self.__lastest_region.get(name)
        print(latest_region, region)
        return latest_region is not None and latest_region != region