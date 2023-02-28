import json
from flask_restful import Resource , request
from flask_restful_swagger_2 import swagger
from flask_api import status
from operations.device_crud import DeviceCrudOperations as DC
from error_handler import error_handler

class DeviceCRUD(Resource):
    
    @swagger.doc({'tags': ['DEVICE CRUD'],
        'description': 'CREATE DEVICE',
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
                    "example": {"status":"enabled"
                    }
                },
            }
        ],
        
        'responses': {}
    ,})
    @error_handler
    def post(self,device_id):
        data=request.get_json()
        response = DC.create_device(device_id,data)
        return response,status.HTTP_200_OK

    @swagger.doc({'tags': ['DEVICE CRUD'],
        'description': 'FETCH DEVICE',
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
        response = DC.fetch_device(device_id)
        return response,status.HTTP_200_OK
    
    @swagger.doc({'tags': ['DEVICE CRUD'],
        'description': 'UPDATE DEVICE',
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
                    "example": {"status":"disabled"
                    }
                },
            }
        ],
        'responses':{}
    ,})
    @error_handler
    def put(self,device_id,):
        data=request.get_json()
        response = DC.update_device(device_id,data)
        return response,status.HTTP_200_OK
    
    @swagger.doc({'tags': ['DEVICE CRUD'],
        'description': 'DELETE DEVICE',
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
    def delete(self,device_id):
        response = DC.delete_device(device_id)
        return response,status.HTTP_200_OK
