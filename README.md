---
title: ChronoLogistics Dashboard
emoji: 🛡️
colorFrom: blue
colorTo: red
sdk: docker
sdk_version: "3.0.0"
app_file: main.py
pinned: false
---

# ChronoLogistics Dashboard

Dashboard de mando y control en tiempo real para ChronoLogistics. Incluye:
- **Precog**: Monitor de riesgo táctico con mapa de calor de Madrid y simulador de riesgos climáticos.
- **Chronos**: Visión estratégica 2040 con selector de estrategias y visualizador de futuros.
- **K-Lang**: Manual interactivo de protocolos.

Desarrollado con Streamlit y Plotly. Desplegado en Hugging Face Spaces para demo de crisis IA.

## Instrucciones
- Ejecuta localmente: `streamlit run main.py`.
- Dependencias: Ver `requirements.txt`.

## Resumen del Desarrollo del Dashboard

Este proyecto ha sido desarrollado paso a paso para crear el **ChronoLogistics Dashboard**, un sistema de mando y control en tiempo real para gestionar crisis con IA. A continuación, se detalla el proceso:

### Pasos Realizados
1. **Configuración Inicial**:
   - Se configuró un repositorio GitHub (`https://github.com/Serdan1/ChronoLogistics-Dashboard`) con Git LFS para manejar imágenes (`imagenes/bunker_tecnologico.jpg`, `imagenes/fortaleza_verde.jpg`).
   - Se creó un Space en Hugging Face (`https://huggingface.co/spaces/Danserrano1/ChronoLogistics-Dashboard-3`) con SDK Docker y un `Dockerfile` para despliegue.

2. **Desarrollo de Pestañas**:
   - **Precog**: Monitor de riesgo táctico con mapa de calor (azul-rojo) y simulador de riesgos climáticos (sliders de viento y lluvia).
   - **Chronos**: Visión estratégica 2040 con selector de estrategias ("Fortaleza Verde", "Búnker Tecnológico"), visualizador de imágenes (300px), texto defensivo y mapa.
   - **K-Lang**: Manual interactivo de protocolos con selector (VÍSPERA, CÓDIGO ROJO, RENACIMIENTO) y simulador con sliders (viento e inundación).

3. **Pruebas Unitarias**:
   - Se implementaron 9 tests en `tests/test_precog.py`, `tests/test_chronos.py`, y `tests/test_k_lang.py` usando pytest, todos pasados exitosamente.

4. **Despliegue y Sincronización**:
   - Se corrigió el `README.md` con YAML para configurar el Space (title, emoji, sdk: docker, app_file: main.py).
   - Se creó un branch limpio (`hf-deploy-clean`) para evitar errores de binarios y se empujó al Space.
   - Las imágenes se subieron manualmente a `imagenes/` en el Space.
   - Se configuró GitHub Actions con `.github/workflows/sync-to-hf.yml` para sincronización automática.

5. **Pruebas y Demo**:
   - Tests locales confirmaron la funcionalidad de las tres pestañas.
   - El dashboard se probó localmente con `streamlit run main.py` y en HF (`https://huggingface.co/spaces/Danserrano1/ChronoLogistics-Dashboard-3`).
   - Preparado para demo con secuencia: Precog (mapa y sliders), Chronos (estrategias e imágenes), K-Lang (simulador y selector).

### Dependencias
- Ver `requirements.txt` para Streamlit, Plotly, Pillow, pytest, numpy, pandas.

### Instrucciones Finales
- URL de demo: `https://huggingface.co/spaces/Danserrano1/ChronoLogistics-Dashboard-3`.
- Backup local: `streamlit run main.py` en Codespaces.
