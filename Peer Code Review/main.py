from flask import Flask, render_template,request,url_for,redirect
import run as apiExercise
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
    auth = apiExercise.authorise_twitter_api()
    api = apiExercise.tweepy.API(auth)#, wait_on_rate_limit=True)
        
    try:
        user = request.form['username']
        folder = request.form['output']
        num = int(request.form['num'])

        isValid = apiExercise.download_images(api, user, num, folder, 1)
        print(user, num, folder)
        
    except Exception as e:
        print(str(e))
        return render_template('index.html')

    else:
        if (isValid):
            apiExercise.doAnalysis(folder)
    return redirect(url_for('cat'))

@app.route('/submission')
def cat():
    with open("labels.json") as outfile:
        lines = json.loads(outfile.read())

    return render_template("output.html")
if __name__ == '__main__':
    app.run(debug=True)
