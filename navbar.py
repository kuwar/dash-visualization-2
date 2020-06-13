#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Time Series", href="/time-series")),
            dbc.NavItem(dbc.NavLink("Candle Chart", href="/candle-stick")),
            dbc.NavItem(dbc.NavLink("Download CSV",
                                    target='_blank',
                                    href="https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")),
        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
    )
    return navbar
