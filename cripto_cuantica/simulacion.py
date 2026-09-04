import random
from canal_cuantico import preparar_cubit, medir_cubit

def ejecutar_bb84(num_bits=24, espiar=False):
    """
    Simula el protocolo cuántico BB84 completo entre Alice y Bob.
    Si espiar=True, Eve interceptará la comunicación en el medio.
    """
    tipo_canal = "🚨 BAJO ESPIONAJE (EVE INTERCEPTANDO)" if espiar else "🔒 CANAL SEGURO (SIN ESPÍAS)"
    print(f"\n==================================================")
    print(f"📡 SIMULACIÓN BB84: {tipo_canal}")
    print(f"==================================================")
    
    # 1. Alice genera sus bits y bases secretas aleatorias
    alice_bits = [random.randint(0, 1) for _ in range(num_bits)]
    alice_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    
    # 2. Bob elige sus bases aleatorias sin saber las de Alice
    bob_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    bob_resultados = []
    
    # 3. Transmisión de cúbits por el canal cuántico
    for i in range(num_bits):
        # Alice codifica su bit en un circuito/cúbit cuántico
        circuito = preparar_cubit(alice_bits[i], alice_bases[i])
        
        # 🕵️‍♂️ ATAQUE DE EVE: Si está activado, Eve intercepta el cúbit antes que Bob
        if espiar:
            base_eve = random.choice(['Z', 'X'])
            # Al medirlo, Eve fuerza al estado cuántico a colapsar prematuramente
            _ = medir_cubit(circuito, base_eve)
            
        # Bob recibe el cúbit y lo mide en su propia base
        bit_medido = medir_cubit(circuito, bob_bases[i])
        bob_resultados.append(bit_medido)
        
    # 4. DISCUSIÓN PÚBLICA: Alice y Bob revelan sus bases (pero NO sus bits)
    # Solo se quedan con los bits donde ambos usaron la misma base (Tamizado)
    clave_alice = []
    clave_bob = []
    
    for i in range(num_bits):
        if alice_bases[i] == bob_bases[i]:
            clave_alice.append(alice_bits[i])
            clave_bob.append(bob_resultados[i])
            
    # 5. CONTROL DE CALIDAD: Comparan una pequeña porción para detectar intrusos
    errores = sum(1 for a, b in zip(clave_alice, clave_bob) if a != b)
    total_coincidentes = len(clave_alice)
    tasa_error = (errores / total_coincidentes) * 100 if total_coincidentes > 0 else 0
    
    # Mostrar resultados en pantalla
    print(f"Bits originales de Alice:  {' '.join(map(str, alice_bits))}")
    print(f"Bases usadas por Alice:    {' '.join(alice_bases)}")
    print(f"Bases usadas por Bob:      {' '.join(bob_bases)}")
    print(f"Bits medidos por Bob:      {' '.join(map(str, bob_resultados))}\n")
    
    print(f"🔑 Clave filtrada de Alice: {clave_alice}")
    print(f"🔑 Clave filtrada de Bob:   {clave_bob}")
    print(f"📊 Bits útiles logrados:    {total_coincidentes} de {num_bits}")
    print(f"⚠️ Tasa de error medida:    {tasa_error:.2f}%")
    
    # Umbral físico: Si Eve espía, el error estadístico sube cerca al 25%
    if tasa_error > 12.0:
        print("\n❌ 🚨 ¡ALERTA MÁXIMA! Anomalía cuántica detectada.")
        print("   La tasa de error supera el umbral seguro. La clave ha sido descartada.")
    else:
        print("\n✅ 🔒 ¡CONEXIÓN EXITOSA!")
        print("   La tasa de error es baja. La clave es matemáticamente segura para encriptar.")

if __name__ == "__main__":
    # Caso 1: Comunicación limpia
    ejecutar_bb84(num_bits=20, espiar=False)
    print("\n" + "· " * 25 + "\n")
    # Caso 2: Comunicación atacada por un hacker
    ejecutar_bb84(num_bits=20, espiar=True)
