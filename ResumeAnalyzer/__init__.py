import json
import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from dash.exceptions import PreventUpdate
from jupyter_dash import JupyterDash

import textract
import pandas as pd
import numpy as np
import en_core_web_sm
import textract

from spacy.matcher import PhraseMatcher
from collections import Counter
from os import listdir
from os.path import isfile, join

# Load spacy model
nlp = en_core_web_sm.load()

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

def create_profile(filename, search_criteria):
    
    content = textract.process(filename, encoding="utf-8").decode()
    content = " ".join(content.split()).lower()

    matcher = PhraseMatcher(nlp.vocab)
    for col in search_criteria.keys():
        words = [nlp(word.lower()) for word in search_criteria[col]]
        matcher.add(col, None, *words)

    doc = nlp(content)

    from collections import Counter
    d = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        
        rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'COLOR'
        span = doc[start : end]  # get the matched slice of the doc
        d.append((rule_id, span.text))

    a = pd.DataFrame.from_dict(Counter(d), orient='index').reset_index()
    df = pd.DataFrame(a['index'].tolist(), columns=["Subject", "Keywords"])
    if len(df)==0:
        df["Count"]=0
    else:
        df["Count"] = a[0]
    df['Candidate'] = filename.split("/")[-1]
    
    return df


def rank(path, search_criteria):
    from os import listdir
    from os.path import isfile, join
    import os
    files = [f for f in listdir(path) if isfile(join(path, f))]
    final_database = pd.DataFrame()

    for file_name in files:
        try:
            data = create_profile(os.path.join(path,file_name), search_criteria)
        except:
            data= "XXXX"
            continue
        
        final_database = final_database.append(data, ignore_index=True)

    df = final_database.groupby(['Candidate','Subject']).count().reset_index()
    df = df.pivot_table(values='Count',index='Candidate', columns='Subject').fillna(0).reset_index()
    df['TOTAL SCORE'] = df.sum(axis=1)
    df = df.astype("int32", errors="ignore")
    df['RANKING']=np.round(df['TOTAL SCORE'].rank(pct=True),1)
    df['RATING'] = df['RANKING'].apply(lambda x:
        '⭐⭐⭐' if x >= .8 else (
        '⭐⭐' if x >= .5 else (
        '⭐' if x >=.2 else '')))
    df = df.sort_values(by='RANKING', ascending=False)

    return df
    
def run_dash(path, search_criteria, mode=None):
    
    PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
    # instantiating dash application
    #app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title="Resume Analyzer"
    
    files = [f for f in listdir(path) if isfile(join(path, f))]

    nlp = en_core_web_sm.load()


    search_bar = dbc.Row(
        [
            dbc.Badge(str(len(files))+ " Resume found", id="doc_info",href="#", color="warning", className="mr-1",),
            dbc.Col(
                dbc.Button("Process ⚙️", color="primary", className="ml-2", id="button", n_clicks=1),
                width="12",
            ),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Resume Analyzer", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://shivanandroy.com",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
        ],
        color="dark",
        dark=True,
    )
    
    text="**The table is filterable and sortable"
    
    summary = html.Div([dbc.Row([

        dbc.Col(dcc.Loading(html.Div([html.Div(text,style={'font-size':'10px'}),dash_table.DataTable(id='table', 
        sort_action="native",
         filter_action="native",
         style_cell = {
                    'font_family': 'Trebuchet MS',
                    'font_size': '15px',
                    'text_align': 'center'
                },
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_header_conditional=[
            {
                'if': {
                    'column_id': 'RANKING',
                },
                'backgroundColor': '#A8A8A8',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'TOTAL SCORE',
                },
                'backgroundColor': '#A8A8A8',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'RATING',
                },
                'backgroundColor': '#A8A8A8',
                'color': 'black'
            }
        ]



         )])), width={'size':10, 'offset':1})

    ], align='end')
    ])





    app.layout = html.Div([navbar, html.Br(), summary])


    @app.callback([
        Output("table", "columns"),
        Output("table", "data")],   
        [Input("button", "n_clicks")],
    )
    def toggle_navbar_collapse(n):
        if n is None:
            raise PreventUpdate
        else:
            files = [f for f in listdir(path) if isfile(join(path, f))]
            df = rank(path=path, search_criteria=search_criteria)
            return [{"name": i, "id": i} for i in df.columns], df.to_dict('records')


    if mode=="browser":
        app.run_server(debug=True)
    if mode=="notebook":
        app.run_server(debug=True, mode="inline", width=950)
        
    

class ResumeAnalyzer:
    
    def __init__(self):
        
        pass
  
    def rank(self, path, metadata):
        
        self.search_criteria = metadata
        self.path = path
        
        from os import listdir
        from os.path import isfile, join
        import os
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        final_database = pd.DataFrame()

        for file_name in files:
            try:
                data = create_profile(os.path.join(self.path,file_name), self.search_criteria)
            except:
                data="XXXX"
                continue
                
            final_database = final_database.append(data, ignore_index=True)

        df = final_database.groupby(['Candidate','Subject']).count().reset_index()
        df = df.pivot_table(values='Count',index='Candidate', columns='Subject').fillna(0).reset_index()
        df['TOTAL SCORE'] = df.sum(axis=1)
        df = df.astype("int32", errors="ignore")
        df['RANKING']=np.round(df['TOTAL SCORE'].rank(pct=True),1)
        df['RATING'] = df['RANKING'].apply(lambda x:
            '⭐⭐⭐' if x >= .8 else (
            '⭐⭐' if x >= .5 else (
            '⭐' if x >=.2 else '')))
        df = df.sort_values(by='RANKING', ascending=False)

        return df

    def render(self, path, metadata, mode="browser"):
        
        self.path = path
        self.search_criteria=metadata
        self.mode = mode
        run_dash(self.path, self.search_criteria, self.mode)