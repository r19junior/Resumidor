# Estructura del Proyecto y Fases de Desarrollo

Este documento detalla la organización de carpetas y el cronograma de implementación para el proyecto **RESUMIDOR**.

## Estructura de Carpetas

```text
RESUMIDOR/
├── data/               # Almacenamiento local de PDFs
├── logs/               # Archivos de registro y auditoría
├── src/                # Código fuente del sistema
│   ├── ai/             # Comunicación con modelos de lenguaje
│   ├── db/             # Scripts de conexión y consultas PostgreSQL
│   └── processor/      # Lógica de extracción de texto
├── .env.example        # Plantilla de variables de entorno
├── .gitignore          # Archivos excluidos de control de versiones
├── main.py             # Script de ejecución principal
├── README.md           # Documentación técnica
└── requirements.txt    # Dependencias del proyecto
```

---

## Fases del Proyecto

### Fase 1: Infraestructura de Datos
- Configuración de la base de datos PostgreSQL.
- Implementación de la creación dinámica de la columna `resumen`.
- Desarrollo de scripts de conexión base.

### Fase 2: Procesamiento de Documentos
- Integración de librería para lectura de PDFs.
- Implementación de límites de lectura para optimización.
- Manejo de excepciones en archivos sin capa de texto.

### Fase 3: Integración de Modelo de Lenguaje
- Conexión con servicio de inferencia local o remoto.
- Ajuste de instrucciones para generación de resúmenes concisos.
- Pruebas de integración.

### Fase 4: Lógica de Negocio
- Desarrollo del bucle de procesamiento principal.
- Lógica de filtrado para registros pendientes.
- Gestión de errores y continuidad del servicio.

### Fase 5: Automatización y Monitoreo
- Configuración de tareas programadas para ejecución periódica.
- Implementación de registro de eventos.

---

## 🛠️ Cómo Inicializar la Estructura

Para crear esta estructura manualmente, puedes ejecutar:

```bash
mkdir -p data logs src/ai src/db src/processor
touch main.py .env.example requirements.txt PROJECT_STRUCTURE.md
```
