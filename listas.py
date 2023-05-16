#squares = [1,4,9,16,25]
# print(squares) [1, 4, 9, 16, 25]

# #indexing returns the item
# print(squares[0]) #1
#print(squares[-3:]) #[9, 16, 25] slicing returns a new list

#listas são mutáveis

# cubes = [1,8,27,65,125]
#cubes[3] = 64
#print(cubes) #[1, 8, 27, 64, 125]

#add itens no final da lista

# cubes.append(216)
# print(cubes) #[1, 8, 27, 64, 125, 216]

#Atribuição a fatias também é possível, e isso pode até alterar o tamanho da lista ou remover todos os itens dela:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#alterar a lista
# letters[2:5] = ['C','D','E']
#print(letters) #['a', 'b', 'C', 'D', 'E', 'f', 'g']

#remover os itens

# letters[2:5] = []
# print(letters) #['a', 'b', 'f', 'g']

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

    print(b)



