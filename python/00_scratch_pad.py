# public_instruments_matching_pi['Fund'][329]['basic_pi_matches'][0]['exchange']

for security_type in d:
    for item in security_type:
        eod_symbol = item[eod_symbol]
        eod_symbol_dict = {
        'EOD_SYMBOL': eod_symbol['Code'],
        'EOD_NAME': eod_symbol['Name'],
        'EOD_CURRENCY': eod_symbol['Currency'],
        'EOD_COUNTRY': eod_symbol['Country'],
        'EOD_ISIN': eod_symbol['Isin'],
        'EOD_SECURITY_TYPE': eod_symbol['Type'],
        'EOD_EXCHANGE': eod_symbol['Exchange']
        }

        for qm in item['qualified_match']:
            

        multiple_matches = item['basic_pi_matches']


