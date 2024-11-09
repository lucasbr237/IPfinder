import requests
from datetime import datetime

def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        
        ip = data.get('ip')
        provider = data.get('org', 'Não disponível')
        city = data.get('city', 'Não disponível')
        region = data.get('region', 'Não disponível')
        country = data.get('country', 'Não disponível')
        timezone = data.get('timezone', 'Não disponível')
        
        # Obtém a hora atual no fuso horário do IP
        if timezone != 'Não disponível':
            time_response = requests.get(f'https://worldtimeapi.org/api/timezone/{timezone}')
            time_data = time_response.json()
            current_time = time_data.get('datetime', 'Hora não disponível')
        else:
            current_time = 'Hora não disponível'
        
        return ip, provider, city, region, country, timezone, current_time
    except Exception as e:
        return f"Erro ao obter informações: {e}"

ip, provider, city, region, country, timezone, current_time = get_ip_info()

print(f"IP Público: {ip}")
print(f"Provedor: {provider}")
print(f"Localização: {city}, {region}, {country}")
print(f"Fuso Horário: {timezone}")
print(f"Hora Atual: {current_time}")
