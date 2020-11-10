#importa a biblioteca random
from random import randint as rand

#utilizando da API padrão seleciona o elemento html cujo id é "botao"
botao = document.getElementById("botao")

def mudar():
    """ Altera o background da página aleatoriamente """

    #utilizando da API padrão seleciona o corpo da página e acessa
    #o atributo style(que seria o css do elemento) alterando seu valor
    #para background-color:rgb(), o rgb recebe 3 valores entre 0 e 255
    #por isso geramos 3 numeros aleatorios e passamos para ele
    document.body.style = "background-color:rgb({},{},{})".format(rand(0,255),rand(0,255),rand(0,255))

#por sim, utilizando a API padrão atrelamos um evento de clique para nosso botao
#claro, chamando a função mudar
botao.addEventListener("click",mudar)
