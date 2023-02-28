
from log import logger
from azure.iot.hub import IoTHubRegistryManager

IOTHUB_CONNECTION_STRING = "HostName=sujithIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=TfyonwXJeZ8IxV3NPuhGmxmDNhOdtYWQdjXUl7swNRc="
iothub_registry_manager = IoTHubRegistryManager(IOTHUB_CONNECTION_STRING)

class DeviceCrudOperations():

    def create_device(device_id,fields):
        new_device = iothub_registry_manager.create_device_with_sas(device_id,primary_key="",secondary_key="",**fields)
        logger.info("device created")
        return {
            "message" : "Device created succesfully",
            "Device_ID" : new_device.device_id,
            "Primary_key" : new_device.authentication.symmetric_key.primary_key,
            "status": new_device.status
        }   
            
    def fetch_device(device_id):
        logger.info(f"Calling fetch device function with device_id:{device_id}")
        device = iothub_registry_manager.get_device(device_id)
        response={
            "message" : "Device fetched succesfully",
            "Device_ID" : device.device_id,
            "etag": device.etag,
            "Primary_key" : device.authentication.symmetric_key.primary_key,
            "status": device.status,
            "connection_state": device.connection_state
        }
        logger.info(f"Device Fetched Successfully:{device}")
        return response

    def update_device(device_id,fields):
        logger.info(f"Update device called for device {device_id}")
        device = iothub_registry_manager.update_device_with_sas(device_id,primary_key="",secondary_key="",etag="*",**fields)
        response={
            "message" : "Device updated succesfully",
            "Device_ID" : device.device_id,
            "etag": device.etag,
            "Primary_key" : device.authentication.symmetric_key.primary_key,
            "status": device.status,
            "connection_state": device.connection_state
        }
        logger.info(f"Device Updated Successfully:{device}")
        return response

    def delete_device(device_id,etag="*"):
        response=iothub_registry_manager.delete_device(device_id,etag)
        response={
            "message" : "Device deleted successfully",
            "Device_ID" : device_id    
        }
        logger.info(response)
        return response



        

    



