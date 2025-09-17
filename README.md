---
title: ChronoLogistics Dashboard
emoji: 🛡️
colorFrom: blue
colorTo: red
sdk: streamlit
sdk_version: 1.38.0
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
   - Se creó un Space en Hugging Face (`https://huggingface.co/spaces/Danserrano1/ChronoLogistics-Dashboard-3`) con SDK Streamlit y un `Dockerfile` para despliegue.

2. **Desarrollo de Pestañas**:
   - **Precog**: Monitor de riesgo táctico con mapa de calor (azul-rojo) y simulador de riesgos climáticos (sliders de viento y lluvia).
   - **Chronos**: Visión estratégica 2040 con selector de estrategias ("Fortaleza Verde", "Búnker Tecnológico"), visualizador de imágenes (300px), texto defensivo y mapa.
   - **K-Lang**: Manual interactivo de protocolos con selector (VÍSPERA, CÓDIGO ROJO, RENACIMIENTO) y simulador con sliders (viento e inundación).

3. **Pruebas Unitarias**:
   - Se implementaron 9 tests en `tests/test_precog.py`, `tests/test_chronos.py`, y `tests/test_k_lang.py` usando pytest, todos pasados exitosamente.

4. **Despliegue y Sincronización**:
   - Se corrigió el `README.md` con YAML para configurar el Space (title, emoji, sdk: streamlit, app_file: main.py).
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

```mermaid
graph TD
    A[Usuario] --> B[Interfaz Streamlit]
    B --> C[Precog]
    B --> D[Chronos]
    B --> E[K-Lang]
    C --> F[Datos Climáticos<br>(Viento, Lluvia)]
    C --> G[Simulador de Riesgo]
    C --> H[Mapa de Calor]
    D --> I[Datos Estratégicos<br>(Fortaleza Verde, Búnker Tecnológico)]
    D --> J[Visualizador de Imágenes]
    D --> K[Mapa Estratégico]
    E --> L[Protocolos<br>(VÍSPERA, CÓDIGO ROJO, RENACIMIENTO)]
    E --> M[Simulador de Protocolos]
    F --> N[API AEMET]
    I --> O[Base de Datos]
    subgraph "ChronoLogistics Dashboard"
        C
        D
        E
    end
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#bfb,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
    style F fill:#ddf,stroke:#333,stroke-width:2px
    style G fill:#ddf,stroke:#333,stroke-width:2px
    style H fill:#ddf,stroke:#333,stroke-width:2px
    style I fill:#ddf,stroke:#333,stroke-width:2px
    style J fill:#ddf,stroke:#333,stroke-width:2px
    style K fill:#ddf,stroke:#333,stroke-width:2px
    style L fill:#ddf,stroke:#333,stroke-width:2px
    style M fill:#ddf,stroke:#333,stroke-width:2px
    style N fill:#ffd,stroke:#333,stroke-width:2px
    style O fill:#ffd,stroke:#333,stroke-width:2px