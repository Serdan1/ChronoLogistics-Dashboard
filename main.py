# main.py
import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Añade directorio raíz para imports

from src.precog import Precog
from src.chronos import Chronos
from src.k_lang import KLang

# Configuración inicial
st.set_page_config(page_title="ChronoLogistics Dashboard", layout="wide", initial_sidebar_state="expanded")
st.title("🛡️ ChronoLogistics Dashboard")
st.markdown("**Sistema Central para Respuesta a Crisis**: Monitoreo táctico, visión estratégica y protocolos operativos.")

# Instanciar clases
precog = Precog()
chronos = Chronos()
klang = KLang()

# Crear pestañas
tab1, tab2, tab3 = st.tabs([
    "Precog: Monitor de Riesgo Táctico",
    "Chronos: Visión Estratégica 2040",
    "K-Lang: Manual de Batalla Interactivo"
])

with tab1:
    precog.render_map()
    precog.render_simulator()

with tab2:
    estrategia = chronos.render_selector()
    chronos.render_visualizer(estrategia)
    chronos.render_map()

with tab3:
    klang.render_selector()
    klang.render_simulator()