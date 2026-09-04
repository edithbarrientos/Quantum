import os
os.environ["PYTHONWARNINGS"] = "ignore"

import pennylane as qml
from pennylane import numpy as np

# 1. CONFIGURACIÓN DEL HARDWARE CUÁNTICO VIRTUAL (3 cúbits)
dev = qml.device("default.qubit", wires=3)

# Topología de la red logística (Conexiones en triángulo)
conexiones = [(0, 1), (1, 2), (0, 2)]

# 2. EL QNODE CUÁNTICO PRINCIPAL (CALCULADOR DE ENERGÍA)
@qml.qnode(dev)
def qnode_energia(parametros):
    """
    Recibe el array completo 'parametros'. El desglose ocurre DENTRO de la zona cuántica
    para que Autograd pueda calcular las derivadas parciales de forma nativa.
    """
    gamma = parametros[0]
    beta = parametros[1]
    
    # Capa A: Superposición uniforme (Hadamard)
    for i in range(3):
        qml.Hadamard(wires=i)
        
    # Capa B: Oráculo de Costo (Hamiltoniano del Problema)
    for u, v in conexiones:
        qml.CNOT(wires=[u, v])
        qml.RZ(2 * gamma, wires=v)
        qml.CNOT(wires=[u, v])
        
    # Capa C: Mezclador Cuántico
    for i in range(3):
        qml.RX(2 * beta, wires=i)
        
    # Definimos los operadores de corte reales (1 - ZiZj) / 2
    corte1 = 0.5 * (qml.Identity(0) - qml.PauliZ(0) @ qml.PauliZ(1))
    corte2 = 0.5 * (qml.Identity(1) - qml.PauliZ(1) @ qml.PauliZ(2))
    corte3 = 0.5 * (qml.Identity(0) - qml.PauliZ(0) @ qml.PauliZ(2))
    
    # Retornamos el valor de expectación puro de las conexiones cortadas
    return qml.expval(corte1 + corte2 + corte3)

# 3. EL QNODE SECUNDARIO (EXTRACTOR DE PROBABILIDADES)
@qml.qnode(dev)
def qnode_probabilidades(parametros):
    """
    Reutiliza la misma estructura para extraer los porcentajes de colapso binarios.
    """
    gamma = parametros[0]
    beta = parametros[1]
    
    for i in range(3):
        qml.Hadamard(wires=i)
    for u, v in conexiones:
        qml.CNOT(wires=[u, v])
        qml.RZ(2 * gamma, wires=v)
        qml.CNOT(wires=[u, v])
    for i in range(3):
        qml.RX(2 * beta, wires=i)
        
    return qml.probs(wires=[0, 1, 2])

# 4. FUNCIÓN DE COSTO CLÁSICA EXTREMADAMENTE LIMPIA
def funcion_costo(parametros):
    # Pasamos el objeto 'parametros' íntegro al QNode cuántico
    # Multiplicamos por -1.0 clásicamente para forzar la maximización de cortes
    return -1.0 * qnode_energia(parametros)

# 5. BLOQUE DE EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    print("📡 --- INICIALIZANDO OPTIMIZADOR LOGÍSTICO REAL (MAX-CUT) ---")
    
    # Ángulos iniciales estándar de la literatura científica para romper mínimos locales
    parametros_iniciales = np.array([1.0, 0.2], requires_grad=True)
    
    # Configuramos el optimizador clásico
    optimizador = qml.GradientDescentOptimizer(stepsize=0.1)
    parametros = parametros_iniciales
    
    print("\n🚀 La IA clásica busca maximizar los cortes en la red:")
    for paso in range(10):
        # El optimizador altera y rastrea el array 'parametros' de forma unificada
        parametros, costo_actual = optimizador.step_and_cost(funcion_costo, parametros)
        print(f"   -> Iteración {paso+1:02d} | Costo de Optimización: {costo_actual:.4f}")
        
    print("\n✅ ¡Optimización Combinatoria Completada!")
    print(f"📐 Ángulos óptimos: Gamma={parametros[0]:.4f}, Beta={parametros[1]:.4f}")
    
    # 6. MUESTREO DE LA RESPUESTA LOGÍSTICA MÁS EFICIENTE
    probabilidades = qnode_probabilidades(parametros)
    estados = ["000", "001", "010", "011", "100", "101", "110", "111"]
    
    print("\n📊 Distribución de rutas calculada por la física cuántica:")
    for est, prob in zip(estados, probabilidades):
        if prob > 0.05:
            print(f"   -> Configuración de Red '{est}': Probabilidad {prob*100:.1f}%")
            
    mejor_ruta = estados[np.argmax(probabilidades)]
    print(f"\n🏆 ¡Ruta sugerida por el QAOA para máxima eficiencia logística!: {mejor_ruta}")
