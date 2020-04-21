from flask import *

# from image_classification import PredictImg
import test

app = Flask(__name__, template_folder='template')


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)


        result = test.PredictImg(f.filename)


        return render_template("success.html", name=result)


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
