#!/usr/bin/env python3
"""
Aplicación de Gestión de Tareas - Enfoque Monolítico No Modular
TICS317 - Arquitectura de Sistemas

Este archivo contiene toda la funcionalidad de la aplicación en un único archivo:
- Definición de la estructura de datos de las tareas
- Lógica para gestionar las tareas (agregar, listar, completar, eliminar)
- Interfaz de usuario en consola
- Persistencia de datos en archivo JSON
"""

import json
import os
from typing import List, Dict, Any, Optional

# Ruta del archivo JSON donde se guardarán las tareas
TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict[str, Any]]:
    """Carga las tareas desde el archivo JSON."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error al leer el archivo {TASKS_FILE}. Iniciando con lista vacía.")
            return []
    return []

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Guarda las tareas en el archivo JSON."""
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

def show_menu() -> str:
    """Muestra el menú de opciones y retorna la opción seleccionada."""
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar nueva tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def add_task(tasks: List[Dict[str, Any]]) -> None:
    """Agrega una nueva tarea a la lista."""
    title = input("Título de la tarea: ")
    description = input("Descripción (opcional): ")
    
    # Crear la nueva tarea
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "completed": False
    }
    
    # Agregar la tarea a la lista
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarea '{title}' agregada correctamente.")

def list_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Muestra la lista de todas las tareas."""
    if not tasks:
        print("No hay tareas registradas.")
        return
    
    print("\n===== LISTA DE TAREAS =====")
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")
        if task["description"]:
            print(f"   {task['description']}")
    print(f"\nTotal: {len(tasks)} tareas")

def complete_task(tasks: List[Dict[str, Any]]) -> None:
    """Marca una tarea como completada."""
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("\nIngrese el ID de la tarea a completar: "))
        
        # Buscar la tarea por ID
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print(f"Tarea '{task['title']}' marcada como completada.")
                return
        
        print(f"No se encontró ninguna tarea con ID {task_id}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def delete_task(tasks: List[Dict[str, Any]]) -> None:
    """Elimina una tarea de la lista."""
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("\nIngrese el ID de la tarea a eliminar: "))
        
        # Buscar y eliminar la tarea por ID
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(i)
                save_tasks(tasks)
                print(f"Tarea '{deleted_task['title']}' eliminada correctamente.")
                return
        
        print(f"No se encontró ninguna tarea con ID {task_id}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def main() -> None:
    """Función principal que ejecuta la aplicación."""
    print("¡Bienvenido a la aplicación de gestión de tareas!")
    
    # Cargar tareas existentes
    tasks = load_tasks()
    
    while True:
        option = show_menu()
        
        if option == "1":
            add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("¡Gracias por usar la aplicación de gestión de tareas!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()