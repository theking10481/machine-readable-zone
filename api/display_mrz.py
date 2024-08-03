import json
from calculate_check_digit import calculate_check_digit
from create_mrz import create_mrz

def handler(request):
    if request.method == 'POST':
        fields = json.loads(request.body)
        mrz = create_mrz(fields)
        
        # Print all fields and MRZ to the console
        print("Received Fields:")
        for key, value in fields.items():
            print(f"{key}: {value}")
        
        print("\nGenerated MRZ:")
        print(mrz)
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "MRZ and fields printed to console. Check your server logs."
            })
        }

    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "Not Found"
        })
    }
