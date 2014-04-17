__author__ = 'ysekky'

from application import app
from flask import render_template

@app.route('/')
def index():
    return 'Hello World'


@app.route('/visualize/<tablename>')
def visualize(tablename='table', chart_id='chart_id', chart_type="bar", chart_height=350):
    chart = {"renderTo": chart_id, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [1, 2, 3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"text": 'My Title'}
    x_axis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    y_axis = {"title": {"text": 'yAxis Label'}}
    return render_template('graph.html', chart_id=chart_id, chart=chart, series=series, title=title,
                           x_axis=x_axis, y_axis=y_axis)

