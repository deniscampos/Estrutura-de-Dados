from operator import itemgetter


def enumeracoes(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinacoes(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutacoes(items):
    return combinacoes(items, len(items))


#print ('Permutacoes')
for p in permutacoes(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
    #print (p)
    pass

#print ('Enumeracoes')
for p in enumeracoes(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
    #print (p)
    pass





'''
Saber se é possível casar as quatro damas com os atuais cavaleiros, seguindo suas preferências pessoais. 
Damas “encalhadas” são fofoqueiras e um sério perigo para o sigilo na corte. É uma tarefa difícil, 
pois existem alguns cavaleiros que são muito disputados e outros que não são atraentes por terem perdido 
alguma parte do corpo nas várias batalhas (olho, perna, braço, etc.) além daqueles que secretamente 
estão comprometidos com damas de outros reinos.
'''
def possivel_casar():
    arquivo = open('casamento.txt', 'r')
    lista = arquivo.readlines()
    preferencias = [p.replace('\n', '') and p.split() for p in lista] #lista com cada linha do arquivo
    arquivo.close() #fechar o arquivo aberto

    pretendentes = {p[0] : p[1:] for p in preferencias} #dicionário com os favoritos de cada dama


    cavaleiros = ['Adriano', 'Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']
    damas = ['Jessica', 'Fernanda', 'Pamela', 'Renata']

    casados = {cavaleiro : 0 for cavaleiro in cavaleiros} #dicionário para saber se os cavaleiros já estão casados
    casadas = {dama : 0 for dama in damas} #dicionário para saber se as damas já estão casadas

    solteiras = '' #damas solteiras

    #Caso não tenha pretendente adiciona a dama em solteiras
    for dama in damas:
        if len(pretendentes[dama]) < 1:
            solteiras += dama + ' '

    #caso todas tenham pretendentes, verifica se é possível casar todas
    if not solteiras:
        for dama in damas: #lista utilizada para serguir prioridade
            for cavaleiro in cavaleiros: #lista utilizada para serguir prioridade
                if cavaleiro in pretendentes[dama] and casados[cavaleiro] == 0:
                    casados[cavaleiro] = dama
                    casadas[dama] = cavaleiro
                    break
            if casadas[dama] == 0:
                solteiras += dama + ' '

    #caso tenha alguma solteira, retorna dizendo que é impossível casar e os casais
    if solteiras:
        return 'Impossível casar %s' %solteiras
    
    casamentos = ''
    for dama in casadas:
        casamentos += dama + " e " + casadas[dama] + "  |  "

    return 'Possível casar: \n%s' %(casamentos[ : -3]) 




'''
Arrumar uma disposição dos sete cavaleiros em torno da Távola Redonda de tal modo que não briguem.
Os cavaleiros amam a guerra e caso a pessoa do lado não seja algum grande amigo, 
ela será desafiada para um duelo. Deste modo morreram muitos cavaleiros nos últimos anos, 
fragilizando o poderio do reinado.
'''
def tavola_redonda():
    arquivo = open('cavaleiros.txt', 'r')
    lista = arquivo.readlines()
    cavaleiros = [c.replace('\n', '') and c.split() for c in lista] #lista com cada linha do arquivo
    arquivo.close()

    amigos = {a[0] : a[1:] for a in cavaleiros} #dicionário com os amigos de cada cavaleiro
  
    combinacoes = []
    sentados = []
    opcoes = ''

    #Caso um dos cavaleiros só tenha 1 amigo ou nenhum, não é possível sentá-los à mesa
    for cavaleiro in amigos:
        if len(amigos[cavaleiro]) < 2:
            return "Não é possível arrumar a mesa para os 7 cavaleiros"


    #Gera todas combinações possíveis dos cavaleiros
    for p in permutacoes(['Adriano', 'Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
        if(p[0] == 'Adriano'):
            combinacoes.append(p) #Guarda apenas as combinações que começam com "Adriano", pois as demais são repetidas em ordem diferente
        else:
            break

    #Verificando se os cavaleiros ao lado nas combinações geradas são amigos
    for combinacao in combinacoes:
        todos_amigos = True

        for i in range(7):
            if combinacao[i] not in amigos[combinacao[(i + 1) % 7]]: #Verifica se o cavaleiro é amigo do seguinte
                todos_amigos = False
                break

        if todos_amigos:
            sentados.append(combinacao)

    #Caso nenhuma das combinações formem a mesa com todos cavaleiros amigos, retorna que não é possível
    if not sentados:
        return "Não é possível arrumar a mesa para os 7 cavaleiros"

    #Apenas formatando o retorno
    for opcao in sentados[ : int(len(sentados) / 2)]:
        opcoes += "\nOpção " + str(sentados.index(opcao)) + ": "
        for cavaleiro in opcao:
            opcoes += cavaleiro
            if(cavaleiro != opcao[-1]):
                opcoes += " - "


    return 'Possível sentar os cavaleiros de %d modo(s): %s' %(int(len(sentados) / 2), opcoes)


print(possivel_casar())
print("\n")
print(tavola_redonda())


