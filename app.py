from flask import Flask, render_template, request, jsonify, send_from_directory
from PIL import Image
import os
import uuid
from model.realesrgan import enhance_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if file:
        filename = str(uuid.uuid4()) + '.jpg'
        original_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(original_path)

        enhanced_path = os.path.join(UPLOAD_FOLDER, 'enhanced_' + filename)
        enhance_image(original_path, enhanced_path)

        return jsonify({
            'original': f'/uploads/{filename}',
            'enhanced': f'/uploads/enhanced_{filename}'
        })

@app.route('/uploads/<filename>')
def send_file_from_uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)