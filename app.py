#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

# Navbar
from navbar import Navbar

df = pd.read_csv(
    './data/Data/Stocks/asa.us.txt')
df.set_index(df.iloc[:, 0], drop=True, inplace=True)
df = df.iloc[:, 1:]

nav = Navbar()

# Options for dropdown
options = [
    {'label': x, 'value': x} for x in df.columns
]

# Range slider options
df['Date'] = pd.to_datetime(df.index)
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
                        html.H2("Select Feature"),
                    ],
                    md=12,
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            dcc.Dropdown(
                                id='feature-dropdown',
                                options=options,
                                value='Open'
                            )
                        )
                    ],
                    md=12,
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            id='time-series-output'
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
                            id='slider',
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


def App():
    layout = html.Div([
        nav,
        body,
    ])
    return layout


def build_graph(ohlc, selectedSliderDate):
    # filtering the data
    df2 = df[(df.Date > dates[selectedSliderDate[0]]) & (df.Date < dates[selectedSliderDate[1]])]

    # traces for scatter plot

    # default make High
    trace_default = go.Scatter(
        x=df2.Date, y=df2['High'],
        name='HIGH',
        line=dict(
            width=2,
            color='rgb(229, 151, 50)'
        )
    )
    # change based on the selected options
    trace_1 = go.Scatter(
        x=df2.index, y=df2[ohlc],
        name='{}'.format(ohlc),
        line=dict(
            width=2,
            color='rgb(106, 181, 135)'
        )
    )

    data = [trace_default, trace_1]
    graph = dcc.Graph(
        figure={
            'data': data,
            'layout': go.Layout(
                title='{}'.format(ohlc),
                yaxis={'title': 'OHLC'},
                hovermode='closest'
            )
        }
    )
    return graph
