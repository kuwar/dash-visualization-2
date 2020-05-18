import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import App, build_graph
from homepage import Homepage
from table import TabularData

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.config.suppress_callback_exceptions = True

# setting title
app.title = "Stock Analysis | AAPL"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/time-series':
        return App()
    elif pathname == '/table':
        return TabularData()
    else:
        return Homepage()


@app.callback(
    Output('output', 'children'),
    [
        Input('pop_dropdown', 'value'),
        Input('slider', 'value')
    ]
)
def update_graph(ohlc, date):
    graph = build_graph(ohlc, date)
    return graph


if __name__ == '__main__':
    app.run_server(debug=True)
