from datetime import datetime

def hitung_hari_sejak_lahir(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    delta = today - birthdate
    return delta.days