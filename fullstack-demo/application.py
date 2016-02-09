import sys
import plot_generator

import flask
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/default_network/<int:site_id>")
def site(site_id):
    return render_template("site.html", site_id=site_id)

@app.route("/default_network/images/<int:site_id>")
def image(site_id):
    plot_generator.gen_plot(site_id)
    fullpath = "static/default_network/{}.png".format(site_id)
    try:
        resp = flask.make_response(open(fullpath, "rb").read())
    except Exception as inst:
         print(inst, file=sys.stderr)
    resp.content_type = "image/png"
    return resp

if __name__ == "__main__":
    app.run()
