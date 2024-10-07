# Faça um programa que se o usuário inserir 
#1 = ele escolhe a classe Bárbara
#2 = ele escolhe a classe a clase mago 
#3 = ele escolhe a classe arqueiro

numero = int(input(" \n 1 = ele escolhe a classe Bárbara \n 2 = ele escolhe a classe a clase mago \n 3 = ele escolhe a classe arqueiro \n Qual classe voçe deseja? "))

if((numero) == 1):
    Escolha = "Bárbaro"
elif(numero == 2):
    print("A sua classe é mago ")
    Escolha = "Mago"
elif (numero == 3):
    Escolha = "Arqueiro"
    print("A sua classe é arqueiro")

else:
    print("Classe inválida, escolha novamente a sua classe!")

#Após a escolha da classe pergunte se ele utilizará um equipamento de curto ou longo alcance.
#Imprima a classe + equipamento ao final
    
equipamento = int(input("\n 1 = Equipamento de curto alcance \n 2 = Equipamento de longo alcance \n"))

if(equipamento == 1):
    Arma = "Curto Alcance"
elif (equipamento == 2):
    Arma = "Longo Alcance"
    print(f"O seu equipamento é de longo alcance e a sua classe é {numero}")
else:
    print(" ")
print(f"A sua classe é: {Escolha} e o seu equipamento é: {Arma}")