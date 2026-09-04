"""
Módulo de Factoría de quantum_immune_mesh con Logging Estructurado.
Encapsula la conmutación de familias de objetos criptográficos Kyber/Dilithium.
"""

import os
import logging
from typing import Union

# Uso de importación relativa para mantener feliz al linter estricto de VS Code
from .strategies import EstrategiaKyberMLKEM, EstrategiaDilithiumMLDSA

logger = logging.getLogger("QuantumImmuneCrypto")


class FabricaCriptograficaPQC:
    """Fábrica abstracta parametrizada encargada de despachar las estrategias criptográficas."""

    @staticmethod
    def obtener_motor_pqc_configurado() -> Union[EstrategiaKyberMLKEM, EstrategiaDilithiumMLDSA]:
        """
        Lee dinámicamente la configuración declarativa de la infraestructura
        y retorna la instancia de la estrategia correspondiente registrando el evento.
        """
        tipo_motor = os.environ.get("PQC_ACTIVE_ENGINE", "KYBER").upper()
        logger.debug(f"Interrogando variable PQC_ACTIVE_ENGINE de Kubernetes. Valor detectado: '{tipo_motor}'")

        if tipo_motor == "KYBER":
            logger.info("🏭 [ABSTRACT-FACTORY] Instanciando familia criptográfica de encapsulación ML-KEM (Kyber).")
            return EstrategiaKyberMLKEM()
        elif tipo_motor == "DILITHIUM":
            logger.info("🏭 [ABSTRACT-FACTORY] Instanciando familia criptográfica de firmado asimétrico ML-DSA (Dilithium).")
            return EstrategiaDilithiumMLDSA()
        else:
            logger.critical(f"🚨 [FACTORY-FAILURE] Intento de invocación de motor PQC corrupto: '{tipo_motor}'")
            raise ValueError(f"❌ [CRYPTO-ENGINE] Motor PQC '{tipo_motor}' no soportado en la infraestructura.")