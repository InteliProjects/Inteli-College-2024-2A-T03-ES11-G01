import streamlit as st
import plotly.graph_objects as go
from components.card import card_container
from streamlit_js_eval import streamlit_js_eval
from numerize.numerize import numerize


st.set_page_config(page_title="Dashboard de Vendas", layout="centered")

st.title("Olá, Ana!")

width:int = streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)

# -- Sales --
meta = 150000
vendas_atual = 100000
progresso = min(vendas_atual / meta, 1)

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
            <p style='text-align: left; color: black;'>SP Capital Sul_32 - Agosto, 2024</p>
            <div class="progress-container">
                <div class="progress-bar">R$ {numerize(vendas_atual)}</div>
            </div>
            <p style='text-align: right; color: black;'>R$ {numerize(meta)}</p>
            <p style='text-align: center; color: black;'>Faltam R$ {numerize(meta - vendas_atual)} para a sua loja atingir a meta. Continue nesse ritmo!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -- Sales Ranking --
mock_ranking_data = [
    {"position": 1, "store": "SP Capital Sul_64", "value": 300000},
    {"position": 2, "store": "SP Capital Sul_9", "value": 200000},
    {"position": 3, "store": "SP Capital Sul_80", "value": 150000},
    {"position": 15, "store": "SP Capital Sul_32", "value": 100000},
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

def create_figure(x_range, height):
    # To-do get data from back-end
    sellers_mock = ['Victor Santos', 'Mariana de Souza', 'Marcello Mello']
    percentuais = [50, 70, 90]

    # Config bars
    fig = go.Figure()

    for i, pessoa in enumerate(sellers_mock):
        fig.add_trace(go.Bar(
            y=[pessoa],
            x=[percentuais[i]],
            name=pessoa,
            orientation='h',
            marker=dict(color='#5FA9C8')
        ))
        fig.add_trace(go.Bar(
            y=[pessoa],
            x=[100 - percentuais[i]],
            orientation='h',
            marker=dict(color='#D3D3D3'),
            showlegend=False
        ))

    # layout config
    fig.update_layout(
        barmode='stack',
        xaxis=dict(range=x_range, tickvals=[0, 100], ticktext=['0%', '100%'], tickfont=dict(color='black')),
        yaxis=dict(tickfont=dict(color='black')),
        yaxis_title=None,
        xaxis_title=None,
        showlegend=False,
        height=height,
        margin=dict(
        t=0.1,
        b=0.2 
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig

with card_container():
    st.markdown(
        f"""
        <div>
            <h3 style='color:black'>Acompanhamento de metas - %</h3>
            <p>Agosto - 2024</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if width < 480:
        x_range = [0, 130]
        height = 150
    else:
        x_range = [0, 115]
        height = 200

    fig = create_figure(x_range, height)
    # plot bar graph
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})