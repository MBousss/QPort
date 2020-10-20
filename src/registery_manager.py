import json

class RegisteryManager():

    data = []

    def __init__(self):
        file = open('assets/ports.json', 'r')
        self.data = json.load(file)
        

    def port_registrated(self, userInput):
        status = False
        if userInput in self.data:
            status = True
        return status

    def retrieve_port_info(self, array):
        description = array['description']
        udp = array['udp']
        status = array['status']
        number = array['port']
        tcp = array['tcp']
        return {
            'description': description, 
            'udp': udp, 
            'status': status, 
            'number': number, 
            'tcp': tcp
        }