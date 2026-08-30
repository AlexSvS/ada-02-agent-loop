# Preguntas obligatorias
## ¿Qué es tool calling?
Tool Calling es la capacidad de los modelos IA de interactuar con herramientas o servicios externos como API's. Esta característica es necesaria para los agentes ya que les permite realizar tareas complejas que impliquen el acceso o modificación de recursos externos, convirtiendo al agente de un asistente pasivo a uno proactivo que realiza mucho más que sólo responder preguntas por texto.
## ¿Qué es una observation?
Es la información que un agente de IA recibe después de ejecutar una acción y esta es utilizada para los pensamientos y acciones subsecuentes del agente, fomentando la adaptación rápida ante nueva información y cambios en el entorno.
## ¿Qué es el Agent Loop?
Es un ciclo iterativo que realiza un agente de IA que consiste en, primero, recibir la solicitud del usuario o máquina para luego planificar las tareas y decidir cuál será la siguiente tarea a realizar. Una vez decidido, el agente ejecuta alguna herramienta o comando para completar su objetivo. Por último, el agente observa el resultado y en el caso de que la tarea fuera completada, termina el ciclo; y en el caso contrario, comienza otro ciclo de vuelta al primer paso, actualizando el contexto con nueva información.
## ¿Qué operaciones corresponden a read, write, edit y bash?
•	READ: Realizar una consulta o leer información de un archivo sin modificarla.\
•	WRITE: Crear contenido nuevo a un archivo.\
•	EDIT: Modificar contenido existente.\
•	BASH: Ejecutar comandos del sistema.\
## ¿Dónde intervino el agente?
El agente se encargó de planear y decidir las tareas a realizar (leer, editar y modificar archivos, etc.). Para cada decisión, el agente ejecutó todas aquellas herramientas que requería para completar su trabajo, interpretó los resultados de la herramienta y vuelve a decidir si continúa con una nueva tarea o finaliza el ciclo.
## ¿Dónde intervino el humano?
El ser humano se encargó de definir y enviar su prompt al agente así como dar los permisos requeridos al agente de leer, editar y modificar archivos y ejecutar comandos del sistema. En el caso de que se presentará algún problema, el ser humano pudo haber rechazado y corregido los cambios propuestos por el agente.
## ¿Qué capacidad se perdería sin ejecución de comandos?
El agente perdería la capacidad de interactuar de manera directa y activa con el entorno del usuario. 
