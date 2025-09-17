# tests/test_precog.py
import pytest
from src.precog import Precog

@pytest.fixture
def precog():
    return Precog()

def test_predecir_riesgo(precog):
    """Testea que predecir_riesgo devuelve un string con % y nivel."""
    result = precog.predecir_riesgo(50, 20)
    assert isinstance(result, str)
    assert "%" in result
    assert any(nivel in result for nivel in ["BAJO", "MEDIO", "ALTO", "CRÍTICO"])

def test_predecir_riesgo_valores_logicos(precog):
    """Testea que los valores de riesgo son lógicos para entradas extremas."""
    result_bajo = precog.predecir_riesgo(10, 5)
    result_alto = precog.predecir_riesgo(120, 80)
    assert "BAJO" in result_bajo or "MEDIO" in result_bajo
    assert "ALTO" in result_alto or "CRÍTICO" in result_alto

def test_puntos_criticos(precog):
    """Testea que los puntos críticos y el Triángulo del Peligro tienen el formato correcto."""
    assert len(precog.puntos_criticos) == 5
    assert all(col in precog.puntos_criticos for col in ['nombre', 'lat', 'lon', 'riesgo'])
    assert all(0 <= r <= 100 for r in precog.puntos_criticos['riesgo'])
    assert len(precog.triangle) == 3
    assert all(col in precog.triangle for col in ['nombre', 'lat', 'lon'])