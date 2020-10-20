class RenderResult:
    
    def display_result(self, results):
        for result in results:
            data = {
                'description': result['description'], 
                'udp': result['udp'], 
                'status': result['status'], 
                'number': result['number'], 
                'tcp': result['tcp'],
                }
            result = """
            Description: {description}
            Udp: {udp} 
            Status: {status} 
            Number: {number} 
            Tcp: {tcp}
            """.format(**data)
            print(result)