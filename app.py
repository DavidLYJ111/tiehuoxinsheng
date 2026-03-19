from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="首页")

@app.route("/problem")
def problem():
    return render_template("problem.html", title="项目背景")

@app.route("/products")
def products():
    return render_template("products.html", title="产品体系")

@app.route("/tech")
def tech():
    return render_template("tech.html", title="技术创新")

@app.route("/platform")
def platform():
    return render_template("platform.html", title="数字平台")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)