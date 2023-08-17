from flask import Flask, render_template
import datetime

app = Flask(name)

@app.route('/')
def home():
    return render_template('index.html')

def calculate_time_until_reset():
    today = datetime.datetime.now()
    target_date = datetime.datetime(today.year, 8, 17, 0, 0, 0)  # August is represented by index 8

    if today > target_date:
        target_date += datetime.timedelta(days=1)  # Move to the next day

    time_until_reset = (target_date - today).total_seconds() * 1000  # Convert to milliseconds
    return time_until_reset

app.jinja_env.globals.update(calculate_time_until_reset=calculate_time_until_reset)

if name == 'main':
    app.run(debug=True)
