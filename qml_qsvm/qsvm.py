import os
# Silenciamos advertencias del sistema y de C++ de fondo
os.environ["PYTHONWARNINGS"] = "ignore"

import pennylane as qml
from pennylane import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 1. Configurar el hardware cuántico virtual (2 cúbits)
dev = qml.device("default.qubit", wires=2)

# 2. Definir el mapeo de datos cuánticos (Feature Map)
@qml.qnode(dev)
def circuito_mapeo(x):
    qml.AngleEmbedding(features=x, wires=[0, 1], rotation='X')
    return qml.state()

# 3. Calcular el Kernel Cuántico (Solapamiento o distancia entre dos datos x1 y x2)
def kernel_cuantico(x1, x2):
    estado_1 = circuito_mapeo(x1)
    estado_2 = circuito_mapeo(x2)
    fidelidad = np.abs(np.dot(np.conj(estado_1), estado_2)) ** 2
    return fidelidad

# 4. Construir la matriz de Kernel Cuántico para el algoritmo SVM
def calcular_matriz_kernel(X1, X2):
    matriz = np.zeros((len(X1), len(X2)))
    for i in range(len(X1)):
        for j in range(len(X2)):
            matriz[i, j] = kernel_cuantico(X1[i], X2[j])
    return matriz

if __name__ == "__main__":
    print("📡 --- INICIALIZANDO CLASIFICADOR DE KERNEL CUÁNTICO ---")
    
    # Generamos datos clásicos (4 puntos complejos en un plano)
    X_entrenamiento = np.array([[0.1, 0.5], [0.9, 0.2], [0.2, 0.8], [0.8, 0.7]])
    Y_entrenamiento = np.array([0, 1, 0, 1])  # 0: Clase A, 1: Clase B
    
    print("\n🔮 Calculando Matriz de Relaciones Cuánticas (Espacio de Hilbert)...")
    matriz_entrenamiento = calcular_matriz_kernel(X_entrenamiento, X_entrenamiento)
    
    print("🤖 Entrenando clasificador SVM clásico con el Kernel Cuántico...")
    modelo_svm = SVC(kernel="precomputed")
    modelo_svm.fit(matriz_entrenamiento, Y_entrenamiento)
    
    # Evaluamos la precisión en el entrenamiento
    predicciones_entrenamiento = modelo_svm.predict(matriz_entrenamiento)
    precision = accuracy_score(Y_entrenamiento, predicciones_entrenamiento) * 100
    print(f"✅ ¡Modelo acoplado con éxito! Precisión de entrenamiento: {precision:.1f}%")
    
    # 5. TESTEO: Clasificar un dato completamente nuevo
    print("\n🚀 Probando el modelo con un dato desconocido...")
    X_nuevo = np.array([[0.15, 0.45]])  # Muy parecido al primer punto de la Clase 0
    
    matriz_testeo = calcular_matriz_kernel(X_nuevo, X_entrenamiento)
    clase_predicha = modelo_svm.predict(matriz_testeo)
    nombre_clase = "Clase A (Azul)" if clase_predicha[0] == 0 else "Clase B (Rojo)"
    print(f"🎯 El dato nuevo {X_nuevo} pertenece a la: {nombre_clase}")
