#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PostMortemInterval.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    def load_data():
        data = pd.read_csv('pmi_new.csv')
        st.write(data)
        return data

    def split(df):
        y = df.Pmi
        x = df.drop(columns=['Pmi',"name"])
        return x,y
    def add(ldh,ast,triglycerides,phlevel,pmi,name=None):
        data = {
            'name': [name],
            'ldh': [ldh],
            'ast': [ast],
            'triglycerides': [triglycerides],
            'phlevel': [phlevel],
            'pmi': [pmi]

        }
        df = pd.DataFrame(data)
        df.to_csv('pmi_new.csv', mode='a', index=False, header=False)
        print("Data appended successfully.")
    df=load_data()
    x,y=split(df)
    C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key="C_LR")
    max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key="max_iter")
    ldh=st.sidebar.number_input("LDH is",step=10)
    ast=st.sidebar.number_input("AST is",step=10)
    triglycerides=st.sidebar.number_input("Triglycerides is",step=5)
    phlevel=st.sidebar.number_input("Ph Level is",step=1)
    name=st.sidebar.text_input("Name of the patient is")
    if "btn_clk" not in st.session_state:
        st.session_state.btn_clk=False
    def callback():
        st.session_state.btn_clk=True
    if st.sidebar.button("Predict",on_click=callback , key="classify") or st.session_state.btn_clk:
        st.subheader("Prediction Results")
        model = LogisticRegression(C=C, max_iter=max_iter)
        model.fit(x, y)
        xc=[(ldh,ast,triglycerides,phlevel)]
        x_test = pd.DataFrame(xc, columns=['ldh', 'ast', 'triglycerides','ph_level'])
        y_pred=model.predict(x_test)
        st.write("The PMI estimated is",(int(y_pred[0])))
        st.write("Wanna add the results to prediction data?")
        #t="name"+","+"ldh"+","+"ast"+","+"trig"+","+str(ph_level)+","+str(int(y_pred[0]))
        s="name= "+str(name)+","+"ldh= "+str(ldh)+","+"ast= "+str(ast)+","+"triglycerides= "+str(triglycerides)+","+"ph_level= "+str(phlevel)+","+"pmi_predicted= "+str(int(y_pred[0]))
        st.write(s)
        if st.button("ADD",key="add"):
            st.subheader("Adding the data")
            if name:
                add(ldh,ast,triglycerides,phlevel,int(y_pred[0]),name=name)
            else:
                add(ldh,ast,triglycerides,phlevel, int(y_pred[0]),name=name)
            f=load_data()




if __name__ == '__main__':
    main()
