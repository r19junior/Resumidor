import time, os
from src.db.operations import init_db, get_pending_docs, update_doc_summary
from src.processor.pdf_loader import extract_text
from src.ai.inference import generate_summary

def main():
    print("🚀 Worker Modulo-Optimizado Iniciado")
    init_db()
    
    while True:
        docs = get_pending_docs(5)
        if not docs:
            print("💤 Esperando 60s...")
            time.sleep(60)
            continue
            
        print(f"📄 Procesando {len(docs)} docs...")
        for doc_id, path in docs:
            if not os.path.exists(path):
                print(f"⚠️ Missing: {path}")
                continue
                
            text = extract_text(path)
            summary = generate_summary(text) if text else None
            
            if summary and update_doc_summary(doc_id, summary):
                print(f"✅ ID {doc_id}: {summary[:40]}...")
            else:
                print(f"❌ Fallo ID {doc_id}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
