# SPARTACO / OM337 — Auditor Interface

**Desktop interface for the SPARTACO Primality Auditor & Verifier**
Auditor v0.9.1 · Verification contract VPSI-CONTRACT-1.0 · Offline · English / Español

---

## 1. Overview

The interface is the screen of the auditor. It lets a user run every evidence channel of the auditor on an integer, load a JSON primality certificate, and inspect the result and the certification chain.

**The interface is a projection, not an authority.** It contains no mathematics of its own and never decides a verdict. Every result it shows is produced by `auditor_descarte.py`, which must sit alongside the interface file.

| | |
|---|---|
| **File** | `modules/interfaz/interfaz_3_AUDITOR.py` |
| **Depends on** | `modules/auditor/auditor_descarte.py` |
| **Technology** | Python 3.11+, `pywebview` (HTML, CSS and JavaScript embedded in one file) |
| **Execution model** | Local, offline, no network access required |
| **Languages** | English and Spanish, switchable at any time |

## 2. What the interface does

- Exposes the **six evidence channels** of the auditor as separate controls, each with a short description.
- Runs a channel (or all of them) on an integer **N** and displays the verdict, its justification and the evidence each channel contributed.
- Loads a **JSON certificate** from the user's disk or from the certificates folder of this repository (`modules/certificates/`, 40 supplied files).
- Verifies the certificate's **TANA chain** with exact integer arithmetic and shows **N**, the bit length, the node count and every node of the chain.
- Runs entirely offline.

## 3. What the interface does not do

- It does not generate primes and does not access the proprietary OM337 or UIS–OMEGA engines.
- It does not accept a prime label, an engine status or any external declaration as proof.
- It does not claim that an arbitrary integer is prime without a verified certificate.

## 4. Screen layout

| Area | Content |
|---|---|
| **Sidebar** | Emblem, language selector (ES / EN), the six evidence channels with their descriptions, connection status |
| **AUDIT tab** | Panel 1: integer input, optional evidence and one button per channel. Panel 2: certificate selection. Panel 3: verdict and evidence |
| **TANA CHAIN tab** | N of the certificate, bits, node count, validity, and the list of verified nodes |
| **ARCHITECTURE tab** | Emblem with legend and a summary of what the auditor covers |

## 5. Evidence channels

Each channel can be run separately from its own button. **AUDIT N** runs all of them with the evidence supplied.

| Channel | Input | What it checks |
|---|---|---|
| **FACTOR** | A divisor | That the divisor is non-trivial (strictly between 1 and N) and divides N exactly. Proves compositeness |
| **MODULO** | Comma-separated moduli | That N has a zero remainder for a supplied modulus greater than 1. Proves compositeness |
| **PINZA** | None | Auxiliary consultation of the engine's external function. It may be unavailable and is recorded as evidence; it does not determine the verdict |
| **TD** | p and d | The declared identity **N = 2p + d**. A broken identity is reported as a contradiction |
| **RESTO** | Comma-separated values | That N has a zero remainder for a supplied value. Proves compositeness |
| **TANA** | A JSON certificate | Verifies a deterministic primality certificate through a finite proof chain (section 7) |

The auditor processes contradictions first, then compositeness evidence, then the certificate. Without a verifiable exclusion, it does not assert primality.

## 6. Verdicts

| Verdict | Meaning |
|---|---|
| `COMPUESTO_VERIFICADO` | A divisor was verified exactly: N is composite |
| `PRIMO_POR_DESCARTE` | A TANA certificate was verified: N is prime by a deterministic proof chain |
| `EVIDENCIA_INSUFICIENTE` | The evidence supplied does not establish a result |
| `CONTRADICCION_DETECTADA` | The evidence contradicts itself (for example, 2p + d does not equal N) |

Verdict names are identifiers of the verification contract and appear unchanged in both languages.

## 7. Certificates

- **Sources:** a local `.json` file, or any of the certificates supplied in `modules/certificates/`, selected from the repository list.
- **Supported formats:** the plain JSON format of the treatise and the `OMEGA337-CANON-1` container.
- **Supported nodes:** exact trial division (`pinza`), Pocklington (`pock`) and multi-Pocklington (`multi_pock`).
- **Acceptance:** the first unmet prerequisite invalidates the certificate. A malformed, unsupported or mathematically insufficient chain is never accepted.
- **Time:** verification time grows with certificate size, since trial-division nodes check divisors up to the square root. Large certificates can take noticeably longer, and the interface stays responsive while they run.

## 8. The emblem

The emblem reuses the visual language of the SPARTACO enclosure (concentric rings of metallic ingots with counter-rotating chips) and encodes the auditor itself:

| Ring | Meaning |
|---|---|
| **Outer** (4 chips) | The four verdicts: CV, PD, EI, CD |
| **Middle** (6 ingots) | The six evidence channels: FA, MO, PZ, TD, RE (RM in English), TA |
| **Inner** (3 ingots) | The three TANA node types: PZ (pinza), PK (pock), MP (multi_pock) |
| **Center** | The integer N under audit |

Chips switch between Spanish and English with the language selector. Animation is disabled automatically when the system requests reduced motion.

## 9. Architecture

```
┌────────────────────────────────────┐
│  Interface (HTML / CSS / JS)       │  presents, never decides
└──────────────┬─────────────────────┘
               │ pywebview bridge
┌──────────────▼─────────────────────┐
│  ApiAuditor (Python)               │
│   listar_certificados()            │
│   cargar_certificado(nombre)       │
│   verificar_json(contenido)        │
│   auditar_numero(payload)          │
└──────────────┬─────────────────────┘
               │
┌──────────────▼─────────────────────┐
│  auditor_descarte.py               │  the mathematics and the verdict
└────────────────────────────────────┘
```

- The interface calls the auditor; it never reimplements it.
- Certificate names loaded from the repository are restricted to `.json` files inside the certificates folder.
- Long computations run in a worker thread so the window does not freeze.

## 10. Requirements and launch

- Python 3.11 or later
- `pywebview` (`python -m pip install pywebview`)

Launch from the repository root with the repository launcher:

```bash
python rum.py
```

## 11. Licensing

Free for personal, educational and non-commercial research use under the **SPARTACO Primality Auditor Community License v1.0** (see [`LICENSE`](LICENSE)).

Commercial use, including internal use by a company, requires a separate commercial license. Additions, maintenance and customization are provided only under a separate written agreement.

The auditor is distributed independently of the proprietary SPARTACO SECURITY, OM337 and UIS–OMEGA technologies. Third-party components such as `pywebview` keep their own licenses.

**Contact:** Ilver Villasmil · Ilvervillasmil@gmail.com · +1 (512) 923-7344

---

Copyright © 2026 Ilver Villasmil. All rights reserved except as expressly licensed.
