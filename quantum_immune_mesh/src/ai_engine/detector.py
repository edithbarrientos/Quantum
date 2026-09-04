"""
Módulo de Inteligencia Artificial de quantum_immune_mesh.
Implementa un clasificador de anomalías perimetral parametrizado y dinámico
bajo el Patrón de Diseño Singleton. El modelo analiza la firma de tráfico HTTP
y muta las directivas de seguridad según variables inyectadas por Kubernetes.
"""

import os
import sys
import math  # <-- Importamos math nativo para usar la función exponencial ultra rápida

# Intentamos importar Scikit-Learn; si no está, usamos un motor lineal puro nativo
# para garantizar el aislamiento y la resiliencia offline de la malla cuántica.
try:
    from sklearn.linear_model import LogisticRegression
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False


class DetectorAnomaliasIA:
    """Clase Singleton que gobierna el cerebro analítico perimetral de la malla."""

    _instancia = None

    def __new__(cls, *args, **kwargs):
        """Asegura que el modelo de IA exista una sola vez en la memoria RAM global."""
        if cls._instancia is None:
            cls._instancia = super(DetectorAnomaliasIA, cls).__new__(cls)
            cls._instancia._inicializar_modelo_parametrizado()
        return cls._instancia

    def _inicializar_modelo_parametrizado(self):
        """Lee la parametrización de Kubernetes e inicializa los coeficientes del clasificador."""
        # 📊 PARAMETRIZACIÓN DECLARATIVA EXTRACTADA DE LA INFRAESTRUCTURA
        self.umbral_anomalia = float(os.environ.get("AI_UMBRAL_ANOMALIA", "0.75"))
        self.nombre_modelo = os.environ.get("AI_MODEL_NAME", "AegisCoreClassifier")
        
        # Guardamos los pesos como flotantes primitivos de Python para optimizar la CPU en runtime
        self.w_payload = float(os.environ.get("AI_WEIGHT_PAYLOAD", "0.05"))
        self.w_burst = float(os.environ.get("AI_WEIGHT_BURST", "0.12"))
        self.w_entropy = float(os.environ.get("AI_WEIGHT_ENTROPY", "0.83"))
        self.sesgo_ia = float(os.environ.get("AI_BIAS", "-1.5"))

        if HAS_SKLEARN:
            # Si sklearn está presente, creamos el objeto formal requerido por la arquitectura
            import numpy as np
            self.modelo = LogisticRegression()
            self.modelo.coef_ = np.array([[self.w_payload, self.w_burst, self.w_entropy]])
            self.modelo.intercept_ = np.array([self.sesgo_ia])
            self.modelo.classes_ = np.array([0, 1])  # Corrección: Clases añadidas correctamente
        else:
            self.modelo = None

    def evaluar_trafico_perimetral(self, tamano_payload: int, velocidad_rafaga: int, entropia_token: float) -> dict:
        """
        Analiza las métricas clásicas de la petición HTTP y predice el nivel de riesgo.
        Aplica aritmética nativa para calcular la probabilidad sin sobrecargar la CPU.
        """
        # OPTIMIZACIÓN CRÍTICA: Multiplicación aritmética directa sin asignación matricial de NumPy.
        # Evita la reserva de memoria dinámica por cada petición HTTP entrante.
        z = (self.w_payload * tamano_payload) + (self.w_burst * velocidad_rafaga) + (self.w_entropy * entropia_token) + self.sesgo_ia
        
        try:
            # Función de activation Sigmoide nativa y optimizada: P(y=1|x) = 1 / (1 + e^-z)
            probabilidad_anomalia = 1.0 / (1.0 + math.exp(-z))
        except OverflowError:
            # Control de desbordamiento matemático si 'z' es un número extremadamente negativo
            probabilidad_anomalia = 0.0
            
        # Desafío contra el umbral configurable de Kubernetes
        es_anomalia = bool(probabilidad_anomalia >= self.umbral_anomalia)

        # Determinación dinámica del nivel de mitigación exigido para API Management
        if probabilidad_anomalia > 0.90:
            nivel_mitigacion = "CRITICAL_LOCKOUT"  # Bloqueo total de la IP
        elif es_anomalia:
            nivel_mitigacion = "UPGRADE_PQC_REQUIREMENT"  # Exigir tokens Dilithium de máxima seguridad
        else:
            nivel_mitigacion = "STANDARD_JWT_VERIFICATION"  # Tráfico clásico autorizado

        return {
            "modelo_auditor": self.nombre_modelo,
            "probabilidad_amenaza": round(float(probabilidad_anomalia), 4),
            "detección_anomalia": es_anomalia,
            "estrategia_mitigacion_sugerida": nivel_mitigacion,
            "umbral_configurado": self.umbral_anomalia
        }