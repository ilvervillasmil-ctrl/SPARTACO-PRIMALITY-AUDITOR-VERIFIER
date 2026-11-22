# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
# ▓╔════════════════════════════════════════════════════════════════════╗▓
# ▓║                                                                    ║▓
# ▓║                 OM 3 3 7   /   S P A R T A C O                     ║▓
# ▓║          INDEPENDENT MATHEMATICAL EVIDENCE AUDITOR                 ║▓
# ▓║               MATHEMATICAL AUDIT BY ELIMINATION                    ║▓
# ▓║                  AUDITOR_DESCARTE  ·  v0.9.1                       ║▓
# ▓║                                                                    ║▓
# ▓╚════════════════════════════════════════════════════════════════════╝▓
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#
# PROJECT:             OMEGA 337 / SPARTACO SECURITY
# COMPONENT:           INDEPENDENT EVIDENCE VERIFIER
# MODULE:              auditor_descarte.py
# MODULE ID:           AUDITOR_DESCARTE
# ARCHITECTURE:        MODULAR MATHEMATICAL VERIFICATION
#
# AUTHOR / IP OWNER:   Ilver Villasmil
# COPYRIGHT:           (c) 2026 Ilver Villasmil
#
# MODULE VERSION:      0.9.1
# CONTRACT VERSION:    1.0
# CONTRACT SCHEMA:     VPSI-CONTRACT-1.0
# DEVELOPMENT STATUS:  DRAFT / UNDER DEVELOPMENT
# VISIBILITY:          PUBLIC CANDIDATE
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ==============================================================================
#  I. MISSION / MISIÓN
# ==============================================================================
#
# Independently evaluate mathematical evidence associated with an integer N.
#
# Evaluar evidencias matemáticas asociadas a un entero N mediante relaciones
# verificables, sin reproducir el procedimiento utilizado para descubrirlo.
#
# PRINCIPLE OF SEPARATION:
#
#     THE DISCOVERY ENGINE IS NOT THE INDEPENDENT VERIFIER.
#
#     QUIEN DESCUBRE NO ES QUIEN VERIFICA.
#
# ==============================================================================
#  II. MATHEMATICAL FOUNDATION / FUNDAMENTO MATEMÁTICO
# ==============================================================================
#
# For every integer N > 1:
#
#     PRIME(N) <=> NOT COMPOSITE(N)
#
# Esta equivalencia lógica no sustituye una demostración matemática.
# La primalidad requiere evidencia suficiente para excluir rigurosamente
# todos los casos de composición aplicables.
#
# ==============================================================================
#  III. EVIDENCE CHANNELS / VÍAS DE EVIDENCIA
# ==============================================================================
#
#     [01] FACTOR    Exact nontrivial divisor verification
#     [02] MODULO    Modular divisibility verification
#     [03] PINZA     External primality-function consultation
#     [04] TD        Algebraic identity N = 2p + d
#     [05] RESTO     Divisibility checks against supplied residues
#     [06] TANA      Exact deterministic certificate verification
#
# The auditor distinguishes verifiable mathematical relations from
# declarations, labels, and unsupported claims.
#
# ==============================================================================
#  IV. AUDIT STATES / ESTADOS DE AUDITORÍA
# ==============================================================================
#
#     COMPUESTO_VERIFICADO
#         A nontrivial divisor of N has been verified.
#
#     PRIMO_POR_DESCARTE
#         Reserved for a mathematically sufficient primality proof.
#
#     EVIDENCIA_INSUFICIENTE
#         Available evidence does not establish the required conclusion.
#
#     CONTRADICCION_DETECTADA
#         A declared mathematical relationship is inconsistent.
#
# ==============================================================================
#  V. ARCHITECTURAL BOUNDARY / LÍMITE ARQUITECTÓNICO
# ==============================================================================
#
# THIS MODULE:
#     - Receives mathematical evidence.
#     - Recalculates supported arithmetic relationships.
#     - Detects certain inconsistencies.
#     - Confirms compositeness through verified nontrivial divisors.
#     - Returns structured audit results.
#
# THIS MODULE DOES NOT:
#     - Reproduce the private discovery algorithm.
#     - Modify the OMEGA 337 engine.
#     - Expose private optimization techniques.
#     - Accept a declared primality state as mathematical proof.
#
# ==============================================================================
#  VI. INTEGRATION / INTEGRACIÓN
# ==============================================================================
#
# PRIVATE MATHEMATICAL ENGINE
#             |
#             v
#     MATHEMATICAL EVIDENCE
#             |
#             v
#      AUDITOR_DESCARTE
#             |
#             v
#      STRUCTURED AUDIT RESULT
#
# Integration context:
#     OM337  module (mathematical ecosystem)
#     SPARTACO SECURITY FRAMEWORK modular contractual architecture
#     VPSI-CONTRACT-1.0
#
# ==============================================================================
#  VII. INTELLECTUAL PROPERTY AND LICENSE / PROPIEDAD INTELECTUAL Y LICENCIA
# ==============================================================================
#
# Copyright (c) 2026 Ilver Villasmil.
# All rights reserved except as expressly licensed.
#
# This component is licensed under the SPARTACO Primality Auditor Community
# License v1.0 (see the LICENSE file in this repository).
#
#     FREE:        Personal, educational, and non-commercial research use.
#     COMMERCIAL:  Commercial use, including internal use by a company,
#                  requires a separate written commercial license.
#     SERVICES:    Additions, maintenance, and customization are provided
#                  only under a separate written agreement and for a fee.
#
# Este componente se licencia bajo la SPARTACO Primality Auditor Community
# License v1.0 (ver el archivo LICENSE de este repositorio). El uso es libre
# para fines personales, educativos y de investigación no comercial. El uso
# comercial, incluido el uso interno de una empresa, requiere una licencia
# comercial aparte.
#
# The private mathematical engines, optimization methods, security
# orchestration components, and other proprietary implementations of
# SPARTACO SECURITY, OM337, and UIS-OMEGA are NOT licensed by this license
# and remain outside its scope.
#
# Third-party components keep their own licenses.
#
# Commercial licensing: Ilver Villasmil · Ilvervillasmil@gmail.com
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# ==============================================================================
# END OF MODULE HEADER
# ==============================================================================
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional
from typing import Any, Dict
from math import gcd, isqrt
import json
import sys

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 01 — MODULE SECURITY DECLARATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Declares module identity, visibility, and responsibilities. ┃
# ┃  Exposes auditar and combinar as module capabilities.        ┃
# ┃  Specifies version, declaration key, and no persistence.     ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
SEGURIDAD: Dict[str, Any] = {
    "id": "AUDITOR_DESCARTE",
    "nombre": "auditor_descarte",
    "visibilidad": "PUBLICO",

    "hace": (
        "Independently evaluates mathematical evidence "
        "produced by the discovery engine through factor, "
        "modular, Pinza, TD, remainder and TANA certificate verification. "
        "Classifies results as COMPUESTO_VERIFICADO, "
        "PRIMO_POR_DESCARTE, EVIDENCIA_INSUFICIENTE, "
        "or CONTRADICCION_DETECTADA. "
        "Does not reproduce the discovery process."
    ),

    "version": "1",
    "clave_declaracion": "capacidades_recurso",

    "capacidades_recurso": [
        "auditar",
        "combinar",
        "verificar_certificado_tana",
    ],

    "persistencia": "Ninguna.",
}



# ◀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ◀  SECTION B1 — BASIC COMPOSITE FILTER
# ◀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ┌──────────────────────────────────────────────────────────────────────┐
# │  Performs deterministic early composite detection using exact      │
# │  divisibility by 3, 2, 7, and 5, in that strict order.              │
# │  Returns a verified divisor and quotient when compositeness is     │
# │  established. Otherwise, the candidate passes to further audit.    │
# └──────────────────────────────────────────────────────────────────────┘

def FDP(N: int):
    """
    Deterministic basic composite filter.

    Returns:
        ("COMPUESTO", divisor, quotient)
            When a nontrivial exact divisor is found.

        ("SUPERA_FILTRO", None, None)
            When no divisor is found in (3, 2, 7, 5).
    """
    if N < 2:
        raise ValueError("N must be greater than or equal to 2")

    for d in (3, 2, 7, 5):
        if N > d and N % d == 0:
            return ("COMPUESTO", d, N // d)

    return ("SUPERA_FILTRO", None, None)


# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 02 — MATHEMATICAL AUDIT STATES
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Defines the four canonical mathematical audit states.       ┃
# ┃  Distinguishes composition, primality, and insufficient      ┃
# ┃  evidence from detected mathematical contradictions.         ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
class EstadoAuditor(Enum):
    COMPUESTO_VERIFICADO = "COMPUESTO_VERIFICADO"
    PRIMO_POR_DESCARTE = "PRIMO_POR_DESCARTE"
    EVIDENCIA_INSUFICIENTE = "EVIDENCIA_INSUFICIENTE"
    CONTRADICCION_DETECTADA = "CONTRADICCION_DETECTADA"

# ┏━━━ 2.1 — MATHEMATICAL EVIDENCE RECORD ━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Stores evidence source, assertion, and supporting data.     ┃
# ┃  Records conclusiveness and the stated elimination reason.   ┃
# ┃  Provides a structured representation of each audit input.   ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
@dataclass
class Evidencia:
    via: str
    afirmacion: str
    datos: dict = field(default_factory=dict)
    concluyente: bool = False
    descarte: str = ""

# ┏━━━ 2.2 — STRUCTURED AUDIT RESULT ━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Associates an integer with its resulting audit state.      ┃
# ┃  Preserves collected evidence and the audit justification.  ┃
# ┃  Includes the originating engine status when provided.      ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
@dataclass
class ResultadoAuditor:
    n: int
    estado: EstadoAuditor
    evidencias: list[Evidencia] = field(default_factory=list)
    justificacion: str = ""
    motor: str = ""

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 03 — EXACT FACTOR VERIFICATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Checks whether a supplied factor divides N exactly.         ┃
# ┃  Requires a nontrivial divisor strictly between 1 and N.     ┃
# ┃  Returns evidence of composition when the check succeeds.    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def via_factor(n: int, factor: Optional[int]) -> Evidencia:
    """Vía Path 1: exact factor. If it exists and divides [the expression], the composition is proven."""
    if factor and 1 < factor < n and n % factor == 0:
        return Evidencia("factor", f"{factor} divide a {n}", {"factor": factor}, True, "proven composition")
    return Evidencia("factor", "without a factor", {}, False, "")

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 04 — MODULAR DIVISIBILITY VERIFICATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Evaluates divisibility against supplied modulus values.     ┃
# ┃  Detects zero remainders for moduli greater than one.        ┃
# ┃  Records the first matching modulus as mathematical evidence.┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def via_modulo(n: int, modulos: list[int]) -> Evidencia:
    """Vía Path 2: congruences. If n ≡ 0 (mod m) that m prime < n, there is composition."""
    for m in modulos:
        if 1 < m < n and n % m == 0:
            return Evidencia("modulo", f"{n} ≡ 0 (mod {m})", {"modulo": m}, True, "composición por módulo")
    return Evidencia("modulo", "sin congruencia nula", {"modulos": modulos}, False, "")

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 05 — PINZA EXTERNAL CONSULTATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Consults the external canal_bits.es_primo function.         ┃
# ┃  Records its Boolean primality or composition declaration.   ┃
# ┃  Returns nonconclusive evidence if consultation fails.       ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def via_pinza(n: int) -> Evidencia:
    """Vía Path 3: Original pinza. Consult without modification."""
    try:
        from .canal_bits import es_primo
        result = es_primo(n)
        if result is True:
            return Evidencia("pinza", "Pinza declara primo", {"resultado": True}, True, "descarte por Pinza")
        if result is False:
            return Evidencia("pinza", "Pinza declara compuesto", {"resultado": False}, True, "composición por Pinza")
    except Exception:
        pass
    return Evidencia("pinza", "Pinza not available", {}, False, "")

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 06 — ALGEBRAIC IDENTITY VERIFICATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Validates the declared identity N = 2p + d.                 ┃
# ┃  Records consistency when the arithmetic relation holds.     ┃
# ┃  Flags a contradiction when the identity does not match N.   ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def via_td(n: int, p: Optional[int], d: Optional[int]) -> Evidencia:
    """Vía Path 4: 2p+d transformation. Verifies the identity if declared."""
    if p is not None and d is not None:
        if 2 * p + d == n:
            return Evidencia("td", f"N = 2*{p}+{d}", {"p": p, "d": d}, False, "identidad algebraica")
        return Evidencia("td", "identidad 2p+d rota", {"p": p, "d": d}, True, "contradicción")
    return Evidencia("td", "sin contexto UIS", {}, False, "")

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 07 — RESIDUE DIVISIBILITY VERIFICATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Evaluates divisibility using supplied residue values.       ┃
# ┃  Records a divisor when N has a zero remainder.              ┃
# ┃  Returns nonconclusive evidence when none is detected.       ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def via_remainder(n: int, residuos: list[int]) -> Evidencia:
    """Vía Path 5: Remainder theorem. Verifies declared remainders."""
    if not residuos:
        return Evidencia("remainder", "no divisors supplied", {}, False, "")
    for r in residuos:
        if 1 < r < n and n % r == 0:
            return Evidencia("remainder", f"{r} divides {n}", {"remainder": r}, True, "composition by remainder")
    return Evidencia("remainder", "residuos coherentes", {"residuos": residuos}, False, "")
    


# ══════════════════════════════════════════════════════════════════════════════
# PART 07B — UIS–TANA–OMEGA DETERMINISTIC PRIMALITY CERTIFICATION
# ══════════════════════════════════════════════════════════════════════════════
# Implements Clamp (exact trial division), Pocklington, and T–MA1.
# The auditor independently verifies ALL mathematical conditions.
# It never trusts engine-provided labels or declared certification states.
# ══════════════════════════════════════════════════════════════════════════════
class CertificadoInvalido(ValueError):
    pass


def verificar_certificado_tana(certificado: dict, objetivo: Optional[int] = None) -> dict:
    """
    Verifies a finite chain of certificates using exact integer arithmetic.

    Supports both the treatise's plain JSON format and the OMEGA337-CANON-1 container.
    Does not use probabilistic tests or rely on the state declared by the engine.
    Raises CertificadoInvalido upon the first unmet prerequisite.
    """
    try:
        if not isinstance(certificado, dict):
            raise CertificadoInvalido("certificado no es objeto")
        cont = certificado.get("certificado", certificado)
        arbol = cont["arbol"]
        N = int(cont["N"])
        bits = int(certificado.get("identidad", {}).get("bits_N", certificado.get("bits_N", N.bit_length())))
        if objetivo is not None and N != objetivo:
            raise CertificadoInvalido("objetivo distinto del certificado")
        if not isinstance(arbol, list) or not arbol:
            raise CertificadoInvalido("cadena vacía")
        if N <= 1 or N.bit_length() != bits:
            raise CertificadoInvalido("N o longitud de bits incorrectos")
        certificados = set()
        detalles = []
        for i, nodo in enumerate(arbol):
            n = int(nodo["n"])
            tipo = nodo["tipo"]
            if n <= 1 or n in certificados:
                raise CertificadoInvalido(f"nodo {i}: n inválido o repetido")
            if tipo == "pinza":
                # División hasta sqrt(n), no confiar en un booleano externo.
                for divisor in range(2, isqrt(n) + 1):
                    if n % divisor == 0:
                        raise CertificadoInvalido(f"nodo {i}: raíz compuesta, divisor {divisor}")
            elif tipo == "pock":
                F, u, a = (int(nodo[k]) for k in ("F", "u", "a"))
                if n <= 2 or n % 2 != 1 or F not in certificados or u < 1 or n != u * F + 1:
                    raise CertificadoInvalido(f"nodo {i}: dependencia o identidad pock inválida")
                # Teorema 6.2 y refinamiento 2-ádico del tratado.
                if not (F * F > n or (F % 2 == 1 and (2 * F + 1) ** 2 > n)):
                    raise CertificadoInvalido(f"nodo {i}: cota pock insuficiente")
                if pow(a, n - 1, n) != 1:
                    raise CertificadoInvalido(f"nodo {i}: Fermat incumplido")
                if gcd(pow(a, u, n) - 1, n) != 1:
                    raise CertificadoInvalido(f"nodo {i}: condición de orden incumplida")
            elif tipo == "multi_pock":
                ancestros = nodo["ancestros"]
                if n <= 2 or n % 2 == 0 or not isinstance(ancestros, list) or len(ancestros) < 2:
                    raise CertificadoInvalido(f"nodo {i}: estructura multi_pock inválida")
                vistos = set()
                F = 1
                for anc in ancestros:
                    q, a = int(anc["q"]), int(anc["a"])
                    if q in vistos or not (2 < q < n) or q % 2 == 0 or q not in certificados:
                        raise CertificadoInvalido(f"nodo {i}: ancestro inválido o repetido")
                    if (n - 1) % q or pow(a, n - 1, n) != 1:
                        raise CertificadoInvalido(f"nodo {i}: divisibilidad o Fermat inválidos")
                    if gcd(pow(a, (n - 1) // q, n) - 1, n) != 1:
                        raise CertificadoInvalido(f"nodo {i}: orden ancestral inválido")
                    vistos.add(q)
                    F *= q
                if (F + 1) ** 2 <= n:
                    raise CertificadoInvalido(f"nodo {i}: cota multiancestral insuficiente")
            else:
                raise CertificadoInvalido(f"nodo {i}: tipo no implementado: {tipo}")
            certificados.add(n)
            detalles.append({"indice": i, "tipo": tipo, "bits": n.bit_length(), "verificado": True})
        if int(arbol[-1]["n"]) != N:
            raise CertificadoInvalido("último nodo distinto del objetivo")
        return {"primo_certificado": True, "bits": bits, "nodos": len(arbol), "detalles": detalles}
    except (KeyError, TypeError, ValueError) as exc:
        if isinstance(exc, CertificadoInvalido):
            raise
        raise CertificadoInvalido(f"certificado mal formado: {exc}") from exc


def via_certificado_tana(n: int, certificado: Optional[dict]) -> Evidencia:
    """
    Vía path 6 (verification): records evidence without verifying it;
    combinar() performs the validation exactly once.

    Never marks an external declaration as conclusive. The final verdict
    can only result from verificar_certificado_tana() within 
    """
    if certificado is None:
        return Evidencia("tana", "sin certificado", {}, False, "")
    return Evidencia("tana", "certificado recibido; pendiente de verificación",
                     {"certificado": certificado}, False, "")


# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 08 — EVIDENCE CONSOLIDATION AND VERDICT
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Revalidates algebraic identities and nontrivial divisors.   ┃
# ┃  Prioritizes contradictions before composition evidence.     ┃
# ┃  Returns insufficient evidence when no proof is established. ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def combinar(n: int, evidencias: list[Evidencia], motor_estado: str = "") -> ResultadoAuditor:
    """Combines the evidence. Certifies only through verifiable relationships.
    Does not trust declared booleans or labels."""
    for e in evidencias:
        if e.via == "td" and e.datos.get("p") is not None:
            p, d = e.datos["p"], e.datos["d"]
            if 2 * p + d != n:
                return ResultadoAuditor(n, EstadoAuditor.CONTRADICCION_DETECTADA, evidencias, "2p+d does not match N", motor_estado)
    for e in evidencias:
        if e.via == "factor" and e.datos.get("factor"):
            f = e.datos["factor"]
            if 1 < f < n and n % f == 0:
                return ResultadoAuditor(n, EstadoAuditor.COMPUESTO_VERIFICADO, evidencias, f"{f} divide a {n}", motor_estado)
    for e in evidencias:
        if e.via == "modulo" and e.datos.get("modulo"):
            m = e.datos["modulo"]
            if 1 < m < n and n % m == 0:
                return ResultadoAuditor(n, EstadoAuditor.COMPUESTO_VERIFICADO, evidencias, f"{m} divide a {n}", motor_estado)
    for e in evidencias:
        if e.via == "remainder" and e.datos.get("remainder"):
            r = e.datos["remainder"]
            if 1 < r < n and n % r == 0:
                return ResultadoAuditor(n, EstadoAuditor.COMPUESTO_VERIFICADO, evidencias, f"{r} divide a {n}", motor_estado)
    for e in evidencias:
        if e.via == "tana" and isinstance(e.datos.get("certificado"), dict):
            try:
                informe = verificar_certificado_tana(e.datos["certificado"], objetivo=n)
                return ResultadoAuditor(n, EstadoAuditor.PRIMO_POR_DESCARTE, evidencias,
                    f"Certificación TANA exacta: {informe['nodos']} nodos, {informe['bits']} bits", motor_estado)
            except CertificadoInvalido:
                pass
    return ResultadoAuditor(n, EstadoAuditor.EVIDENCIA_INSUFICIENTE, evidencias, "without a verifiable exclusion", motor_estado)


# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 09 — MATHEMATICAL AUDIT ENTRY POINT
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Coordinates all five mathematical evidence channels.        ┃
# ┃  Collects results without modifying the discovery engine.    ┃
# ┃  Delegates the final audit verdict to combinar().            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def auditar(n: int, factor: Optional[int] = None, p: Optional[int] = None,
            d: Optional[int] = None, modulos: Optional[list[int]] = None,
            residuos: Optional[list[int]] = None, motor_estado: str = "",
            certificado_tana: Optional[dict] = None) -> ResultadoAuditor:
    """Audit interface. Does not modify the engine."""
    evs = [
        via_factor(n, factor),
        via_modulo(n, modulos or []),
        via_pinza(n),
        via_td(n, p, d),
        via_remainder(n, residuos or []),
        via_certificado_tana(n, certificado_tana),
    ]
    return combinar(n, evs, motor_estado)




__all__ = ["SEGURIDAD", "EstadoAuditor", "Evidencia", "ResultadoAuditor", "CertificadoInvalido", "verificar_certificado_tana", "via_certificado_tana", "combinar", "auditar"]


# ==============================================================================
#  NOTE ON PINZA / NOTA SOBRE PINZA
# ==============================================================================
#
# PINZA (channel 03) is NOT enabled in this public distribution.
#
# It consults an external function (canal_bits.es_primo) that belongs to the
# private OM337 engine and is not included here. In this distribution that
# channel always reports "Pinza not available" and contributes no verdict.
# The public auditor does not depend on it: its verdicts come only from the
# FACTOR, MODULO, TD, RESTO and TANA channels.
#
# PINZA (vía 03) NO está habilitada en esta distribución pública. Consulta una
# función externa del motor privado OM337 que no se incluye aquí. El auditor
# público no depende de ella. El motor privado y sus vías quedan fuera del
# alcance de esta distribución.
#
# ==============================================================================
if __name__ == "__main__":
    # Python 3.11 limits the conversion of long decimal integers by default.
    # It is disabled only in the CLI interface for giant certificates.
    sys.set_int_max_str_digits(0) if hasattr(sys, "set_int_max_str_digits") else None
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python auditor_descarte.py certificate.json")
    from pathlib import Path
    try:
        certificado = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        resultado = verificar_certificado_tana(certificado)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"Certificate rejected: {exc}")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
