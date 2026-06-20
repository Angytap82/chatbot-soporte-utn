# chatbot-soporte-utn
# Trabajo Integrador: Simulador de Chatbot de Soporte Técnico

Este proyecto es el Trabajo Práctico Integrador para la materia **Organización Empresarial** de la *Tecnicatura Universitaria en Programación (UTN)*. Consiste en un simulador de chatbot desarrollado en Python 3 que automatiza el proceso administrativo de soporte técnico de una empresa, siguiendo de forma exacta un modelo de diseño BPMN 2.0.

##  Características Principales
- **Gestión de Estados (Memoria):** Control del flujo dinámico de la conversación a través de diferentes etapas (`BIENVENIDA`, `PEDIR_LEGAJO`, `ENVIAR_SOLUCION`, `DERIVAR_HUMANO`).
- **Persistencia de Datos Simulada:** Validación de usuarios mediante una lista de legajos habilitados (`BD_USUARIOS`) y registro automático de reclamos en una lista de tickets (`BD_TICKETS`).
- **Robustez (Camino Infeliz):** Control de errores ante ingresos inválidos en el menú y bloqueo automático por seguridad tras 3 intentos fallidos con el legajo.

##  Cómo Ejecutar el Proyecto

1. Asegúrate de tener instalado **Python 3** en tu computadora.
2. Descarga el archivo de código fuente de este repositorio (`chatbot.py` o el nombre que le hayas puesto).
3. Abri la terminal de comandos, consola o CMD en la carpeta donde guardaste el archivo.
4. Ejecuta el siguiente comando:
   ```bash
   python chatbot.py
   ```
5. Sigue las instrucciones interactivas que el bot desplegará en la pantalla.

## 👥 Integrantes / Autor
- **Tapia Maria de los Angeles** - *Tecnicatura Universitaria en Programación (UTN)*
- **link TP https://docs.google.com/document/d/11xCT8FpjYaDLtOye8EXiqfRMbdX_p0wQHMax1VlyHBs/edit?usp=sharing
- 
