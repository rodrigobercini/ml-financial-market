import streamlit as st
import datetime
import numpy as np
import time
import pandas as pd

st.set_page_config(
    page_title='Data Science Guild - Testando Algoritmos de Machine Learning no Mercado de Ações',
    #page_icon=r"C:\Users\rodrigo\Documents\stock-market-app\0_Main.ico"
)

stock = st.sidebar.selectbox(
    'Escolha uma ação:',
     ['PETR4.SA', 'ABEV3.SA','VT'])

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.sidebar.date_input('Start date', datetime.datetime(2015,1,1))
end_date = st.sidebar.date_input('End date', datetime.datetime(2020,1,1))

pressed = st.sidebar.button('Prever!')

if start_date > end_date:
    st.sidebar.error('Error: A data final deve ser maior que inicial.')
elif end_date > today:
    st.sidebar.error('Erro: A data inicial deve ser antes de hoje')
elif start_date > today:
    st.sidebar.error('Erro: A data inicial deve ser antes de hoje')
else:
    if pressed:
        st.sidebar.success('O modelo está sendo treinado usando dados de `%s` até `%s`' % (start_date, end_date))




st.title('Testando Algoritmos de Machine Learning no Mercado de Ações')

st.write("Como usar: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras libero ante, imperdiet vitae ipsum eget, blandit porta arcu. Morbi mi mauris, placerat a aliquam iaculis, venenatis sit amet urna. Nunc consectetur erat id eros mollis, sed malesuada nibh ullamcorper. Vestibulum tempor mauris in nisi pharetra, quis sagittis ex aliquet. In volutpat maximus sapien, facilisis vestibulum quam auctor quis. Nullam ac dapibus dui, ut tincidunt felis. Nulla mauris leo, rhoncus eget sem at, scelerisque viverra sapien. Nam volutpat volutpat ligula, quis pharetra erat commodo in. Proin lobortis egestas felis, vel dapibus ex rutrum id. Nam interdum commodo ultricies. Donec accumsan turpis id neque efficitur luctus. In viverra, erat vitae finibus gravida, metus dolor pretium elit, vehicula faucibus quam libero id turpis.")
st.markdown(f"""
Rentabilidades\n
Modelo: \n
Ação: \n
Ibovespa: \n
CDI: \n
Inflação: \n
Poupança: \n
""")


chart_data = pd.DataFrame(
     np.random.randn(20, 6),
     columns=['Modelo', 'Ação', 'Ibovespa', 'CDI', 'Inflação', 'Poupança'])

st.line_chart(chart_data)

expander = st.beta_expander("Sobre o projeto")
expander.write("Este é um projeto open-source que busca a disseminaçãoo do conhecimento relacionado a ciência de dados no Brasil.")
expander.write("Essa é uma iniciativa da Data Science Guild, a primeiro liga acadêmica de dados do Brasil.")
expander.write("Se você gostou do app e quer alavancar seu conhecimento na área, acesse o link abaixo e faça parte da Guild")