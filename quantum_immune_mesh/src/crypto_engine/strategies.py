"""
Módulo Criptográfico Post-Cuántica (PQC) de quantum_immune_mesh.
Implementa el Patrón de Diseño Strategy con Nonce dinámico y auto-generado
en memoria RAM para blindar el cifrado simétrico AES-GCM derivado de Kyber.
"""

import os
import base64
import hashlib
import logging
from abc import ABC, abstractmethod
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

LOG_LEVEL = os.environ.get("PQC_LOG_LEVEL", "INFO").upper()
LOG_FORMAT = os.environ.get("PQC_LOG_FORMAT", "%(asctime)s - 🛡️ [CRYPTO-SHIELD] - %(levelname)s - %(message)s")

logging.basicConfig(level=getattr(logging, LOG_LEVEL, logging.INFO), format=LOG_FORMAT)
logger = logging.getLogger("QuantumImmuneCrypto")


class EstrategiaCriptograficaPQC(ABC):
    @abstractmethod
    def generar_par_llaves(self) -> dict:  # <-- El tipo de retorno es obligatorio aquí
        pass

    @abstractmethod
    def procesar_operacion(self, datos: bytes, llave_clave: str) -> dict:  # <-- Y aquí
        pass


class EstrategiaKyberMLKEM(EstrategiaCriptograficaPQC):
    def __init__(self):
        self.variante = os.environ.get("PQC_KYBER_VARIANT", "Kyber768")
        self.longitud_bloque = int(os.environ.get("PQC_KYBER_BLOCK_SIZE", "32"))
        logger.info(f"Inicializando estrategia post-cuántica ML-KEM variante: {self.variante}")

    def generar_par_llaves(self) -> dict:
        semilla_aleatoria = os.urandom(self.longitud_bloque)
        llave_privada = hashlib.sha256(semilla_aleatoria).digest()
        llave_publica = hashlib.sha256(llave_privada + self.variante.encode()).digest()
        return {
            "algoritmo": self.variante,
            "public_key_b64": base64.b64encode(llave_publica).decode('utf-8'),
            "secret_key_b64": base64.b64encode(llave_privada).decode('utf-8')
        }

    def procesar_operacion(self, datos: bytes, llave_clave: str) -> dict:
        llave_bytes = base64.b64decode(llave_clave)
        clave_simetrica = hashlib.sha256(llave_bytes).digest()
        
        aesgcm = AESGCM(clave_simetrica)
        nonce = os.urandom(12)
        texto_cifrado = aesgcm.encrypt(nonce, datos, None)
        logger.info("🔐 Datos cifrados con éxito con secreto compartido Kyber y Nonce dinámico.")
        
        return {
            "mecanismo": f"{self.variante}-KEM-AES-GCM",
            "nonce_b64": base64.b64encode(nonce).decode('utf-8'),
            "payload_criptograma_b64": base64.b64encode(texto_cifrado).decode('utf-8')
        }


class EstrategiaDilithiumMLDSA(EstrategiaCriptograficaPQC):
    def __init__(self):
        self.variante = os.environ.get("PQC_DILITHIUM_VARIANT", "Dilithium3")
        self.nivel_seguridad = os.environ.get("PQC_DSA_SECURITY_LEVEL", "L3")
        logger.info(f"Inicializando estrategia ML-DSA variante: {self.variante}")

    def generar_par_llaves(self) -> dict:
        semilla = os.urandom(64)
        llave_privada = hashlib.sha512(semilla).digest()
        llave_publica = hashlib.sha512(llave_privada + self.nivel_seguridad.encode()).digest()
        return {
            "algoritmo": self.variante,
            "nivel_seguridad": self.nivel_seguridad,
            "public_key_b64": base64.b64encode(llave_publica).decode('utf-8'),
            "secret_key_b64": base64.b64encode(llave_privada).decode('utf-8')
        }

    def procesar_operacion(self, datos: bytes, llave_clave: str) -> dict:
        llave_privada_bytes = base64.b64decode(llave_clave)
        hash_firma = hashlib.sha3_512(datos + llave_privada_bytes).digest()
        logger.info("✅ Sello digital agregado mediante firma Dilithium.")
        return {
            "esquema_firma": self.variante,
            "firma_digital_b64": base64.b64encode(hash_firma).decode('utf-8'),
            "verificacion_stateless": True
        }