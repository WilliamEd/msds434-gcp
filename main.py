import dash
from dash import dash, dcc, html
from google.cloud import bigquery
import plotly.express as px

app=dash.Dash(__name__)
server=app.server
client = bigquery.Client()

query = """
    SELECT * FROM
    FROM ML.FORECAST(MODEL covid19.Covid_model,
                     STRUCT(14 AS horizon, 0.9 AS confidence_level))
"""

query_job = client.query(query)

df = query_job.to_dataframe()

fig = px.line(df, x='TIME_SERIES_TIMESTAMP_COL', y = 'TIME_SERIES_DATA_COL')

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

#Modified from other projects

#from flask import Flask
#import requests
#info = 'https://us-central1-prediction-aiplatform.googleapis.com/v1alpha1/projects/msds434-gcp/locations/us-central1/endpoints/2857701089334001664'
#data = {'PROJECT_ID':'msds434-gcp', 'REGION':'us-central1', 'ENDPOINT_ID':'2857701089334001664', 'INPUT_DATA_FILE':'INPUT-JSON'}
#app = Flask(__name__)

#@app.route("/")
#def hello_world():
#   response = requests.post(info, data)
#   return response

#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=8080)