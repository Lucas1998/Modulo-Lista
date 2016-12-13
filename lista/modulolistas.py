 
'''
Created on 30 nov. 2016

@author: usuario
'''
def crearLista(lista): 
    '''
        voy a hacer una lista donde incluya una serie de elemenetos
    '''
    for indice in range(5):
        
        try:
            elemento=int(input("introducir un elemento"))
            lista.append(elemento)
        except:
             elemento=input("introducir elemento")
             lista.append(elemento)
        
def imprimirLista (lista):
   '''
         voy a imprimir una lista donde incluya una serie de elemenetos
        
   '''
   try:
        for indice in lista:
            print(indice)
   except:
        print("alerta de bomba")    
def separarLista (lista):
   '''
        voy a separar una lista donde incluya una serie de elemenetos
        
   '''
   id_paciente=lista[0] 
   fase_ensayo=lista[1]
   serie_temperaturas=lista[2:]
   return id_paciente, fase_ensayo, serie_temperaturas
if __name__=="__main__":
    l=[]
    crearLista(l)
    imprimirLista(l)
    id_p, fase_e, s_temp=separarLista(l)
    print(id_p,fase_e,s_temp)
    

    