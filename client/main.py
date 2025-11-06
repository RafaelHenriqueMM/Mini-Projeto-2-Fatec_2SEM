import requests
import json

API_BASE_URL = "http://127.0.0.1:8000/tasks/"

def create_task(title: str, description: str = None):
    """Cria uma nova tarefa (POST /tasks/)."""
    print(f"\n[POST] Tentando criar tarefa: '{title}'")
    
    task_data = {
        "title": title,
        "description": description,
        "completed": False
    }
    
    try:
        response = requests.post(API_BASE_URL, json=task_data)
        response.raise_for_status()
        
        task = response.json()
        print(f"✅ Tarefa criada com sucesso! ID: {task['id']}, Título: {task['title']}")
        return task
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao criar tarefa: {e}")
        print(f"Detalhes da Resposta (se houver): {response.text if 'response' in locals() else 'N/A'}")
        return None

def list_tasks():
    """Lista todas as tarefas (GET /tasks/)."""
    print("\n[GET] Buscando todas as tarefas...")
    
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()
        
        tasks = response.json()
        
        if tasks:
            print(f"✅ Total de {len(tasks)} tarefas encontradas:")
            for task in tasks:
                status = "CONCLUÍDA" if task['completed'] else "PENDENTE"
                print(f"   - ID: {task['id']}, Título: {task['title']}, Status: {status}")
        else:
            print("✅ Nenhuma tarefa encontrada.")
            
        return tasks
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao listar tarefas: {e}")
        return None

def update_task_status(task_id: int, completed: bool):
    """Atualiza o status (completed) de uma tarefa (PATCH /tasks/{task_id})."""
    print(f"\n[PATCH] Tentando atualizar o status da tarefa ID {task_id} para 'completed={completed}'...")
    
    update_data = {"completed": completed}
    url = f"{API_BASE_URL}{task_id}"
    
    try:
        response = requests.patch(url, json=update_data)
        response.raise_for_status()
        
        task = response.json()
        print(f"✅ Tarefa ID {task['id']} atualizada. Novo status: {'CONCLUÍDA' if task['completed'] else 'PENDENTE'}")
        return task
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao atualizar tarefa ID {task_id}: {e}")
        return None

def delete_task(task_id: int):
    """Deleta uma tarefa (DELETE /tasks/{task_id})."""
    print(f"\n[DELETE] Tentando deletar a tarefa ID {task_id}...")
    url = f"{API_BASE_URL}{task_id}"
    
    try:
        response = requests.delete(url)
        # O status 204 (No Content) é esperado para exclusão bem-sucedida
        if response.status_code == 204:
            print(f"✅ Tarefa ID {task_id} deletada com sucesso (Status 204).")
            return True
        else:
            response.raise_for_status()
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao deletar tarefa ID {task_id}: {e}")
        return False

def run_demonstration():
    """Sequência de chamadas para demonstrar o consumo da API."""
    print("==============================================")
    print("      INÍCIO DA DEMONSTRAÇÃO DO CLIENTE       ")
    print("==============================================")
    
    list_tasks()
    
    task1 = create_task("Estudar FastAPI", "Revisar rotas CRUD e Pydantic.")
    task2 = create_task("Preparar o README", "Detalhar as instruções de execução do projeto.")
    
    if not task1 or not task2:
        print("\nDemonstração interrompida devido a falha na criação de tarefas.")
        return

    list_tasks()

    updated_task1 = update_task_status(task1['id'], completed=True)

    list_tasks()

    delete_task(task2['id'])

    print("\n[FINAL] Resultado após a exclusão:")
    list_tasks()
    
    print("\n==============================================")
    print("        FIM DA DEMONSTRAÇÃO DO CLIENTE        ")
    print("==============================================")


if __name__ == "__main__":
    # IMPORTANTE: Certifique-se de que o servidor (server/app/main.py) esteja
    # rodando em http://127.0.0.1:8000 antes de executar este cliente!
    run_demonstration()