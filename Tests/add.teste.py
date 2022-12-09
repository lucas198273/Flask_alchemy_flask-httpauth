from .add import AddOperation

def test_soma():
    addOperation = AddOperation()

    resultado = addOperation.soma(45,15)

    assert resultado == 45 + 15