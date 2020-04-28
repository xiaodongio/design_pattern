from account import Account
from sms_sender import SmsSender
import time

account = Account()
account.addObserver(SmsSender())
account.login("dek", "127.0.0.1", time.time())
account.login("dek1", "112.10.69.191", time.time())