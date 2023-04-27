import flask
import pandas as pd

import pandas as pd
import plotly.graph_objects as go


import dash
from dash import dcc
#import dash_core_components as dcc
from dash import html
#import dash_html_components as html



app = flask.Flask(__name__)

@app.route('/mostrar_estacionesnivel')
def mostrar_estacionesnivel():
  data = flask.request.args
  url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json"
  captura_web = pd.read_json(url,convert_dates='True')

  if data['psw'] == '12345678':
    print(captura_web)

    url = "http://35.174.200.0:5000/mostrar_estacionesnivel?psw=12345678"
    data = pd.read_json(url,convert_dates='True')

    latr = []
    lonr = []
    zr = []
    for i in range(0,100):
      zr.append(data['datos'][i]['porcentajeNivel'])
      latr.append(data['datos'][i]['coordenadas'][0]['latitud'])
      lonr.append(data['datos'][i]['coordenadas'][0]['longitud'])

    fig = go.Figure(go.Densitymapbox(lat=latr,lon=lonr,z=zr,radius=20, opacity=0.9, zmin=0, zmax = 100))
    fig.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.589,mapbox_center_lat=6.2429)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



#    return captura_web.to_dict()
  else:
    return "permiso no autorizado"


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
