def funcao1(N):
  for number in range(int(N)):
    if number % 5 == 0 and number % 2 != 0:
      print(number)
      
      def funcao2():
  nume_entradas = int(input("Digite o numero de entradas: "))
  lista = []
  i = 0
  while i < nume_entradas:
    lista.append(input("Adicione na lista por aqui: "))
    i += 1
  return lista


print (funcao2())
def funcao3(lista):
  os_numeros_maiores_que_5 = 0
  for elemento in lista:
    if elemento > 5:
      os_numeros_maiores_que_5 += 1
  return os_numeros_maiores_que_5

#Adicione na lista por aqui:
lista = []
print (funcao3(lista))
def funcao4():
  opcao = input("Insira aqui a sua opção:")
  while opcao != 'z':
    if opcao == 'a':
      print("PSG")
    elif opcao == 'b':
      print("BAYERN")
    elif opcao == 'd':
      break
    opcao = input()
