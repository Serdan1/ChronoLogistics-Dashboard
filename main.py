# main.py
import streamlit as st
from src.precog import Precog
from src.chronos import Chronos

# Configuración inicial
st.set_page_config(page_title="ChronoLogistics Dashboard", layout="wide", initial_sidebar_state="expanded")
st.title("🛡️ ChronoLogistics Dashboard")
st.markdown("**Sistema Central para Respuesta a Crisis**: Monitoreo táctico, visión estratégica y protocolos operativos.")

# Instanciar clases
precog = Precog()
chronos = Chronos()

# Crear pestañas
tab1, tab2 = st.tabs(["Precog: Monitor de Riesgo Táctico", "Chronos: Visión Estratégica 2040"])

with tab1:
    precog.render_map()
    precog.render_simulator()

with tab2:
    estrategia = chronos.render_selector()
    chronos.render_visualizer(estrategia)
    chronos.render_map()