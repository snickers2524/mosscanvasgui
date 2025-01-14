import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


def execute():
    return dbc.Card(
        [
            dbc.CardHeader(
                dbc.Button("Download",
                           id="right-group-2-toggle",
                           className="sidebarbuttons"),
                className="sidebarcards"
            ),
            dbc.Collapse(
                dbc.CardBody(children=[
                    dbc.Button("Download Requested Assignments",
                               id='download-button',
                               className="sidebarbuttons",
                               disabled=True),

                ]),
                id="right-collapse-2"
            ),
        ],
        className="card"
    )
    #
    # return html.Div(
    #     dbc.Button("Download",
    #                className="sidebarbuttons", id='download-button', disabled=True),
    #     id="execute-container")


def mossSideBar():
    return dbc.Card(
        [
            dbc.CardHeader(
                dbc.Button("Moss", id="right-group-1-toggle", className="sidebarbuttons"),
                className="sidebarcards"
            ),
            dbc.Collapse(
                dbc.CardBody(children=[
                    dbc.Button("Run", id="run-moss", className="sidebarbuttons", disabled=True),
                    html.Br(),
                    html.Br(),
                    html.H6('Moss Report:', id='prev-moss-report-header'),
                    html.A(children='No Moss Report Detected',
                           href='/',
                           style={'cursor': 'default', 'pointer-events': 'none', 'text-decoration': 'none', 'color': 'grey'},
                           id='moss-report-link',
                           target="_blank"),
                    html.Br(),
                    html.A(children='No Bar-plot Detected',
                           href='/',
                           style={'cursor': 'default', 'pointer-events': 'none', 'text-decoration': 'none', 'color': 'grey'},
                           id='moss-barplot-link',
                           target="_blank")
                ]),
                id="right-collapse-1"
            ),
        ],
        className="card"
    )


def results():
    return html.Div("Moss Results", id='results', className="hidden")


def results2():
    return html.Div("Moss Results", id='results2', className="hidden")
