from resources.crud_resource import DeviceCRUD
from resources.twin_resource import TwinOperationsResource
from resources.telemetry_resource import TelemetryResource

def pages(api):
    
    api.add_resource(DeviceCRUD, '/api/v1/device/<device_id>')
    api.add_resource(TwinOperationsResource,'/api/v1/device/<device_id>/twin')
    api.add_resource(TelemetryResource,'/api/v1/device/<device_id>/send_message')