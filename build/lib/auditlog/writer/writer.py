class KinesisWriter():

    client = None
    def __init__(self):
        pass

    def set_client(self, client):
        self.client = client
    
    def write(self, data):
        response = self.client.put_record(
            StreamName='teststream',
            Data=data,
            PartitionKey='1'
        )
        print(response)

kinesis_writer = KinesisWriter()