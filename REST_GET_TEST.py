from datetime import datetime
import requests, json
from requests.adapters import HTTPAdapter
import time

class REST_GET_TEST():
    
    def __init__(self,websites):
        self.websites:list = websites # ['www.facebook.com','www.google.com']
        self.response:dict = {} # {datetime:response_status in bool}

    def GET_TEST(self) -> bool:
        for website in self.websites:
            try:
                session = requests.Session()
                response = session.get(website) # REST GET request to website url
                status_code = response.status_code
                session.close()
            except:
                return False
            if status_code != 200:
                return False
            else:
                return True
    def SAVE_RESPONSE(self):
        self.response[datetime.now()] = self.GET_TEST()
        return self.GET_TEST()

if __name__ == "__main__":
    google = REST_GET_TEST(websites=['https://www.google.com'])
    UserSwitch = False
    input:list = [] # read INPUTS.txt file
    with open('INPUTS.txt','r') as fileh:
        for line in fileh:
            input.append(line)
    while UserSwitch:
        google.SAVE_RESPONSE()
        time.sleep(1)
        print(google.response)
