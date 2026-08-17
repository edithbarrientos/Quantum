"""
Módulo del Motor Cuántico Local (Quantum Compute Engine).
Encapsula el simulador de hardware virtual de PennyLane y gestiona las operaciones
de álgebra lineal compleja sobre vectores de estado cuánticos en la memoria RAM.
"""

import os
# Desactivamos advertencias de bajo nivel del compilador de C++ de fondo
os.environ["PYTHONWARNINGS"] = "ignore"

import pennylane as qml
from pennylane import numpy as np

# Inicializamos el dispositivo lógico de simulación cuántica nativa (2 Cúbits)
# Estado inicial en el Espacio de Hilbert: |00> (Matriz columna de 4 elementos)
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def ejecutar_circuito_cuantico(angulo_rotacion: float) -> np.tensor:
    """
    Construye y ejecuta un circuito cuántico variacional parametrizado.
    
    Aplica una compuerta Hadamard para abrir superposición y una rotación en el 
    eje X basada en el ángulo de la API web, concluyendo con una compuerta CNOT 
    para forzar un estado entrelazado de Bell máximo de dos partículas.
    
    Parámetros:
        angulo_rotacion (float): Escalar real en radianes inyectado desde el backend.
        
    Retorna:
        np.tensor: Un vector clásico de 4 elementos con las probabilidades netas (|α|^2).
    """
    # PASO A: Superposición uniforme en el cúbit 0 mediante la matriz de Hadamard.
    # Rompe el determinismo clásico: El cúbit ahora es 50% cero y 50% uno a la vez.
    qml.Hadamard(wires=0)
    
    # PASO B: Rotación unitaria en el eje X (RX) basada en el parámetro clásico.
    # Altera de forma continua las amplitudes complejas de probabilidad en la Esfera de Bloch.
    qml.RX(angulo_rotacion, wires=0)
    
    # PASO C: Entrelazamiento Cuántico Máximo mediante la compuerta CNOT.
    # Cúbit control: 0, Cúbit objetivo: 1. Amarra físicamente los dos sistemas cuánticos.
    qml.CNOT(wires=[0, 1])
    
    # PASO D: Extracción de Amplitudes Clásicas (Medición estadística).
    # Retorna la probabilidad al cuadrado absoluto para las combinaciones: [00, 01, 10, 11]
    return qml.probs(wires=[0, 1])
