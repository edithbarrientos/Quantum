import time
from motor_cuantico import lanzar_dado_cuantico

def iniciar_juego():
    print("=========================================")
    print("🎲 ¡BIENVENIDO AL JUEGO DE DADOS CUÁNTICO! 🎲")
    print("=========================================")
    print("Este juego utiliza superposición cuántica real")
    print("para generar números 100% aleatorios.")
    print("=========================================\n")
    
    while True:
        input("Presiona [ENTER] para lanzar el dado cuántico...")
        
        print("\n🔮 Poniendo los cúbits en superposición...")
        time.sleep(0.5)
        print("⚡ Midiendo el circuito cuántico (el estado colapsa)...")
        time.sleep(0.5)
        
        # Llamamos a la función cuántica que creamos en el otro archivo
        numero, binario = lanzar_dado_cuantico()
        
        print(f"\n🎉 ¡Resultado obtenido!")
        print(f"   -> Código binario medido: {binario}")
        print(f"   -> Valor del dado (1-8): ¡{numero}!\n")
        
        # Preguntar al usuario si quiere seguir jugando
        jugar_de_nuevo = input("¿Quieres lanzar otra vez? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("\n👋 ¡Gracias por jugar con física cuántica! Hasta la próxima.")
            break
        print("-" * 41 + "\n")

if __name__ == "__main__":
    iniciar_juego()
