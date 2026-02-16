# 📘 Documentación: Enriquecimiento de Base de Datos con Llama 3

Este sistema automatiza la lectura de documentos PDF almacenados en PostgreSQL, utiliza un modelo de lenguaje Llama 3 (vía Ollama o API) para generar resúmenes de una sola línea y actualiza la base de datos de forma autónoma.

## 🏗️ 1. Arquitectura del Sistema

El flujo sigue un modelo de **Worker (Trabajador)** que monitorea la base de datos para procesar registros pendientes.

### Componentes principales:
- **Capa de Datos (PostgreSQL):** Almacena la ruta del PDF y el resultado del resumen.
- **Capa de Procesamiento (Python):** Extrae el texto del PDF y gestiona la lógica de control.
- **Capa de Inteligencia (Llama 3):** Genera la síntesis semántica del contenido.

## 🛠️ 2. Requisitos Técnicos

### Dependencias de Software
- PostgreSQL 12+
- Python 3.9+
- Ollama (con el modelo `llama3` descargado)

### Librerías de Python
Instalación: `pip install psycopg2-binary pymupdf requests python-dotenv`

| Librería | Función |
| :--- | :--- |
| `psycopg2-binary` | Conexión y ejecución de comandos en PostgreSQL. |
| `pymupdf` | Extracción de texto de archivos PDF de alta velocidad. |
| `requests` | Comunicación con el servidor de IA (Ollama). |
| `python-dotenv` | Gestión segura de credenciales. |

## 📝 3. Diseño del Proceso (Workflow)

### Fase 1: Preparación Automática
El sistema verifica la existencia de la columna de destino. Si no existe, la crea dinámicamente:

```sql
ALTER TABLE documentos ADD COLUMN IF NOT EXISTS resumen TEXT;
```

### Fase 2: Extracción y Filtrado
El script selecciona únicamente registros que cumplen dos condiciones:
1. Tienen un PDF asociado.
2. La columna `resumen` está vacía (`NULL` o `''`).

### Fase 3: Inferencia de IA (Prompting)
Se utiliza una técnica de **Few-Shot** o **Instruction Prompting** para asegurar que el resumen sea de una sola línea:

> "Sintetiza el siguiente texto en una oración de máximo 15 palabras. Responde directamente con el resumen."

## 🚀 4. Guía de Implementación

### Configuración del Entorno (`.env`)
```env
DB_HOST=localhost
DB_NAME=mi_base_de_datos
DB_USER=admin
DB_PASS=password123
TABLE_NAME=expedientes
PDF_COLUMN=path_archivo
```

### Automatización con Cron (Linux)
Para que el proceso sea automático con cada registro que se agregue, se programa una tarea en el sistema:

```bash
# Ejecutar cada 10 minutos
*/10 * * * * /usr/bin/python3 /ruta/al/proyecto/main.py
```

## ⚠️ 5. Manejo de Casos Especiales

- **PDFs de Solo Imagen:** Si el PDF no tiene capa de texto, el script devuelve un error. *Sugerencia: Implementar Tesseract OCR en una fase futura.*
- **Documentos Extensos:** Para optimizar tokens, solo se leen las primeras 3 páginas del documento, lo cual suele ser suficiente para un resumen ejecutivo.
- **Control de Errores:** Si la IA falla, el script no detiene el proceso; simplemente salta al siguiente registro para no bloquear la cola.

## 📊 6. Beneficios del Diseño

- **Eficiencia:** No procesa registros que ya tienen resumen.
- **Escalabilidad:** Puede manejar miles de registros de forma asíncrona.
- **Consistencia:** El prompt asegura que todos los resúmenes tengan un formato uniforme.
