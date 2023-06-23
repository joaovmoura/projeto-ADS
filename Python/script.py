import requests
import concurrent.futures

URL = "http://192.168.15.7:5001/hello/klebervitinhomarcosluiz"

# Função para enviar uma requisição
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {url}: {str(e)}")

# Número de requisições a serem enviadas
num_requests = 10000

# Envia as requisições em paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Inicia as requisições em paralelo
    futures = [executor.submit(send_request, URL) for _ in range(num_requests)]

    # Espera todas as requisições serem concluídas
    concurrent.futures.wait(futures)

