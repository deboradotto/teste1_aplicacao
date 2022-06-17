# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import streamlit as st


analistas = ['Débora','Marcel', 'Raul', 'Vinícius']

treinamentos = ['Filas','Onboarding', 'Template', 'Thundera','Grupo Controle','SQL','Azure Synapse','Análise Grupo','Grupo Controle + Atividade']



analista = st.selectbox('Selecione o analista: ',['Todos'] + analistas)

Treinamento = st.selectbox('Selecione o treinamento concluído: ', treinamentos)

