# Documentación: Enriquecimiento de Base de Datos con Llama 3

Este sistema automatiza la lectura de documentos PDF almacenados en PostgreSQL, utiliza un modelo de lenguaje Llama 3 (vía Ollama o API) para generar resúmenes de una sola línea y actualiza la base de datos de forma autónoma.

## 1. Arquitectura del Sistema

El flujo sigue un modelo de **Worker** que monitorea la base de datos para procesar registros pendientes.

### Componentes principales:
- **Capa de Datos (PostgreSQL):** Almacena la ruta del PDF y el resultado del resumen.
- **Capa de Procesamiento (Python):** Extrae el texto del PDF y gestiona la lógica de control.
- **Capa de Inteligencia (Llama 3):** Genera la síntesis semántica del contenido.

## 2. Requisitos Técnicos

### Dependencias de Software
- PostgreSQL 12+
- Python 3.9+
- Ollama (con el modelo `llama3` descargado)

### Librerías de Python
Instalación: `pip install -r requirements.txt`

| Librería | Función |
| :--- | :--- |
| `psycopg2-binary` | Conexión y ejecución de comandos en PostgreSQL. |
| `pymupdf` | Extracción de texto de archivos PDF. |
| `requests` | Comunicación con el servidor de inferencia. |
| `python-dotenv` | Gestión de configuración. |

## 3. Diseño del Proceso

### Fase 1: Preparación Automática
El sistema verifica la existencia de la columna de destino. Si no existe, la crea dinámicamente:

```sql
ALTER TABLE documentos ADD COLUMN IF NOT EXISTS resumen TEXT;
```

### Fase 2: Extracción y Filtrado
El script selecciona únicamente registros que cumplen dos condiciones:
1. Tienen un PDF asociado.
2. La columna `resumen` está vacía (`NULL` o `''`).

### Fase 3: Inferencia
Se utiliza una técnica de *Instruction Prompting* para asegurar que el resumen sea conciso:

> "Sintetiza el siguiente texto en una oración de máximo 15 palabras."

## 4. Guía de Implementación

### Configuración del Entorno (`.env`)
```env
DB_HOST=localhost
DB_NAME=mi_base_de_datos
DB_USER=admin
DB_PASS=password123
TABLE_NAME=expedientes
PDF_COLUMN=path_archivo
```

### Automatización
Para ejecución periódica, configure una tarea programada (Cron en Linux o Task Scheduler en Windows) que ejecute:

```bash
python /ruta/al/proyecto/main.py
```

## 5. Manejo de Casos Especiales

- **PDFs de Solo Imagen:** Si el PDF no tiene capa de texto, el script devuelve un error controlado.
- **Documentos Extensos:** Para optimizar recursos, solo se procesan las primeras páginas del documento.
- **Control de Errores:** El sistema registra fallos y continúa con el siguiente registro para mantener la disponibilidad.

## 6. Beneficios del Diseño

- **Eficiencia:** Evita el reprocesamiento de registros.
- **Escalabilidad:** Arquitectura diseñada para manejo asíncrono de volúmenes altos.
- **Consistencia:** Formato uniforme en los resúmenes generados.
