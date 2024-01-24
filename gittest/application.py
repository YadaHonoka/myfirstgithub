from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return render_template('in.html',
            	username=request.form['username'],
            	password=request.form['password'])
    return render_template('login.html')

#↓今回追加したプログラム
#クライアントの命名したファイル名を利用するためのsecure_filename()
from werkzeug.utils import secure_filename

@app.route('/uploads', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files["the_file"]
        #任意の階層をフルパスで指定(macの場合。任意のユーザー名は変更してください。)
        f.save('/Users/honoka/Develop/flask/flask_240118/uploads/' + secure_filename(f.filename))
        #アップロードしてサーバーにファイルが保存されたらfinishedを表示
        return render_template('finished.html')
    else:
    	#GETでアクセスされた時、uploadsを表示
    	return render_template('uploads.html')
    
if __name__ == ('__main__'):
    app.run(debug=True, host='0.0.0.0')