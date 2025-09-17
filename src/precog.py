# src/precog.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

class Precog:
    def __init__(self):
        # Coordenadas de Madrid y ubicaciones clave
        self.madrid_center = [40.4165, -3.7026]  # Centro de Madrid
        self.bunker = [40.3571, -3.9006]  # Villaviciosa de Odón
        self.fortaleza = [40.7406, -4.0568]  # Cercedilla
        # Puntos críticos ficticios (barrios/pueblos de Madrid con riesgo simulado)
        self.puntos_criticos = pd.DataFrame({
            'nombre': ['Centro', 'Usera', 'Puente de Vallecas', 'Leganés', 'Alcorcón'],
            'lat': [40.4165, 40.3886, 40.3918, 40.3316, 40.3457],
            'lon': [-3.7026, -3.7003, -3.6690, -3.7757, -3.8249],
            'riesgo': [80, 65, 90, 70, 55]  # Riesgo ficticio (0-100)
        })
        # Triángulo del Peligro (3 puntos más críticos)
        self.triangle = self.puntos_criticos.nlargest(3, 'riesgo')[['lat', 'lon']]

    def predecir_riesgo(self, velocidad_viento, intensidad_lluvia):
        """Calcula el nivel de riesgo basado en umbrales AEMET."""
        # Fórmula ajustada: 60% viento, 35% lluvia, 5% aleatorio
        viento_norm = min(velocidad_viento / 150, 1) * 100  # Normaliza a 0-100
        lluvia_norm = min(intensidad_lluvia / 100, 1) * 100
        riesgo = (0.6 * viento_norm) + (0.35 * lluvia_norm) + (0.05 * np.random.uniform(0, 20))
        riesgo = min(100, max(0, riesgo))  # Limita a 0-100
        # Niveles basados en AEMET
        if riesgo >= 90:
            nivel = "CRÍTICO"
        elif riesgo >= 70:
            nivel = "ALTO"
        elif riesgo >= 30:
            nivel = "MEDIO"
        else:
            nivel = "BAJO"
        return f"{riesgo:.0f}% - {nivel}"

    def render_map(self):
        """Renders a Plotly map with heatmap, Triángulo del Peligro, and key locations."""
        st.subheader("Mapa de Calor de Riesgo")
        st.markdown("**Descripción**: Mapa interactivo de Madrid mostrando áreas de riesgo climático (heatmap). "
                    "El **Triángulo del Peligro** resalta los 3 puntos más críticos (rojo). "
                    "Marcadores indican el Búnker Tecnológico (Villaviciosa de Odón) y la Fortaleza Verde (Cercedilla).")

        # Crear mapa con Plotly
        fig = px.scatter_mapbox(
            self.puntos_criticos,
            lat="lat", lon="lon", size="riesgo", color="riesgo",
            color_continuous_scale="hot", size_max=20, zoom=10,
            center={"lat": self.madrid_center[0], "lon": self.madrid_center[1]},
            mapbox_style="carto-positron"  # Estilo claro y profesional
        )

        # Añadir Triángulo del Peligro
        fig.add_trace(go.Scattermapbox(
            lat=self.triangle['lat'].tolist() + [self.triangle['lat'].iloc[0]],
            lon=self.triangle['lon'].tolist() + [self.triangle['lon'].iloc[0]],
            mode='lines+markers', line=dict(width=2, color='red'), name='Triángulo del Peligro'
        ))

        # Añadir marcadores para Búnker y Fortaleza
        fig.add_trace(go.Scattermapbox(
            lat=[self.bunker[0], self.fortaleza[0]],
            lon=[self.bunker[1], self.fortaleza[1]],
            mode='markers+text',
            marker=dict(size=15, color=['blue', 'green']),
            text=['Búnker Tecnológico', 'Fortaleza Verde'],
            textposition='top center',
            name='Ubicaciones Estratégicas'
        ))

        fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0}, height=500)
        st.plotly_chart(fig)

    def render_simulator(self):
        """Renders an interactive risk simulator with sliders."""
        st.subheader("Simulador de Riesgo Interactivo")
        st.markdown("**Descripción**: Ajusta la velocidad del viento (km/h) y la intensidad de la lluvia (mm/h) "
                    "para simular el nivel de riesgo en tiempo real, basado en umbrales AEMET.")

        col1, col2 = st.columns(2)
        with col1:
            velocidad = st.slider("Velocidad del Viento (km/h)", 0, 150, 50)
            lluvia = st.slider("Intensidad de Lluvia (mm/h)", 0, 100, 20)
        with col2:
            if st.button("Predecir Riesgo"):
                riesgo = self.predecir_riesgo(velocidad, lluvia)
                st.metric("Nivel de Riesgo en Cascada", riesgo)