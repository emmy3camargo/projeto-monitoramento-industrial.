import random
import time

def monitorar_temperatura():
    print("SISTEMA DE MONITORAMENTO - SETOR SECADOR")
    print("---------------------------------------")
    
    for i in range(1, 6):
        temp = random.randint(50, 120)
        print(f"Leitura {i}: {temp}°C")
        
        if temp > 100:
            print("⚠️ ALERTA: Temperatura Crítica! Acionar resfriamento.")
        elif temp < 70:
            print("❄️ AVISO: Temperatura baixa para secagem ideal.")
        else:
            print("✅ Status: Operação Normal.")
        
        time.sleep(1)

if __name__ == "__main__":
    monitorar_temperatura()
