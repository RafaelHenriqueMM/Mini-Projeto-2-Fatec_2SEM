from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

class TaskBase(BaseModel):
    """Modelo base para dados de entrada (criação e atualização de tarefa)."""
    title: str = Field(..., min_length=1, max_length=100) # O '...' indica que é obrigatório
    description: Optional[str] = None
    completed: bool = False

class Task(TaskBase):
    """Modelo completo para representar uma tarefa, incluindo o ID."""
    id: int

class TaskUpdate(BaseModel):
    """Modelo para atualizar campos específicos de uma tarefa (PATCH)."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

tasks_db: List[Task] = []
next_id = 1

app = FastAPI(
    title="Gerenciador de Tarefas API",
    description="API CRUD simples para o mini projeto de consumo de API.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    """Endpoint raiz para testar se a API está funcionando."""
    return {"message": "Bem-vindo ao Gerenciador de Tarefas FastAPI. Acesse /docs para a documentação interativa."}

@app.post("/tasks/", response_model=Task, status_code=201, tags=["Tarefas"])
def create_task(task: TaskBase):
    """Cria uma nova tarefa e a adiciona ao 'banco de dados'."""
    global next_id
    
    new_task = Task(
        id=next_id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    
    tasks_db.append(new_task)
    next_id += 1
    
    return new_task

@app.get("/tasks/", response_model=List[Task], tags=["Tarefas"])
def list_tasks():
    """Retorna a lista completa de todas as tarefas."""
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task, tags=["Tarefas"])
def get_task(task_id: int):
    """Retorna uma tarefa específica pelo ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    
    raise HTTPException(status_code=404, detail=f"Tarefa com ID {task_id} não encontrada.")

@app.patch("/tasks/{task_id}", response_model=Task, tags=["Tarefas"])
def update_task(task_id: int, task_update: TaskUpdate):
    """Atualiza parcialmente uma tarefa existente (título, descrição ou status)."""
    global tasks_db
    
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            existing_task_data = task.model_dump()
            
            update_data = task_update.model_dump(exclude_unset=True)
            
            updated_task_data = {**existing_task_data, **update_data}
            
            tasks_db[index] = Task(**updated_task_data)
            
            return tasks_db[index]

    raise HTTPException(status_code=404, detail=f"Tarefa com ID {task_id} não encontrada.")

@app.delete("/tasks/{task_id}", status_code=204, tags=["Tarefas"])
def delete_task(task_id: int):
    """Remove uma tarefa pelo ID."""
    global tasks_db
    
    initial_length = len(tasks_db)
    tasks_db = [task for task in tasks_db if task.id != task_id]
    
    if len(tasks_db) == initial_length:
        raise HTTPException(status_code=404, detail=f"Tarefa com ID {task_id} não encontrada.")
    
    # Se a exclusão foi bem-sucedida, retorna 204 No Content
    return