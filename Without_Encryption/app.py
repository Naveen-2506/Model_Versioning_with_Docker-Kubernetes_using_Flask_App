from flask import Flask, send_file

app = Flask(__name__)

@app.route('/api/weights')
def serve_weights():
    # Set the content type for weights file (adjust as needed)
    response = send_file('yolo/yolov3-tiny.weights', as_attachment=True)
    response.headers["Content-Disposition"] = "attachment; filename=yolov3-tiny.weights"
    return response

@app.route('/api/cfg')
def serve_config():
    # Set the content type for configuration file (adjust as needed)
    response = send_file('yolo/yolov3-tiny-obj.cfg', as_attachment=False)
    response.headers["Content-Disposition"] = "inline; filename=yolov3.cfg"
    return response

@app.route('/api/names')
def serve_names():
    # Set the content type for coco.names file (adjust as needed)
    response = send_file('yolo/coco.names', as_attachment=False)
    response.headers["Content-Disposition"] = "inline; filename=coco.names"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
