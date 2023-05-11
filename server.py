from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def boxes():
    return render_template("index.html", num=3, color="blue")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<color>')
def num_boxes_color(num, color):
    if not color:
        color = "blue"
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
