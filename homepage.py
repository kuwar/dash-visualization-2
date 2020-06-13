#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Apple stock data"),
                        html.P(
                            """\
                            A stock market, equity market or share market is the aggregation of buyers and sellers 
                            of stocks (also called shares), which represent ownership claims on businesses; these may 
                            include securities listed on a public stock exchange, as well as stock that is only traded 
                            privately, such as shares of private companies which are sold to investors through equity 
                            crowdfunding platforms. Investment in the stock market is most often done via stockbrokerages 
                            and electronic trading platforms. Investment is usually made with an investment strategy in mind.
                            """
                        ),
                        html.P(
                            """\
                            Apple Inc. is an American multinational technology company headquartered in Cupertino, 
                            California, that designs, develops, and sells consumer electronics, computer software, and 
                            online services. It is considered one of the Big Five technology companies, alongside 
                            Microsoft, Amazon, Google, and Facebook.
                            """
                        ),
                    ],
                    md=12,
                )
            ]
        )
    ],
    className="mt-4",
)


def Homepage():
    layout = html.Div([
        nav,
        body
    ])
    return layout


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()
