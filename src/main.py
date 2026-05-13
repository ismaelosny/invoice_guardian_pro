import pdfplumber
import os
from extractor import InvoiceExtractor
from exporter import InvoiceExporter # Importamos o novo módulo

def main():
    pasta = "raw_invoices"
    extractor = InvoiceExtractor()
    exporter = InvoiceExporter() # Inicializamos o exportador
    
    resultados_finais = []

    print("🚀 Iniciando processamento de faturas...")

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta, arquivo)
            
            with pdfplumber.open(caminho) as pdf:
                texto_bruto = pdf.pages[0].extract_text()
                dados = extractor.extract_data(texto_bruto)
                dados['arquivo'] = arquivo
                resultados_finais.append(dados)

    # Exportar para Excel
    exporter.save_to_excel(resultados_finais)

if __name__ == "__main__":
    main()