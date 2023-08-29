import datetime


def palabra_al_reves(palabra):
    palabra_reves = palabra[::-1]
    return palabra_reves



def ohce ( frase ):

    nombre= "Sin nombre"
    if frase.split()[0]!=frase and frase.split()[0]=="ohce":
        nombre = frase.split()[1]
        hora_actual = datetime.datetime.now().time()
        if hora_actual >= datetime.time(6) and hora_actual < datetime.time(12):
            return "Buenos días "+nombre+" !"
        elif hora_actual >= datetime.time(12) and hora_actual < datetime.time(20):
            return "Buenas tardes "+nombre+" !"
        else:
            return "¡Buenas noches "+nombre+" !"
    

    if(palabra_al_reves(frase)==frase):
        return(palabra_al_reves(frase)+'\n'+"¡Bonita palabra!")
    
    if(frase==""):
        return ("palabra vacia")
    
   
    
    return(palabra_al_reves(frase))
    

        
    


