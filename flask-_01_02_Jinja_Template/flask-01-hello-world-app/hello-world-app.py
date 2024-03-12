from flask import Flask 
app = Flask(__name__)

@app.route("/")

def index():
    return "Hello World!!"

@app.route("/second")

def second():
    return "This is the 2nd page!!"

@app.route('/third/subthird')

def third():
    return "This is the subpage of third page"

# Create a dynamic url which takes id number dynamically and return 
#with a massage which show id of page.

@app.route("/forth/<string:my_id>")
def forth(my_id):
    return f"The page id is {my_id}"

if __name__ == '__main__':

    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=8081)