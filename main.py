while True:
    print('''
          1) Ejercicio 1
          2) Ejercicio 2
          3) Ejercicio 3
          4) Ejercicio 4
          5) Ejercicio 5
          6) Salir  
''')
    opcion = input("Ingrese el numero de ejercicio que quiere ejecutar: ")
    
    match opcion:
        case "1":
        
            while True:
                nombre = input("Ingrese el nombre del cliente: ")
                if nombre.isalpha():
                    break
                else:
                    print("Solo se aceptan letras, sin espacios ni numeros")
                
                

            while True:
                cantidad_de_productos = input("Ingrese la cantidad de productos que quiere comprar: ")
                if cantidad_de_productos.isdigit() and int(cantidad_de_productos) > 0:
                    cantidad_de_productos = int(cantidad_de_productos)
                    break
                else:
                    print("Ingrese un numero entero mayor a cero")
                    


            total_sin_descuento = 0
            total_con_descuento = 0


            print(f"Cliente: {nombre}")
            print(f"Cantidad de productos: {cantidad_de_productos}")


            for i in range(1, cantidad_de_productos + 1):

                while True:
                    precio = input(f"Producto {i} - Precio: ")
                    if precio.isdigit() and int(precio) > 0:
                        precio = int(precio)
                        break
                    else:
                        print("solo se aceptan numeros enteros mayores a cero")

            
            
                while True:
                    descuento = input("Descuento (S/N): ").lower()
                    if descuento in ("s", "n"):
                        break
                    else:
                        print("Solo se acepta S o N")


                
                print(f"Producto {i} - Precio: {precio} Descuento (S/N): {descuento}")

                total_sin_descuento += precio

                if descuento == "s":
                    precio_final = precio * 0.9
                else:
                    precio_final = precio

                total_con_descuento += precio_final


            ahorro = total_sin_descuento - total_con_descuento
            promedio = total_con_descuento / cantidad_de_productos


            print(" ")
            print(f"Total sin descuentos: ${total_sin_descuento}")
            print(f"Total con descuentos: ${total_con_descuento:.2f}")
            print(f"Ahorro: ${ahorro:.2f}")
            print(f"Promedio por producto: ${promedio:.2f}")

        case "2":

            usuario_correcto = "alumno"
            clave_correcta = "python123"
            acceso = False


            for intento in range(3):
                
                usuario = input("Intento " + str(intento + 1) + "/3 - Usuario: ")
                clave = input("Clave: ")
                

                if usuario == usuario_correcto and clave == clave_correcta:
                    acceso = True
                    print("Acceso concedido.")
                    break
                else:
                    print("Error: credenciales inválidas.")
                    



            if acceso == False:
                print("Cuenta bloqueada.")


            if acceso == True:

                while True:
                    
                    print('''
1) Estado  2) cambiar clave  3) mensaje  4) salir''')
                    opcion = input("Opción: ")

                
                    if opcion.isdigit() == False:
                        print("Error: ingrese un número válido.")
                        continue

                    opcion = int(opcion)

                
                    if opcion < 1 or opcion > 4:
                        print("Error: opción fuera de rango.")
                        continue


                    if opcion == 1:
                        print("Inscripto.")

                    
                    elif opcion == 2:
                        nueva_clave = input("Nueva clave: ")


                        if len(nueva_clave) < 6:
                            print("Error: mínimo 6 caracteres.")
                            
                        else:
                            confirmacion = input("Confirmacion de la clave: ")

                            if nueva_clave == confirmacion:
                                clave_correcta = nueva_clave
                                print("Clave cambiada")
                                
                            else:
                                print("Error: no coinciden las claves")

                    
                    elif opcion == 3:
                        print("Dale loco que podes")

                
                    elif opcion == 4:
                        print("se cerro la sesion")
                        break
                    
        case "3":
                      
            lunes1 = ""
            lunes2 = ""
            lunes3 = ""
            lunes4 = ""
            martes1 = ""
            martes2 = ""
            martes3 = "" 

            while True:            
                nombre_operador = input("Ingrese el nombre del operador: ")
                print(" ")
                if nombre_operador.isalpha():
                    break
                else:
                    print("Use solamente letras")
                    print(" ")

            #Menu del inicio          
            while True:
                print("""1. Reservar turno
2. Cancelar turno 
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
""")
                opcion = input("opcion: ")
                print(" ")

                if opcion.isdigit() == False:
                    print("solo se pueden usar numeros del 1 al 5")
                    print(" ")
                    continue

                opcion = int(opcion)

                if opcion < 1 and opcion > 5:
                    print("solo se pueden usar numeros del 1 al 5")
                    print(" ")
                    continue
                
                #agendar turnos
                if opcion == 1:
                    dia = input("1 = lunes, 2 = martes: ")
                    print(" ")

                    if dia.isdigit() == False:
                        print("Solo puede ingresar el numero 1 o 2")
                        print(" ")
                        continue
                    
                    dia = int(dia)

                    if dia < 1 or dia > 2:
                        print("Solo se puede ingresar el numero 1 o 2")
                        print(" ")
                        continue
                    
                    nombre = input("Ingrese el nombre del paciente: ").lower()
                    print(" ")
                    if nombre.isalpha() == False:
                        print("solo se pueden usar letras, sin simbolos ni espacios")
                        print(" ")
                        continue
                    
                    
                    if dia == 1:
                        if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                            print("el paciente ya tiene un turno")
                            print(" ")

                        else:
                            if lunes1 == "":
                                lunes1 = nombre
                                print("Ahora tiene reservado el primer turno del dia lunes, muchas gracias")
                                print(" ")
                            elif lunes2 == "":
                                lunes2 = nombre
                                print("Ahora tiene reservado el segundo turno del dia lunes, muchas gracias") 
                                print(" ")  
                            elif lunes3 == "":
                                lunes3 = nombre
                                print("Ahora tiene reservado el tercer turno del dia lunes, muchas gracias") 
                                print(" ")  
                            elif lunes4 == "":
                                lunes4 = nombre
                                print("Ahora tiene reservado el cuarto turno del dia lunes, muchas gracias")
                                print(" ")
                            else:
                                print("No hay mas turnos disponibles en este dia")
                                print(" ")

                    elif dia == 2:
                        if nombre == martes1 or nombre == martes2 or nombre == martes3:
                            print("El paciente ya tiene un turno el dia martes")
                            print(" ")
                        else:
                            if martes1 == "":
                                martes1 = nombre
                                print("Ya tiene reservado el primer turno del dia martes, muchas gracias")
                                print(" ")
                            elif martes2 == "":
                                martes2 = nombre
                                print("Ya tiene reservado el segundo turno del dia martes, muchas gracias")
                                print(" ")  
                            elif martes3 == "":
                                martes3 = nombre
                                print("Ya tiene reservado el tercer turno del dia martes, muchas gracias")
                                print(" ")
                            else:
                                print("No hay mas turnos disponibles en este dia")
                                print(" ")

                #Cancelar turno 
                elif opcion == 2:

                    print(" ")
                    dia = input("Día (1=Lunes, 2=Martes): ")
                    print(" ")

                    if dia.isdigit() == False:
                        print("Solo puede ingresar el numero 1 o 2")
                        print(" ")
                        continue
                    
                    dia = int(dia)

                    if dia < 1 or dia > 2:
                        print("Solo se puede ingresar el numero 1 o 2")
                        print(" ")
                        continue
                    
                    nombre = input("Ingrese el nombre del paciente: ").lower()
                    print(" ")
                    if nombre.isalpha() == False:
                        print("use solo letras, sin numeros ni espacios")
                        print(" ")
                        continue
                    
                    if dia == 1:

                        if lunes1 == nombre:
                            lunes1 = ""
                            print("El turno ha sido cancelado")
                            print(" ")
                        elif lunes2 == nombre:
                            lunes2 = ""
                            print("El turno ha sido cancelado.")
                            print(" ")
                        elif lunes3 == nombre:
                            lunes3 = ""
                            print("El turno ha sido cancelado")
                            print(" ")
                        elif lunes4 == nombre:
                            lunes4 = ""
                            print("El turno ha sido cancelado")
                            print(" ")
                        else:
                            print("No se ha encontrado al paciente")
                            print(" ")

                    elif dia == 2:
                        if martes1 == nombre:
                            martes1 = ""
                            print("El turno ha sido cancelado")
                            print(" ")
                        elif martes2 == nombre:
                            martes2 = ""
                            print("El turno ha sido cancelado")
                            print(" ")
                        elif martes3 == nombre:
                            martes3 = ""
                            print("El turno ha sido cancelado")
                            print(" ")
                        else:
                            print("No se ha encontrado al paciente")
                            print(" ")

                #Agenda
                elif opcion == 3:
                    print(" ")
                    dia = input("Día (1=Lunes, 2=Martes): ")

                    if dia.isdigit() == False:
                        print("Solo puede ingresar el numero 1 o 2")
                        print(" ")
                        continue
                    
                    dia = int(dia)

                    if dia < 1 or dia > 2:
                        print("Solo se puede ingresar el numero 1 o 2")
                        print(" ")
                        continue
                    
                    if dia == 1:
                        print(" ")
                        print("Agenda Lunes")
                        print(" ")

                        if lunes1 != "":
                            print(f"Turno 1: {lunes1}")
                        else:
                            print("Turno 1: (libre)")

                        if lunes2 != "":
                            print(f"Turno 2: {lunes2}")
                        else:
                            print("Turno 2: (libre)")

                        if lunes3 != "":
                            print(f"Turno 3: {lunes3}")
                        else:
                            print("Turno 3: (libre)")

                        if lunes4 != "":
                            print(f"Turno 4: {lunes4}")
                        else:
                            print("Turno 4: (libre)")

                    elif dia == 2:
                        print("    Agenda Martes")
                        if martes1 != "":
                            print(f"Turno 1: {martes1}")
                        else:
                            print("Turno 1: (libre)")

                        if martes2 != "":
                            print(f"Turno 2: {martes2}")
                        else:
                            print("Turno 2: (libre)")

                        if martes3 != "":
                            print(f"Turno 3: {martes3}")
                        else:
                            print("Turno 3: (libre)")

                #resumen general          
                elif opcion == 4:

                    ocupados_en_el_lunes = 0

                    if lunes1 != "":
                        ocupados_en_el_lunes += 1
                    if lunes2 != "":
                        ocupados_en_el_lunes += 1   
                    if lunes3 != "":
                        ocupados_en_el_lunes += 1
                    if lunes4 != "":
                        ocupados_en_el_lunes += 1

                    disponibles_lunes = 4 - ocupados_en_el_lunes


                    ocupados_en_el_martes = 0

                    if martes1 != "":
                        ocupados_en_el_martes += 1
                    if martes2 != "":
                        ocupados_en_el_martes += 1
                    if martes3 != "":
                        ocupados_en_el_martes += 1

                    disponibles_martes = 3 - ocupados_en_el_martes


                    print("Resumen General")
                    print(" ")
                    print(f"Lunes: {ocupados_en_el_lunes} ocupados, {disponibles_lunes} disponibles")
                    print(" ")
                    print(f"Martes: {ocupados_en_el_martes} ocupados, {disponibles_martes} disponibles")
                    print(" ")

                    if ocupados_en_el_lunes > ocupados_en_el_martes:
                        print("Dia con mas turnos: Lunes")
                        print(" ")
                    elif ocupados_en_el_martes > ocupados_en_el_lunes:
                        print("Dia con mas turnos: Martes")
                        print(" ")
                    else:
                        print("Empate entre Lunes y Martes")
                        print(" ")

                #cerrar el sistema         
                elif opcion == 5:
                    print(f"Se cerro el sistema, muchas gracias {nombre_operador}")
                    break
                
        case "4":
                #stats
                energia = 100
                tiempo = 12
                cerraduras_abiertas = 0
                alarma = False
                codigo_parcial = ""
                forzaduras = 0
                
                #pido el nom y val
                nombre_agente = input("Ingresa su nombre de agente: ")
                
                while not nombre_agente.isalpha():  
                        print("Solo se aceptan letras, sin espacios ni numeros")
                        nombre_agente = input("Ingresa su nombre de agente: ")
                        
                while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
                    
                    if alarma == True and tiempo <= 3:
                        print(" ")
                        print(f"Se activo la alarma y perdiste agente {nombre_agente}")
                        break
                    
                    print(" ")
                    print(f"Agente: {nombre_agente}")
                    print(f"Energia: {energia}")
                    print(f"Tiempo: {tiempo}")
                    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
                    print(f"Alarma: {alarma}")
                    print(f"Codigo parcial: {codigo_parcial}")
                    print(" ")
                    print("Elegi lo que queres hacer: ")
                    print("1) Forzar cerradura (-20 energia, -2 tiempo)")
                    print("2) Hackear panel (-10 energia, -3 tiempo)")
                    print("3) Descansar (+15 energia, -1 tiempo)")
                    
                    opcion = input("Elige una accion: ")
                    
                    while not opcion.isdigit():
                        print("Ingresa un numero del 1 al 3")
                        opcion = input("Elige una accion: ")
                        
                    opcion = int(opcion)
                    
                    while opcion < 1 or opcion > 3:
                        print("Ingresa un numero del 1 al 3")
                        opcion = input("elige una accion: ")
                        
                        while not opcion.isdigit():
                            print("Ingresa un numero del 1 al 3")
                            opcion = input("elige una accion")
                            
                        opcion = int(opcion)
                        
                #forzar
                    if opcion == 1:
                        energia -= 20
                        tiempo -= 2
                        forzaduras += 1
                        
                #la regla del spam
                        if forzaduras == 3:
                            print("La alarma se actibo por forzar 3 veces seguidas y no abriste la cerradura")
                            alarma = True
                            
                        else:
                            if energia < 40:
                                
                                numero = input("se esta por activar la alarma, elegi un numero del 1 al 3 para que no se active: ")
                                
                                while not numero.isdigit():
                                    numero = input("solo podes escribir numeros del 1 al 3: ")
                                    
                                numero = int(numero)
                                
                                while numero < 1 or numero > 3:
                                    numero = input("solo podes escribir numeros del 1 al 3: ")
                                    
                                    while not numero.isdigit():
                                        numero = input("solo podes escribir numeros del 1 al 3: ")
                                        
                                    numero = int(numero)
                                    
                                if numero == 3:
                                    print("activaste la alarma")
                                    alarma = True
                                else:
                                    print("no la activaste de pedo papa")
                                    
                #sale del spam 
                            if alarma == False:
                                cerraduras_abiertas += 1
                                print(f"Se forzo la cerradura, tenes {cerraduras_abiertas}/3 cerraduras abiertas")
                            else:
                                print("La cerradura se trabo y no se abrio, tenes que elegir otra opcion para cortar la racha de forzar seguidas")
                                
                #el hackeo del panel
                    elif opcion == 2:
                        energia -= 10
                        tiempo -= 3
                        forzaduras = 0
                        
                        print("estas hackeando el panel")
                        for paso in range(4):
                            codigo_parcial += "A"
                            print(f"Paso {paso + 1}/4 - codigo: {codigo_parcial}")
                        
                        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                            cerraduras_abiertas += 1
                            print(f"completaste el codigo, abriste una cerradura, tienes {cerraduras_abiertas}/3 abiertas")
                            
                        elif len(codigo_parcial) < 8:
                            print(f"Codigo incompleto: {codigo_parcial}, tienes ({len(codigo_parcial)}/8 caracteres)")
                            
                #el descanso
                    elif opcion == 3:
                        forzaduras = 0
                        energia += 15
                        tiempo -= 1
                        
                        if alarma == True:
                            energia -= 10
                            print(f"La alarma esta activa por lo que perdiste 10 de energia, te queda {energia} de energia")
                            
                        if energia > 100:
                            energia = 100
                        print(f"has descansado y ahora tienes {energia} de energia y {tiempo} de tiempo")
                        
                #final      
                if cerraduras_abiertas == 3:
                    print(" ")
                    print(f"Ganaste Agente {nombre_agente}")
                    
                elif energia <= 0 or tiempo <= 0:
                    print(" ")
                    print(f"Perdiste por quedarte sin energia o sin tiempo, agente {nombre_agente}")
                else:
                    print(" ")
                    print("Perdiste por bloqueo de alarma, suerte la proxima papa") 
        
        case "5": 
                                       
            #stats del inicio
            vida_del_gladiador = 100
            vida_del_enemigo = 100
            pociones_de_Vida = 3 
            daño_base_Ataque_Pesado = 15
            daño_base_del_enemigo = 12
            turno_gladiador = True

            #pido el nombre y val
            print("--- BIENVENIDO A LA ARENA --- ")
            nombre_gladiador = input("Ingresa tu nombre de gladiador: ")

            while not nombre_gladiador.isalpha():
                print("Error: solo se permiten letras")
                nombre_gladiador = input("Ingresa tu nombre de gladiador: ")

            print(f"=== INICIO DEL COMBATE ===")

            #armo el menu
            while vida_del_gladiador > 0 and vida_del_enemigo > 0:
                
                print(f"{nombre_gladiador} (HP: {vida_del_gladiador}) vs Enemigo (HP: {vida_del_enemigo}) | Pociones: {pociones_de_Vida}")

                print(f"""   
                Menu de ataque
            opcion "1": ataque pesado
            opcion "2": Rafaga veloz 
            opcion "3": Curar
                    """)
                
                opcion = input("elige una accion: ")
            #val opc

                while not opcion.isdigit():
                    print("Error: ingrese un numero entero positivo")
                    opcion = input("elige una accion: ")
                
                opcion = int(opcion)
                
                while opcion < 1 or opcion > 3:
                    print("Ingresa un numero del 1 al 3")
                    opcion = input("elige una accion: ")
                    while not opcion.isdigit():
                        print("Ingresa un numero del 1 al 3")
                        opcion = input("elige una accion: ")
                    opcion = int(opcion)

            #ataque pesado
                if opcion == 1:
                    
                    if vida_del_enemigo < 20: 
                        daño = daño_base_Ataque_Pesado * 1.5
                        print("Golpe critico")
                    else:
                        daño = daño_base_Ataque_Pesado
                    
                    vida_del_enemigo -= daño
                    print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

            #rafaga    
                elif opcion == 2:
                    print("¡Inicias una ráfaga de golpes!")
                    for i in range(3):
                        vida_del_enemigo -= 5
                        print("Golpe conectado por 5 de daño")
                        
            #curarte
                elif opcion == 3:
                    if pociones_de_Vida > 0:
                        vida_del_gladiador += 30
                        pociones_de_Vida -= 1
                        print("te has curado 30 de vida")
                    else:
                        print("¡No quedan pociones!")
            #daño de enemigo           
                if vida_del_enemigo > 0:
                    vida_del_gladiador -= daño_base_del_enemigo
                    print(f"¡El enemigo contraataca por 12 puntos!")
                print("=== NUEVO TURNO ===")
                
            if vida_del_gladiador > 0:
                print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
            else:
                print(f"DERROTA. Has caído en combate." )
        
        case "6":
            print("gracias por todo y perdon por tan poco!")
            break