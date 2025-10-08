class Node:
    def __init__(this, valor):
        this.valor = valor
        this.next = None
        this.prev = None


class DequeTasks:
    """Deque duplamente encadeado, usado para gerenciar as tarefas do zoologico, priorizando as mais urgentes na frente a fim de serem feitas antes"""
    def __init__(this):
        this.head = None
        this.tail = None
        this.size = 0

    def pushFront(this, valor): #insercao na frente do deque (tarefas mais urgentes)
        new = Node(valor) #criacao do novo no
        if this.head is None: #caso o deque esteja vazio
            this.head = new
            this.tail = new
        else: #rearranjo do deque com o novo no na frente
            new.next = this.head
            this.head.prev = new
            this.head = new
        this.size += 1

    def pushBack(this, valor): #insercao atras do deque (tarefas menos urgentes)
        new = Node(valor) #criacao do novo no
        if this.tail is None: #caso o deque esteja vazio
            this.head = new
            this.tail = new
        else: #rearranjo do deque com o novo no atras
            this.tail.next = new
            new.prev = this.tail
            this.tail = new
        this.size += 1

    def popFront(this): #pegando tarefas mais urgentes primeiro
        if this.head is None: #deque vazio
            print("Nenhuma tarefa pendente.")
            return None

        valor = this.head.valor
        this.head = this.head.next

        if this.head is not None: #sobrou ao menos um elemento no deque
            this.head.prev = None
        else: #o ultimo item levou pop
            this.tail = None

        this.size -= 1
        return valor

    def exibir(this):
        print("TAREFAS PENDENTES")
        current = this.head
        while current is not None:
            print(" ->", current.valor)
            current = current.next

#classe para cada animal especifico
class Animal:
    def __init__(this, ID, nome, dieta):
        this.ID = ID
        this.nome = nome
        this.dieta = dieta
        this.estado = "Saudavel"

    def __repr__(this):
        return f"[{this.ID}] {this.nome} | Dieta: {this.dieta} | {this.estado}"

#para ser posto na lista de animais
class NodeAnimal:
    def __init__(this, animal):
        this.valor = animal
        this.next = None


class ListaAnimais: #lista dos animais de um TAD(habitat/recinto)
    def __init__(this):
        this.head = None
        this.size = 0

    def insertOrdenado(this, animal):
        new = NodeAnimal(animal) #criacao do novo no (animal)

        if this.head is None or animal.ID < this.head.valor.ID: #caso nao haja animais ou o ID do novo seja menor que o do head
            new.next = this.head
            this.head = new
        else: #caso o novo ID deva ser posto no meio ou fim da lista (mantendo a ordem crescente)
            current = this.head
            while current.next is not None and current.next.valor.ID < animal.ID: #procurando onde por o novo ID, seja no meio, seja no fim
                current = current.next
            new.next = current.next
            current.next = new
        this.size += 1 #aumentando o tamanho da fila

    def searchBinario(this, IDProcurado):
        """busca binaria (O(log n)) sobre lista temporaria ordenada de animais"""

        animaisTemp = [] #lista temporaria apenas para essa busca binaria
        current = this.head

        while current is not None: #jogando todos os animais, ja ordenados, na lista temporaria
            animaisTemp.append(current.valor)
            current = current.next
        #principio da busca binaria, ''divide-se'' a lista atual conforme a magnitude do ID e pega o lado que precisar ate achar
        currentIndex = 0
        lastIndex = this.size - 1

        while currentIndex <= lastIndex: #percorre a lista ate o fim
            mid = (currentIndex + lastIndex) // 2
            if animaisTemp[mid].ID == IDProcurado:
                return animaisTemp[mid] #achou
            elif animaisTemp[mid].ID < IDProcurado: #ID na direita
                currentIndex = mid + 1
            else: #ID na esquerda
                lastIndex = mid - 1
        return None

    def exibir(this):
        current = this.head
        while current is not None:
            print(" ", current.valor)
            current = current.next

#classe para cada habitat e suas operacoes
class Habitat:
    def __init__(this, nome):
        this.nome = nome
        this.animais = ListaAnimais()

    def addAnimal(this, animal):
        this.animais.insertOrdenado(animal)

    def searchAnimal(this, IDProcurado):
        animal = this.animais.searchBinario(IDProcurado)
        return animal if animal is not None else f"Animal de ID [{IDProcurado}] nao encontrado. Insira um ID valido."

    def exibirAnimais(this):
        print(f"Habitat: {this.nome}")
        this.animais.exibir()

#classe de administracao
class ZooSystem:
    def __init__(this):
        this.head = None
        this.size = 0
        this.tarefas = DequeTasks()

    #montando uma lista no sistema com os habitats
    def addHabitat(this, nome):
        new = Node(Habitat(nome))

        if this.head is None: #primeiro habitat
            this.head = new
        else: #habitats subsequentes
            current = this.head
            while current.next is not None:
                current = current.next
            current.next = new
        this.size += 1

    def getHabitat(this, nome):
        current = this.head
        while current is not None:
            if current.valor.nome == nome:
                return current.valor #retornando o proprio  habitat caso encontre
            current = current.next
        return None

    def exibirHabitats(this):
        current = this.head
        while current is not None:
            current.valor.exibirAnimais()
            print()
            current = current.next


#TESTE
#=================================================================================================================
#iniciando sistema
zoologico = ZooSystem()
#=================================================================================================================
#criacao de habitats
zoologico.addHabitat("Savana dos Leoes")
zoologico.addHabitat("Lago dos Jacares")
#=================================================================================================================
#adicao de animais
zoologico.getHabitat("Savana dos Leoes").addAnimal(Animal(101, "Leao 1", "Carne"))
zoologico.getHabitat("Savana dos Leoes").addAnimal(Animal(103, "Leao 3", "Carne"))
zoologico.getHabitat("Savana dos Leoes").addAnimal(Animal(102, "Leao 2", "Carne"))
zoologico.getHabitat("Lago dos Jacares").addAnimal(Animal(101, "Jacare 1", "Carne, Peixe"))
#=================================================================================================================
#exibicao dos animais de um recinto especifico, ja deverao estar ordenados
print("EXIBICAO DE HABITATS, ESPECIFICO:")
zoologico.getHabitat("Savana dos Leoes").exibirAnimais()
#exibicao de todos os habitats e animais
print("\nEXIBICAO DE HABITATS, TODOS:")
zoologico.exibirHabitats()
#=================================================================================================================
#busca de algum animal por ID
print("\nBUSCAS BINARIAS:")
print("Busca binaria:", zoologico.getHabitat("Savana dos Leoes").searchAnimal(104), "\n") #testando errado
print("Busca binaria:", zoologico.getHabitat("Savana dos Leoes").searchAnimal(103), "\n") #testando certo
#=================================================================================================================
#pondo tarefas de acordo com a prioridade (urgente a frente, nao urgente atras)
zoologico.tarefas.pushFront("Trocar agua da Savana dos Leoes")
zoologico.tarefas.pushFront("Colocar peixes vivos no Lago dos Jacares")
zoologico.tarefas.pushBack("Limpar calcadas")
#=================================================================================================================
#exibindo tarefas pendentes
zoologico.tarefas.exibir()
#realizando uma tarefa (urgentes primeiro)
print("\nRealizando tarefa:", zoologico.tarefas.popFront(), "\n")
#exibindo tarefas pendentes (atualizado)
zoologico.tarefas.exibir()
