from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product/capsule')
def product_capsule():
    return render_template('product1_a.html')

@app.route('/product/stick')
def product_stick():
    return render_template('product1_b.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product/stick/prototype')
def product_stick_prototype():
    return render_template('product1_b_prototype.html')

if __name__ == '__main__':
    app.run(debug=True)