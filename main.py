import time, os
from src.db.operations import init_db, get_pending_docs, update_doc_summary
from src.processor.pdf_loader import extract_text
from src.ai.inference import generate_summary

def main():
    print("[INFO] Iniciando servicio de procesamiento.")
    init_db()
    
    while True:
        docs = get_pending_docs(5)
        if not docs:
            print("[INFO] Sin tareas pendientes. Esperando 60s...")
            time.sleep(60)
            continue
            
        print(f"[INFO] Procesando lote de {len(docs)} documentos.")
        for doc_id, path in docs:
            if not os.path.exists(path):
                print(f"[WARN] Archivo no encontrado: {path}")
                continue
                
            text = extract_text(path)
            summary = generate_summary(text) if text else None
            
            if summary and update_doc_summary(doc_id, summary):
                print(f"[OK] Documento ID {doc_id} procesado.")
            else:
                print(f"[ERROR] Fallo en procesamiento de ID {doc_id}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
