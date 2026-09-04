import os
# ⚡ Apagamos todas las advertencias del sistema antes de cargar las librerías
os.environ["PYTHONWARNINGS"] = "ignore"

import warnings
warnings.filterwarnings("ignore")

import pennylane as qml
import torch

# 1. Configurar el dispositivo cuántico virtual (2 cúbits)
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev, interface="torch")
def circuito_cuantico(pesos, una_muestra):
    qml.RY(una_muestra[0], wires=0)
    qml.RY(una_muestra[1], wires=1)
    qml.RX(pesos[0], wires=0)
    qml.RX(pesos[1], wires=1)
    qml.CNOT(wires=[0, 1])
    qml.RY(pesos[2], wires=1)
    return qml.expval(qml.PauliZ(1))

def funcion_costo(pesos, X, Y):
    costo_total = torch.tensor(0.0)
    for x, y in zip(X, Y):
        prediccion = circuito_cuantico(pesos, x)
        costo_total = costo_total + (prediccion - y) ** 2
    return costo_total / len(X)

if __name__ == "__main__":
    print("🧠 Inicializando el Entrenamiento de la IA Cuántica con PyTorch...")
    
    X_entrenamiento = torch.tensor([[0.1, 0.2], [0.8, 0.9], [0.1, 0.9], [0.8, 0.2]], dtype=torch.float32)
    Y_real = torch.tensor([-1.0, 1.0, -1.0, 1.0], dtype=torch.float32)
    pesos = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float32, requires_grad=True)
    optimizador = torch.optim.SGD([pesos], lr=0.4)
    
    print("\n🚀 Comenzando optimización híbrida clásico-cuántica:")
    for epoca in range(6):
        optimizador.zero_grad()
        costo_actual = funcion_costo(pesos, X_entrenamiento, Y_real)
        costo_actual.backward()
        optimizador.step()
        print(f"   -> Época {epoca+1:02d} | Error (Costo): {costo_actual.item():.4f}")
            
    print("\n✅ ¡Entrenamiento completado exitosamente con PyTorch!")
    pesos_lista = pesos.detach().tolist()
    print(f"📐 Pesos cuánticos finales optimizados: {pesos_lista}")
    
    with torch.no_grad():
        dato_prueba = torch.tensor([0.7, 0.85], dtype=torch.float32)
        prediccion_final = circuito_cuantico(pesos, dato_prueba)
        clase = "Clase A" if prediccion_final > 0 else "Clase B"
        print(f"\n🔮 Predicción para nuevo dato [0.7, 0.85]: {prediccion_final.item():.4f} -> Clasificado en: {clase}")
