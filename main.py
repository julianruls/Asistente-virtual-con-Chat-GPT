# Importamos la biblioteca de OpenAI
import openai

# Importamos el módulo donde guardamos la API key
import config

# Configuramos la API key de OpenAI desde el módulo "config"
openai.api_key = config.api_key

# Configuramos al asistente y lo contextualizamos
mensajes = [{"role": "system", "content": "Eres un desarrollador web especializado en Python"}]

while True:  # Con el bucle logramos generar una interacción constante con el asistente
    contenido = input("¿Sobre qué quieres hablar? ")  # Pregunta del usuario
    
    if contenido.lower() == "exit":  # Usando el comando "exit" salimos del bucle
        print("Saliendo del chat...")
        break

    mensajes.append({"role": "user", "content": contenido})  # Añadimos el mensaje del usuario al historial

    # Definimos el modelo a utilizar y le pasamos un conjunto de mensajes
    # en formato clave/valor que indica quién envía el mensaje y su contenido.
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Especificamos el modelo
        messages=mensajes  # Mensajes acumulados
    )

    respuesta_del_contenido = respuesta.choices[0].message.content  # Extraemos el contenido de la respuesta

    mensajes.append({"role": "assistant", "content": respuesta_del_contenido})  # Añadimos la respuesta al historial

    # Imprimimos la respuesta generada por OpenAI
    print("Asistente:", respuesta_del_contenido)
