__author__ = 'ysekky'

from application import app
from flask import render_template, request

@app.route('/')
def index():
    return 'Hello World'


@app.route('/visualize')
def visualize():
    table = request.args.get('table', 'table')
    chart_id = request.args.get('chart_id', 'chart_id').encode('utf-8')
    chart_type = request.args.get('chart_type', 'bar').encode('utf-8')
    chart_height = int(request.args.get('chart_height', 350))
    chart = {"renderTo": chart_id, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [1, 2, 3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"text": 'My Title'}
    x_axis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    y_axis = {"title": {"text": 'yAxis Label'}}
    return render_template('graph.html', chart_id=chart_id, chart=chart, series=series, title=title,
                           x_axis=x_axis, y_axis=y_axis)

