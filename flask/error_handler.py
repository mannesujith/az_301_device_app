from msrest.exceptions import HttpOperationError
from log import logger
from flask_api import status
def error_handler(func):
    """
    Decorator to handle common exceptions in resources
    """

    def func_wrapper(*args, **kwargs):
        """
        Function wrapper
        """
        try:
            return func(*args, **kwargs)
        except HttpOperationError as ex:
            if ex.response.status_code == 409:
                # 409 indicates a conflict. This happens because the device already exists.
                logger.error("CONFLICT! device already present")
                return {"message":"device already present"},status.HTTP_409_CONFLICT
            elif ex.response.status_code == 404:
                logger.error("Device not found")
                return {"message":"device not found"},status.HTTP_404_NOT_FOUND
            else:
                logger.error(f"Error at {ex}")
                raise
        except Exception as ex:
            logger.error(f"Error at {ex}")
            return {"message" : "Internal Server Error"},status.HTTP_500_INTERNAL_SERVER_ERROR
    
    return func_wrapper