import pdfplumber
import os

def testar_leitura():
    pasta = "raw_invoices"
    
    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        print(f"⚠️ A pasta '{pasta}' não foi encontrada! Crie-a e coloque os PDFs nela.")
        return

    arquivos = [f for f in os.listdir(pasta) if f.endswith(".pdf")]
    
    for arquivo in arquivos:
        print(f"\n{'='*40}")
        print(f"📄 LENDO: {arquivo}")
        print(f"{'='*40}")
        
        caminho_completo = os.path.join(pasta, arquivo)
        
        with pdfplumber.open(caminho_completo) as pdf:
            # Pegamos a primeira página (nossas faturas só tem uma)
            pagina = pdf.pages[0]
            texto = pagina.extract_text()
            
            if texto:
                print(texto)
            else:
                print("❌ Não foi possível extrair texto deste PDF.")

if __name__ == "__main__":
    testar_leitura()