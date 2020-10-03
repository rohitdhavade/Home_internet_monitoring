import time
from REST_GET_TEST import REST_GET_TEST
from datetime import datetime

class AVG_MAIN(REST_GET_TEST):
    def __init__(self,interval:int,web_to_test:list):
        self.interval:int = interval #time interval in minutes
        self.web_to_test:list = web_to_test
        self.avg_uptime:dict = {} #average uptime of internet for given interval
        self._subscribers = [] # list of subscriber objects
        
    def AVG_UPTIME_CALC(self):
        int_secs:int = self.interval*60  # interval in seconds
        true_count:int = 0 # keeps no. of successful responses to tests
        google_test = REST_GET_TEST(websites=self.web_to_test)
        bool_dict:dict = {} # saves responses coming from each tests {datetime:boolean}
        for i in range(0,int_secs):
            bool_dict[datetime.now()] = (google_test.SAVE_RESPONSE())
            time.sleep(1)
        for key in bool_dict:
            if bool_dict[key] == True:
                true_count += 1
        print('AVG_MAIN.AVG_UPTIME_CALC completed')
        #print(str(bool_dict))
        return float((true_count/int_secs)*100)

    def SAVE_AVG_UPTIME(self):
        self.avg_uptime[datetime.now()] = self.AVG_UPTIME_CALC()
        self._notify()

# below is implementation for Observer Design Pattern
    def get_state(self):
        return self.avg_uptime
    def attach(self,subscriber):
        self._subscribers.append(subscriber)
    def detach(self,subscriber):
        self._subscribers.remove(subscriber)
    def _notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self)


if __name__ == "__main__":
    interval:int = 15
    input:list = [] # PUT INPUTS.txt content in this list
    input_filename = 'C:\\Users\\rdhavade\\OneDrive\\OneDrive - Cisco\\working_directory\\Home_Network_monitoring\\INPUTS.txt'
    with open(input_filename,'r') as fileh:
        for line in fileh:
            input.append(line)
    interval = int(input[input.index('INTERVAL=\n')+1].rstrip())


