"""
Modelo de datos para representar una tarea en la aplicación.
"""
from typing import Dict, Any, Optional


class Task:
    """Clase que representa una tarea."""
    
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Inicializa una nueva tarea.
        
        Args:
            task_id: Identificador único de la tarea
            title: Título de la tarea
            description: Descripción detallada de la tarea (opcional)
            completed: Estado de completitud de la tarea
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def mark_as_completed(self) -> None:
        """Marca la tarea como completada."""
        self.completed = True
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte la tarea a un diccionario para su serialización.
        
        Returns:
            Diccionario con los datos de la tarea
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Crea una instancia de Task a partir de un diccionario.
        
        Args:
            data: Diccionario con los datos de la tarea
            
        Returns:
            Una nueva instancia de Task
        """
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )