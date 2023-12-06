from flask import render_template, request
from app import app
from .physical_properties import staticbhp

@app.route('/estimate')
def index():
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    well_depth = float(request.form['well_depth'])
    average_temperature_in_fahrenheit = float(request.form['average_temperature_in_fahrenheit'])
    specific_gas_gravity = float(request.form['specific_gas_gravity'])
    wellhead_pressure = float(request.form['wellhead_pressure'])

    sbph_estimator = staticbhp.staticBHP()
    result = sbph_estimator.print_staticbhp(well_depth, average_temperature_in_fahrenheit, specific_gas_gravity, wellhead_pressure)

    return render_template('result.html', result=result)
