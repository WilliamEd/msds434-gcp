#from flask import Flask

import dash
from dash import dash, dcc, html
from google.cloud import bigquery
import plotly.express as px

#@app = Flask(__name__)
app = dash.Dash(__name__)
server= app.server


#@app.route("/")
#def hello_world():
    
client = bigquery.Client()
query = """
SELECT *
FROM ML.FORECAST(MODEL covid19.Covid_model,
                    STRUCT(14 AS horizon, 0.9 AS confidence_level))
"""
query_job = client.query(query)
df = query_job.to_dataframe()
fig = px.line(df, x='forecast_timestamp', y = 'forecast_value')

response = "Test Values2"

#return response

app.layout = html.Div(children = [
    html.H1("Covid-19 cases forecast"),
    html.Div(children = '''Covid-19 cases in Germany'''),
    dcc.Graph(
        id='Covid-19 cases forecast',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)