from datetime import datetime
import random
import json
import time
from azure.iot.device import IoTHubDeviceClient,Message
from operations.device_crud import iothub_registry_manager
from log import logger

def get_device_connection_string(device_id):
        # Get the device identity from the registry manager
        device = iothub_registry_manager.get_device(device_id)
        print(iothub_registry_manager)
        # Get the hostname of the IoT Hub 
        hub_hostname = iothub_registry_manager.protocol.config.credentials._dict["HostName"]
        # Generate the connection string for the device
        connection_string = "HostName={};DeviceId={};SharedAccessKey={}".format(
            hub_hostname,
            device.device_id,
            device.authentication.symmetric_key.primary_key
        )

        print("Connection string for device {}: {}".format(device_id, connection_string))

        return connection_string



def random_generate():
        mydict={}
        now=datetime.now()
        mydict['temperature_@_'+now.strftime("%Y-%m-%d-%H:%M:%S")] = random.randint(30,90)
        mydict['humidity_@_'+now.strftime("%Y-%m-%d-%H:%M:%S")] = random.randint(10,80)
        json_object= json.dumps(mydict,indent=4)
        return json_object

def send_message(device_id):
    device_conn_string= get_device_connection_string(device_id)

    #create device client
    device_client = IoTHubDeviceClient.create_from_connection_string(device_conn_string)

    #connect device client
    device_client.connect()


    logger.info("Send Message from device called")
    i=0
    while(i<5):    
        json_payload = random_generate()
        message = Message(json_payload)

        device_client.send_message(message)
        logger.info(f"Message with payload {json_payload} sent Successfully to IoT Hub.")
        time.sleep(10)
        i+=1
    device_client.disconnect()

    return {"message":"Successfully sent message to IoT hub"}

