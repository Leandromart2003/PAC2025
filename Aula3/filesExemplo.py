import os as PCOS
filename="./Aula3/PastaFiles/pessoas.txt"
nomes=[]
moradas=[]
Texto="Ola Mundo"
if PCOS.path.exists(filename):
   with open(filename,'r',encoding='utf-8') as manipfile:
            Texto=manipfile.read()
while True:
   print("1- Insere")
   print("2- lista")
   print("3- Salva")
   print("4- Sair")
   opc= input("intrud Opção")
   match opc:
      case "1":
         nomes.append(input("insert nome"))
         moradas.append(input("insert nome"))
      case "2":
         for nome in nomes:
             print(nome)
         for morada in moradas:
             print(morada)
      case "3":
            print("Salvo")
            with open(filename,'w',encoding='utf-8') as manipfile:
               manipfile.write(Texto)
      case "4":
            print("Sair")
            with open(filename,'w',encoding='utf-8') as manipfile:
               manipfile.write(Texto)
            break