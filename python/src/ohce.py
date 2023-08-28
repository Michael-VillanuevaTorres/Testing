import datetime


def ohce ( frase ):

    nombre= "Sin nombre"
    if frase.split()[0]!=frase:
        nombre = frase.split()[1]

    hora_actual = datetime.datetime.now().time()
    if hora_actual >= datetime.time(6) and hora_actual < datetime.time(12):
        return "Buenos días "+nombre+" !"
    elif hora_actual >= datetime.time(12) and hora_actual < datetime.time(20):
        return "Buenas tardes "+nombre+" !"
    else:
        return "¡Buenas noches "+nombre+" !"
    
while(True):
    entrada = input("")

    if entrada == "Stop!":
        print("Deteniendo el bucle...")
        break  
    print(entrada[0])
    if(entrada.split()[0]=="ohce"):
        print("sds")
        print(ohce(entrada))
        continue
        
    


