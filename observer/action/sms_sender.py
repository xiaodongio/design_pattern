
import sys
sys.path.append("..")
from observer import Observer

class SmsSender(Observer):
    
    def update(self, observable, object):
        print("name : " + object["name"] + "region : " + object["region"])