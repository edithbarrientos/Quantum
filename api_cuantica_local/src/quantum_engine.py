import os
os.environ["PYTHONWARNINGS"] = "ignore"

import pennylane as qml
from pennylane import numpy as np

# Inicializamos el dispositivo cuántico local en la memoria del contenedor
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def ejecutar_circuito_cuantico(angulo_rotacion):
    """Abre superposición, aplica rotación variable y entrelaza cúbits."""
    qml.Hadamard(wires=0)
    qml.RX(angulo_rotacion, wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])
