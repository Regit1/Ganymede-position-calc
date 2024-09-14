from flask import Flask, request, render_template
import math
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    day = float(request.form['day'])
    time = float(request.form['time'])
    month = float(request.form['month'])
    year = float(request.form['year'])

    mm = {
        1: 31, 2: 29.5, 3: 30, 4: 30, 5: 30.2, 6: 30.16666666,
        7: 30.285714, 8: 30.375, 9: 30.3333333, 10: 30.4,
        11: 30.36363636, 12: 30.41666666
    }.get(month, 30)

    k = year - 2024 if year >= 2024 else 0

    ndays1 = day - 9.40625
    ndays2 = (month - 8) * mm
    ndays3 = (year - 2024) * 365
    ndays4 = (time/24)

    d = ndays1 + ndays2 + ndays3 + ndays4
    t = 6.28318530718 + d * 0.87815308
    n = np.sin(t)
    f = n * 309.10809005423164

    if f < 0:
        result = f"Ganymede is {abs(f):.2f} arcseconds from Jupiter, and on the left side"
    else:
        result = f"Ganymede is {f:.2f} arcseconds from Jupiter, and on the right side"

    return result

if __name__ == '__main__':
    app.run(debug=True)