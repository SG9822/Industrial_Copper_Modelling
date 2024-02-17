import streamlit as st
import pickle
import numpy as np
import plotly.express as px
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide",
                   page_title="Industrial Copper Modeling",
                   page_icon="https://media.istockphoto.com/id/999815314/vector/the-periodic-table-element-copper-vector.jpg?s=612x612&w=0&k=20&c=084K0Nb4xJbOvfPQmY_rCBSa09J4L65nEgwh_Z7bLlo=")

tit1, tit2 = st.columns([1, 3])

with tit1:
    st.markdown("### [:brown[Copper Modelling | Project]]() <style>a { text-decoration: none; }</style>",
                unsafe_allow_html=True)
with tit2:
    selected = option_menu(
        menu_title=None,
        options=["Classification & Price Prediction"],
        icons=["grid-1x2-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal", )

if selected == 'Classification & Price Prediction':
    st.header(":blue[Give the Details to Predict the Status of progress of orders or transactions & Price]")
    inp1, inp2 = st.columns(2)
    with inp1:
        st.markdown("###### Customer Id")
        i1 = st.text_input('i1', label_visibility="collapsed", placeholder="Enter 8 digit Customer id")
        st.markdown("###### Application Code")
        app_code = [10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66, 29, 22, 25, 40, 79, 3, 99, 2, 67, 5, 39, \
                    69, 70, 65, 58, 68]
        app_code.sort()
        app_code.append("")
        i3 = st.selectbox('i3', app_code, index=len(app_code) - 1, label_visibility="collapsed")
        st.markdown("###### Width")
        i5 = st.text_input("i5", label_visibility="collapsed", placeholder="width in mm")
        st.markdown("###### Product Reference")
        i7 = st.text_input("i7", label_visibility="collapsed", placeholder="Enter 10 digit Product reference No.")
    with inp2:
        st.markdown("###### Country Code")
        country_code = [78, 26, 25, 32, 27, 28, 84, 77, 30, 39, 79, 38, 40, 80, 113, 89, 107]
        country_code.sort()
        country_code.append("")
        i2 = st.selectbox('i2', country_code, label_visibility="collapsed", index=len(country_code) - 1)
        st.markdown("###### Item Type")
        item_encode = {'W': 1, 'WI': 2, 'S': 3, 'PL': 4, 'IPL': 5, 'SLAWR': 6, 'Others': 7}
        item_list = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR', '']
        i4 = st.selectbox('i4', item_list, index=len(item_list) - 1, label_visibility="collapsed")
        st.markdown("###### Thickness")
        i6 = st.text_input("i6", label_visibility="collapsed", placeholder="Thickness in mm")
        st.markdown("###### Quantity")
        i8 = st.text_input("i8", label_visibility="collapsed", placeholder="Enter the Quantity in Tons")

    inp3, inp4, inp5 = st.columns(3)
    with inp3:
        st.markdown("###### Item Date")
        i9 = st.text_input("i9", label_visibility="collapsed", placeholder="Enter a Item Date")
        st.markdown("###### Delivery Date")
        i10 = st.text_input("i10", label_visibility="collapsed", placeholder="Enter a Delivery Date")
    with inp4:
        mon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "Select Month"]
        st.markdown("###### Item Month")
        i11 = st.selectbox("i11", mon, label_visibility="collapsed", index=len(mon) - 1)
        st.markdown("###### Delivery Month")
        i12 = st.selectbox("i12", mon, label_visibility="collapsed", index=len(mon) - 1)
    with inp5:
        st.markdown("###### Item Year")
        i13 = st.text_input('i13', label_visibility="collapsed", placeholder="Enter a Item Year")
        st.markdown("###### Delivery Year")
        i14 = st.text_input('i14', label_visibility="collapsed", placeholder="Enter a Delivery Year")

    st.markdown("")
    st.markdown("")

    i, j = st.columns(2)

    with i:
        bt = st.button("Get Status")
        if bt:
            with open('Classification.pkl', 'rb') as file:
                clf = pickle.load(file)
            i6_log = np.log(float(i6))
            i8_log = np.log(float(i8))

            clf_pred = [[i1, i2, i3, i5, i7, i8_log, i6_log, item_encode[i4],  i9, i11, i13, i10, i12, i14]]

            pre = clf.predict(clf_pred)
            a, b = st.columns([0.4, 2.6])
            with b:
                if pre[0] == 1:
                    st.markdown(f"# :blue[Invoice Status: Won]")
                else:
                    st.markdown(f"# :blue[Invoice Status: Lost]")
    with j:
        bt = st.button("Get Price")
        if bt:
            with open('Regression.pkl', 'rb') as file_:
                reg = pickle.load(file_)
            i6_log = np.log(float(i6))
            i8_log = np.log(float(i8))

            pred_r = [[i1, i2, i3, i5, i7, i8_log, i6_log, item_encode[i4], i9, i11, i13, i10, i12, i14]]

            pre = reg.predict(pred_r)
            a, b = st.columns([0.01, 3.99])
            with b:
                st.markdown(f"# :blue[Price of the Copper: ${round(np.exp(pre[0]), 2)}]")

# [30156308.0, 28.0, 10.0, 1500.0, 1670798778, 3.991779, 0.693147, 1, 1, 4, 2021,	1,	7,	2021]
# 30202938.0	25.0	1	41.0	1210.0	1668701718	6.643822	-0.223144	6.953684	1	1	4	2021	1	4	2021