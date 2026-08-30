# ==============================================
# AGENT LOOP
# ==============================================

finished = False

while not finished:
 # El agente consigue la tarea
 task = get_task()

 # El agente decide qué operación hacer
 action = decide_action(task)

 # El agente ejecuta la herramienta y consigue un resultado
 result = execute_tool(action)

 # Una vez obtenido los resultados, el agente actualiza el contexto
 update_context(result)

 # El agente revisa si ya logró completar su trabajo.
 # En caso contrario, regresa al ciclo
 finished = is_finished(result)


# ==============================================
# get_task
# ==============================================
def get_task():
 task = input(
        "Realizar X tarea"
    )
 return task

# ==============================================
# decide_action
# ==============================================
def decide_action(task):
 # El agente decide cuál de todas de las operaciones realizar
 action = input(
        "Acción (READ / WRITE / EDIT / BASH / FINISH)"
    ).upper()
 return action

# ==============================================
# execute_tool
# ==============================================
def execute_tool(action):
    
    if action == "READ":
        return tool_read()

    elif action == "WRITE":
        return tool_write()

    elif action == "EDIT":
        return tool_edit()

    elif action == "BASH":
        return tool_bash()

    elif action == "FINISH":
        return "finished"

    else:
        return "Acción desconocida"

# ==============================================
# READ
# ==============================================
def tool_read():
   # El agente consigue la dirección a leer
   path = input("Archivo/directorio a leer")
   content = read_file(path)
   return content

def read_file(path):
   print(f"[READ] El agente está leyendo: {path}")
   return f"Contenido de {path}"

# ==============================================
# WRITE
# ==============================================
def tool_write():
   # El agente consigue el archivo a escribir
   path = input("Archivo/directorio a escribir")

   # El agente genera el contenido que debe escribir
   content = input("Contenido a escribir")

   result = write_file(path,content)
   return result

def write_file(path,content):
   print(f"[WRITE] El agente está escribiendo '{content}' en: {path}")
   return f"Archivo escrito correctamente"

# ==============================================
# EDIT
# ==============================================
def tool_edit():
   # El agente consigue la dirección a modificar
   path = input("Archivo a editar")

   # El agente introduce el texto que se desea reemplazar
   old = input("Texto que se desea reemplazar")

   # El agente introduce el nuevo texto
   new = input("Nuevo texto")

   result = edit_file(path, old, new)
   return result

def edit_file(path, old, new):
   print(f"[EDIT] El agente está reemplazando '{old}' por '{new}' en: {path}")
   return f"Archivo modificado correctamente"

# ==============================================
# BASH
# ==============================================
def tool_bash():
   # El agente consigue el comando a ejecutar
   command = input("Comando a ejecutar")

   result = execute_command(command)
   return result

def execute_command(command):
   print(f"[BASH] El agente está ejecutando '{command}'")
   return f"Resultado del commando"