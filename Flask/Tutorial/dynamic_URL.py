from flask import Flask, redirect, url_for

app = Flask(__name__)

## Variable Rule Method

@app.route('/')
def welcome():
    return "welcome to flask"

# appending values
@app.route('/success/<int:score>')  # by default, route url is string. So, we want to pass int value, so int written
def success(score):
    return ("Passed with marks"+ str(score)) 

@app.route('/fail/<int:score>')  # by default, route url is string. So, we want to pass int value, so int written
def fail(score):
    return ("Failed with marks"+ str(score))

@app.route('/results/<int:score>')
def results(score):
    result=""
    if score>50:
        result="Pass"
    else:
        result="Fail"
    # return result             # was used with variable rule method
    return redirect(url_for(results, score=score))
if __name__ == '__main__':
    app.run(debug = True)