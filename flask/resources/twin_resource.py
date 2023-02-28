from flask_restful import Resource , request
from flask_restful_swagger_2 import swagger
from flask_api import status
from operations.device_twin import TwinOperations 
from error_handler import error_handler

class TwinOperationsResource(Resource):
    
    @swagger.doc({'tags': ['DEVICE TWIN OPERATIONS'],
        'description': 'FETCH DEVICE TWIN',
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
    def get(self,device_id):
        twin_props = TwinOperations.fetch_device_twin(device_id)
        response={
            "message" : "Device twin fetched successfully.",
            "properties" : twin_props
        }
        return response,status.HTTP_200_OK

    @swagger.doc({'tags': ['DEVICE TWIN OPERATIONS'],
        'description': 'UPDATE DEVICE TWIN',
        'parameters': [
            {
                "in": "path",
                "name": "device_id",
                "type": "string",
                "required": True,
                "default": "1234"
            },
            {
                "in": "body",
                "name": "body",
                "required": True,
                "schema": {
                    "example":{ "desired":{"pressure":"55"},
                               "reported" : {"temperature":"60"}
                }
                },
            }
        ],
        'responses': {}
    ,})
    @error_handler
    def post(self,device_id):
        data=request.get_json()
        udpated_twin= TwinOperations.update_twin(device_id,data)
        response={
            "message":"Device Twin Updated Successfully.",
            "properties": udpated_twin
        }
        return response,status.HTTP_200_OK
    
    