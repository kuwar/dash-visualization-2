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
                        html.H2("Huge Stock Market Dataset"),
                        html.Strong("Historical daily prices and volumes of all U.S. stocks and ETFs"),
                        html.P("""\
                            The data includes the full historical daily price and volume data for all US-based stocks and 
                            ETFs trading on the NYSE, NASDAQ, and NYSE MKT
                            """),
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
                        html.H2("Terminologies in data"),
                        html.P(
                            """\
                            OHLC stands for the open, high, low and close prices of a share's price on a trading day.
                            """
                        ),
                        html.P(
                            """\
                            Normally on a chart this is visually represented by a vertical line between the low price 
                            and the high price with a left and right horizontal ledge showing the open price and close price.
                            """
                        ),
                        html.P(
                            """\
                            The color on chart plays vital role. Normally, red color indicates opening price is greater than the
                            closing price (Bearish). And green color indicates closing price is greater than the closing
                            price (Bullish)
                            """
                        ),
                        html.A(children=[
                            "Click here to view stock chart"
                        ], href="/candle-stick")
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
