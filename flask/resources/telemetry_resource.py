from flask_restful import Resource
from flask_restful_swagger_2 import swagger
from flask_api import status
from operations.device_telemetry import send_message
from error_handler import error_handler

class TelemetryResource(Resource):

    @swagger.doc({'tags': ['DEVICE TELEMETRY'],
        'description': 'SEND MESSAGE',
        'parameters': [
            {
                "in": "path",
                "name": "device_id",
                "type": "string",
                "required": True,
                "default": "1234"
            },
        ],
        'responses':{}
    ,})
    @error_handler
    def post(self,device_id):
        response = send_message(device_id)
        return response,status.HTTP_200_OK
