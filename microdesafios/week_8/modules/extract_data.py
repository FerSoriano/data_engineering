import pandas as pd
from anonymizedf.anonymizedf import anonymize

CSV_FILE = '../data.csv'

def encrypt_data() -> pd.DataFrame:
    df = pd.read_csv(CSV_FILE,delimiter=';')

    an = anonymize(df)
    an.fake_names("Comisionado")
    an.fake_dates("Fecha")
    an.fake_whole_numbers("Telefono")

    return df

if __name__ == '__main__':
    data = encrypt_data()
    print(data)
