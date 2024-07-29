import requests

# Define the external IP address or hostname of your GKE LoadBalancer service
BASE_URL = 'http://your-gke-external-ip/api'  # Replace 'your-gke-external-ip' with the actual IP

# Function to retrieve YOLO weights
def get_yolo_weights():
    response = requests.get(f'{BASE_URL}/weights')
    if response.status_code == 200:
        weights_data = response.content
        return weights_data
    else:
        print("Failed to retrieve weights file")
        return None

# Function to retrieve YOLO configuration
def get_yolo_config():
    response = requests.get(f'{BASE_URL}/cfg')
    if response.status_code == 200:
        config_data = response.text
        return config_data
    else:
        print("Failed to retrieve configuration file")
        return None

# Function to retrieve COCO names
def get_coco_names():
    response = requests.get(f'{BASE_URL}/names')
    if response.status_code == 200:
        names_data = response.text
        return names_data
    else:
        print("Failed to retrieve names file")
        return None

# Example usage
if __name__ == "__main__":
    weights_data = get_yolo_weights()
    config_data = get_yolo_config()
    names_data = get_coco_names()
    # Use the data as needed in your client code
