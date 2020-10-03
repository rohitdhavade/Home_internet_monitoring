from AVG_MAIN import AVG_MAIN
from Subscriber_Graph_Output import Subscriber_Graph_Output
from datetime import datetime
from GET_DATA_FROM_INPUTS import GET_DATA_FROM_INPUTS
from Subscriber_Excel import Subscriber_Excel

input_from_file = GET_DATA_FROM_INPUTS(filename='C:\\Users\\rdhavade\\OneDrive\\OneDrive - Cisco\\working_directory\\Home_Network_monitoring\\INPUTS.txt')
input_from_file.GET_DATA_FROM_INPUTS()

if __name__ == "__main__":
    publisher_obj = AVG_MAIN(interval=input_from_file.interval,web_to_test=input_from_file.website_list)
    subscriber_graph_obj = Subscriber_Graph_Output(uptime_dict={})
    subscriber_excel_obj = Subscriber_Excel(uptime_dict={})

    #subscribe the graph_obj to the publisher
    publisher_obj.attach(subscriber_graph_obj)
    publisher_obj.attach(subscriber_excel_obj)

    while input_from_file.AppOn:
        publisher_obj.SAVE_AVG_UPTIME()
        subscriber_graph_obj.update_graph()
        subscriber_excel_obj.update_excel_graph()
        input_from_file.GET_DATA_FROM_INPUTS()
