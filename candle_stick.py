import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from navbar import Navbar

nav = Navbar()

# datasets path
filepath = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
# Read dataset using Pandas
df = pd.read_csv(filepath)

# Range slider options
dates = [
    '2015-02-17', '2015-05-17', '2015-08-17', '2015-11-17',
    '2016-02-17', '2016-05-17', '2016-08-17', '2016-11-17', '2017-02-17'
]

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Apple stock plot"),
                        dcc.Graph(
                            id="candle-stick-graphic",
                        )
                    ],
                    md=12
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.RangeSlider(
                            id='candle-slider-date',
                            marks={i: dates[i] for i in range(0, 9)},
                            min=0,
                            max=8,
                            value=[1, 7]
                        )
                    ],
                    md=12
                )
            ]
        )
    ],
    className="mt-4",
)


def plot_candle_stick(date_range=None):
    return {
        'data': [
            go.Candlestick(
                x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close']
            )
        ],
        'layout': go.Layout(
            title="Candle Stick",
            xaxis={'title': "Date"},
            yaxis={'title': "Market Fluctuation"}
        )
    }


def candle_stick_chart():
    layout = html.Div(children=[
        nav,
        body
    ])
    return layout


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = candle_stick_chart()
if __name__ == "__main__":
    app.run_server()
