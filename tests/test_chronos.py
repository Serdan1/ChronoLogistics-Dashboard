# tests/test_chronos.py
import pytest
from src.chronos import Chronos

@pytest.fixture
def chronos():
    return Chronos()

def test_get_defensa(chronos):
    """Testea que get_defensa devuelve un string no vacío."""
    for estrategia in ["Fortaleza Verde", "Búnker Tecnológico"]:
        defensa = chronos.get_defensa(estrategia)
        assert isinstance(defensa, str)
        assert len(defensa) > 0
        assert estrategia in defensa

def test_imagenes_existen(chronos):
    """Testea que las rutas de las imágenes están definidas."""
    assert "Fortaleza Verde" in chronos.imagenes
    assert "Búnker Tecnológico" in chronos.imagenes
    assert chronos.imagenes["Fortaleza Verde"] == "imagenes/fortaleza_verde.jpg"
    assert chronos.imagenes["Búnker Tecnológico"] == "imagenes/bunker_tecnologico.jpg"

def test_coordenadas_ubicaciones(chronos):
    """Testea que las coordenadas de las ubicaciones son correctas."""
    assert len(chronos.bunker) == 2
    assert len(chronos.fortaleza) == 2
    assert isinstance(chronos.bunker[0], float) and isinstance(chronos.bunker[1], float)
    assert isinstance(chronos.fortaleza[0], float) and isinstance(chronos.fortaleza[1], float)