from operations.device_crud import iothub_registry_manager
from azure.iot.device import IoTHubDeviceClient
from log import logger
from operations.device_telemetry import get_device_connection_string


class TwinOperations():
    
    def fetch_device_twin(device_id):
        # Get the twin object for the device
        twin = iothub_registry_manager.get_twin(device_id)
        # Get the desired properties from the twin object
        twin_props = twin.properties.__dict__
        logger.info(f"Device Twin fetched successfully for {device_id}: {twin_props}")
        return twin_props

    def update_desired_properties(device_id,desired_props):
        # Get the twin object for the device
        twin = iothub_registry_manager.get_twin(device_id)
        # Update the desired properties in the twin object
        twin.properties.desired.update(desired_props)

        # Update the twin object in the IoT Hub
        iothub_registry_manager.update_twin(device_id, twin)

        print("Desired properties updated successfully.")

    def update_reported_properties(device_id,reported_props):
        # Get the twin object for the device
        twin = iothub_registry_manager.get_twin(device_id)
        
        # Update the desired properties in the twin object
        twin.properties.reported.update(reported_props)
        
        # Update the twin object in the IoT Hub
        iothub_registry_manager.update_twin(device_id,twin)
        
        logger.info("Reported properties updated successfully.")

    def update_twin(device_id,properties):
        logger.info("Update device twin called")
        if properties.get('reported'):
            TwinOperations.update_desired_properties(device_id,properties['desired'])
        if properties.get('reported'):
            TwinOperations.update_reported_properties2(device_id,properties['reported'])
        return TwinOperations.fetch_device_twin(device_id)

    def update_reported_properties2  (device_id,reported_props):
        device_conn_string= get_device_connection_string(device_id)

        #create device client
        device_client = IoTHubDeviceClient.create_from_connection_string(device_conn_string)
        device_client.connect()
        try:
            reported_patch=reported_props

            device_client.patch_twin_reported_properties(reported_patch)

            device_client.disconnect()
        except Exception:
            device_client.disconnect()
            raise