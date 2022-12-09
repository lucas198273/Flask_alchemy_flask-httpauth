from calculadora  import Calculadora
from add import AddOperation
from sub import SubOperation

calc = Calculadora(AddOperation(), SubOperation())
ops1 = calc.add(2,85,True)
ops2 = calc.sub(5,2,True)
print('==='*100)

print(ops1)                             ### Biblioteca utilizada para fazer o teste unitario sera o  pyTest
print(ops2)