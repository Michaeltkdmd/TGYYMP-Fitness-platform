import streamlit as st
from streamlit_lottie import st_lottie
import time
import datetime 
import requests
import math
import random
from annotated_text import annotated_text
import numpy as numpy
import json
import requests
import streamlit_authenticator as stauth 
import re
from deta import Deta
from streamlit_option_menu import streamlit_option_menu

st.title("TGYYMP")

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Questionnaire", "Calender", "Cross Section", "Fitness Tracker", "Visuals & Content", "Nutrition", "Body Composition" , "Cognitive Performance"])
