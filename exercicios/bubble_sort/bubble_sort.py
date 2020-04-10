# Algoritmo do artigo do wikipedia em https://pt.wikipedia.org/wiki/Bubble_sort
#
# procedure bubbleSort( A : lista de itens ordenaveis ) defined as:
#   do
#     trocado := false
#     for each i in 0 to length( A ) - 2 do:
#       // verificar se os elementos estão na ordem certa
#       if A[ i ] > A[ i + 1 ] then
#         // trocar elementos de lugar
#         trocar( A[ i ], A[ i + 1 ] )
#         trocado := true
#       end if
#     end for
#   // enquanto houver elementos sendo reordenados.
#   while trocado
# end procedure

lista = [ 30, 3, 23, 324, 42, 234, 2, 505, 234 ]
print('Antes: ', lista)
trocado = True ### para entrar no while abaixo pela primeira vez
while trocado:
    # enquanto tiver havido alguma troca de elementos
    trocado = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            # os elementos estão fora de ordem
            tmp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = tmp
            trocado = True
print('Depois: ', lista)

