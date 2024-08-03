import json
import logging
from .calculate_check_digit import calculate_check_digit
from .create_mrz import create_mrz

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handler(request):
    try:
        logger.info("Received request: %s", request.method)
        
        if request.method == 'POST':
            fields = json.loads(request.body)
            logger.info("Received fields: %s", fields)
            
            mrz = create_mrz(fields)
            logger.info("Generated MRZ: %s", mrz)
            
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "MRZ and fields printed to console. Check your server logs.",
                    "mrz": mrz
                })
            }

        return {
            "statusCode": 404,
            "body": json.dumps({
                "message": "Not Found"
            })
        }

    except Exception as e:
        logger.error("Error processing request: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error"
            })
        }
