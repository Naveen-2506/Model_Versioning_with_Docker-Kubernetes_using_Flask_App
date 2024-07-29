from flask import Flask, send_file
import base64

app = Flask(__name__)

def encode_file(file_path):
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode('utf-8')
    return encoded

@app.route('/api/weights')
def serve_weights():
    weights_data = encode_file('yolo/yolov3-tiny.weights')
    return weights_data

@app.route('/api/cfg')
def serve_config():
    config_data = encode_file('yolo/yolov3-tiny-obj.cfg')
    return config_data

@app.route('/api/names')
def serve_names():
    names_data = encode_file('yolo/coco.names')
    return names_data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
