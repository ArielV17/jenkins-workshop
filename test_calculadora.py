from calculadora import Calculadora


def test_sumar():
    calculadora = Calculadora()
    resultado = calculadora.sumar(2, 3)

    assert resultado == 5
