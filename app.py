from flask import Flask, render_template, request
import functions

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


# took from hw 6 CHANGE IT
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        return "Wrong HTTP method", 400

    form_data = request.form
    lyric = form_data["lyric"]

    songs_results = functions.find_songs(lyric)

    return render_template("results.html", songs=songs_results, lyric=lyric)


if __name__ == '__main__':
    app.run(debug=True)