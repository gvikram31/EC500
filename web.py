from flask import Flask, redirect, render_template, request, url_for
import run as apiExercise

website = Flask(__name__)

@website.route('/')
def form():
    return render_template('index.html')

@website.route('/', methods=['POST'])
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

@website.route('/submission')
def cat():
    with open("labels.json") as outfile:
        lines = json.loads(outfile.read())

    return render_template("output.html")

if __name__ == "__main__":
    website.run(host="0.0.0.0", port=8080, threaded=True)
