# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
# ▓╔════════════════════════════════════════════════════════════════════╗▓
# ▓║                                                                    ║▓
# ▓║                 OM 3 3 7   /   S P A R T A C O                     ║▓
# ▓║          INDEPENDENT MATHEMATICAL EVIDENCE AUDITOR                 ║▓
# ▓║               MATHEMATICAL AUDIT BY ELIMINATION                    ║▓
# ▓║                  AUDITOR_DESCARTE  ·  v0.9.3                       ║▓
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
# MODULE VERSION:      0.9.3
# CONTRACT VERSION:    1.0
# CONTRACT SCHEMA:     VPSI-CONTRACT-1.0
# DEVELOPMENT STATUS:  CONTINUOUS EVOLUTION
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
import hashlib
import json
import re
import sys
import time

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
        "verificar_nodo_certificado",
        "inspeccionar_certificado",
        "verificar_numero_manual",
        "verificar_paso_manual",
        "FDP",
    ],

    "persistencia": "Ninguna.",
}



# ◀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ◀  SECTION B1 — BASIC COMPOSITE FILTER
# ◀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ┌──────────────────────────────────────────────────────────────────────┐
# │  Performs deterministic early composite detection using exact        │
# │  divisibility by 3, 2, 7, and 5, in that strict order.               │
# │  Returns a verified divisor and quotient when compositeness is       │
# │  established. Otherwise, the candidate passes to further audit.      │
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
# ┃  PINZA is private OM337 engine logic, NOT included here.     ┃
# ┃  No import is attempted; the channel always reports that it  ┃
# ┃  is unavailable and contributes no verdict.                  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def via_pinza(n: int) -> Evidencia:
    """Vía Path 3: PINZA belongs to the private OM337 engine and is NOT part of
    this public distribution (see NOTE ON PINZA). It never imports private code
    and never contributes a verdict; it reports its unavailability explicitly."""
    return Evidencia("pinza", "Pinza: motor privado no incluido en el verificador público / "
                     "private engine not included in the public verifier",
                     {"disponible": False}, False, "")

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
    

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 07B — UIS–TANA–OMEGA DETERMINISTIC PRIMALITY CERTIFICATION
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ══════════════════════════════════════════════════════════════════════════════
# Implements Clamp (exact trial division), Pocklington, T–MA1 and the Lucas
# closure T–B2 / T–B5 (TANA.md §6–§7, §11). Public, classical mathematics only:
# Pocklington (1914), Lehmer (1930), Morrison (1975), Jacobi symbol,
# Miller–Rabin with the Sinclair (2011) base set for N < 2^64.
# The auditor independently verifies ALL mathematical conditions.
# It never trusts engine-provided labels or declared certification states.
# The integer N is the single source of truth: bits, digits and SHA-256(N)
# are always recomputed from N.
# ══════════════════════════════════════════════════════════════════════════════

# ┏━━━ 7B.0 — PUBLIC MILLER–RABIN · NOT PART OF THE ENGINE ━━━━━━━━━━┓
# ┃┃ Miller–Rabin (Miller 1976, Rabin 1980) is a classical public   ┃┃
# ┃┃ test, included only as a tool so this verifier can check other ┃┃
# ┃┃ primes typed by hand.                                          ┃┃
# ┃┃ It does NOT belong to the OM337 engine: it never builds,       ┃┃
# ┃┃ approves or replaces an OM337 certificate.                     ┃┃
# ┃┃                                                                ┃┃     
# ┃┃ • N < 2^64: Sinclair's 7 bases form a complete set, so the     ┃┃
# ┃┃    result is deterministic (a proof, not a probability).       ┃┃
# ┃┃ • N ≥ 2^64: used only to search for a compositeness witness.   ┃┃
# ┃┃    A witness proves N composite; with no witness the verdict   ┃┃
# ┃┃    is EVIDENCIA_INSUFICIENTE. Primality is never claimed from  ┃┃
# ┃┃    the probabilistic test.                                     ┃┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# Deterministic upper bound for `pinza` leaves (exact trial division up to
# floor(sqrt(n))). Real repository leaves are <= 32 bits; a forged larger
# leaf is rejected immediately instead of hanging the verifier.
MAX_PINZA_LEAF_BITS = 48

# Public deterministic Miller–Rabin base set, valid for every N < 2^64
# (J. Sinclair, 2011).
BASES_MR_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
# Small prime bases used only to search for a compositeness witness (N >= 2^64).
BASES_TESTIGO = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
LIMITE_DIVISION_MANUAL = 100000

_ENTERO_RE = re.compile(r"[+-]?[0-9]+")
_CLAVES_GEMELAS_EN = ("type", "rule", "ancestors")

# ┏━━━ 7B.1 — BILINGUAL REJECTION EXCEPTIONS ━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ CertificadoInvalido: rejected certificate. str(exc) keeps the    ┃
# ┃ Spanish message (backward compatible), .en carries the English   ┃
# ┃ one and .informe the partial report, so the interface shows how  ┃
# ┃ far the chain was verified.                                      ┃
# ┃ EnteroInvalido: input that is not an exact integer, with its .es ┃
# ┃ / .en messages.                                                  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
class CertificadoInvalido(ValueError):
    """Rejected certificate. str(exc) keeps the Spanish message (backward
    compatible); .en carries the English message; .informe a partial report."""

    def __init__(self, mensaje: str, en: Optional[str] = None, informe: Optional[dict] = None):
        super().__init__(mensaje)
        self.es = mensaje
        self.en = en or mensaje
        self.informe = informe


class EnteroInvalido(ValueError):
    def __init__(self, es: str, en: str):
        super().__init__(f"{es} / {en}")
        self.es = es
        self.en = en

# ┏━━━ 7B.2 — EXACT INTEGER INPUT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ _sin_limite_digitos: removes Python's 4300-digit int↔str limit   ┃
# ┃ (set_int_max_str_digits(0)), so N of any size (e.g. 50,381 bits  ┃
# ┃ = 15,166 digits) converts exactly.                               ┃
# ┃ entero_estricto: accepts an int (never bool) or a clean string   ┃
# ┃ ^[+-]?[0-9]+$. Rejects 71.9, 1e3, True, NaN, non-ASCII digits    ┃
# ┃ and garbage. Optional lower bound `minimo`.                      ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _sin_limite_digitos() -> None:
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)


def entero_estricto(valor: Any, etiqueta: str = "valor", minimo: Optional[int] = None) -> int:
    """Exact integer parsing. Accepts int (never bool) or a clean base-10
    string ^[+-]?[0-9]+$ (surrounding whitespace ignored). Rejects floats,
    scientific notation, NaN, booleans, internal garbage and other types."""
    if isinstance(valor, bool):
        raise EnteroInvalido(f"{etiqueta}: un booleano no es un entero", f"{etiqueta}: a boolean is not an integer")
    if isinstance(valor, int):
        x = valor
    elif isinstance(valor, str):
        s = valor.strip()
        if not _ENTERO_RE.fullmatch(s):
            muestra = s if len(s) <= 24 else s[:24] + "…"
            raise EnteroInvalido(f"{etiqueta}: se esperaba un entero decimal exacto, recibido '{muestra}'",
                                 f"{etiqueta}: expected an exact decimal integer, got '{muestra}'")
        x = int(s, 10)
    else:
        tipo = type(valor).__name__
        raise EnteroInvalido(f"{etiqueta}: se esperaba un entero exacto, recibido {tipo}",
                             f"{etiqueta}: expected an exact integer, got {tipo}")
    if minimo is not None and x < minimo:
        raise EnteroInvalido(f"{etiqueta}: debe ser ≥ {minimo}", f"{etiqueta}: must be ≥ {minimo}")
    return x

# ┏━━━ 7B.3 — IDENTITY OF N (SINGLE SOURCE OF TRUTH) ━━━━━━━━━━━━━━━━┓
# ┃ sha256_decimal: SHA256-ASCII-DECIMAL-v1 =                        ┃
# ┃ SHA-256(ASCII(str(N))).                                          ┃
# ┃ identidad_entero: N_str, bits = N.bit_length() = ⌊log₂ N⌋ + 1,   ┃
# ┃ digits = len(str(N)), sha256_N. Every value is computed from the ┃
# ┃ integer N alone.                                                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def sha256_decimal(x: int) -> str:
    """SHA256-ASCII-DECIMAL-v1: SHA-256 of the ASCII decimal representation."""
    _sin_limite_digitos()
    return hashlib.sha256(str(x).encode("ascii")).hexdigest()


def identidad_entero(x: int) -> dict:
    _sin_limite_digitos()
    s = str(x)
    return {"N_str": s, "bits": x.bit_length(), "digitos": len(s.lstrip("-")),
            "sha256_N": hashlib.sha256(s.encode("ascii")).hexdigest()}

# ┏━━━ 7B.4 — JACOBI SYMBOL (a/n) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Exact Jacobi symbol for odd n > 0, without factoring n, in O(log ┃
# ┃ n) steps by quadratic reciprocity:                               ┃
# ┃ • (2/n) = −1  ⇔  n ≡ 3, 5 (mod 8)                                ┃
# ┃ • (a/n)(n/a) = −1  ⇔  a ≡ n ≡ 3 (mod 4)                          ┃
# ┃ Returns 0 when gcd(a, n) > 1.                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def jacobi(a: int, n: int) -> int:
    """Exact Jacobi symbol (a/n) for odd n > 0."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("jacobi: n must be odd and positive")
    a %= n
    resultado = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                resultado = -resultado
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            resultado = -resultado
        a %= n
    return resultado if n == 1 else 0

# ┏━━━ 7B.5 — LUCAS SEQUENCES U_k, V_k (mod n) ━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Sequences of x² − Px + Q: U₀ = 0, U₁ = 1, V₀ = 2, V₁ = P, D = P² ┃
# ┃ − 4Q.                                                            ┃
# ┃ • doubling: U₂ₖ = Uₖ·Vₖ,  V₂ₖ = Vₖ² − 2Qᵏ                          ┃
# ┃ • add one: Uₖ₊₁ = (P·Uₖ + Vₖ)/2,  Vₖ₊₁ = (D·Uₖ + P·Vₖ)/2           ┃
# ┃ Division by 2 uses the inverse (n + 1)/2 mod n (n odd). O(log k) ┃
# ┃ steps, one per bit of k.                                         ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def lucas_uv(P: int, Q: int, k: int, n: int) -> tuple[int, int]:
    """(U_k(P,Q) mod n, V_k(P,Q) mod n) by binary doubling, O(log k) steps.
    U_0=0, U_1=1, V_0=2, V_1=P. Requires n odd > 1 (uses the inverse of 2)."""
    if n <= 1 or n % 2 == 0:
        raise ValueError("lucas_uv: n must be odd and > 1")
    if k < 0:
        raise ValueError("lucas_uv: k must be >= 0")
    D = P * P - 4 * Q
    inv2 = (n + 1) // 2
    U, V, Qk = 0, 2 % n, 1
    for bit in bin(k)[2:]:
        U, V = (U * V) % n, (V * V - 2 * Qk) % n
        Qk = (Qk * Qk) % n
        if bit == "1":
            U, V = ((P * U + V) * inv2) % n, ((D * U + P * V) * inv2) % n
            Qk = (Qk * Q) % n
    return U, V

# ┏━━━ 7B.6 — MILLER–RABIN COMPOSITENESS WITNESS ━━━━━━━━━━━━━━━━━━━━┓
# ┃ Write n − 1 = 2ˢ·d with d odd. `a` is a witness iff a^d ≢ 1 and  ┃
# ┃ a^(2ʳ·d) ≢ −1 (mod n) for every 0 ≤ r < s.                       ┃
# ┃ If n were prime, the only square roots of 1 mod n are ±1, so the ┃
# ┃ chain would reach 1 through −1; a witness therefore proves n     ┃
# ┃ composite.                                                       ┃
# ┃ Returns False for a ≡ 0, ±1. On its own it never proves          ┃
# ┃ primality.                                                       ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def testigo_miller_rabin(n: int, a: int) -> bool:
    """True iff `a` is a Miller–Rabin witness of compositeness for odd n > 3."""
    a %= n
    if a in (0, 1, n - 1):
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x in (1, n - 1):
        return False
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return False
    return True

# ┏━━━ 7B.7 — REPORT HELPERS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ _corto: short form (first 18 digits … last 8, bits) used only    ┃
# ┃ inside messages; every computation uses the full integer.        ┃
# ┃ _chk: one check record {id, formula, ok, detail_es, detail_en}.  ┃
# ┃ _s: serializes ints as decimal strings, because a JavaScript     ┃
# ┃ Number loses precision above 2^53.                               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _corto(x: int, max_dig: int = 40) -> str:
    s = str(x)
    return s if len(s) <= max_dig else f"{s[:18]}…{s[-8:]} ({x.bit_length()} bits)"


def _chk(ident: str, formula: str, ok: bool, es: str, en: str) -> dict:
    return {"id": ident, "formula": formula, "ok": bool(ok), "detail_es": es, "detail_en": en}


def _s(x: Any) -> Any:
    """Serializes ints as decimal strings (JS never loses precision)."""
    if isinstance(x, bool):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, list):
        return [_s(v) for v in x]
    if isinstance(x, dict):
        return {k: _s(v) for k, v in x.items()}
    return x

# ◢▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◣
# ◢  PART 7B.8 — NODE THEOREMS
# ◥▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◤
# ┏━━━  — NODE THEOREMS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Each theorem returns (checks, refs, params, ok).                 ┃
# ┃ • A failed mathematical condition is recorded as a failed        ┃
# ┃    check, never raised; evaluation stops at the first failure    ┃
# ┃    to avoid useless costly exponentiations.                      ┃
# ┃ • refs = ancestors the node needs proven earlier in the          ┃
# ┃    chain.                                                        ┃
# ┃ • Malformed input raises EnteroInvalido / KeyError /             ┃
# ┃    TypeError.                                                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ┏━━━ TEO-5 — PINZA (EXACT TRIAL DIVISION) ━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ If n = a·b with 1 < a ≤ b then a ≤ √n, so: n prime ⇔ no d ∈ [2,  ┃
# ┃ ⌊√n⌋] divides n.                                                 ┃
# ┃ Bound bits(n) ≤ 48 (≈ 2²³ odd divisors at most): a forged large  ┃
# ┃ leaf is rejected at once instead of hanging the verifier.        ┃
# ┃ Checks: PZ-1 n ≥ 2 · PZ-2 bit bound · PZ-3 no divisor.           ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _teorema_pinza(n: int, nodo: dict):
    checks = []
    params: dict = {}
    if not (n >= 2):
        checks.append(_chk("PZ-1", "n ≥ 2", False, "n debe ser ≥ 2", "n must be ≥ 2"))
        return checks, [], params, False
    checks.append(_chk("PZ-1", "n ≥ 2", True, "n ≥ 2", "n ≥ 2"))
    b = n.bit_length()
    if b > MAX_PINZA_LEAF_BITS:
        checks.append(_chk("PZ-2", f"bits(n) ≤ {MAX_PINZA_LEAF_BITS}", False,
                           f"Hoja de {b} bits supera la cota determinista de {MAX_PINZA_LEAF_BITS} bits para división exacta",
                           f"{b}-bit leaf exceeds the deterministic {MAX_PINZA_LEAF_BITS}-bit bound for exact trial division"))
        return checks, [], params, False
    checks.append(_chk("PZ-2", f"bits(n) ≤ {MAX_PINZA_LEAF_BITS}", True, f"{b} bits ≤ {MAX_PINZA_LEAF_BITS}", f"{b} bits ≤ {MAX_PINZA_LEAF_BITS}"))
    r = isqrt(n)
    params["raiz_entera"] = r
    divisor = None
    if n % 2 == 0 and n != 2:
        divisor = 2
    else:
        d = 3
        while d <= r:
            if n % d == 0:
                divisor = d
                break
            d += 2
    if divisor is not None:
        checks.append(_chk("PZ-3", "∀ d ∈ [2, ⌊√n⌋]: n mod d ≠ 0  (TEO-5)", False,
                           f"divisor encontrado: {divisor} (n = {divisor} · {n // divisor})",
                           f"divisor found: {divisor} (n = {divisor} · {n // divisor})"))
        return checks, [], params, False
    checks.append(_chk("PZ-3", "∀ d ∈ [2, ⌊√n⌋]: n mod d ≠ 0  (TEO-5)", True,
                       f"ningún divisor hasta ⌊√n⌋ = {r}: n es primo (división exacta completa)",
                       f"no divisor up to ⌊√n⌋ = {r}: n is prime (complete exact trial division)"))
    return checks, [], params, True

# ┏━━━ TEO-9 — POCKLINGTON ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Premise: n − 1 = u·F with F prime proven earlier (ref).          ┃
# ┃ If a^(n−1) ≡ 1 and gcd(a^u − 1, n) = 1, then for every prime ℓ | ┃
# ┃ n the order of a mod ℓ divides uF but not u, so F | ord | ℓ − 1, ┃
# ┃ i.e. ℓ ≡ 1 (mod F).                                              ┃
# ┃ • F² > n  ⇒  ℓ ≥ F + 1 > √n                                      ┃
# ┃ • F odd: ℓ ≡ 1 (mod 2F)  ⇒  ℓ ≥ 2F + 1; enough if (2F + 1)² >    ┃
# ┃    n                                                             ┃
# ┃ No prime factor ≤ √n, so n is prime. Checks T3-1, T3-3 … T3-6.   ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _teorema_pock(n: int, nodo: dict):
    F = entero_estricto(nodo["F"], "F")
    u = entero_estricto(nodo["u"], "u")
    a = entero_estricto(nodo["a"], "a")
    params = {"F": F, "u": u, "a": a}
    checks = []

    def fin(ok):
        return checks, [F], params, ok

    ok = n > 2 and n % 2 == 1
    checks.append(_chk("T3-1", "n ≡ 1 (mod 2) ∧ n > 2", ok, "n es impar y mayor que 2" if ok else "n debe ser impar y > 2",
                       "n is odd and greater than 2" if ok else "n must be odd and > 2"))
    if not ok:
        return fin(False)
    ok = u >= 1 and n - 1 == u * F
    checks.append(_chk("T3-3", "n − 1 = u · F", ok, "identidad exacta n − 1 = u·F" if ok else "n − 1 ≠ u·F",
                       "exact identity n − 1 = u·F" if ok else "n − 1 ≠ u·F"))
    if not ok:
        return fin(False)
    c1 = F * F > n
    c2 = F % 2 == 1 and (2 * F + 1) ** 2 > n
    ok = c1 or c2
    cual = "F² > n" if c1 else "(2F + 1)² > n (F impar, refinamiento 2-ádico)"
    cual_en = "F² > n" if c1 else "(2F + 1)² > n (odd F, 2-adic refinement)"
    checks.append(_chk("T3-4", "F² > n  ∨  (F ≡ 1 (mod 2) ∧ (2F + 1)² > n)", ok,
                       f"cota de Pocklington: {cual}" if ok else "cota de Pocklington insuficiente",
                       f"Pocklington bound: {cual_en}" if ok else "insufficient Pocklington bound"))
    if not ok:
        return fin(False)
    r = pow(a, n - 1, n)
    ok = r == 1
    checks.append(_chk("T3-5", "a^(n−1) ≡ 1 (mod n)", ok, f"Fermat con a = {_corto(a)}: resultado {_corto(r)}",
                       f"Fermat with a = {_corto(a)}: result {_corto(r)}"))
    if not ok:
        return fin(False)
    g = gcd(pow(a, u, n) - 1, n)
    ok = g == 1
    checks.append(_chk("T3-6", "gcd(a^u − 1, n) = 1", ok, f"condición de orden: gcd = {_corto(g)}",
                       f"order condition: gcd = {_corto(g)}"))
    return fin(ok)

# ┏━━━ TEO-12 — MULTI-POCKLINGTON (T–MA1) ━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Premise: distinct odd primes qᵢ | n − 1, each proven earlier.    ┃
# ┃ For each qᵢ: aᵢ^(n−1) ≡ 1 and gcd(aᵢ^((n−1)/qᵢ) − 1, n) = 1  ⇒   ┃
# ┃ qᵢ | ℓ − 1 for every prime ℓ | n.                                ┃
# ┃ So F = ∏ qᵢ divides ℓ − 1 and ℓ ≥ F + 1; (F + 1)² > n ⇒ n prime. ┃
# ┃ a^(n−1) is cached per base so it is not repeated. Checks MA-1,   ┃
# ┃ MA-2, MA-anc-k(a–d), MA-3.                                       ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _teorema_multi_pock(n: int, nodo: dict):
    ancestros_raw = nodo["ancestros"]
    if not isinstance(ancestros_raw, list):
        raise TypeError("ancestros debe ser lista / ancestros must be a list")
    ancestros = [(entero_estricto(x["q"], "q"), entero_estricto(x["a"], "a")) for x in ancestros_raw]
    params = {"ancestros": [{"q": q, "a": a} for q, a in ancestros]}
    refs = [q for q, _ in ancestros]
    checks = []

    def fin(ok):
        return checks, refs, params, ok

    ok = n > 2 and n % 2 == 1
    checks.append(_chk("MA-1", "n ≡ 1 (mod 2) ∧ n > 2", ok, "n es impar y mayor que 2" if ok else "n debe ser impar y > 2",
                       "n is odd and greater than 2" if ok else "n must be odd and > 2"))
    if not ok:
        return fin(False)
    ok = len(ancestros) >= 2
    checks.append(_chk("MA-2", "|{qᵢ}| ≥ 2", ok, f"{len(ancestros)} ancestros", f"{len(ancestros)} ancestors"))
    if not ok:
        return fin(False)
    vistos: set = set()
    fermat_cache: dict = {}
    F = 1
    for k, (q, a) in enumerate(ancestros, 1):
        ok = q not in vistos and 2 < q < n and q % 2 == 1
        checks.append(_chk(f"MA-anc-{k}a", f"q{k} ≡ 1 (mod 2), q{k} ≠ qⱼ, 2 < q{k} < n", ok,
                           f"q{k} = {_corto(q)}" if ok else f"q{k} inválido o repetido",
                           f"q{k} = {_corto(q)}" if ok else f"q{k} invalid or repeated"))
        if not ok:
            return fin(False)
        ok = (n - 1) % q == 0
        checks.append(_chk(f"MA-anc-{k}b", f"q{k} | n − 1", ok, "divisibilidad exacta" if ok else f"q{k} no divide n − 1",
                           "exact divisibility" if ok else f"q{k} does not divide n − 1"))
        if not ok:
            return fin(False)
        if a not in fermat_cache:
            fermat_cache[a] = pow(a, n - 1, n)
        ok = fermat_cache[a] == 1
        checks.append(_chk(f"MA-anc-{k}c", f"a{k}^(n−1) ≡ 1 (mod n)", ok, f"Fermat con a{k} = {_corto(a)}",
                           f"Fermat with a{k} = {_corto(a)}"))
        if not ok:
            return fin(False)
        g = gcd(pow(a, (n - 1) // q, n) - 1, n)
        ok = g == 1
        checks.append(_chk(f"MA-anc-{k}d", f"gcd(a{k}^((n−1)/q{k}) − 1, n) = 1", ok, f"orden ancestral: gcd = {_corto(g)}",
                           f"ancestral order: gcd = {_corto(g)}"))
        if not ok:
            return fin(False)
        vistos.add(q)
        F *= q
    params["F_producto"] = F
    ok = (F + 1) ** 2 > n
    checks.append(_chk("MA-3", "(F + 1)² > n,  F = ∏ qᵢ  (TEO-12, T–MA1)", ok,
                       f"F tiene {F.bit_length()} bits; cota {'cumplida' if ok else 'insuficiente'}",
                       f"F has {F.bit_length()} bits; bound {'met' if ok else 'insufficient'}"))
    return fin(ok)

# ┏━━━ TEO-16 / TEO-18 — LUCAS CLOSURE (T–B2 / T–B5) ━━━━━━━━━━━━━━━━┓
# ┃ Premise: n + 1 = u·F with F = p prime proven earlier (u = 2      ┃
# ┃ gives n = 2p − 1, T–B2).                                         ┃
# ┃ Conditions: D = P² − 4Q, (D/n) = −1, gcd(n, 2PQD) = 1, gcd(U_u,  ┃
# ┃ n) = 1, U_(n+1) ≡ 0 (mod n).                                     ┃
# ┃ For every prime ℓ | n the rank of apparition ω(ℓ) divides n + 1  ┃
# ┃ = uF but not u, so F | ω(ℓ) | ℓ − (D/ℓ), i.e. ℓ ≡ ±1 (mod F);    ┃
# ┃ with ℓ, F odd, ℓ ≡ ±1 (mod 2F) and ℓ ≥ 2F − 1.                   ┃
# ┃ Bound (LEM-2): (F odd ∧ (2F − 1)² > n) ∨ (F − 1)² > n ⇒ n prime. ┃
# ┃ Checks LU-1 … LU-7.                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _teorema_lucas(n: int, nodo: dict):
    F = entero_estricto(nodo["F"], "F")
    u = entero_estricto(nodo["u"], "u")
    P = entero_estricto(nodo["P"], "P")
    Q = entero_estricto(nodo.get("Q", 1), "Q")
    D = P * P - 4 * Q
    params = {"F": F, "u": u, "P": P, "Q": Q, "D": D}
    checks = []

    def fin(ok):
        return checks, [F], params, ok

    ok = n > 3 and n % 2 == 1
    checks.append(_chk("LU-1", "n ≡ 1 (mod 2) ∧ n ≥ 5", ok, "n es impar y ≥ 5" if ok else "n debe ser impar y ≥ 5",
                       "n is odd and ≥ 5" if ok else "n must be odd and ≥ 5"))
    if not ok:
        return fin(False)
    ok = u >= 1 and F >= 3 and n + 1 == u * F
    rel = "n = 2p − 1 (TEO-16, T–B2)" if u == 2 else "n = u·p − 1 (TEO-18, T–B5 / Morrison)"
    checks.append(_chk("LU-2", "n + 1 = u · F,  F = p ≥ 3", ok, f"identidad exacta: {rel}" if ok else "n + 1 ≠ u·F o F < 3",
                       f"exact identity: {rel}" if ok else "n + 1 ≠ u·F or F < 3"))
    if not ok:
        return fin(False)
    j = jacobi(D, n) if D != 0 else 0
    ok = D != 0 and j == -1
    checks.append(_chk("LU-3", "D = P² − 4Q,  (D/n) = −1", ok, f"D = {_corto(D)}, símbolo de Jacobi (D/n) = {j}",
                       f"D = {_corto(D)}, Jacobi symbol (D/n) = {j}"))
    if not ok:
        return fin(False)
    g = gcd(n, 2 * P * Q * D)
    ok = g == 1
    checks.append(_chk("LU-4", "gcd(n, 2·P·Q·D) = 1", ok, f"gcd = {_corto(g)}", f"gcd = {_corto(g)}"))
    if not ok:
        return fin(False)
    Uu, _ = lucas_uv(P, Q, u, n)
    g = gcd(Uu, n)
    ok = g == 1
    checks.append(_chk("LU-5", "gcd(U_u(P,Q), n) = 1", ok,
                       f"U_{u}(P,Q) mod n coprimo con n (gcd = {_corto(g)})" + (" — para u = 2, U₂ = P" if u == 2 else ""),
                       f"U_{u}(P,Q) mod n coprime to n (gcd = {_corto(g)})" + (" — for u = 2, U₂ = P" if u == 2 else "")))
    if not ok:
        return fin(False)
    U, _ = lucas_uv(P, Q, n + 1, n)
    ok = U == 0
    checks.append(_chk("LU-6", "U_(n+1)(P,Q) ≡ 0 (mod n)", ok,
                       f"sucesión de Lucas por duplicación binaria: U_(n+1) mod n = {_corto(U)}",
                       f"Lucas sequence by binary doubling: U_(n+1) mod n = {_corto(U)}"))
    if not ok:
        return fin(False)
    c1 = F % 2 == 1 and (2 * F - 1) ** 2 > n
    c2 = (F - 1) ** 2 > n
    ok = c1 or c2
    checks.append(_chk("LU-7", "(F ≡ 1 (mod 2) ∧ (2F − 1)² > n)  ∨  (F − 1)² > n  (LEM-2)", ok,
                       "todo primo ℓ | n cumple ℓ ≡ ±1 (mod 2F), luego ℓ ≥ 2F − 1 > √n" if ok else "cota de Lucas insuficiente",
                       "every prime ℓ | n satisfies ℓ ≡ ±1 (mod 2F), hence ℓ ≥ 2F − 1 > √n" if ok else "insufficient Lucas bound"))
    return fin(ok)

# ┏━━━ 7B.9 — THEOREM DISPATCH TABLE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ One function per node type. The full chain, the single-node      ┃
# ┃ check and the manual step all call these same functions, so all  ┃
# ┃ three evaluate identical mathematics.                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
TEOREMAS = {"pinza": _teorema_pinza, "pock": _teorema_pock, "multi_pock": _teorema_multi_pock, "lucas": _teorema_lucas}
TEOREMA_NOMBRE = {"pinza": "TEO-5 (Pinza / Clamp)", "pock": "TEO-9 (Pocklington)",
                  "multi_pock": "TEO-12 (T–MA1 Multi-Pocklington)", "lucas": "TEO-16 / TEO-18 (Lucas T–B2 / T–B5)"}

# ┏━━━ 7B.10 — NODE EVALUATION (THEOREM ONLY) ━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Parses n, selects the theorem by `tipo` and runs it. Returns     ┃
# ┃ identity of n (bits, digits, SHA-256), params, checks and        ┃
# ┃ nodo_matematicamente_valido.                                     ┃
# ┃ It does NOT check ancestors; that is _checks_dependencia. A      ┃
# ┃ malformed node becomes a bilingual CertificadoInvalido.          ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _evaluar_nodo(nodo: dict, i: int) -> dict:
    """Runs the node theorem only (no ancestor dependency). Raises
    CertificadoInvalido for a malformed node."""
    t0 = time.perf_counter()
    try:
        if not isinstance(nodo, dict):
            raise TypeError("nodo no es objeto / node is not an object")
        n = entero_estricto(nodo["n"], f"nodo {i}: n")
        tipo = nodo["tipo"]
        if tipo not in TEOREMAS:
            raise CertificadoInvalido(f"nodo {i}: tipo no implementado: {tipo}", f"node {i}: unsupported node type: {tipo}")
        checks, refs, params, ok = TEOREMAS[tipo](n, nodo)
    except CertificadoInvalido:
        raise
    except EnteroInvalido as exc:
        raise CertificadoInvalido(f"nodo {i}: {exc.es}", f"node {i}: {exc.en}") from exc
    except (KeyError, TypeError, ValueError) as exc:
        raise CertificadoInvalido(f"nodo {i}: nodo mal formado: {exc}", f"node {i}: malformed node: {exc}") from exc
    ident = identidad_entero(n)
    return {"indice": i, "tipo": tipo, "teorema": TEOREMA_NOMBRE[tipo],
            "regla": nodo.get("regla"), "regla_en": nodo.get("rule", nodo.get("regla")),
            "n": n, "n_str": ident["N_str"], "bits": ident["bits"], "digitos": ident["digitos"],
            "sha256_n": ident["sha256_N"], "parametros": _s(params), "refs": refs, "checks": checks,
            "nodo_matematicamente_valido": ok, "tiempo_ms": round((time.perf_counter() - t0) * 1000, 3)}

# ┏━━━ 7B.11 — ANCESTOR DEPENDENCY (TEO-21) ━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Every ref q must equal nⱼ of a node j < i already verified: q ∈  ┃
# ┃ {nⱼ : j < i}.                                                    ┃
# ┃ The chain is therefore well-founded: each premise is proven      ┃
# ┃ before it is used. Returns DEP-k checks, the global ok and info  ┃
# ┃ on each ancestor.                                                ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _checks_dependencia(refs: list, previos: dict, i: int) -> tuple[list, bool, list]:
    """previos: {n: index} of the nodes verified before node i."""
    checks, ok_total, refs_info = [], True, []
    for k, r in enumerate(refs, 1):
        j = previos.get(r)
        ok = j is not None and j < i
        ok_total = ok_total and ok
        refs_info.append({"valor_str": str(r), "bits": r.bit_length(), "indice_ancestro": j})
        checks.append(_chk(f"DEP-{k}", "q ∈ {nⱼ : j < i}  (TEO-21)", ok,
                           f"ancestro de {r.bit_length()} bits probado en el nodo #{j + 1:02d}" if ok else
                           f"ancestro de {r.bit_length()} bits NO aparece certificado antes en la cadena",
                           f"{r.bit_length()}-bit ancestor proven at node #{j + 1:02d}" if ok else
                           f"{r.bit_length()}-bit ancestor does NOT appear certified earlier in the chain"))
    return checks, ok_total, refs_info

# ┏━━━ 7B.12 — CERTIFICATE CONTAINER AND KEY LOOKUP ━━━━━━━━━━━━━━━━━┓
# ┃ _contenedor: accepts the plain treatise JSON or the              ┃
# ┃ OMEGA337-CANON-1 container ("certificado"); requires N and a     ┃
# ┃ non-empty "arbol".                                               ┃
# ┃ _primero: returns the first present key, Spanish first and       ┃
# ┃ English twin second; skips {"$ref": …} links.                    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _contenedor(certificado: Any) -> tuple[dict, list]:
    if not isinstance(certificado, dict):
        raise CertificadoInvalido("certificado no es objeto", "certificate is not a JSON object")
    cont = certificado.get("certificado", certificado)
    if not isinstance(cont, dict):
        raise CertificadoInvalido("contenedor 'certificado' no es objeto", "'certificado' container is not an object")
    if "arbol" not in cont:
        raise CertificadoInvalido("certificado mal formado: falta 'arbol'", "malformed certificate: missing 'arbol'")
    if "N" not in cont:
        raise CertificadoInvalido("certificado mal formado: falta 'N'", "malformed certificate: missing 'N'")
    arbol = cont["arbol"]
    if not isinstance(arbol, list) or not arbol:
        raise CertificadoInvalido("cadena vacía", "empty chain")
    return cont, arbol


def _primero(d: Any, *claves):
    if not isinstance(d, dict):
        return None
    for k in claves:
        v = d.get(k)
        if v is not None and not (isinstance(v, dict) and "$ref" in v):
            return v
    return None

# ┏━━━ 7B.13 — TREE HASH ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ OM337-JSON-SORTED-UTF8-v1: SHA-256 of the tree with Spanish keys ┃
# ┃ only (drops type, rule, ancestors), sorted keys, compact         ┃
# ┃ separators, UTF-8.                                               ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _sha256_arbol(arbol: list) -> str:
    """OM337-JSON-SORTED-UTF8-v1: Spanish-key tree, sorted keys, compact separators."""
    limpio = [{k: v for k, v in n.items() if k not in _CLAVES_GEMELAS_EN} if isinstance(n, dict) else n for n in arbol]
    return hashlib.sha256(json.dumps(limpio, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()

# ┏━━━ 7B.14 — DECLARED METADATA (SEPARATE VERDICT) ━━━━━━━━━━━━━━━━━┓
# ┃ Compares what the file declares against N: bits_N vs             ┃
# ┃ N.bit_length(), sha256_N vs computed, tree hash, file name       ┃
# ┃ OM337_prime_<bits>bits_<16 hex>.json and UIS identity N = 2p +   ┃
# ┃ d.                                                               ┃
# ┃ State: SIN_METADATOS / COHERENTES / INCOHERENTES. A declared     ┃
# ┃ verdict is recorded and ignored as proof. Never changes          ┃
# ┃ veredicto_matematico.                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _metadatos(certificado: dict, cont: dict, arbol: list, N: int, sha_N: str) -> dict:
    """Declared metadata. Never used as proof; only compared against N."""
    ident = _primero(certificado, "identidad") or {}
    if not isinstance(ident, dict):
        ident = {}
    notas, coherente, declarado = [], True, False

    def nota(ok, es, en):
        notas.append({"ok": ok, "es": es, "en": en})

    bits_decl_raw = _primero(ident, "bits_N")
    if bits_decl_raw is None:
        bits_decl_raw = _primero(certificado, "bits_N") if certificado is not cont else None
        if bits_decl_raw is None:
            bits_decl_raw = _primero(cont, "bits_N")
    bits_decl, bits_ok = None, None
    if bits_decl_raw is not None:
        declarado = True
        try:
            bits_decl = entero_estricto(bits_decl_raw, "bits_N")
            bits_ok = bits_decl == N.bit_length()
        except EnteroInvalido:
            bits_ok = False
        coherente &= bool(bits_ok)
        nota(bits_ok, f"bits_N declarado = {bits_decl_raw}; calculado desde N = {N.bit_length()}",
             f"declared bits_N = {bits_decl_raw}; computed from N = {N.bit_length()}")
    sha_decl = _primero(ident, "sha256_N")
    sha_ok = None
    if sha_decl is not None:
        declarado = True
        sha_ok = isinstance(sha_decl, str) and sha_decl.lower() == sha_N
        coherente &= sha_ok
        nota(sha_ok, "SHA-256(N) declarado " + ("coincide" if sha_ok else "NO coincide") + " con el calculado",
             "declared SHA-256(N) " + ("matches" if sha_ok else "does NOT match") + " the computed one")
    arbol_decl = _primero(ident, "sha256_arbol", "sha256_tree")
    arbol_calc = _sha256_arbol(arbol)
    arbol_ok = None
    if arbol_decl is not None:
        declarado = True
        arbol_ok = isinstance(arbol_decl, str) and arbol_decl.lower() == arbol_calc
        coherente &= arbol_ok
        nota(arbol_ok, "SHA-256 del árbol declarado " + ("coincide" if arbol_ok else "NO coincide"),
             "declared tree SHA-256 " + ("matches" if arbol_ok else "does NOT match"))
    archivo = _primero(certificado, "archivo", "file")
    nombre_ok = None
    m = re.fullmatch(r"OM337_prime_(\d+)bits_([0-9a-f]{16})(\.json)?", str(_primero(certificado, "nombre", "name") or archivo or ""))
    if m:
        nombre_ok = int(m.group(1)) == N.bit_length() and m.group(2) == sha_N[:16]
        coherente &= nombre_ok
        nota(nombre_ok, "nombre de archivo (bits + prefijo SHA-256) " + ("coherente con N" if nombre_ok else "NO coherente con N"),
             "file name (bits + SHA-256 prefix) " + ("consistent with N" if nombre_ok else "NOT consistent with N"))
    uis_p, uis_d, uis_ok = cont.get("p"), cont.get("d"), None
    if uis_p is not None and uis_d is not None:
        try:
            uis_ok = 2 * entero_estricto(uis_p, "p") + entero_estricto(uis_d, "d") == N
        except EnteroInvalido:
            uis_ok = False
        coherente &= uis_ok
        nota(uis_ok, "identidad UIS declarada N = 2p + d " + ("se cumple" if uis_ok else "NO se cumple"),
             "declared UIS identity N = 2p + d " + ("holds" if uis_ok else "does NOT hold"))
    veredicto_decl = None
    for fuente in (certificado, cont):
        v = _primero(fuente, "veredicto", "verdict", "estado", "status", "primo", "prime")
        if v is not None:
            veredicto_decl = v
            nota(None, "veredicto declarado presente: se ignora como prueba (solo cuenta la matemática)",
                 "declared verdict present: ignored as proof (only the mathematics counts)")
            break
    estado = "SIN_METADATOS" if not declarado else ("COHERENTES" if coherente else "INCOHERENTES")
    return {
        "estado_metadatos": estado,
        "notas_metadatos": notas,
        "metadatos": _s({
            "titulo_es": _primero(certificado, "titulo"), "title_en": _primero(certificado, "title"),
            "emisor_es": _primero(certificado, "emisor"), "issuer_en": _primero(certificado, "issuer"),
            "nombre": _primero(certificado, "nombre", "name"), "archivo": archivo,
            "formato": _primero(certificado, "esquema", "schema", "formato", "format"),
            "version": _primero(certificado, "version", "versión"), "fecha": _primero(certificado, "fecha", "date"),
            "motor": _primero(certificado, "motor", "engine"),
            "mecanismo_es": cont.get("mecanismo"), "mechanism_en": cont.get("mechanism", cont.get("mecanismo")),
            "algoritmo_sha256_N": _primero(ident, "algoritmo_sha256_N", "algorithm_sha256_N"),
            "bits_declarados": bits_decl if bits_decl is not None else bits_decl_raw, "bits_coinciden": bits_ok,
            "sha256_declarado": sha_decl, "sha256_coincide": sha_ok,
            "sha256_arbol_declarado": arbol_decl, "sha256_arbol_calculado": arbol_calc, "sha256_arbol_coincide": arbol_ok,
            "nombre_coherente": nombre_ok, "uis_p": uis_p, "uis_d": uis_d, "uis_coincide": uis_ok,
            "veredicto_declarado": veredicto_decl,
        }),
    }

# ┏━━━ 7B.15 — FAST CERTIFICATE INSPECTION ━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ No theorem is run. Returns identity of N, SHA-256 of the JSON    ┃
# ┃ bytes (kept separate from SHA-256(N)), metadata, node-type       ┃
# ┃ summary and, for each node, n, bits, digits, SHA-256(n) and raw  ┃
# ┃ parameters.                                                      ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def inspeccionar_certificado(certificado: Any, raw: Optional[bytes] = None) -> dict:
    """Fast inspection (no theorem verification): identity of N, metadata and
    every node's integer, bits, digits, SHA-256 and raw parameters."""
    _sin_limite_digitos()
    cont, arbol = _contenedor(certificado)
    try:
        N = entero_estricto(cont["N"], "N")
    except EnteroInvalido as exc:
        raise CertificadoInvalido(exc.es, exc.en) from exc
    ident = identidad_entero(N)
    info = {**ident, "num_nodos": len(arbol), "sha256_json": hashlib.sha256(raw).hexdigest() if raw is not None else None}
    info.update(_metadatos(certificado, cont, arbol, N, ident["sha256_N"]))
    nodos, tipos = [], {}
    for i, nodo in enumerate(arbol):
        entrada = {"indice": i, "tipo": None, "regla": None, "regla_en": None, "n_str": None, "bits": None,
                   "digitos": None, "sha256_n": None, "parametros": {}}
        if isinstance(nodo, dict):
            entrada["tipo"] = nodo.get("tipo")
            entrada["regla"] = nodo.get("regla")
            entrada["regla_en"] = nodo.get("rule", nodo.get("regla"))
            try:
                n = entero_estricto(nodo.get("n"), "n")
                d = identidad_entero(n)
                entrada.update({"n_str": d["N_str"], "bits": d["bits"], "digitos": d["digitos"], "sha256_n": d["sha256_N"]})
            except EnteroInvalido as exc:
                entrada["error_es"], entrada["error_en"] = exc.es, exc.en
            entrada["parametros"] = _s({k: v for k, v in nodo.items()
                                        if k not in ("n", "tipo", "regla") + _CLAVES_GEMELAS_EN})
        tipos[str(entrada["tipo"])] = tipos.get(str(entrada["tipo"]), 0) + 1
        nodos.append(entrada)
    info["resumen_tipos"] = tipos
    info["nodos_inspeccion"] = nodos
    return info

# ┏━━━ 7B.16 — FULL CHAIN VERIFICATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ For each node in order: theorem (_evaluar_nodo) + ancestors      ┃
# ┃ (_checks_dependencia) + n not repeated. The last node must equal ┃
# ┃ N.                                                               ┃
# ┃ On the first failure it raises CertificadoInvalido with the      ┃
# ┃ partial report. Mathematical verdict and metadata state stay     ┃
# ┃ separate.                                                        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def verificar_certificado_tana(certificado: dict, objetivo: Optional[int] = None, raw: Optional[bytes] = None) -> dict:
    """
    Verifies a finite chain of certificates using exact integer arithmetic.

    Supports both the treatise's plain JSON format and the OMEGA337-CANON-1 container.
    Does not use probabilistic tests or rely on the state declared by the engine.
    Raises CertificadoInvalido upon the first unmet mathematical prerequisite
    (exc.informe carries the partial report). Declared metadata (bits_N,
    sha256_N, names, verdict labels) never decides the mathematical verdict:
    it is reported separately in `estado_metadatos`.
    """
    _sin_limite_digitos()
    t0 = time.perf_counter()
    informe = inspeccionar_certificado(certificado, raw)
    cont, arbol = _contenedor(certificado)
    N = int(informe["N_str"])
    informe["veredicto_matematico"] = "EN_CURSO"
    detalles: list = []
    informe["detalles"] = detalles

    def rechazar(es, en):
        informe["veredicto_matematico"] = "CERTIFICADO_INVALIDO"
        informe["primo_certificado"] = False
        informe["motivo_es"], informe["motivo_en"] = es, en
        informe["tiempo_ms"] = round((time.perf_counter() - t0) * 1000, 3)
        raise CertificadoInvalido(es, en, informe)

    if objetivo is not None and N != objetivo:
        rechazar("objetivo distinto del certificado", "target differs from the certificate")
    if N <= 1:
        rechazar("N debe ser > 1", "N must be > 1")
    previos: dict = {}
    for i, nodo in enumerate(arbol):
        try:
            r = _evaluar_nodo(nodo, i)
        except CertificadoInvalido as exc:
            rechazar(exc.es, exc.en)
        dep_checks, dep_ok, refs_info = _checks_dependencia(r.pop("refs"), previos, i)
        n = r.pop("n")
        repetido = n in previos
        if repetido:
            dep_checks.append(_chk("DEP-0", "n ∉ {nⱼ : j < i}", False, "n ya fue certificado antes", "n was already certified earlier"))
            dep_ok = False
        r.update({"checks_dependencia": dep_checks, "dependencia_ancestros_valida": dep_ok,
                  "ancestros_referenciados": refs_info, "ancestros_ok": dep_ok,
                  "valido": r["nodo_matematicamente_valido"] and dep_ok, "verificado": r["nodo_matematicamente_valido"] and dep_ok})
        detalles.append(r)
        if not r["nodo_matematicamente_valido"]:
            fallo = next((c for c in r["checks"] if not c["ok"]), None)
            rechazar(f"nodo {i}: {fallo['id']} {fallo['detail_es']}" if fallo else f"nodo {i}: inválido",
                     f"node {i}: {fallo['id']} {fallo['detail_en']}" if fallo else f"node {i}: invalid")
        if not dep_ok:
            rechazar(f"nodo {i}: dependencia de ancestros inválida o n repetido",
                     f"node {i}: invalid ancestor dependency or repeated n")
        previos[n] = i
    if detalles[-1]["n_str"] != informe["N_str"]:
        rechazar("último nodo distinto del objetivo", "last node differs from the target N")
    informe.update({"primo_certificado": True, "veredicto_matematico": "PRIMO_CERTIFICADO",
                    "bits": N.bit_length(), "nodos": len(arbol),
                    "tiempo_ms": round((time.perf_counter() - t0) * 1000, 3)})
    informe.pop("nodos_inspeccion", None)
    return informe

# ┏━━━ 7B.17 — SINGLE-NODE VERIFICATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Verifies node i (0-based) with the same theorem functions.       ┃
# ┃ Ancestors are looked up among nodes 0 … i − 1.                   ┃
# ┃ Reports nodo_matematicamente_valido and                          ┃
# ┃ dependencia_ancestros_valida separately: if the equations hold   ┃
# ┃ but an ancestor is missing, the node is NOT proven.              ┃
# ┃ profundo=True also verifies the ancestors recursively            ┃
# ┃ (memoized).                                                      ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def verificar_nodo_certificado(certificado: dict, indice: Any, profundo: bool = False) -> dict:
    """Verifies ONE node (0-based `indice`) with the same theorem functions.
    Reports separately: the node's own equations (nodo_matematicamente_valido)
    and whether every referenced ancestor appears as an earlier node of the
    chain (dependencia_ancestros_valida). With profundo=True the referenced
    ancestors are also verified recursively (cadena_ancestros_valida)."""
    _sin_limite_digitos()
    t0 = time.perf_counter()
    cont, arbol = _contenedor(certificado)
    try:
        i = entero_estricto(indice, "indice", minimo=0)
    except EnteroInvalido as exc:
        raise CertificadoInvalido(exc.es, exc.en) from exc
    if i >= len(arbol):
        raise CertificadoInvalido(f"índice {i} fuera de rango (0..{len(arbol) - 1})", f"index {i} out of range (0..{len(arbol) - 1})")
    previos: dict = {}
    for j in range(i):
        try:
            v = entero_estricto(arbol[j].get("n"), "n") if isinstance(arbol[j], dict) else None
        except EnteroInvalido:
            v = None
        if v is not None and v not in previos:
            previos[v] = j
    r = _evaluar_nodo(arbol[i], i)
    refs = r.pop("refs")
    n = r.pop("n")
    dep_checks, dep_ok, refs_info = _checks_dependencia(refs, previos, i)
    if n in previos:
        dep_checks.append(_chk("DEP-0", "n ∉ {nⱼ : j < i}", False, "n ya aparece antes", "n already appears earlier"))
        dep_ok = False
    r.update({"checks_dependencia": dep_checks, "dependencia_ancestros_valida": dep_ok, "ancestros_referenciados": refs_info})
    if profundo and dep_ok:
        memo: dict = {}

        def cadena(j):
            if j in memo:
                return memo[j]
            rj = _evaluar_nodo(arbol[j], j)
            ok = rj["nodo_matematicamente_valido"]
            for ref in rj["refs"]:
                k = previos.get(ref)
                ok = ok and k is not None and k < j and cadena(k)
            memo[j] = ok
            return ok
        r["cadena_ancestros_valida"] = all(cadena(previos[x]) for x in refs)
        r["nodos_ancestros_verificados"] = len(memo)
    m_ok = r["nodo_matematicamente_valido"]
    if m_ok and dep_ok:
        es = f"Nodo #{i + 1:02d} válido: las ecuaciones del teorema se cumplen y sus ancestros aparecen antes en la cadena."
        en = f"Node #{i + 1:02d} valid: the theorem equations hold and its ancestors appear earlier in the chain."
    elif m_ok:
        es = f"Nodo #{i + 1:02d}: las ecuaciones se cumplen, pero un ancestro no está certificado antes en la cadena; el nodo no queda probado."
        en = f"Node #{i + 1:02d}: the equations hold, but an ancestor is not certified earlier in the chain; the node is not proven."
    else:
        fallo = next((c for c in r["checks"] if not c["ok"]), {"id": "?", "detail_es": "", "detail_en": ""})
        es = f"Nodo #{i + 1:02d} rechazado: falla {fallo['id']} — {fallo['detail_es']}"
        en = f"Node #{i + 1:02d} rejected: {fallo['id']} fails — {fallo['detail_en']}"
    r.update({"valido": m_ok and dep_ok, "veredicto_es": es, "veredicto_en": en,
              "tiempo_ms": round((time.perf_counter() - t0) * 1000, 3)})
    return r


# ------------------------------------------------------------------------------
# Manual (hand-typed) integer verification with the verifier's public tools.
# ------------------------------------------------------------------------------
# ┏━━━ 7B.18 — MANUAL INTEGER VERIFICATION · PUBLIC TOOLS ━━━━━━━━━━━┓
# ┃ Hand-typed integers are checked only with public mathematics. No ┃
# ┃ OM337 engine logic is used and no certificate is produced.       ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━━━ MANUAL AUDIT OF N ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Order:                                                           ┃
# ┃ • N < 2 not prime; N ∈ {2, 3} prime (definition).                ┃
# ┃ • FDP B1: divisibility by 3, 2, 7, 5.                            ┃
# ┃ • Exact division by odd d ≥ 11, up to ⌊√N⌋ if N ≤ 10¹⁰, else     ┃
# ┃    up to 100,000. Reaching ⌊√N⌋ is a complete proof.             ┃
# ┃ • N < 2^64: Miller–Rabin with Sinclair's 7 bases,                ┃
# ┃    deterministic.                                                ┃
# ┃ • N ≥ 2^64: witnesses with bases 2 … 37: composite proven, or    ┃
# ┃    EVIDENCIA_INSUFICIENTE. Primality ≥ 2^64 needs a TANA         ┃
# ┃    certificate or a manual step.                                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def verificar_numero_manual(valor: Any) -> dict:
    """Public deterministic audit of a hand-typed integer. Never claims
    primality for N >= 2^64 without a certificate or a manual theorem step."""
    _sin_limite_digitos()
    t0 = time.perf_counter()
    N = entero_estricto(valor, "N")
    out = identidad_entero(N)
    checks = []

    def fin(estado, metodo, es, en, **extra):
        out.update({"estado": estado, "metodo": metodo, "veredicto_es": es, "veredicto_en": en, "checks": checks,
                    "tiempo_ms": round((time.perf_counter() - t0) * 1000, 3), **_s(extra)})
        return out

    if N < 2:
        checks.append(_chk("DEF", "N ≥ 2", False, "N < 2 no es primo por definición", "N < 2 is not prime by definition"))
        return fin("NO_PRIMO", "DEFINICION", "N < 2: no es primo (definición).", "N < 2: not prime (definition).")
    if N in (2, 3):
        checks.append(_chk("DEF", "N ∈ {2, 3}", True, "primo por definición", "prime by definition"))
        return fin("PRIMO_DETERMINISTA", "DEFINICION", f"{N} es primo (definición).", f"{N} is prime (definition).")
    estado_fdp, d, q = FDP(N)
    checks.append(_chk("FDP-B1", "N mod d, d ∈ (3, 2, 7, 5)", estado_fdp == "SUPERA_FILTRO",
                       "supera el filtro FDP" if d is None else f"{d} divide N", "passes the FDP filter" if d is None else f"{d} divides N"))
    if d is not None:
        return fin("COMPUESTO_VERIFICADO", "FDP", f"Compuesto: N = {d} · {_corto(q)} (filtro FDP B1).",
                   f"Composite: N = {d} · {_corto(q)} (FDP B1 filter).", divisor=d, cociente=q)
    raiz = isqrt(N)
    limite = raiz if N <= 10 ** 10 else min(raiz, LIMITE_DIVISION_MANUAL)
    divisor = None
    k = 11
    while k <= limite:
        if N % k == 0:
            divisor = k
            break
        k += 2
    if divisor is not None:
        checks.append(_chk("TD", f"N mod d ≠ 0, d ≤ {limite}", False, f"divisor exacto {divisor}", f"exact divisor {divisor}"))
        return fin("COMPUESTO_VERIFICADO", "DIVISION_EXACTA", f"Compuesto: N = {divisor} · {_corto(N // divisor)} (división exacta).",
                   f"Composite: N = {divisor} · {_corto(N // divisor)} (exact trial division).", divisor=divisor, cociente=N // divisor)
    if limite >= raiz:
        checks.append(_chk("TD", "∀ d ≤ ⌊√N⌋: N mod d ≠ 0", True, f"sin divisores hasta ⌊√N⌋ = {raiz}", f"no divisors up to ⌊√N⌋ = {raiz}"))
        return fin("PRIMO_DETERMINISTA", "DIVISION_EXACTA", f"Primo: división exacta completa hasta ⌊√N⌋ = {raiz}.",
                   f"Prime: complete exact trial division up to ⌊√N⌋ = {raiz}.")
    checks.append(_chk("TD", f"∀ d ≤ {limite}: N mod d ≠ 0", True, f"sin divisores hasta {limite}", f"no divisors up to {limite}"))
    if N < 2 ** 64:
        for a in BASES_MR_64:
            if testigo_miller_rabin(N, a):
                checks.append(_chk("MR64", f"Miller–Rabin base {a}", False, f"{a} es testigo de composición", f"{a} is a compositeness witness"))
                return fin("COMPUESTO_VERIFICADO", "TESTIGO_MILLER_RABIN", f"Compuesto: la base a = {a} es testigo de Miller–Rabin.",
                           f"Composite: base a = {a} is a Miller–Rabin witness.", testigo=a)
        checks.append(_chk("MR64", "Miller–Rabin, bases {2, 325, 9375, 28178, 450775, 9780504, 1795265022}", True,
                           "ninguna base es testigo; el conjunto es completo para N < 2^64 (Sinclair 2011)",
                           "no base is a witness; the set is complete for N < 2^64 (Sinclair 2011)"))
        return fin("PRIMO_DETERMINISTA", "MILLER_RABIN_DETERMINISTA_64",
                   "Primo: Miller–Rabin determinista con las 7 bases de Sinclair, prueba completa para N < 2^64 (teorema público; no es un certificado OM337).",
                   "Prime: deterministic Miller–Rabin with Sinclair's 7 bases, a complete proof for N < 2^64 (public theorem; not an OM337 certificate).")
    for a in BASES_TESTIGO:
        if testigo_miller_rabin(N, a):
            checks.append(_chk("MR-W", f"Miller–Rabin base {a}", False, f"{a} es testigo de composición", f"{a} is a compositeness witness"))
            return fin("COMPUESTO_VERIFICADO", "TESTIGO_MILLER_RABIN", f"Compuesto: la base a = {a} es testigo de Miller–Rabin (prueba determinista de composición).",
                       f"Composite: base a = {a} is a Miller–Rabin witness (deterministic proof of compositeness).", testigo=a)
    checks.append(_chk("MR-W", "Miller–Rabin, a ∈ {2, 3, 5, …, 37}", True, "ningún testigo de composición", "no compositeness witness"))
    return fin("EVIDENCIA_INSUFICIENTE", "SIN_TESTIGO",
               "Sin testigo de composición. Para N ≥ 2^64 la primalidad determinista exige un certificado TANA o un paso manual Pocklington / Multi-Pocklington / Lucas.",
               "No compositeness witness. For N ≥ 2^64 deterministic primality requires a TANA certificate or a manual Pocklington / Multi-Pocklington / Lucas step.")

# ┏━━━ MANUAL FACTOR LIST ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Accepts "q1:a1, q2:a2", "q1, q2" with a common base a, or a list ┃
# ┃ of {q, a}. Every value goes through entero_estricto.             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def _parse_factores(valor: Any, a_comun: Optional[int]) -> list:
    """'q1:a1, q2:a2' or 'q1, q2' (with common a) or a list of {q, a}."""
    if isinstance(valor, list):
        items = valor
    else:
        items = [x for x in str(valor or "").replace(";", ",").split(",") if x.strip()]
    res = []
    for it in items:
        if isinstance(it, dict):
            res.append({"q": entero_estricto(it.get("q"), "q"), "a": entero_estricto(it.get("a", a_comun), "a")})
            continue
        partes = str(it).split(":")
        if len(partes) == 2:
            res.append({"q": entero_estricto(partes[0], "q"), "a": entero_estricto(partes[1], "a")})
        elif len(partes) == 1:
            if a_comun is None:
                raise EnteroInvalido("falta la base a para el factor", "missing base a for the factor")
            res.append({"q": entero_estricto(partes[0], "q"), "a": a_comun})
        else:
            raise EnteroInvalido("formato de factor: q:a", "factor format: q:a")
    return res

# ┏━━━ MANUAL THEOREM STEP ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Builds a node {n, tipo, params} and runs the same TEOREMAS       ┃
# ┃ function used for certificate nodes (pock, multi_pock, lucas).   ┃
# ┃ If u is omitted: u = (N − 1) // p (pock) or (N + 1) // p         ┃
# ┃ (lucas); T3-3 / LU-2 still check the identity exactly. Defaults: ┃
# ┃ a = 2, Q = 1.                                                    ┃
# ┃ Each ancestor is checked with verificar_numero_manual:           ┃
# ┃ • all deterministic primes → PRIMO_DETERMINISTA                  ┃
# ┃ • any composite → PASO_RECHAZADO                                 ┃
# ┃ • otherwise → PASO_VALIDO_PREMISA_EXTERNA (N is prime IF the     ┃
# ┃    ancestor is prime).                                           ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
def verificar_paso_manual(payload: dict) -> dict:
    """Manual theorem step on a hand-typed N with the same public theorem
    functions used for certificate nodes (pock, multi_pock, lucas)."""
    _sin_limite_digitos()
    t0 = time.perf_counter()
    if not isinstance(payload, dict):
        raise EnteroInvalido("se esperaba un objeto", "an object was expected")
    tipo = payload.get("tipo")
    if tipo not in ("pock", "multi_pock", "lucas"):
        raise EnteroInvalido("tipo de paso: pock, multi_pock o lucas", "step type: pock, multi_pock or lucas")
    N = entero_estricto(payload.get("N", payload.get("n")), "N", minimo=2)

    def opcional(k, etiqueta, defecto=None):
        v = payload.get(k)
        if v is None or (isinstance(v, str) and not v.strip()):
            return defecto
        return entero_estricto(v, etiqueta)

    nodo: dict = {"n": N, "tipo": tipo}
    if tipo in ("pock", "lucas"):
        p = opcional("p", "p")
        if p is None:
            p = opcional("F", "F")
        if p is None or p < 2:
            raise EnteroInvalido("p debe ser un entero ≥ 2", "p must be an integer ≥ 2")
        u = opcional("u", "u")
        if u is None:
            base = N - 1 if tipo == "pock" else N + 1
            u = base // p
        nodo.update({"F": p, "u": u})
        if tipo == "pock":
            nodo["a"] = opcional("a", "a", 2)
        else:
            nodo["P"] = opcional("P", "P")
            if nodo["P"] is None:
                raise EnteroInvalido("falta P", "missing P")
            nodo["Q"] = opcional("Q", "Q", 1)
    else:
        nodo["ancestros"] = _parse_factores(payload.get("factores"), opcional("a", "a"))
    checks, refs, params, ok = TEOREMAS[tipo](N, nodo)
    premisas, todas = [], True
    algun_compuesto = False
    if ok:
        for r in refs:
            pr = verificar_numero_manual(r)
            estado = pr["estado"]
            prob = estado == "PRIMO_DETERMINISTA"
            algun_compuesto |= estado in ("COMPUESTO_VERIFICADO", "NO_PRIMO")
            todas &= prob
            premisas.append({"valor_str": str(r), "bits": r.bit_length(), "estado": estado, "metodo": pr["metodo"]})
            checks.append(_chk(f"PREM-{len(premisas)}", "p ∈ ℙ", prob,
                               f"ancestro de {r.bit_length()} bits: {estado}" + ("" if prob else " — sin prueba determinista propia"),
                               f"{r.bit_length()}-bit ancestor: {estado}" + ("" if prob else " — no deterministic proof of its own")))
    nombre = {"pock": "Pocklington (TEO-9)", "multi_pock": "Multi-Pocklington (TEO-12, T–MA1)", "lucas": "Lucas (TEO-16 T–B2 / TEO-18)"}[tipo]
    if not ok:
        fallo = next((c for c in checks if not c["ok"]), {"id": "?", "detail_es": "", "detail_en": ""})
        estado, es, en = "PASO_RECHAZADO", f"{nombre}: falla {fallo['id']} — {fallo['detail_es']}", f"{nombre}: {fallo['id']} fails — {fallo['detail_en']}"
    elif algun_compuesto:
        estado, es, en = "PASO_RECHAZADO", f"{nombre}: las ecuaciones se cumplen pero un ancestro es compuesto.", f"{nombre}: the equations hold but an ancestor is composite."
    elif todas:
        estado, es, en = "PRIMO_DETERMINISTA", f"Primo: {nombre} verificado y todos los ancestros tienen prueba determinista.", f"Prime: {nombre} verified and every ancestor has a deterministic proof."
    else:
        estado = "PASO_VALIDO_PREMISA_EXTERNA"
        es = f"{nombre}: ecuaciones verificadas. N es primo SI el ancestro es primo (premisa externa ≥ 2^64: certifíquelo con un certificado TANA)."
        en = f"{nombre}: equations verified. N is prime IF the ancestor is prime (external premise ≥ 2^64: certify it with a TANA certificate)."
    out = identidad_entero(N)
    out.update({"tipo": tipo, "teorema": nombre, "estado": estado, "veredicto_es": es, "veredicto_en": en,
                "nodo_matematicamente_valido": ok, "premisas": premisas, "checks": checks, "parametros": _s(params),
                "tiempo_ms": round((time.perf_counter() - t0) * 1000, 3)})
    return out


def via_certificado_tana(n: int, certificado: Optional[dict]) -> Evidencia:
    """
    Vía path 6 (verification): records evidence without verifying it;
    combinar() performs the validation exactly once.

    Never marks an external declaration as conclusive. The final verdict
    can only result from verificar_certificado_tana() within combinar().
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




__all__ = ["SEGURIDAD", "FDP", "EstadoAuditor", "Evidencia", "ResultadoAuditor", "CertificadoInvalido", "EnteroInvalido",
           "MAX_PINZA_LEAF_BITS", "entero_estricto", "sha256_decimal", "identidad_entero", "jacobi", "lucas_uv",
           "testigo_miller_rabin", "inspeccionar_certificado", "verificar_certificado_tana", "verificar_nodo_certificado",
           "verificar_numero_manual", "verificar_paso_manual", "via_certificado_tana", "combinar", "auditar"]


# ==============================================================================
#  NOTE ON PINZA / NOTA SOBRE PINZA
# ==============================================================================
#
# PINZA (channel 03) is NOT enabled in this public distribution.
#
# The PINZA channel belongs to the private OM337 engine and is not included
# here. via_pinza() does not import anything: it always reports "private engine
# not included in the public verifier" and contributes no verdict. (The `pinza`
# certificate NODE type is different: it is public exact trial division,
# TEO-5, bounded by MAX_PINZA_LEAF_BITS.)
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
        crudo = Path(sys.argv[1]).read_bytes()
        certificado = json.loads(crudo.decode("utf-8"))
        resultado = verificar_certificado_tana(certificado, raw=crudo)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"Certificate rejected: {exc}")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
