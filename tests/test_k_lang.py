# tests/test_k_lang.py
import pytest
from src.k_lang import KLang

@pytest.fixture
def klang():
    return KLang()

def test_get_protocolo_activo(klang):
    """Testea que get_protocolo_activo devuelve protocolo, disparador y acciones."""
    protocolo, disparador, acciones = klang.get_protocolo_activo(50, 10)
    assert protocolo == "RENACIMIENTO"
    assert isinstance(disparador, str)
    assert isinstance(acciones, list)
    assert len(acciones) > 0

def test_protocolos_umbrales(klang):
    """Testea que los umbrales activan el protocolo correcto."""
    assert klang.get_protocolo_activo(95, 60)[0] == "CÓDIGO ROJO"
    assert klang.get_protocolo_activo(70, 30)[0] == "VÍSPERA"
    assert klang.get_protocolo_activo(40, 10)[0] == "RENACIMIENTO"

def test_protocolos_definidos(klang):
    """Testea que todos los protocolos están definidos con disparador y acciones."""
    for protocolo in ["VÍSPERA", "CÓDIGO ROJO", "RENACIMIENTO"]:
        assert protocolo in klang.protocolos
        assert "disparador" in klang.protocolos[protocolo]
        assert "acciones" in klang.protocolos[protocolo]
        assert isinstance(klang.protocolos[protocolo]["acciones"], list)
        