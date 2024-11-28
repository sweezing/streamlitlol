import streamlit as st
import pandas as pd
import numpy as np
from select import select


class Project1:
    def __init__(self):
        pass
    def app(self):
        st.write('Ceration of strange dataframe fr')

        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None

        upload = st.file_uploader("choose yr way to get high")
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)

            column = st.selectbox("Choose column for filter yeah", df.columns)

            if column:

                un_values = df[column].unique()
                select_value = st.multiselect(f"Select values for {column}", options=un_values, default=un_values)

                filtered_df = df[df[column].isin(select_value)]

                st.dataframe(filtered_df, height=400, width=600)

                try:
                    st.area_chart(filtered_df, height=400, width=600)

                except:
                    st.write("Can't draw so manny data")
        else:
            st.warning("Please do smth (i assume you will upload ur datafile)")

        st.markdown("""<style>
                    h1 {
                    color: rgb(200, 200, 200);
                    font-size: 18px;
                    text-align: center;
                    }
                    """, unsafe_allow_html=True)
