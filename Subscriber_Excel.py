from SubscriberInterface import SubscriberInterface
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.chart import LineChart, BarChart, Reference, Series
from datetime import date, timedelta  
from openpyxl.chart.axis import DateAxis
from openpyxl.chart.axis import NumericAxis, TextAxis, SeriesAxis, DateAxis, ChartLines

wb = Workbook()
ws = wb.create_sheet(title="Report")
dest_filename = 'Report.xlsx'
ws.append(['Date Time','Reachability Percent for selected interval'])
x_ax_date = "%d/%m-%H:%M" #specifies format for date in graph

class Subscriber_Excel(SubscriberInterface):
    
    def __init__(self, uptime_dict:dict):
        self.uptime_dict = uptime_dict

    def update(self, publisher):
        self.uptime_dict = publisher.get_state()

    def update_excel(self):
        latest_key = sorted(self.uptime_dict.keys())[-1]
        print('dictionary is ' + str(self.uptime_dict))
        print('and the latest_key extracted is ' + latest_key.strftime(x_ax_date))
        try:
            print('Append executing')
            ws.append([latest_key.strftime(x_ax_date),self.uptime_dict[latest_key]])
            print('Append Executed')
            #wb.save(filename=dest_filename)
        except PermissionError:
            print('We didn\'t get permission to write to excel file, may it is open somewhere.')
    def update_excel_graph(self):
        self.update_excel()
        values = Reference(ws, min_col=2, min_row=2, max_row=ws.max_row)
        chart = LineChart()
        chart.height=8
        chart.width=25
        chart.style = 12
        chart.y_axis.crossAx = 500
        chart.y_axis.title = 'Avg Uptime'
        chart.x_axis = DateAxis(crossAx=100)
        chart.x_axis.title = 'Date'
        chart.x_axis.scaling.max = 50
        chart.x_axis.scaling.min = 1

        chart.x_axis.minorGridlines = ChartLines()
        chart.y_axis.minorGridlines = ChartLines()

        chart.add_data(values, titles_from_data=True)
        dates = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
        chart.set_categories(dates) # dates set a x-axis

        try:
            ws.add_chart(chart, "E1") # 'E1' is anchor pint where graph starts in sheet
            wb.save(filename=dest_filename)
        except PermissionError:
            print('We didn\'t get permission to write to excel file, may it is open somewhere.')
