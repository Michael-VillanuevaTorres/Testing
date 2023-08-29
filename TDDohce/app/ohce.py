import datetime



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
    

    
    

        
    


