import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

from random import seed
from random import randint

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventhub-eh.servicebus.windows.net/;SharedAccessKeyName=eventhub-access;SharedAccessKey=blRsZarPh4nnFniflGlRBLePO3fV8a9HhVuusabojls=", eventhub_name="test-hub-eh")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        seed(1)
        for _ in range(1000):
            # Add events to the batch.
            value = randint(0,10)
    
            data = str.format('{{ "name":"John", "age":30, "city":"New York", random:{}}}', value)

            event_data_batch.add(EventData(data))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())