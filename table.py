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
                        dt.DataTable(
                            id='table-sorting-filtering',
                            style_data={
                                'whiteSpace': 'normal',
                                'height': 'auto'
                            },
                            style_table={
                                'maxHeight': '800px',
                                'overflowY': 'scroll'
                            },
                            columns=[{"name": i, "id": i, } for i in (st.columns)],
                            data=st.to_dict('records'),
                            sort_action="native",
                            filter_action='native',
                            page_current=0,
                            page_size=20,
                        )
                    ],
                    md=12
                ),
            ]
        )
    ],
    className="mt-4",
)


def TabularData():
    layout = html.Div([
        nav,
        body
    ])
    return layout


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = TabularData()
if __name__ == "__main__":
    app.run_server()
