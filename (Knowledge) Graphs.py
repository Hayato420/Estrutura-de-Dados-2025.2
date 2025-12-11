triplosInfo = [ #(sujeito, predicado, objeto)

    # PLANTAS||BENEFICO
    ("Tomate", "ajudaCrescer", "Manjericao"),
    ("Cenoura", "ajudaCrescer", "Alface"),
    ("Rabanete", "ajudaCrescer", "Pepino"),
    ("Alho", "protege", "Roseira"),
    ("Espinafre", "ajudaCrescer", "Cebolinha"),
    ("Repolho", "ajudaCrescer", "Salsinha"),
    ("Milho", "ajudaCrescer", "Abobora"),
    ("Amendoim", "ajudaCrescer", "Quiabo"),

    # PLANTAS||MALEFICO
    ("Batata", "compete", "Tomate"),
    ("Erva Daninha", "compete", "Alface"),
    ("Alecrim", "inibeCrescer", "Feijao"),
    ("Eucalipto", "inibeCrescer", "Repolho"),
    ("Hibisco", "compete", "Cenoura"),
    ("Girassol", "inibeCrescer", "Espinafre"),

    #PLANTAS||REPELENTES//ISCAS
    ("Manjericao", "repele", "Mosca Branca"),
    ("Calendula", "repele", "Nematoide"),
    ("Capuchinha", "isca", "Pulgao"),
    ("Coentro", "repele", "Acaro"),
    ("Hortela", "repele", "Besouro Preto"),
    ("Cebolinha", "repele", "Mosca Branca"),
    ("Salsinha", "isca", "Nematoide"),
    ("Arruda", "repele", "Mariposa Cinzenta"),

    # INSETOS||BENEFICIOS
    ("Joaninha", "come", "Pulgao"),
    ("Joaninha", "come", "Acaro"),
    ("Vespa Parasitica", "come", "Lagarta Verde"),
    ("Aranha de Jardim", "come", "Mosquito da Terra"),
    ("Escaravelho Amarelo", "come", "Besouro Preto"),
    ("Libelula", "come", "Mariposa Cinzenta"),

    # PRAGAS
    ("Pulgao", "ataca", "Rosa"),
    ("Mosca Branca", "ataca", "Tomate"),
    ("Acaro", "ataca", "Pepino"),
    ("Nematoide", "ataca", "Cenoura"),
    ("Lagarta Verde", "ataca", "Repolho"),
    ("Mosquito da Terra", "ataca", "Espinafre"),
    ("Besouro Preto", "ataca", "Abobora"),
    ("Mariposa Cinzenta", "ataca", "Cebolinha"),

    #CONDICOES
    ("Tomate", "prefere", "Sol Pleno"),
    ("Cenoura", "prefere", "Solo Solto"),
    ("Hortela", "prefere", "Solo Umido"),
    ("Alface", "tolera", "Sombra Parcial"),
    ("Alecrim", "exige", "Boa Drenagem"),
    ("Abobora", "prefere", "Sol Pleno"),
    ("Repolho", "tolera", "Clima Frio"),
    ("Espinafre", "prefere", "Clima Frio"),
    ("Cebolinha", "tolera", "Baixa Umidade"),
    ("Salsinha", "exige", "Solo Rico"),
    ("Milho", "prefere", "Solo Rico")
]

nosTipos = {
    #PLANTAS
    "Tomate": "Planta",
    "Cenoura": "Planta",
    "Rabanete": "Planta",
    "Alface": "Planta",
    "Batata": "Planta",
    "Pepino": "Planta",
    "Feijao": "Planta",
    "Roseira": "Planta",
    "Rosa": "Planta",
    "Espinafre": "Planta",
    "Repolho": "Planta",
    "Abobora": "Planta",
    "Cebolinha": "Planta",
    "Salsinha": "Planta",
    "Milho": "Planta",
    "Quiabo": "Planta",
    "Amendoim": "Planta",
    "Hibisco": "Planta",
    "Girassol": "Planta",
    "Eucalipto": "Planta",

    #COMPANHEIRAS
    "Manjericao": "Companheira",
    "Alho": "Companheira",
    "Calendula": "Companheira",
    "Capuchinha": "Companheira Isca",
    "Coentro": "Companheira",
    "Hortela": "Companheira",
    "Arruda": "Companheira",

    #INSETOR||BENEFICO
    "Joaninha": "Inseto Benefico",
    "Vespa Parasitica": "Inseto Benefico",
    "Aranha de Jardim": "Inseto Benefico",
    "Escaravelho Amarelo": "Inseto Benefico",
    "Libelula": "Inseto Benefico",

    #PRAGAS
    "Pulgao": "Praga",
    "Mosca Branca": "Praga",
    "Acaro": "Praga",
    "Nematoide": "Praga",
    "Lagarta Verde": "Praga",
    "Mosquito da Terra": "Praga",
    "Besouro Preto": "Praga",
    "Mariposa Cinzenta": "Praga",
    "Erva Daninha": "Praga",

    #CONDICOES
    "Sol Pleno": "Condicao",
    "Solo Solto": "Condicao",
    "Solo Umido": "Condicao",
    "Sombra Parcial": "Condicao",
    "Boa Drenagem": "Condicao",
    "Clima Frio": "Condicao",
    "Solo Rico": "Condicao",
    "Baixa Umidade": "Condicao"
}


def gerarGrafo(triplos): #pega uma lista de tuplas e monta um grafo

    grafoVizinhanca = {} #dicionario vazio
    for head, relacao, tail in triplos:
        if head not in grafoVizinhanca: #para nos nao adicionados
            grafoVizinhanca[head] = []
        grafoVizinhanca[head].append((relacao, tail)) #adiciona cada relacao a seu no

        if tail not in grafoVizinhanca: #adiciona os nos (tails), mesmo que nao tenham relacao ativa com ninguem (la ele!)
            grafoVizinhanca[tail] = []
            
    return grafoVizinhanca


def contarVizinhos(grafo): #calcula o numero de conexoes por no com base no numero de relacoes no grafo (dicionario)

    vizinhosPorNos = {} #dicionario de nos : numero de conexoes

    for no in grafo:
        vizinhos = grafo[no]
        conexoesNo = len(vizinhos) #ele conta quantas tuplas (relacoes) existem na valor (lista)
        vizinhosPorNos[no] = conexoesNo

    return vizinhosPorNos


from collections import deque
def menorCaminho(grafo, noInicial, noAlvo):
    #como as arestas tem mesmo peso(nao-ponderadas), a distancia e determinada pelo numero de arestas, ou seja, sempre acha o menor caminho
    caminho = {noInicial: [noInicial]}
    #deque facilita implementacao
    fila = deque([noInicial])

    while fila: #enquanto houver possibilidades
        noAtual = fila.popleft() #pega no mais antigo

        if noAtual == noAlvo:
            return caminho[noAtual]

        for relacao, vizinho in grafo.get(noAtual, []): #"relacao" apenas pela forma do dicionario(grafo), nao sera usado

            if vizinho not in caminho: #se nao passou ainda pelo no
                
                #cria uma copia para cada adicao
                oldCaminho = caminho[noAtual]
                newCaminho = oldCaminho + [vizinho]
                
               
                caminho[vizinho] = newCaminho
                fila.append(vizinho)

    #alvo nao encontrado
    return "Caminho nao encontrado."


def addRelacao(grafo, sujeito, predicado, objeto): #so adiciona uma nova tupla no dicionario com values de lista

    if sujeito not in grafo: #novo no (cabeca)
        grafo[sujeito] = []

    if objeto not in grafo: #novo no (cauda)
        grafo[objeto] = []

    new_triplo = (predicado, objeto) #nova relacao adicionada ao value (lista)
    if new_triplo not in grafo[sujeito]:
        grafo[sujeito].append(new_triplo)
        print(f"Novo relacionamento adicionado: ({sujeito}, {predicado}, {objeto})")
    else:
        print(f"Esse relacionamento ja existe.")


def removerRelacao(grafo, sujeito, predicado, objeto): #removendo uma tupla da lista 

    if sujeito not in grafo:
        print(f"No inicial nao encontrado, confira a digitacao.")
        return False
        
    relacaoARemover = (predicado, objeto)
    if relacaoARemover in grafo[sujeito]:
        grafo[sujeito].remove(relacaoARemover)
        print(f"O seguinte relacionamento foi removido: ({sujeito}, {predicado}, {objeto})")    
        return True
    else:
        print(f"Relacionamento nao encontrado para {sujeito}, confira a digitacao.")
        return False
    

def consultarRelacoesNo(grafo, noConsultado): #so puxa as relacoes de um no
    if noConsultado in grafo:
        relacoes = grafo[noConsultado]
        
        if not relacoes:
            return f"No encontrado, porem sem relacoes."
        
        print(f"\nRelacoes de {noConsultado} encontradas:")
        for relacao, vizinho in relacoes:
            print(f"RELACAO: {relacao} | ALVO: {vizinho}")
        return True

    else:
        print(f"No nao encontrado, confira a digitacao.")
        return False

def consultarTipoNo(tiposDeNos, noConsultado): #so consulta o tipo do no

    if noConsultado in tiposDeNos:
        tipo = tiposDeNos[noConsultado]
        return f"Tipo semantico: {tipo}."
    else:
        return f"Tipo nao definido."


def compatibilidade(grafo, noVizinho, condicoesPrincipal):
    #sem requisicoes, qualquer coisa serve
    if not condicoesPrincipal:
        return True

    condicoesVizinho = {
        condicoes for relac, condicoes in grafo.get(noVizinho, [])
        if relac in ["prefere", "exige", "tolera"]
    }
    #vizinhos sem requisicoes, ou seja, se adapta a qualquer coisa
    if not condicoesVizinho:
        return True
    #se qualquer condicao do vizinho for compativel com do principal, retorna true
    if condicoesVizinho & condicoesPrincipal:
        return True

    #nao compativeis
    return False


def gerarComunidade(grafo, nosTipos, noPrincipal):
    tipoMain = nosTipos.get(noPrincipal)
    if tipoMain is None:
        return f"Tipo de no nao reconhecido, confira a digitacao."
    if tipoMain not in ["Planta", "Companheira"]:
        return f"A analise de Comunidade so serve para Plantas ou Companheiras. (No '{noPrincipal}' é '{tipoMain}')."

    relacoesPositivas = [
        "ajudaCrescer", "repele", "isca", "protege", "come"
    ]
    
    comunidade = {
        "No Principal": noPrincipal,
        "Condicoes exigidas": [],
        "Companheiros compativeis": [],
    }
    
    if noPrincipal not in grafo:
        return f"Esse no nao se encontra no grafo."

    condicoesPrincipal = set()#evita duplicatas e acelera a busca
    #selecao das condicoes do no principal com base na relacao
    for relation, vizinho in grafo.get(noPrincipal, []):
        if relation in ["prefere", "exige", "tolera"]:
            condicoesPrincipal.add(vizinho)
            comunidade["Condicoes exigidas"].append({"No": vizinho, "Relacao": relation})
    
    if not condicoesPrincipal:
        print(f"Aviso: {noPrincipal} sem condicoes definidas. Comunidade sera criada sem filtro de condicoes.")

    for relation, vizinho in grafo.get(noPrincipal, []): #para os vizinhos do principal
        if relation in relacoesPositivas: #se relacao positiva
            if compatibilidade(grafo, vizinho, condicoesPrincipal) or not condicoesPrincipal: #se compativeis
                 comunidade["Companheiros compativeis"].append({ #poe na comunidade
                    "No": vizinho,
                    "Relacao": relation,
                    "Tipo": f"{noPrincipal} atua sobre"
                })

    #agora o caminho inverso, percorrendo todo o grafo (outras plantas que beneficiam o no principal)
    for head, relacoes in grafo.items():
        if head == noPrincipal: continue #se for o no analisado principal, pula
        
        for relation, tail in relacoes:
            if tail == noPrincipal and relation in relacoesPositivas: #se o objeto for o no principal e a relacao benefica
                if compatibilidade(grafo, head, condicoesPrincipal) or not condicoesPrincipal: #testa compatibilidade, se for compativel, poe na comunidade
                    comunidade["Companheiros compativeis"].append({
                        "No": head,
                        "Relacao": relation,
                        "Tipo": f"{noPrincipal} sofre acao"
                    })

    return comunidade

#FUNCAO APENAS PARA IMPRIMIR UMA SAIDA LIMPA
def formatarComunidade(comunidade):
    if isinstance(comunidade, str):
        return comunidade

    saida = []
    saida.append(f"NO PRINCIPAL: {comunidade['No Principal']}\n")

    saida.append("CONDICOES EXIGIDAS:")
    if comunidade["Condicoes exigidas"]:
        for item in comunidade["Condicoes exigidas"]:
            saida.append(f"  - {item['No']} ({item['Relacao']})")
    else:
        saida.append("  Nenhuma")

    saida.append("\nCOMPANHEIROS COMPATIVEIS:")
    if comunidade["Companheiros compativeis"]:
        for item in comunidade["Companheiros compativeis"]:
            saida.append(f"  - {item['No']} ({item['Relacao']}) [{item['Tipo']}]")
    else:
        saida.append("  Nenhum")

    return "\n".join(saida)


#=========TESTES==============================
if __name__ == "__main__":
    grafo = gerarGrafo(triplosInfo)
    print("\nTESTE 1: Comunidade de Tomate")
    comunidade = gerarComunidade(grafo, nosTipos, "Tomate")
    print(formatarComunidade(comunidade))

    print("\nTESTE 2: Comunidade de Alface")
    comunidade = gerarComunidade(grafo, nosTipos, "Alface")
    print(formatarComunidade(comunidade))

    print("\nTESTE 3: Caminho minimo entre Manjericao e Tomate")
    caminho = menorCaminho(grafo, "Manjericao", "Tomate")
    print("Caminho encontrado:", caminho)

    print("\nTESTE 4: Caminho minimo entre Joaninha e Rosa")
    caminho = menorCaminho(grafo, "Joaninha", "Rosa")
    print("Caminho encontrado:", caminho)

    print("\nTESTE 5: Adicionar, testar e remover relacao")
    print("Adicionando relacao: (Cenoura, protege, Alface)")
    addRelacao(grafo, "Cenoura", "protege", "Alface")
    consultarRelacoesNo(grafo, "Cenoura")

    print()
    print("Checando compatibilidade entre Cenoura e Alface:")
    cond_cenoura = {"Solo Solto"}
    print("Compatibilidade:", compatibilidade(grafo, "Alface", cond_cenoura))
    print()

    print("Removendo relacao adicionada:")
    removerRelacao(grafo, "Cenoura", "protege", "Alface")
    consultarRelacoesNo(grafo, "Cenoura")

    print("\nTESTE 6: Consultar no e relacionamentos de Tomate (Direcional)")
    consultarRelacoesNo(grafo, "Tomate")
    print(consultarTipoNo(nosTipos, "Tomate"))