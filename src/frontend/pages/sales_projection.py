import streamlit as st
import streamlit_shadcn_ui as ui
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from components.card import card_container

st.title("Projeção de Vendas")




meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
serie1 = [500, 520, 480, 550, 600, 620, 580, 560, 600]
serie2 = [500, 520, 480, 550, 600, 620, 580, 560, 600, 600, 570, 550]
serie3 = [600, 600, 600, 610, 610, 600, 600, 590, 590, 590, 590, 590]

with card_container():
    st.markdown("### Desempenho de Vendas")
    st.markdown("Revisite sua performance em diferentes períodos.")
    
    # create checkboxes
    cols = st.columns(2)
    with cols[0]:
        meta_checked = ui.checkbox(default_checked=True, label='Meta')
    with cols[1]:
        predicao_checked = ui.checkbox(default_checked=True, label='Predição')

    if meta_checked and predicao_checked:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=meses, y=serie1, mode='lines', name='Valor real', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=meses, y=serie2, mode='lines', name='Predição', line=dict(color='grey', dash='dash')))
        fig.add_trace(go.Scatter(x=meses, y=serie3, mode='lines', name='Meta', line=dict(color='orange')))
        fig.update_layout(
            title='Orçamento Anual',
            xaxis_title='Meses',
            yaxis_title='R$',
            yaxis_tickprefix='R$ ',
            legend_title='Séries',
            width=600,
            yaxis=dict(
            tick0=0,         
            dtick=1000,      
            range=[0, 1000]
            )
        )
        st.plotly_chart(fig)
    
    elif not meta_checked and predicao_checked:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=meses, y=serie1, mode='lines', name='Série 1', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=meses, y=serie2, mode='lines', name='Série 2', line=dict(color='grey', dash='dash')))
        fig.update_layout(
            title='Orçamento Anual',
            xaxis_title='Meses',
            yaxis_title='R$',
            yaxis_tickprefix='R$ ',
            width=600, 
            legend_title='Séries',
            yaxis=dict(
            tick0=0,         
            dtick=1000,      
            range=[0, 1000]
            )
        )
        st.plotly_chart(fig)

    elif meta_checked and not predicao_checked:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=meses, y=serie1, mode='lines', name='Série 1', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=meses, y=serie3, mode='lines', name='Série 2', line=dict(color='orange')))
        fig.update_layout(
            title='Orçamento Anual',
            xaxis_title='Meses',
            yaxis_title='R$',
            yaxis_tickprefix='R$ ', 
            width=600,
            legend_title='Séries',
            yaxis=dict(
            tick0=0,         
            dtick=1000,      
            range=[0, 1000]
            )
        )
        st.plotly_chart(fig)
