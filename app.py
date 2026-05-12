from flask import Flask, render_template, request
from scrapper import search_incruit
from file import save_to_csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, 15 AI DATA!"

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # print(keyword)
    jobs = search_incruit(keyword, 1)
    return render_template("search.html" , jobs=jobs)


@app.route("/file")
def file():
    keyword = request.args.get("keyword")
    save_to_csv()
if __name__ == "__main__":
    app.run(debug=True)