"""
Aplicación de Gestión de Tareas - Enfoque MVC
TICS317 - Arquitectura de Sistemas

Punto de entrada de la aplicación que instancia los componentes MVC.
"""
from views.task_view import TaskView
from controllers.task_controller import TaskController
from storage.task_repo import TaskRepo


def main() -> None:
    """Función principal que inicializa y ejecuta la aplicación."""
    # Crear instancias de los componentes MVC
    view = TaskView()
    repo = TaskRepo("mvc_tasks.json")  # Nombre diferente para el archivo JSON
    controller = TaskController(view, repo)
    
    # Ejecutar la aplicación
    controller.run()


if __name__ == "__main__":
    main()