from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def lanzar_dado_cuantico():
    """
    Crea un circuito de 3 cúbits en superposición para generar
    un número puramente aleatorio entre 1 y 8.
    """
    # 1. Crear circuito con 3 cúbits y 3 bits clásicos
    circuito = QuantumCircuit(3, 3)
    
    # 2. Poner los 3 cúbits en superposición (estado intermedio entre 0 y 1)
    circuito.h(0)
    circuito.h(1)
    circuito.h(2)
    
    # 3. Medir los cúbits y guardar el resultado clásico
    circuito.measure([0, 1, 2], [0, 1, 2])
    
    # 4. Configurar el simulador cuántico local
    simulador = AerSimulator()
    
    # 5. Ejecutar el experimento una sola vez (1 shot)
    resultado = simulador.run(circuito, shots=1).result()
    conteos = resultado.get_counts()
    
    # 6. Procesar el resultado binario (ej. '101') a número entero (base 10)
    resultado_binario = list(conteos.keys())[0]
    numero_entero = int(resultado_binario, 2)
    
    # Sumamos 1 para que el rango sea de 1 a 8 (en vez de 0 a 7)
    return numero_entero + 1, resultado_binario
