
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        site_url = request.form.get('site_url')
        result = f"Simulated testing of {site_url} complete. No critical errors."
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
