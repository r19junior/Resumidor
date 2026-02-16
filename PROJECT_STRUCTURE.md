# 📂 Estructura del Proyecto y Fases de Desarrollo

Este documento detalla la organización de carpetas y el cronograma de implementación para el proyecto **RESUMIDOR**.

## 🏗️ Estructura de Carpetas

```text
RESUMIDOR/
├── data/               # Almacenamiento local de PDFs (temporal o de prueba)
├── logs/               # Archivos de registro para auditoría y errores
├── src/                # Código fuente del sistema
│   ├── ai/             # Lógica de comunicación con Llama 3 (Ollama/API)
│   ├── db/             # Scripts de conexión y consultas PostgreSQL
│   └── processor/      # Lógica de extracción de texto (PyMuPDF)
├── .env.example        # Plantilla de variables de entorno
├── .gitignore          # Archivos excluidos de Git (logs, .env)
├── main.py             # Punto de entrada principal (el Worker)
├── README.md           # Documentación general
└── requirements.txt    # Dependencias del proyecto
```

---

## 🚀 Fases del Proyecto

### Fase 1: Cimiento y Datos 🏗️
- Configuración de la base de datos PostgreSQL.
- Implementación de la creación dinámica de la columna `resumen`.
- Script de conexión base en `src/db/`.

### Fase 2: Extracción de Contenido 📄
- Integración de **PyMuPDF** para leer documentos.
- Implementación del límite de 3 páginas para optimización.
- Manejo de excepciones para PDFs sin capa de texto.

### Fase 3: Integración de IA 🧠
- Conexión con **Ollama** o API externa.
- Refinamiento del *Prompt* para resúmenes de una sola línea.
- Pruebas de inferencia en `src/ai/`.

### Fase 4: Orquestación (Worker) 🔄
- Desarrollo del bucle principal en `main.py`.
- Lógica de filtrado: procesar solo registros con `resumen IS NULL`.
- Manejo de errores para evitar bloqueos en la cola.

### Fase 5: Automatización y Monitoreo 📈
- Configuración de la tarea cron para ejecución periódica.
- Implementación de sistema de logs en `logs/`.

---

## 🛠️ Cómo Inicializar la Estructura

Para crear esta estructura manualmente, puedes ejecutar:

```bash
mkdir -p data logs src/ai src/db src/processor
touch main.py .env.example requirements.txt PROJECT_STRUCTURE.md
```
