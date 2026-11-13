from flask import Flask, request, jsonify
from pyzbar.pyzbar import decode
from PIL import Image
import base64
import io

app = Flask(__name__)

# Route for standard file upload (optional, useful for testing from desktop)
@app.route('/decode_qr', methods=['POST'])
def decode_qr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    image = Image.open(file.stream)

    decoded_data = decode(image)
    if not decoded_data:
        return jsonify({'error': 'No QR code found'}), 400

    return jsonify({'data': decoded_data[0].data.decode('utf-8')}), 200

# Route for clients that send the image as a base64 string
@app.route('/decode_qr_base64', methods=['POST'])
def decode_qr_base64():
    try:
        image_data = request.json.get('image_base64')
        if not image_data:
            return jsonify({'error': 'Missing image_base64'}), 400

        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # For debugging
        print("Image received and decoded.")

        decoded_data = decode(image)
        if not decoded_data:
            image.save("debug_received.png")  # Save image for inspection
            return jsonify({'error': 'No QR code found'}), 400

        return jsonify({'data': decoded_data[0].data.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)