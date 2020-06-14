#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from navbar import Navbar

nav = Navbar()

# datasets path
filepath = './data/Data/Stocks/asa.us.txt'
# Read dataset using Pandas
df = pd.read_csv(filepath)

# Range slider options
dates = [
    '2005-02-25', '2006-05-17', '2007-08-17', '2008-11-17',
    '2009-02-17', '2010-05-17', '2011-08-17', '2012-11-17', '2013-02-17',
    '2014-02-17', '2015-02-17', '2016-02-17', '2017-11-10'
]

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Daily prices and volumes of all U.S. stocks"),
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
    df2 = df[(df['Date'] > dates[date_range[0]]) & (df['Date'] < dates[date_range[1]])]

    return {
        'data': [
            go.Candlestick(
                x=df2['Date'],
                open=df2['Open'],
                high=df2['High'],
                low=df2['Low'],
                close=df2['Close']
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
