import pandas as pd
import os

class InvoiceExporter:
    def __init__(self, output_folder="data"):
        self.output_folder = output_folder
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def save_to_excel(self, data_list, filename="fechamento_contabil.xlsx"):
        """Converte a lista de dicionários em um arquivo Excel."""
        if not data_list:
            print("⚠️ Nenhum dado para exportar.")
            return

        # Criamos um DataFrame (a 'planilha' do Pandas)
        df = pd.DataFrame(data_list)

        # Reorganizamos as colunas para ficar mais bonito
        cols = ['arquivo', 'invoice_num', 'date', 'cnpj', 'total']
        df = df[cols]

        # Renomeamos para português para o cliente final
        df.columns = ['Arquivo', 'Nº da Nota', 'Data Emissão', 'CNPJ Prestador', 'Valor Total']

        caminho_final = os.path.join(self.output_folder, filename)
        
        # Salvamos o Excel
        df.to_excel(caminho_final, index=False)
        print(f"\n✅ Sucesso! Relatório gerado em: {caminho_final}")