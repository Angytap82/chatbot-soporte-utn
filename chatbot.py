# =====================================================================
# TRABAJO INTEGRADOR: SIMULADOR DE CHATBOT DE SOPORTE TÉCNICO
# =====================================================================

# 1. SIMULACIÓN DE BASE DE DATOS (Plantillas de datos en formato de listas)
# Lista de legajos válidos en la empresa
BD_USUARIOS = ["1001", "1002", "1003", "1004"]
# Lista para guardar los tickets que se vayan creando
BD_TICKETS = []

def iniciar_chatbot():
    print("--- CHATBOT DE SOPORTE TÉCNICO INICIADO ---")
    print("Bot: ¡Hola! Soy tu asistente virtual de Soporte Técnico.")
    
    # 2. GESTIÓN DE ESTADOS (La memoria del Bot)
    # Empezamos en el Estado 1
    estado_actual = "BIENVENIDA"
    
    # Variables para guardar lo que escribe el usuario
    falla_seleccionada = ""
    legajo_usuario = ""
    intentos_legajo = 0  # Control para evitar bucles infinitos

    # El bucle mantiene el chat activo mientras no llegue al final
    while estado_actual != "FIN":
        
        # -------------------------------------------------------------
        # ESTADO 1: BIENVENIDA Y MENÚ DE FALLAS
        # -------------------------------------------------------------
        if estado_actual == "BIENVENIDA":
            print("\nBot: Por favor, selecciona el número de tu problema:")
            print("1. No tengo conexión a Internet")
            print("2. Olvidé mi contraseña del sistema")
            print("3. La impresora no responde")
            
            entrada = input("Usuario: ").strip()
            
            # CONTROL DE ERRORES (Camino Infeliz)
            if entrada in ["1", "2", "3"]:
                falla_seleccionada = entrada
                # Avanzamos al siguiente paso en el diagrama
                estado_actual = "PEDIR_LEGAJO" 
            else:
                print("Bot: ❌ Opción inválida. Por favor, ingresa solo 1, 2 o 3.")
                # No cambiamos de estado, se repite el menú

        # -------------------------------------------------------------
        # ESTADO 2: PEDIR Y VALIDAR LEGAJO (Compuerta ¿Existe Legajo?)
        # -------------------------------------------------------------
        elif estado_actual == "PEDIR_LEGAJO":
            print("\nBot: Para continuar, por favor ingresa tu número de Legajo (Ej: 1001):")
            legajo_usuario = input("Usuario: ").strip()
            
            # Simulación de consulta a la Base de Datos
            if legajo_usuario in BD_USUARIOS:
                print("Bot: ✅ Legajo verificado con éxito.")
                estado_actual = "ENVIAR_SOLUCION"
            else:
                intentos_legajo += 1
                print(f"Bot: ❌ El legajo '{legajo_usuario}' no existe en el sistema.")
                
                # Si se equivoca muchas veces, lo derivamos por seguridad
                if intentos_legajo >= 3:
                    print("Bot: Demasiados intentos fallidos con el legajo.")
                    estado_actual = "DERIVAR_HUMANO"
                else:
                    print("Bot: Por favor, vuelve a intentarlo.")
                    # El estado sigue siendo PEDIR_LEGAJO (vuelve a preguntar)

        # -------------------------------------------------------------
        # ESTADO 3: ENVIAR SOLUCIÓN Y EVALUAR (Compuerta ¿Se solsi--------
        elif estado_actual == "ENVIAR_SOLUCION":
            print("\nBot: Aplicando guía de solución paso a paso...")
            if falla_seleccionada == "1":
                print("-> Instrucción: Desconecta el cable de red, espera 10 segundos y conéctalo de nuevo.")
            elif falla_seleccionada == "2":
                print("-> Instrucción: Ingresa al link '://empresa.com' y usa tu código SMS.")
            elif falla_seleccionada == "3":
                print("-> Instrucción: Revisa que la luz verde esté encendida y reinicia la cola de impresión.")
                
            print("\nBot: ¿Se solucionó tu problema técnico? (Responde SI o NO)")
            respuesta = input("Usuario: ").strip().upper()
            
            if respuesta == "SI":
                print("\nBot: 🎉 ¡Excelente! Procedo al cierre del ticket de forma exitosa.")
                print("Bot: Gracias por comunicarte con Soporte Técnico. ¡Adiós!")
                estado_actual = "FIN"
            elif respuesta == "NO":
                estado_actual = "DERIVAR_HUMANO"
            else:
                print("Bot: ❌ Respuesta no válida. Por favor, escribe exactamente SI o NO.")
                # Se mantiene en este estado para volver a preguntar

        # -------------------------------------------------------------
        # ESTADO 4: DERIVACIÓN A HUMANO (Creación de Ticket en BD)
        # -------------------------------------------------------------
        elif estado_actual == "DERIVAR_HUMANO":
            print("\nBot: Lamentamos no haberlo solucionado de forma automática.")
            print("Bot: Creando un ticket de soporte en la Base de Datos...")
            
            # Creamos el registro del ticket (Persistencia de datos)
            nuevo_ticket = {
                "id_ticket": len(BD_TICKETS) + 1,
                "legajo": legajo_usuario,
                "tipo_falla": falla_seleccionada,
                "estado": "Abierto - Derivado a Humano"
            }
            BD_TICKETS.append(nuevo_ticket)
            
            print(f"Bot: 🎫 Ticket N° {nuevo_ticket['id_ticket']} generado correctamente.")
            print("Bot: Un técnico humano se pondrá en contacto con vos en breve. ¡Adiós!")
            estado_actual = "FIN"

    # Muestra los datos guardados al finalizar la ejecución
    print("\n--- DATOS FINALES DE LA BASE DE DATOS SIMULADA ---")
    print("Tickets registrados en BD:", BD_TICKETS)

# Ejecutar el programa
iniciar_chatbot()
