<div align="center">

# SPARTACO / OM337

### DETERMINISTIC PRIMALITY AUDITOR & CERTIFICATE VERIFIER

**Free local verification · Offline operation · Exact integer arithmetic**

*A public mathematical verification tool from SPARTACO SECURITY / OMEGA337\.*

**Discover the evidence\. Inspect the mathematics\. Verify independently\.**

</div>

---


## The SPARTACO Technology Family

**SPARTACO SECURITY** is a proprietary security architecture developed by Ilver Villasmil. It brings together cryptographic protection, identity and authorization controls, mathematical computation, and independently verifiable evidence.

Its components serve distinct purposes within a common technological framework.

<img width="1168" height="784" alt="image" src="https://github.com/user-attachments/assets/1ce44e89-07bd-49bf-be7e-52ee9293e5a9" />



```text
                  SPARTACO SECURITY
             Unified Security Architecture
                           │
          ┌────────────────┼────────────────┐
          │                │                │
        OM337          UIS–OMEGA       MATHEMATICAL
     Cryptographic     Mathematical     CERTIFICATION
        Engine           Engine           UIS–TANA
          │                │                │
          └────────────────┼────────────────┘
                           │
                INDEPENDENT AUDITOR
               Public · Free · Offline
```

### Core Technologies

**OM337 — Cryptographic Engine.** A specialized cryptographic component operating on structured bit transformations, with defined encryption and decryption procedures.

**UIS–OMEGA — Mathematical Engine.** A mathematical framework for prime-number construction, analysis, and deterministic certification through verifiable arithmetic evidence.

**UIS–TANA — Mathematical Certification.** A nodal-algebraic framework combining certified dependencies, number-theoretic conditions, and finite proof chains to establish primality.

**SPARTACO Primality Auditor — Independent Verifier.** The public tool provided in this repository. It independently checks mathematical evidence and compatible primality certificates, including those produced by UIS–OMEGA, without requiring access to the proprietary engine.

### One Architecture. Distinct Capabilities.

**Independently verifiable mathematics.**

The auditor is freely available as a public verification instrument. The underlying proprietary technologies remain separate from its distribution.

---

## Mathematics you can verify

Primality is a mathematical property, not a label assigned by software\. A deterministic certificate makes that distinction concrete: it supplies a finite chain of statements that can be checked using exact integer arithmetic\.

**SPARTACO / OM337** provides an independent primality\-certificate verifier and mathematical evidence auditor\. It is designed to validate compatible certificates **regardless of which system generated the prime or constructed its proof**\.

The repository also includes **40 JSON certificate files** produced within the SPARTACO SECURITY / OMEGA337 technology line, spanning multiple integer sizes and including a **50,381\-bit** example\. These certificates give users immediately available material for exploring and reproducing the verification process offline\.

**The discovery engine and the independent verifier are separate components\.**

## Two complementary capabilities

### 01 — Verify deterministic primality certificates

Load a compatible JSON certificate and let the verifier check its mathematical chain\. The verifier independently recalculates the implemented conditions; it does not accept a prime label, an engine status, or an external assertion as proof\.

The supported TANA certificate nodes include **exact trial division &#40;pinza&#41;, Pocklington, and multi\-Pocklington &#40;T–MA1&#41;**\ [TANA](modules/auditor/docs/TANA.md). A valid chain leads to a deterministic primality verdict\. A malformed, unsupported, or mathematically insufficient chain is not accepted as proof\.

This capability is **not restricted to OM337\-generated primes**\. A prime from another source can be verified when accompanied by a certificate satisfying the verifier’s supported proof format and premises\.

### 02 — Audit integer evidence

Enter an integer and, optionally, provide evidence such as a candidate factor, modular information, or a supported algebraic relation\. The auditor evaluates the supplied evidence and reports whether it establishes compositeness, reveals a contradiction, or remains insufficient\.

<img width="1245" height="819" alt="image" src="https://github.com/user-attachments/assets/d7ee8649-9b1f-4577-b94d-068a3976acbd" />

**Entering an arbitrary prime without a certificate does not automatically produce a deterministic primality proof\.** This distinction keeps the auditor’s conclusions mathematically meaningful\.

## What is included

|Component                               |Role                                                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------------------------------|
|`modules/auditor/auditor_descarte.py`   |Independent mathematical auditor and TANA certificate verifier                                       |
|`modules/interfaz/interfaz_3_AUDITOR.py`|Desktop interface for integer auditing, JSON verification, verdicts, and certificate-chain inspection|
|`modules/auditor/docs/TANA.md`          |Mathematical description of the certification framework                                              |
|`modules/certificates/`                 |40 supplied JSON certificates, including the 50,381-bit example                                      |

The auditor provides six evidence channels: **FACTOR · MODULO · PINZA · TD · RESTO · TANA**\. Each has a defined role; the certificate channel is responsible for deterministic primality certification through a verified proof chain\.

## Run the verifier locally

**Requirements:** Python 3\.11\+; `pywebview` for the desktop interface\.

```bash
python -m pip install pywebview
```

If your checkout includes the application bootstrap, start the desktop application from the repository root:

```bash
python rum.py
```

The supplied repository snapshot may not contain `run.py`; in that case, use the auditor directly or add the bootstrap before launching the GUI\.

### Verify a supplied certificate from the command line

```bash
python modules/auditor/auditor_descarte.py modules/certificates/OM337_prime_1024bits_9d4faafa2400d5c2.json
```

### Explore the 50,381\-bit certificate

```text
modules/certificates/OM337_prime_50381bits_5c3a1980b8645775.json
```

### Verify your own certificate

Supply a compatible JSON certificate to the same command\-line verifier or select it in the desktop interface\. The candidate may come from OM337 or from another mathematical workflow; acceptance depends on the proof, not its origin\.

Verification time depends on certificate size, hardware, and the arithmetic implementation\.

## The technology behind the certificates

**SPARTACO SECURITY** is the broader security and mathematical software technology line\. **OMEGA337** is the originating computational architecture associated with the supplied prime results and their deterministic certificates\.

This public repository presents a deliberately separate capability: **independent mathematical verification**\. Users can examine the certificate structure and reproduce the verifier’s checks without requiring access to the proprietary discovery and certificate\-production engine\.

<img width="847" height="497" alt="image" src="https://github.com/user-attachments/assets/8ee75475-da08-4394-b682-2245c6243598" />

The distinction matters:

- **OMEGA337:** produces prime results and their supporting certification artifacts within the originating technology line\.
- **UIS–TANA:** defines the mathematical certification structure used by the supplied proofs\.
- **AUDITOR\_DESCARTE:** independently checks the supported mathematical conditions and issues the resulting verdict\.

The verifier is a useful tool in its own right, not merely a viewer for OM337 output\.

**SPARTACO SECURITY / OMEGA337 — originating technology and research:** &#91;[(https://www.academia.edu/176025899/SPARTACO_SECURITY)]&#93;

## Inspect the mathematics

A deterministic verification workflow is designed to be reproducible\. Users can inspect the JSON nodes, trace their dependencies, and compare each mathematical condition against the implemented verifier and the accompanying TANA documentation\.

The verification process uses exact integer arithmetic rather than probabilistic primality tests\. It does not trust the generating engine’s declared state\.

The supplied certificate collection illustrates the workflow across different bit lengths\. The public verifier also accepts compatible certificates supplied independently by users\.

## Intended audience

This project is intended for mathematical researchers, software engineers, cryptographic developers, educators, and anyone who wants to examine deterministic primality evidence locally\.

A certified prime is a mathematical result\. It is **not automatically a secure cryptographic key**, and the verifier is not a replacement for a security\-reviewed key\-generation system\.

## Project information

**Auditor:** v0\.9\.1
**Verification contract:** VPSI\-CONTRACT\-1\.0
**Execution model:** Local / offline
**Author and intellectual\-property owner:** Ilver Villasmil
**Technology:** SPARTACO SECURITY / OMEGA337

## Licensing

SPARTACO Primality Auditor & Verifier is available free of charge for personal, educational, and non-commercial research use under the SPARTACO Primality Auditor Community License v1.0. The full terms are in the [LICENSE](LICENSE.md) file.

This license covers the Python source code, the desktop interface, the launcher, the 40 JSON certificate files, and the documentation [TANA](modules/auditor/docs/TANA.md). Each material has specific permissions, described in the [LICENSE](LICENSE.md) file.

Commercial use, enterprise deployment, product integration, commercial redistribution, and commercial exploitation of modified versions require a separate commercial license. **This includes internal use by a company, even when the auditor is neither sold nor redistributed.**

The following are not included in the free license and are provided only under a separate written agreement and for a fee: additions or changes requested by you, maintenance, customization, and any other support or development work.

The auditor is distributed independently of the proprietary SPARTACO SECURITY, OM337, and UIS–OMEGA technologies, which are not licensed by this repository. Third-party components, such as `pywebview`, keep their own licenses.

***DOCUMENTATION AND CONTEXT*** [SPARTACO_SECURITY](docs/README.md) 

The official versions and updates are those published in this repository.

Copyright © 2026 Ilver Villasmil. All rights reserved except as expressly licensed.

For commercial licensing and enterprise agreements, contact the rights holder through the official SPARTACO SECURITY licensing channel:

**Ilver Villasmil**
Email: Ilvervillasmil@gmail.com
Phone: +1 (512) 923-7344


---

<div align="center">

**SPARTACO / OM337**

*The result is a claim\. The certificate is the evidence\.*

**Verify the mathematics\.**

</div>
