import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app_helper import get_prediction

app = Flask(__name__)

# Upload folder
#UPLOAD_FOLDER = '/home/vipinainvijayan4286/ChestXray-Classification-App/uploads/'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            image_path= os.path.join(basepath,'static', 'uploads', secure_filename(file.filename))
            file.save(image_path)            
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            class_name = get_prediction(image_path)
            return render_template('upload.html', class_name=class_name, display_image=file.filename)
        else:
            return redirect(request.url)
            

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port="4100")

