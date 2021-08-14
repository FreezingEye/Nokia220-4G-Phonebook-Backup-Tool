from waitress import serve
from flask import Flask,request,send_file 
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/upload')
def upload_file():
   return send_file('D:\\python\\nfs\\invoice_file_sender\\upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      return 'file uploaded successfully'

if __name__ == '__main__':
    serve(app,host='127.0.0.1',port=9086,threads=8) 


#http://127.0.0.1:9086/upload
