# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import streamlit as st


analistas = ['Débora','Marcel', 'Raul', 'Vinícius']


st.selectbox('Selecione o analista: ',['Todos'] + analistas)

