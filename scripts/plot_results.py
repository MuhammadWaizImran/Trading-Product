from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'experiment_001'
fig=make_subplots(rows=2,cols=1,subplot_titles=[
    'Frozen experiment: one-day trades, close/reopen costs',
    'Post-test diagnostic: carry positions, costs on transitions'],vertical_spacing=.17)
colors=dict(model='#007f86',trend='#c06416',buy_hold='#6068bc',cash='#888888')
for row,filename in [(1,'daily_portfolio_returns.csv'),(2,'carry_positions_30bps_round_trip.csv')]:
    data=pd.read_csv(OUT/filename,index_col=0,parse_dates=True)
    equity=(1+data).cumprod()
    initial=pd.DataFrame(1.,index=[equity.index[0]-pd.Timedelta(days=1)],columns=equity.columns)
    equity=pd.concat([initial,equity])
    for name in data.columns:
        fig.add_trace(go.Scatter(x=equity.index,y=equity[name],name=name,legendgroup=name,
            showlegend=row==1,line=dict(color=colors[name],width=2)),row=row,col=1)
    fig.update_yaxes(title_text='Simulated equity (start = 1)',row=row,col=1)
fig.update_layout(title='Experiment 001 — insufficient evidence for live agents',height=880,
    template='plotly_white',hovermode='x unified',margin=dict(t=110,b=90),
    annotations=list(fig.layout.annotations)+[dict(x=0,y=-.12,xref='paper',yref='paper',showarrow=False,
    text='BTC/ETH only · 2024–2025 · 15 bps per side · No leverage · Historical simulation, not prospective results',xanchor='left')])
fig.write_html(OUT/'equity_charts.html',include_plotlyjs=True,full_html=True)
print(OUT/'equity_charts.html')
