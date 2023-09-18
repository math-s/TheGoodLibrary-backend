import json
import jsonschema


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, world!"
        })
    }
