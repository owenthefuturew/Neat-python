numofinputs = 3
numofoutputs = 1

activationfunctioninput = 'sigmoid'
activationfunctionmain = 'sigmoid'
activationfunctionoutinput = 'sigmoid'

weightminmax = [-2,2]

c1 = 1
c2 = 2 
c3 = 3

inherit_desabled = 0.75
added_connection_chace = 0.3
mutitate_connection_chace = 0.3
weight_prebutered_chance = 0.8
weight_prebuted_added = 0.2
weight_random_chance = 0.1
n = 1

populationsize = 10
closeness = 3

totalnodegenes = 4
totalconnectiongenes = 4
allconnectiongenes = [{'from':0,'to':3,'inno':0},{'from':1,'to':3,'inno':1},{'from':2,'to':3,'inno':2}]
allsplitnodes = []

def addaconnection(net):
    global totalconnectiongenes, allconnectiongenes
    print(totalconnectiongenes,'connection')
    ret = net.addconnection(totalconnectiongenes,allconnectiongenes)
    if(ret == 'impossible'):
        mutitateaconnection(net)
    elif(ret not in allconnectiongenes):
        allconnectiongenes.append(ret)
        totalconnectiongenes += 1
        
def mutitateaconnection(net):
    global totalconnectiongenes, totalnodegenes, allsplitnodes
    ret = net.mutitateconnection(totalnodegenes,totalconnectiongenes,allsplitnodes)
    if(ret == None):
        addaconnection(net)
    elif(ret not in allsplitnodes):
        allsplitnodes.append(ret)
        totalconnectiongenes += 2
        totalnodegenes += 1
