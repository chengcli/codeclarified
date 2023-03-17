from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from modules import code_processor
#from flask_socketio import SocketIO
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'py', 'java', 'js', 'c', 'cpp', 'h', 'hpp'}

app = Flask(__name__)
#app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code_file = request.files['codefile']

        if code_file and allowed_file(code_file.filename):
            filename = secure_filename(code_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                print(filepath)
                print(os.path.exists(filepath))
            code_file.save(filepath)

        else:
            return "Invalid file type", 400

        prettified_code, comments, prettified_file_path = code_processor.process_code(filepath)
        os.remove(filepath)
        return render_template('result.html', prettified_code=prettified_code, comments=comments)

        # Return the results as JSON
        #return jsonify({'prettified_code': prettified_code, 'comments': comments})

    return render_template('index.html')

#@socketio.on('connect')
#def on_connect():
#    print('Client connected')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    #socketio.run(app, debug=True)
    app.run(debug=False)

