import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def crear_oraculo(circuito, secreto):
    """
    El Oráculo: Modifica la fase (invierte el estado) del elemento secreto.
    Para 2 cúbits, usamos combinaciones de compuertas CZ (Controlled-Z) y X.
    """
    # Si el secreto es '00', invertimos los cúbits antes y después del CZ
    if secreto == '00':
        circuito.x([0, 1])
        circuito.cz(0, 1)
        circuito.x([0, 1])
    # Si el secreto es '01'
    elif secreto == '01':
        circuito.x(1)
        circuito.cz(0, 1)
        circuito.x(1)
    # Si el secreto es '10'
    elif secreto == '10':
        circuito.x(0)
        circuito.cz(0, 1)
        circuito.x(0)
    # Si el secreto es '11'
    elif secreto == '11':
        circuito.cz(0, 1)

def crear_difusor(circuito):
    """
    El Difusor (Operador de Grover): Amplifica la amplitud del estado marcado
    haciendo una reflexión sobre la media de todas las probabilidades.
    """
    circuito.h([0, 1])
    circuito.x([0, 1])
    circuito.cz(0, 1)
    circuito.x([0, 1])
    circuito.h([0, 1])

def ejecutar_grover(elemento_secreto):
    print(f"🔎 Iniciando algoritmo de Grover para buscar el estado secreto: '{elemento_secreto}'")
    
    # Creamos un circuito con 2 cúbits cuánticos y 2 bits clásicos
    circuito = QuantumCircuit(2, 2)
    
    # Paso 1: Poner todos los estados en superposición uniforme (00, 01, 10, 11 tienen 25% de probabilidad)
    circuito.h([0, 1])
    circuito.barrier()
    
    # Paso 2: Aplicar el Oráculo para marcar nuestra respuesta secreta
    crear_oraculo(circuito, elemento_secreto)
    circuito.barrier()
    
    # Paso 3: Aplicar el Difusor para amplificar la probabilidad del elemento marcado
    crear_difusor(circuito)
    circuito.barrier()
    
    # Paso 4: Medir los cúbits
    circuito.measure([0, 1], [0, 1])
    
    # Ejecutar en el simulador
    simulador = AerSimulator()
    resultado = simulador.run(circuito, shots=100).result()
    conteos = resultado.get_counts()
    
    print("\n📊 Resultados de la medición cuántica (sobre 100 intentos):")
    for estado, veces in conteos.items():
        porcentaje = (veces / 100) * 100
        print(f"   -> Estado '{estado}': medido {veces} veces ({porcentaje:.1f}%)")
        
    # Encontrar cuál fue el ganador
    ganador = max(conteos, key=conteos.get)
    if ganador == elemento_secreto:
        print(f"\n✅ ¡ÉXITO! La computadora cuántica amplificó y encontró el secreto '{ganador}' con precisión matemática.")
    else:
        print("\n❌ Error en las amplitudes del circuito.")

if __name__ == "__main__":
    # Puedes cambiar el secreto por '00', '01', '10' o '11'
    SECRETO = "01"
    ejecutar_grover(SECRETO)
