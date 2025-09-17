# src/chronos.py
import streamlit as st
import plotly.graph_objects as go
import os

class Chronos:
    def __init__(self):
        # Rutas a las imágenes
        self.imagenes = {
            "Fortaleza Verde": "imagenes/fortaleza_verde.jpg",
            "Búnker Tecnológico": "imagenes/bunker_tecnologico.jpg"
        }
        # Coordenadas de ubicaciones clave
        self.bunker = [40.3571, -3.9006]  # Villaviciosa de Odón
        self.fortaleza = [40.7406, -4.0568]  # Cercedilla
        self.madrid_center = [40.4165, -3.7026]  # Centro de Madrid

    def get_defensa(self, estrategia):
        """Devuelve el texto defensivo para la estrategia seleccionada."""
        if estrategia == "Fortaleza Verde":
            return ("**Fortaleza Verde**: Ubicada en Cercedilla, esta estrategia prioriza la sostenibilidad, "
                    "integrando logística de cero emisiones con IA para optimizar rutas en Madrid. "
                    "Reduce un 40% las emisiones para 2040, atrayendo inversores ESG y asegurando resiliencia climática.")
        else:
            return ("**Búnker Tecnológico**: Situado en Villaviciosa de Odón, este enfoque refuerza la ciberseguridad "
                    "y la automatización subterránea. Usa IA predictiva para garantizar continuidad operativa, "
                    "protegiendo activos clave contra disrupciones urbanas.")

    def render_selector(self):
        """Renders el selector de estrategia."""
        st.subheader("Selector de Estrategia")
        st.markdown("**Descripción**: Selecciona una visión estratégica ('Fortaleza Verde' o 'Búnker Tecnológico') "
                    "para visualizar su impacto y justificación para el futuro de ChronoLogistics.")
        estrategia = st.selectbox("Elige Visión:", ["Fortaleza Verde", "Búnker Tecnológico"])
        return estrategia

    def render_visualizer(self, estrategia):
        """Renders la imagen y texto defensivo de la estrategia."""
        st.subheader("Visualizador de Futuros")
        st.markdown("**Descripción**: Muestra la imagen generada (GAN) para la estrategia seleccionada, "
                    "junto con una defensa argumentada de su valor para ChronoLogistics.")

        # Usar columnas para mostrar imagen a la izquierda y texto a la derecha
        col1, col2 = st.columns([1, 2])
        with col1:
            if os.path.exists(self.imagenes[estrategia]):
                st.image(self.imagenes[estrategia], caption=f"Visión: {estrategia}", width=300)  # Tamaño reducido
            else:
                st.warning(f"Imagen no encontrada: {self.imagenes[estrategia]}")
        with col2:
            st.markdown(self.get_defensa(estrategia))

    def render_map(self):
        """Renders un mapa con las ubicaciones del Búnker y la Fortaleza."""
        st.subheader("Mapa de Ubicaciones Estratégicas")
        st.markdown("**Descripción**: Mapa interactivo mostrando la ubicación del Búnker Tecnológico (Villaviciosa de Odón) "
                    "y la Fortaleza Verde (Cercedilla) en la Comunidad de Madrid.")
        fig = go.Figure(go.Scattermapbox(
            lat=[self.bunker[0], self.fortaleza[0]],
            lon=[self.bunker[1], self.fortaleza[1]],
            mode='markers+text',
            marker=dict(size=15, color=['blue', 'green']),
            text=['Búnker Tecnológico', 'Fortaleza Verde'],
            textposition='top center'
        ))
        fig.update_layout(
            mapbox=dict(
                style="carto-positron",
                center={"lat": self.madrid_center[0], "lon": self.madrid_center[1]},
                zoom=9
            ),
            margin={"r":0, "t":0, "l":0, "b":0}, height=400
        )
        st.plotly_chart(fig)