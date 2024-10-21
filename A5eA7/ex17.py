# Programa para calcular o tempo de download

# Variáveis de entrada
tamanho_arquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Informe a velocidade da Internet (em Mbps): "))

# Conversão da velocidade de Mbps para MBps (1 Mbps = 0.125 MBps)
velocidade_internet_MBps = velocidade_internet * 0.125

# Cálculo do tempo de download em segundos
tempo_segundos = tamanho_arquivo / velocidade_internet_MBps

# Conversão do tempo de segundos para minutos
tempo_minutos = tempo_segundos / 60

# Exibir o resultado
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")
