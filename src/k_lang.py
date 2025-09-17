# src/k_lang.py
import streamlit as st

class KLang:
    def __init__(self):
        # Umbrales basados en AEMET para protocolos
        self.protocolos = {
            "VÍSPERA": {
                "disparador": "Viento 60-89 km/h o Inundación 20-49 cm",
                "acciones": [
                    "1. Alertar a conductores en rutas críticas.",
                    "2. Monitorear condiciones en tiempo real.",
                    "3. Preparar desvíos logísticos."
                ]
            },
            "CÓDIGO ROJO": {
                "disparador": "Viento >90 km/h o Inundación >50 cm",
                "acciones": [
                    "1. Evacuar rutas críticas inmediatamente.",
                    "2. Activar drones de inspección aérea.",
                    "3. Redirigir flota a rutas seguras."
                ]
            },
            "RENACIMIENTO": {
                "disparador": "Condiciones nominales post-crisis (Viento <60 km/h, Inundación <20 cm)",
                "acciones": [
                    "1. Evaluar daños en infraestructura.",
                    "2. Reactivar rutas logísticas.",
                    "3. Optimizar operaciones con IA."
                ]
            }
        }

    def get_protocolo_activo(self, viento, inundacion):
        """Determina el protocolo activo basado en datos de sensores."""
        if viento > 90 or inundacion > 50:
            return "CÓDIGO ROJO", self.protocolos["CÓDIGO ROJO"]["disparador"], self.protocolos["CÓDIGO ROJO"]["acciones"]
        elif viento > 60 or inundacion > 20:
            return "VÍSPERA", self.protocolos["VÍSPERA"]["disparador"], self.protocolos["VÍSPERA"]["acciones"]
        else:
            return "RENACIMIENTO", self.protocolos["RENACIMIENTO"]["disparador"], self.protocolos["RENACIMIENTO"]["acciones"]

    def render_selector(self):
        """Renders el selector de protocolos."""
        st.subheader("Selector de Protocolos")
        st.markdown("**Descripción**: Selecciona un protocolo (VÍSPERA, CÓDIGO ROJO, RENACIMIENTO) "
                    "para ver su ficha técnica: disparador y secuencia de acciones.")
        protocolo = st.selectbox("Selecciona Protocolo:", ["VÍSPERA", "CÓDIGO ROJO", "RENACIMIENTO"])
        st.markdown(f"**Ficha Técnica - {protocolo}**")
        st.markdown(f"**Disparador**: {self.protocolos[protocolo]['disparador']}")
        st.markdown("**Acciones**:")
        for accion in self.protocolos[protocolo]['acciones']:
            st.markdown(f"- {accion}")

    def render_simulator(self):
        """Renders el simulador de protocolos con sliders."""
        st.subheader("Simulador de Protocolos")
        st.markdown("**Descripción**: Ajusta la velocidad del viento (km/h) y el nivel de inundación (cm) "
                    "para determinar el protocolo activo en tiempo real, basado en umbrales AEMET.")
        col1, col2 = st.columns(2)
        with col1:
            viento = st.slider("Velocidad del Viento (km/h)", 0, 150, 40)
            inundacion = st.slider("Nivel de Inundación (cm)", 0, 100, 10)
        with col2:
            if st.button("Simular Protocolo Activo"):
                protocolo, disparador, acciones = self.get_protocolo_activo(viento, inundacion)
                st.error(f"**PROTOCOLO ACTIVO: {protocolo}**")
                st.markdown(f"**Disparador**: {disparador}")
                st.markdown("**Acciones**:")
                for accion in acciones:
                    st.markdown(f"- {accion}")
