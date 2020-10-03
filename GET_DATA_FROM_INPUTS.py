
class GET_DATA_FROM_INPUTS():
    def __init__(self,filename:str):
        self.filename = filename
        self.interval = 0
        self.AppOn = False
        self.website_list = []
    def GET_DATA_FROM_INPUTS(self):
        input:list = [] # PUT INPUTS.txt content in this list
        with open(self.filename,'r') as fileh:
            for line in fileh:
                input.append(line)
        self.interval = int(input[input.index('INTERVAL=\n')+1].rstrip())
        self.AppOn = bool(int(input[input.index('APPLICATION_ON=\n')+1].rstrip()))
        website = (input[input.index('WEBSITE=\n')+1].rstrip())
        self.website_list = [(input[input.index('WEBSITE=\n')+1].rstrip())]
