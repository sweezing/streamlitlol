import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from Pages import Home, Project1, Project2, Project3

from PIL import Image
import pandas as pd
import numpy as np

image = Image.open("img/pupaduta.png")
# navlogo = Image.open("img/123.svg")

st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)


pages = ['Home','Project1','Project2','Project3']

style = {
    "nav": {
        "background-color": "gray",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(50, 50, 50)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(105, 114, 225, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
pages = st_navbar(pages, styles= style)

styles = {
    "nav": {
        "background-color": "gray",
        "display": "flex",
        "justify-content": "center",
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "span": {
        "display": "block",
        "color": "white",
        "padding": "0.2rem 0.725rem",
        "font-size": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px",
    },
}

if pages == 'Home':
    Home.Home().app()
elif pages == 'Project1':
    Project1.Project1().app()
elif pages == 'Project2':
    Project2.Project2().app()
elif pages == 'Project3':
    Project3.Project3().app()
else:
    Home.Home().app()