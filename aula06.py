#enviar um email com detalhes da compra online (maximo 3 tentativas)
#para compras confirmadas
'''
compra_confirmanda = False
dados_compra = 'Compra no valor de R$ 12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmanda:
        print(dados_compra)
        print('detalhes enviado para seu email.')
        break
else:
    print('falha na compra.')
'''
"""
#for loop - Nest loops (laços aninhados)
#outer loop
#inner loop

for num1 in range(1,6):
    print('produto'+str(num1))
    for num2 in range(5):
        print(num1,num2)
 """
'''
 #imprimindo uma matriz de 2 linhas
def main():
    a = [1 , 2 , 3 , 4 , 5] #criando uma lista
    b = a #atribuindo a lista "a"  a váriavel "b"

    b[1] = 7 #modificando o (indice 1) da lista para o numero 7

    print("a = ", a) #imprimindo a lista "a"
    print("b = ", b) #imprimindo a lista "b"

main() #chamando a função main do inicio do código

'''
'''
palavra = "FANTASTICO"

for space in palavra:
    print(f' {space}', end='')
'''

#operador ternario
"""
idade = 13

if idade >= 16:
    resultado = print('voto permitido')
else:
    resultado = print ('voto não permitido')
"""

resultado ='voto permitido' if idade >= 16 else 'voto não permitido'