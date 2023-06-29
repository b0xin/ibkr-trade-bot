# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:49:07 2023

@author: boxin
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class TradingApp(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson = ""):
        print("Error {} {} {} {}".format(reqId,errorCode,errorString, advancedOrderRejectJson))
        
app = TradingApp()
app.connect("127.0.0.1", 7497, clientId = 1)