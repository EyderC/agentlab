NOVIEMBRE 2 DE 2026

1 - Configuración inicial del Servidor 
- Acceder como root al vps desde mi PC por SSH (Ya habia generado las claves SSH)
- Crear el usuario agentlab con permisos de administración
- Configurar el firewall ufw para permitir conexiones por SSH
- Acceder desde al VPS como el usuario agentlab por SSH

2 - Verfificar los recursos disponibles del servidor
- Memoria RAM libre --> 6.3 GB libres
- Número de nucleos de procesamiento(CPU) --> 2 Núcleos
- Procesos Activos --> principalmente tenemos dos bots de trading, ollama, etc. 
- Puertos Ocupados --> la 127.0.0.1 puerto 8080 ocupado  

3 - Crear el repositorio agentlab en github
- Crear directorio local repositorios_github para almacenar repos
- Crear directorio local-llm-vps en el repo agentlab
- Crear directorio docs y archivo runbook.md documentando lo hecho hoy. 
- Hacer primer commit del repo  --> docs: add VPS diagnosis and initial setup. 




