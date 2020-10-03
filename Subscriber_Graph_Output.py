from SubscriberInterface import SubscriberInterface
import numpy as np
import matplotlib.pyplot as plt

class Subscriber_Graph_Output(SubscriberInterface):
    
    def __init__(self, uptime_dict:dict):
        self.uptime_dict = uptime_dict
    
    def update(self, publisher):
        self.uptime_dict = publisher.get_state()
 
    def update_graph(self):
        x_axis = list(self.uptime_dict.keys())
        y_axis = list(self.uptime_dict.values())
        print('x-axis' + str(x_axis))
        print('y-axis' + str(y_axis))
        print('type of y-axis first element is ' + str(type(y_axis[0])))
        print('type of x-axis first element is ' + str(type(x_axis[0])))
        plt.figure('Internet Uptime')
        plt.plot(x_axis, y_axis)
        plt.xlabel('Time - DD HH:MM')
        plt.ylabel('Reachability %')
        plt.title('Uptime Percentage')
        plt.show()
        print('after plotting')
