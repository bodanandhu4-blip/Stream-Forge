import json


def process_event(message):
    # Convert JSON message into Python dictionary
    data = json.loads(message)

    # Filter: accept only temperature greater than 0
    if data["temperature"] <= 0:
        return None

    # Map: create the processed format
    processed_data = {
        "truck_id": data["truck_id"],
        "temperature": data["temperature"],
        "timestamp": data["timestamp"],
        "status": "valid"
    }

    return processed_data


# Sample Kafka message for testing
message = json.dumps({
    "truck_id": "TRUCK-001",
    "temperature": 32.5,
    "timestamp": "2026-08-19T20:30:00"
})

result = process_event(message)

if result:
    print("Processed Event:")
    print(result)
else:
    print("Event filtered out")