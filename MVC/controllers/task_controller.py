"""
Controlador para gestionar la lógica de negocio de la aplicación de tareas.
"""
from typing import List, Optional
from models.task import Task
from views.task_view import TaskView
from storage.task_repo import TaskRepo


class TaskController:
    """Clase controlador que actúa como intermediario entre el modelo y la vista."""
    
    def __init__(self, view: TaskView, repo: TaskRepo):
        """
        Inicializa el controlador con sus dependencias.
        
        Args:
            view: Instancia de TaskView para interactuar con el usuario
            repo: Instancia de TaskRepo para la persistencia de datos
        """
        self.view = view
        self.repo = repo
        self.tasks = self.repo.load_tasks()
    
    def add_task(self) -> None:
        """Gestiona el proceso de agregar una nueva tarea."""
        title, description = self.view.get_task_input()
        
        if not title:
            self.view.show_message("Error: El título de la tarea no puede estar vacío.")
            return
        
        # Crear una nueva tarea
        next_id = self.repo.get_next_id(self.tasks)
        new_task = Task(task_id=next_id, title=title, description=description)
        
        # Agregar la tarea a la lista y guardar
        self.tasks.append(new_task)
        self.repo.save_tasks(self.tasks)
        self.view.show_message(f"Tarea '{title}' agregada correctamente.")
    
    def list_tasks(self) -> None:
        """Muestra la lista de tareas al usuario."""
        self.view.show_tasks(self.tasks)
    
    def complete_task(self) -> None:
        """Gestiona el proceso de marcar una tarea como completada."""
        self.list_tasks()
        if not self.tasks:
            return
        
        task_id = self.view.get_task_id("completar")
        if task_id is None:
            return
        
        # Buscar la tarea por ID
        task = self._find_task_by_id(task_id)
        if task:
            task.mark_as_completed()
            self.repo.save_tasks(self.tasks)
            self.view.show_message(f"Tarea '{task.title}' marcada como completada.")
        else:
            self.view.show_message(f"No se encontró ninguna tarea con ID {task_id}.")
    
    def delete_task(self) -> None:
        """Gestiona el proceso de eliminar una tarea."""
        self.list_tasks()
        if not self.tasks:
            return
        
        task_id = self.view.get_task_id("eliminar")
        if task_id is None:
            return
        
        # Buscar y eliminar la tarea
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                deleted_task = self.tasks.pop(i)
                self.repo.save_tasks(self.tasks)
                self.view.show_message(f"Tarea '{deleted_task.title}' eliminada correctamente.")
                return
        
        self.view.show_message(f"No se encontró ninguna tarea con ID {task_id}.")
    
    def _find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Busca una tarea por su ID.
        
        Args:
            task_id: ID de la tarea a buscar
            
        Returns:
            La tarea encontrada o None si no existe
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def run(self) -> None:
        """Ejecuta el bucle principal de la aplicación."""
        self.view.show_welcome()
        
        while True:
            option = self.view.show_menu()
            
            if option == "1":
                self.add_task()
            elif option == "2":
                self.list_tasks()
            elif option == "3":
                self.complete_task()
            elif option == "4":
                self.delete_task()
            elif option == "5":
                self.view.show_goodbye()
                break
            else:
                self.view.show_message("Opción no válida. Por favor, intente nuevamente.")