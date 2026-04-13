from base64 import standard_b64decode
import aiohttp 
import asyncio
import time

# async def fetch_page(url) define una corrutina que puede 
# pausarse mientras espera la respuesta del servidor. Dentro, 

# async with aiohttp.ClientSession() abre una sesión HTTP — 
# una conexión persistente con el servidor que evita reconectarse 
# en cada petición — y el with garantiza que esa conexión se 
# cierre automáticamente al terminar, aunque haya un error.

# El async with es exactamente lo mismo, pero la apertura y el cierre pueden pausarse porque son operaciones de red que toman tiempo:


# async with aiohttp.ClientSession() as session:
#     # abrir la sesion puede tardar (await interno)
#     # usas la sesion aqui
# # cerrar la sesion puede tardar (await interno)
# Sin el async, el with bloquearía el programa mientras abre/cierra la conexión. Con async with, puede pausarse y dejar que otras corrutinas avancen mientras tanto.

# En resumen: async with = with normal + puede hacer await al entrar y salir.

async def fetch_page(url): # async def — indica que es una corrutina, puede pausarse con await mientras espera la respuesta del servidor
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            #print(response.status)
            print(f'the page took {time.time() - page_start}')
            return response.status


loop = asyncio.get_event_loop()

tasks = [fetch_page('http://google.com') for i in range(50)]

start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'all requests took {time.time() - start}')

# FLUJO DE EJECUCION:
#
# tasks = [fetch_page('http://google.com') for i in range(50)]
# Crea 50 corrutinas — aun no ejecuta nada, solo las prepara.
#
# loop.run_until_complete(asyncio.gather(*tasks))
# gather agrupa las 50 corrutinas y el event loop las corre todas a la vez:
#
#   event loop arranca las 50 corrutinas simultaneamente:
#
#   fetch_page #1  -> abre sesion -> manda GET -> PAUSA (espera servidor)
#   fetch_page #2  -> abre sesion -> manda GET -> PAUSA (espera servidor)
#   fetch_page #3  -> abre sesion -> manda GET -> PAUSA (espera servidor)
#   ...
#   fetch_page #50 -> abre sesion -> manda GET -> PAUSA (espera servidor)
#
#   --- todas esperando al mismo tiempo ---
#
#   servidor responde a #7  -> event loop reanuda #7  -> imprime tiempo -> termina
#   servidor responde a #23 -> event loop reanuda #23 -> imprime tiempo -> termina
#   servidor responde a #1  -> event loop reanuda #1  -> imprime tiempo -> termina
#   ...
#
# Ninguna bloquea a las demas — mientras una espera la respuesta, las otras siguen
# esperando tambien. El event loop va reanudando cada una a medida que llegan las respuestas.
# Sin async harias 50 peticiones una por una — tardaria 50x mas.
#
# LAS RESPUESTAS NO LLEGAN EN ORDEN — llegan segun quien responda primero:
#   mandas:   #1  #2  #3  #4  #5 ...
#   recibes:  #3  #1  #5  #2  #4 ...
# Depende de la congestion de la red, que tan ocupado este el servidor,
# y la ruta que toma cada paquete por internet.
# gather si espera a que todas terminen, y devuelve los resultados en orden original.
#
# CLIENT SESSION SE CREA 50 VECES — una por cada fetch_page:
#   async with aiohttp.ClientSession() as session:  # abre una sesion HTTP
#       async with session.get(url) as response:    # hace un GET con esa sesion
#   ClientSession — la conexion con el servidor (se abre y cierra 50 veces)
#   session.get(url) — AQUI es la pausa real, espera que el servidor responda
#   ClientSession() es rapido, es local, solo crea un objeto en memoria —
#   la espera real ocurre en session.get(url), donde sale el paquete por internet.
#
# SI HUBIERA DOS OPERACIONES BLOQUEANTES SEGUIDAS:
#   async with aiohttp.ClientSession() as session:  # PAUSA #1 — espera abrir sesion
#       async with session.get(url) as response:    # PAUSA #2 — espera respuesta servidor
#
#   fetch_page #1 -> PAUSA #1 (abriendo sesion)
#     event loop -> fetch_page #2 -> PAUSA #1 (abriendo sesion)
#     event loop -> fetch_page #3 -> PAUSA #1 (abriendo sesion)
#     ...todas pausadas abriendo sesion...
#   sesion #3 lista -> reanuda #3 -> PAUSA #2 (esperando GET)
#   sesion #1 lista -> reanuda #1 -> PAUSA #2 (esperando GET)
#     ...todas pausadas esperando GET...
#   respuesta #2 llega -> reanuda #2 -> termina
#   respuesta #1 llega -> reanuda #1 -> termina
#
# IMPORTANTE — dependencias dentro de una corrutina:
#   Las 50 corrutinas son independientes entre si -> corren en paralelo.
#   Pero dentro de cada una, las instrucciones son secuenciales:
#     async with ClientSession() as session:  # paso 1 — si o si primero
#         async with session.get(url) as r:   # paso 2 — depende del paso 1
#   Si crear la sesion tardara 2 segundos, ESA corrutina esperaria 2 segundos
#   antes de poder hacer el GET. Las otras 49 seguirian avanzando en paralelo.
#   Async no elimina las dependencias dentro de una corrutina —
#   solo permite que corrutinas independientes no se bloqueen entre si.

