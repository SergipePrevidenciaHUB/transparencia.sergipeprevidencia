"""Concilia remuneração na tabela unificada, mantendo a conciliação cadastral."""
from testar_servidores import main
from integrar_servidores import PAY_SOURCE
from openpyxl import load_workbook
import unicodedata

def check_payroll_source():
    book = load_workbook(PAY_SOURCE, read_only=True, data_only=True)
    rows = [row for sheet in book for row in list(sheet.values)[1:] if any(v is not None for v in row)]
    book.close()
    assert len(rows) == 2312, 'Fonte de remuneração alterada; rever conciliação.'
    def normalized(row):
        text = ' '.join(str(v) for v in row if v is not None).casefold()
        return ''.join(c for c in unicodedata.normalize('NFD', text) if not unicodedata.combining(c))
    interns = [row for row in rows if 'estagiar' in normalized(row) and 'universit' in normalized(row)]
    assert len(interns) == 714, 'Conferir exclusão dos estagiários universitários.'
    assert len(rows) - len(interns) == 1598

if __name__ == '__main__':
    check_payroll_source()
    main()
