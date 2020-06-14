#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Time Series", href="/time-series")),
            dbc.NavItem(dbc.NavLink("Candle Chart", href="/candle-stick")),
            dbc.NavItem(dbc.NavLink("Data Sets",
                                    target='_blank',
                                    href="https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs")),
        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
    )
    return navbar
