"""
Repositorio para la persistencia de tareas en archivo JSON.
"""
import json
import os
from typing import List, Dict, Any
from models.task import Task


class TaskRepo:
    """Clase para gestionar la persistencia de tareas."""
    
    def __init__(self, file_name: str = "mvc_tasks.json"):
        """
        Inicializa el repositorio de tareas.
        
        Args:
            file_name: Nombre del archivo JSON donde se guardarán las tareas
        """
        self.file_path = file_name
    
    def load_tasks(self) -> List[Task]:
        """
        Carga las tareas desde el archivo JSON.
        
        Returns:
            Lista de objetos Task
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    tasks_data = json.load(file)
                    return [Task.from_dict(task_data) for task_data in tasks_data]
            except json.JSONDecodeError:
                print(f"Error al leer el archivo {self.file_path}. Iniciando con lista vacía.")
                return []
        return []
    
    def save_tasks(self, tasks: List[Task]) -> None:
        """
        Guarda las tareas en el archivo JSON.
        
        Args:
            tasks: Lista de objetos Task a guardar
        """
        tasks_data = [task.to_dict() for task in tasks]
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(tasks_data, file, indent=4)
    
    def get_next_id(self, tasks: List[Task]) -> int:
        """
        Obtiene el siguiente ID disponible para una nueva tarea.
        
        Args:
            tasks: Lista actual de tareas
            
        Returns:
            Siguiente ID disponible
        """
        if not tasks:
            return 1
        return max(task.id for task in tasks) + 1