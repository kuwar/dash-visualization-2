# import libraries
import pandas as pd
import pickle
# Graphing
import plotly.graph_objects as go
# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
# Navbar
from navbar import Navbar

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df.set_index(df.iloc[:, 0], drop=True, inplace=True)
df = df.iloc[:, 1:]

nav = Navbar()

# Options for dropdown
options = [
    {'label': x.replace('AAPL.', ''), 'value': x} for x in df.columns
]

# Range slider options
df['Date'] = pd.to_datetime(df.index)
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
                                id='pop_dropdown',
                                options=options,
                                value='AAPL.Open'
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
                            id='output',
                            children=[],
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
        x=df2.Date, y=df2['AAPL.High'],
        name='AAPL HIGH',
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