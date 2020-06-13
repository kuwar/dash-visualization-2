import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table as dt

from navbar import Navbar

nav = Navbar()

# datasets path
filepath = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
# Read dataset using Pandas
st = pd.read_csv(filepath)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Table of stock data"),
                        dcc.Graph(
                            id="candle-stick-graphic"
                        )
                    ],
                    md=12
                ),
            ]
        )
    ],
    className="mt-4",
)


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
