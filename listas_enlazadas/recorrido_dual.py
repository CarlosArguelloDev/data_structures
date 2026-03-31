from lista_enlazada import ListaEnlazada

l1 = ListaEnlazada()
l2 = ListaEnlazada()
l_res = ListaEnlazada()

l1.agregar_final(4)
l1.agregar_final(2)
l1.agregar_final(3)

l2.agregar_final(6)
l2.agregar_final(7)

carry = 0
actual1 = l1.cabeza
actual2 = l2.cabeza

while actual1 or actual2 or carry:
    val1 = actual1.dato if actual1 else 0
    val2 = actual2.dato if actual2 else 0

    res = val1 + val2 + carry
    digito = res % 10
    carry = res // 10

    l_res.agregar_final(digito)
    
    if actual1:
        actual1 = actual1.siguiente
    if actual2:
        actual2 = actual2.siguiente

l_res.recorrido_seguro()







