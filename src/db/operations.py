import os
from .connection import get_db_cursor

TABLE = os.getenv('TABLE_NAME', 'documentos')
COL_PDF = os.getenv('PDF_COLUMN', 'ruta_archivo')
COL_SUM = os.getenv('SUMMARY_COLUMN', 'resumen')

def init_db():
    with get_db_cursor(commit=True) as cur:
        cur.execute(f"ALTER TABLE {TABLE} ADD COLUMN IF NOT EXISTS {COL_SUM} TEXT;")
        print(f"✅ DB Inicializada.")

def get_pending_docs(limit=10):
    with get_db_cursor() as cur:
        cur.execute(f"SELECT id, {COL_PDF} FROM {TABLE} WHERE {COL_PDF} IS NOT NULL AND ({COL_SUM} IS NULL OR {COL_SUM} = '') LIMIT %s;", (limit,))
        return cur.fetchall() or []

def update_doc_summary(doc_id, summary):
    with get_db_cursor(commit=True) as cur:
        cur.execute(f"UPDATE {TABLE} SET {COL_SUM} = %s WHERE id = %s", (summary, doc_id))
        return True
