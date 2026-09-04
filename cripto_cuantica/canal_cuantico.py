from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def preparar_cubit(bit: int, base: str) -> QuantumCircuit:
    """
    Alice prepara un cúbit basándose en su bit (0 o 1) 
    y la base elegida ('Z' para estándar, 'X' para diagonal).
    """
    circuito = QuantumCircuit(1, 1)
    
    # Si el bit es 1, aplicamos una compuerta X (NOT cuántico) para cambiar de |0> a |1>
    if bit == 1:
        circuito.x(0)
    
    # Si la base es Diagonal (X), aplicamos la compuerta Hadamard (H)
    # Esto pone al cúbit en superposición antes de ser enviado
    if base == 'X':
        circuito.h(0)
        
    return circuito

def medir_cubit(circuito: QuantumCircuit, base_bob: str) -> int:
    """
    Bob recibe el circuito cuántico y lo mide usando su propia base al azar.
    Retorna el bit colapsado (0 o 1).
    """
    # Si Bob decide medir en la base Diagonal (X), debe deshacer la superposición
    # aplicando una compuerta Hadamard antes de realizar la medición.
    if base_bob == 'X':
        circuito.h(0)
        
    # Añadimos la instrucción de medición en el cúbit 0 y guardamos en el bit clásico 0
    circuito.measure(0, 0)
    
    # Inicializamos el simulador local de Qiskit
    simulador = AerSimulator()
    
    # Ejecutamos el circuito una sola vez (shots=1) para simular el paso de un solo fotón
    resultado = simulador.run(circuito, shots=1).result()
    conteo = resultado.get_counts()
    
    # Extraemos el valor del bit medido ('0' o '1') y lo convertimos a entero
    bit_medido = int(list(conteo.keys())[0])
    
    return bit_medido
