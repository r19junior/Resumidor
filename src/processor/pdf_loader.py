import fitz

def extract_text(pdf_path, max_pages=3):
    """Extrae texto de las primeras páginas de un PDF."""
    try:
        with fitz.open(pdf_path) as doc:
            return "\n".join([page.get_text() for page in doc[:max_pages]]).strip()
    except Exception as e:
        print(f"[WARN] Error en lectura de PDF {pdf_path}: {e}")
        return ""
