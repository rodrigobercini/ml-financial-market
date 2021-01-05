import streamlit as st
import datetime
import numpy as np
import time
import pandas as pd

from main import simulate_neural_network

st.set_page_config(
    page_title='Data Science Guild - Testando Algoritmo de Machine Learning no Mercado de Ações',
    #page_icon=r"C:\Users\rodrigo\Documents\stock-market-app\0_Main.ico"
)

stock_selection = st.sidebar.selectbox(
    'Escolha uma ação:',[
        'PETR4.SA - Petroleo Brasileiro S.A. - Petrobras',
        'ABEV3.SA - Ambev',
        'BBAS3.SA - Banco do Brasil S.A.',  
        'PCAR3.SA - Companhia Brasileira de Distribuicao',
        'OIBR4.SA - Oi S.A.',
        'SBSP3.SA - Companhia de Saneamento Basico do Estado de Sao Paulo - SABESP',
        'CCRO3.SA - CCR S.A.',
        'LREN3.SA - Lojas Renner S.A.', 
        'BBSE3.SA - BB Seguridade Participacoes S.A.',
        'TIMP3.SA - TIM Participacoes S.A.',
        'EQTL3.SA - Equatorial Energia S.A.',
        'VIVT4.SA - Telefonica Brasil S.A.', 'BRKM5.SA - Braskem S.A.',
        'MULT3.SA - Multiplan Empreendimentos Imobiliarios S.A.',
        'ITSA4.SA - Itausa - Investimentos Itau S.A.',
        'CMIG4.SA - Companhia Energetica de Minas Gerais',
        'USIM5.SA - Usinas Siderurgicas de Minas Gerais S.A.',
        'BRML3.SA - BR Malls Participacoes S.A.',
        'BBDC3.SA - Banco Bradesco S.A.',
        'ENBR3.SA - EDP - Energias do Brasil S.A.',
        'RADL3.SA - Raia Drogasil S.A.',
        'LAME4.SA - Lojas Americanas S.A.',
        'BBDC4.SA - Banco Bradesco S.A.',
        'PETR3.SA - Petroleo Brasileiro S.A. - Petrobras',
        'UGPA3.SA - Ultrapar Participacoes S.A.',
        'ECOR3.SA - EcoRodovias Infraestrutura e Logistica S.A.',
        'JBSS3.SA - JBS S.A.',
        'VALE3.SA - Vale do Rio Doce AS',
        'KLBN11.SA - KLABIN S/A UNT N2',
        'TBLE3.SA - TBLE3.SA'
])

stock = stock_selection[:7]

# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
# start_date = st.sidebar.date_input('Start date', datetime.datetime(2015,1,1))
# end_date = st.sidebar.date_input('End date', datetime.datetime(2020,1,1))

# pressed = st.sidebar.button('Prever!')

# if start_date > end_date:
#     st.sidebar.error('Error: A data final deve ser maior que inicial.')
# elif end_date > today:
#     st.sidebar.error('Erro: A data inicial deve ser antes de hoje')
# elif start_date > today:
#     st.sidebar.error('Erro: A data inicial deve ser antes de hoje')
# else:
#     if pressed:
#         st.sidebar.success('O modelo está sendo treinado usando dados de `%s` até `%s`' % (start_date, end_date))

st.title('Testando Algoritmos de Machine Learning no Mercado de Ações')

portfolio = simulate_neural_network()

chart_data = pd.DataFrame(
     np.random.randn(20, 6),
     columns=['Modelo', 'Ação', 'Ibovespa', 'CDI', 'Inflação', 'Poupança'])

#df[['stocks_owned', 'close', 'Total$']].plot()

st.line_chart(portfolio[['stocks_owned', 'close']])

#st.line_chart(chart_data['Ação'])

expander = st.beta_expander("Sobre o projeto")
expander.write("Este é um projeto open-source que busca a disseminaçãoo do conhecimento relacionado a ciência de dados no Brasil.")
expander.write("Essa é uma iniciativa da Data Science Guild, a primeiro liga acadêmica de dados do Brasil.")
expander.write("Se você gostou do app e quer alavancar seu conhecimento na área, acesse o link abaixo e faça parte da Guild")