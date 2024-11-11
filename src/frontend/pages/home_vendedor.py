import streamlit as st
import plotly.graph_objects as go
from components.card import card_container
from streamlit_js_eval import streamlit_js_eval
from numerize.numerize import numerize

st.set_page_config(page_title="Dashboard de Vendas", layout="centered")
width:int = streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)

st.title("Olá, Arthur!")

meta = 5000
vendas_atual = 4500
progresso = min(vendas_atual / meta, 1) # to-do >100%

with card_container():
    st.markdown(
            f"""
        <style>
        .progress-container {{
            background-color: #34A75E;
            height: 40px;
            display: flex;
            align-items: end;
        }}
        .progress-bar {{
            width: {progresso * 100}%;
            height: 100%;
            background-color: #297846;
            text-align: center;
            line-height: 40px;
            color: white;
            display: flex;
            justify-content: end;
            padding-right: 15px;
        }}
        </style>
        <div style='display: flex; flex-direction: column; max-width:100%'>
            <h3 style='text-align: left; color: black;'>Andamento das Vendas</h3>
            <p style='text-align: left; color: black;'>Agosto - 2024</p>
            <div class="progress-container">
                <div class="progress-bar">R$ {numerize(vendas_atual)}</div>
            </div>
            <p style='text-align: right; color: black;'>R$ {numerize(meta)}</p>
            <p style='text-align: center; color: black;'>Faltam R$ {numerize(meta - vendas_atual)} para você atingir sua meta. Continue nesse ritmo!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -- Sales Ranking--
mock_ranking_data = [
    {"position": 1, "store": "Mariana de Souza", "value": 30000.00},
    {"position": 2, "store": "Marcelo Mello", "value": 20000.00},
    {"position": 3, "store": "Beatriz Freitas", "value": 10000.00},
    {"position": 15, "store": "Arthur Loures", "value": 7000.00},
]

def display_ranking_item(pos, store, value, currency="R$"):
    medal = ""
    borderStyle = "none"
    padding = "0"
    paddingSide = "0"
    if pos == 1:
        medal = "🥇"
    elif pos == 2:
        medal = "🥈"
    elif pos == 3:
        medal = "🥉"
    else:
        medal = pos
        borderStyle = "0.8px solid black"
        padding = "6px"
        paddingSide = "14px"

    st.markdown(
        f"""
        <div style='display: flex; justify-content: space-between; align-items: center; max-width:100%; border: {borderStyle}; border-radius: 4px; padding:{padding} {paddingSide} {padding} {paddingSide}; margin-bottom:{paddingSide}' >
            <div style='display: flex; align-items: center;'>
                <span style='font-size: 24px; padding-right: 10px;'>{medal}</span>
                <span style='font-size: 18px;'>{store}</span>
            </div>
            <div style='font-size: 18px;'>{currency} {numerize(value)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with card_container():
    st.markdown(
        """
        <div style='display: flex; flex-direction: column; width:100%'>
            <h3>
                Ranking de vendas
            </h3>
            <p>SP Capital Sul - Agosto, 2024</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    for item in mock_ranking_data[:3]:
        display_ranking_item(item['position'], item['store'], item['value'],)

    st.markdown("<div style='font-size: 24px; text-align: center;'>...</div>", unsafe_allow_html=True)

    for item in mock_ranking_data[3:]:
        display_ranking_item(item['position'], item['store'], item['value'])

# -- Remuneration --

def create_figure(x_range, legenda):

    total_value = 2378.54
    st.write(f"""
    <p style="font-size:32px; margin: 0px">
    R${numerize(total_value)}
    </p>
    """, unsafe_allow_html=True)

    values_1 = [10]
    values_2 = [25]
    values_3 = [60]

    fig = go.Figure()

    colors = ["#5FA9C8", "#F45F5F", "#7EDA6E"]

    fig.add_trace(go.Bar(
        x=values_1,
        name='Atingimento da meta',
        orientation='h',
        width=0.3,
        marker_color=colors[0],
    ))

    fig.add_trace(go.Bar(
        x=values_2,
        name='Comissão 5%',
        orientation='h',
        width=0.3,
        marker_color=colors[1],
    ))

    fig.add_trace(go.Bar(
        x=values_3,
        name='Comissão 10%',
        orientation='h',
        width=0.3,
        marker_color=colors[2],
    ))

    fig.update_layout(
        barmode='stack', 
        yaxis=dict(showticklabels=False), 
        xaxis=dict(range=x_range, showticklabels=False),
        legend=dict(
            orientation="h",
            yanchor="bottom", 
            y=legenda,         
            xanchor="left",  
            x=0
        ),
        margin=dict(
        t=0,
        b=2 
        ),
        height=200,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

with card_container():
    title = "Remuneração total"
    st.markdown(
        f"""
        <div style='display: flex; flex-direction: column; width:100%'>
            <h3>{title}</h3>
            <p style="margin: 0px">Agosto, 2024</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    legenda = 0.05

    if width < 600:
        x_range = [0, 115]
        if width < 420:
            legenda = 0
    else:
        x_range = [0, 103]
        
    fig = create_figure(x_range, legenda)
    
    # plot bar graph
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})