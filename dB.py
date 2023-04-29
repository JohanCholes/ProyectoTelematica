import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
		html.H1("Este es prueba dB"),
		#dcc.Graph(figure=fig)
		])

app.run_server(host='0.0.0.0',port=80)
