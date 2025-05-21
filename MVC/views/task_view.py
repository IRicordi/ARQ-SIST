"""
Vista para la interfaz de usuario en consola de la aplicación de tareas.
"""
from typing import List, Optional
from models.task import Task


class TaskView:
    """Clase para gestionar la presentación de información al usuario."""
    
    def show_menu(self) -> str:
        """
        Muestra el menú principal de la aplicación.
        
        Returns:
            La opción seleccionada por el usuario
        """
        print("\n===== GESTOR DE TAREAS (MVC) =====")
        print("1. Agregar nueva tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        return input("Seleccione una opción (1-5): ")
    
    def show_tasks(self, tasks: List[Task]) -> None:
        """
        Muestra la lista de tareas al usuario.
        
        Args:
            tasks: Lista de tareas a mostrar
        """
        if not tasks:
            print("No hay tareas registradas.")
            return
        
        print("\n===== LISTA DE TAREAS =====")
        for task in tasks:
            status = "✓" if task.completed else " "
            print(f"[{status}] {task.id}. {task.title}")
            if task.description:
                print(f"   {task.description}")
        print(f"\nTotal: {len(tasks)} tareas")
    
    def get_task_input(self) -> tuple:
        """
        Solicita al usuario los datos para una nueva tarea.
        
        Returns:
            Tupla con el título y descripción de la tarea
        """
        title = input("Título de la tarea: ")
        description = input("Descripción (opcional): ")
        return title, description
    
    def get_task_id(self, action: str) -> Optional[int]:
        """
        Solicita al usuario el ID de una tarea para realizar una acción.
        
        Args:
            action: Acción a realizar (completar, eliminar, etc.)
            
        Returns:
            ID de la tarea o None si la entrada no es válida
        """
        try:
            task_id = int(input(f"\nIngrese el ID de la tarea a {action}: "))
            return task_id
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return None
    
    def show_message(self, message: str) -> None:
        """
        Muestra un mensaje al usuario.
        
        Args:
            message: Mensaje a mostrar
        """
        print(message)
    
    def show_welcome(self) -> None:
        """Muestra un mensaje de bienvenida."""
        print("¡Bienvenido a la aplicación de gestión de tareas (MVC)!")
    
    def show_goodbye(self) -> None:
        """Muestra un mensaje de despedida."""
        print("¡Gracias por usar la aplicación de gestión de tareas!")