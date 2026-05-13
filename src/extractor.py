import re

class InvoiceExtractor:
    def __init__(self):
        # Patterns melhorados para lidar com "ruído" entre as palavras
        self.patterns = {
            'cnpj': r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}',
            
            # Pega datas em vários formatos
            'date': r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|\d{2} de [A-Za-z]+ de \d{4}',
            
            # Melhoria: Procura por indicadores de nota e ignora palavras genéricas como 'ELETRONICA'
            # Ele vai buscar o padrão alfanumérico que vem depois de termos de nota
            'invoice_number': r'(?:Nota Fiscal|ID do Documento|INV-|NF-|numero da nota)\s?:?\s?([A-Z0-9]{3,}-[A-Z0-9]+|[A-Z]{2}-\d+)',
            
            # Melhoria: O .*? permite que existam outras palavras (como 'CALCULADO') entre o marcador e o valor
            'total_value': r'(?:TOTAL|LIQUIDO|PAGAR|VALOR).*?(\d{1,3}(?:\.\d{3})*,\d{2})'
        }

    def extract_data(self, text):
        extracted = {}
        
        # Limpamos quebras de linha para o Regex não se perder entre frases
        clean_text = text.replace('\n', ' ')

        # 1. CNPJ
        cnpj_match = re.search(self.patterns['cnpj'], clean_text)
        extracted['cnpj'] = cnpj_match.group(0) if cnpj_match else "Não encontrado"

        # 2. Data
        date_match = re.search(self.patterns['date'], clean_text)
        extracted['date'] = date_match.group(0) if date_match else "Não encontrada"

        # 3. Número da Nota (Usamos findall e pegamos o que parece mais um ID)
        invoice_matches = re.finditer(self.patterns['invoice_number'], clean_text, re.IGNORECASE)
        # Filtramos para evitar pegar "ELETRONICA" ou títulos
        invoice_num = "Não encontrado"
        for m in invoice_matches:
            val = m.group(1)
            if val.upper() != "ELETRONICA":
                invoice_num = val
                break
        extracted['invoice_num'] = invoice_num

        # 4. Valor Total
        value_match = re.search(self.patterns['total_value'], clean_text, re.IGNORECASE)
        extracted['total'] = value_match.group(1) if value_match else "Não encontrado"

        return extracted