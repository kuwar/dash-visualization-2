import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import App, build_graph
from homepage import Homepage
from candle_stick import candle_stick_chart, plot_candle_stick

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.config.suppress_callback_exceptions = True

# setting title
app.title = "Stock Analysis | AAPL"

server = app.server

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
    elif pathname == '/candle-stick':
        return candle_stick_chart()
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


@app.callback(
    Output('candle-stick-graphic', 'figure'),
    [
        Input(component_id="candle-slider-date", component_property="value")
    ]
)
def update_graph(date_range):
    print("#############")
    print(date_range)
    print("#############")
    candle_graph = plot_candle_stick()
    return candle_graph


if __name__ == '__main__':
    app.run_server(debug=True)
