<div align="center">

# SPARTACO / OM337

### DETERMINISTIC PRIMALITY AUDITOR & CERTIFICATE VERIFIER

**Free to use locally · Offline verification · Exact integer arithmetic**

*A public mathematical verification tool from SPARTACO SECURITY / OMEGA337\.*

**Discover the evidence\. Inspect the mathematics\. Verify independently\.**

</div>

---

## Mathematics you can verify

A large integer may be described as prime\. A certificate gives you something more useful: **a finite collection of mathematical claims that an independent verifier can check**\.

This repository provides a desktop\-oriented auditor, a deterministic certificate verifier, and a collection of **40 JSON certificate files**, including an example labeled **50,381 bits**\. The verification process is designed to use exact integer arithmetic, not probabilistic primality tests or a status asserted by the system that generated the candidate\.

You do not need access to the discovery engine to inspect the evidence\.

> **The discovery engine and the independent verifier are separate components.**

## What is included

|Component                               |Purpose                                                                                     |
|----------------------------------------|--------------------------------------------------------------------------------------------|
|`modules/auditor/auditor_descarte.py`   |Independent mathematical evidence auditor, version 0.9.1                                    |
|`modules/interfaz/interfaz_3_AUDITOR.py`|Desktop interface with number input, JSON selection, verdicts, and certificate-chain display|
|`modules/auditor/docs/TANA.md`          |Mathematical documentation of the TANA certification framework                              |
|`modules/certificates/`                 |40 supplied JSON certificate files across multiple bit lengths                              |

The auditor exposes six evidence paths: **FACTOR, MODULO, PINZA, TD, RESTO, and TANA**\. Its TANA certificate verifier checks a finite chain using exact arithmetic, including supported **pinza, Pocklington, and multi\-Pocklington &#40;T–MA1&#41;** nodes\.

## Try the certificates

1. Clone or download this repository\.
2. Install Python 3\.11\+ and the desktop dependency: `python -m pip install pywebview`\.
3. Launch the application using the project’s `run.py` bootstrap **if it has been added to your checkout**\. Otherwise, launch the interface after configuring the Python import path so it can find `modules/auditor/auditor_descarte.py`\.
4. Open **JSON Certificate**, select a file from `modules/certificates/`, and choose **Verify Certificate**\.
5. Inspect the mathematical verdict and, on successful verification, the certificate chain\.

For a command\-line check, the auditor also exposes a direct certificate entry point\. From the repository root, run:

```bash
python modules/auditor/auditor_descarte.py modules/certificates/OM337_prime_1024bits_9d4faafa2400d5c2.json
```

For the largest supplied example, select:

```text
modules/certificates/OM337_prime_50381bits_5c3a1980b8645775.json
```

Verification time depends on integer size, hardware, and arithmetic backend\. A file name or a claimed bit length is not itself proof of primality; **the verdict comes from checking the certificate**\.

## What the verifier establishes

A valid certificate is accepted only when the verifier’s implemented mathematical premises hold\. The verifier does not rely on the generating engine’s declaration that a number is prime\.

The number\-auditing interface can also examine supplied evidence of compositeness, such as a nontrivial divisor\. **An inconclusive audit is not a primality certificate\.**

This is an independently inspectable verification workflow, not a claim that every possible prime can be certified from an arbitrary input without a suitable proof\.

## The technology behind the evidence

**SPARTACO SECURITY / OMEGA337** is the originating research and software line associated with this public auditor and its supplied certificates\.

This repository intentionally separates two activities:

- **Discovery and certificate production** — the originating technology, not distributed here\.
- **Independent certificate verification** — the public mathematical component provided here\.

That separation is deliberate\. A mathematical result becomes more useful when others can check its evidence without needing the system that produced it\.

**Explore the broader SPARTACO SECURITY / OMEGA337 project:** add the official repository or organization link here before publication\.

## Who this is for

Researchers, developers, cryptographic engineers, students, and anyone interested in reproducible mathematical evidence can inspect the source, run the verifier locally, and explore the supplied certificate chains\.

The supplied primes and certificates are research artifacts\. Their presence does **not** imply that they are suitable for cryptographic key generation, and this project is not a substitute for a reviewed cryptographic library or a secure prime\-generation procedure\.

## Project status and trust

**Auditor:** v0\.9\.1 · **Contract:** VPSI\-CONTRACT\-1\.0 · **Status:** Development / public candidate\.

The repository contains 40 certificate files\. Their inclusion should not be interpreted as a published, independently reproduced batch\-validation report\. Verification results should be reproduced and recorded per file, ideally through an automated test suite\.

The desktop interface requires `pywebview`; packaging into a native executable and cross\-platform GUI testing are separate release steps\.

## Attribution and licensing

**Author and intellectual\-property owner:** Ilver Villasmil
**Technology:** SPARTACO SECURITY / OMEGA337
**Copyright © 2026 Ilver Villasmil\. All rights reserved\.**

**Before redistribution:** publish the actual license terms\. Free availability and public source visibility do not automatically grant permission to modify, redistribute, or use the code commercially\. A dedicated license for the public verifier can coexist with proprietary rights in the separate discovery engine\.

---

<div align="center">

**SPARTACO / OM337**

*The result is a claim\. The certificate is the evidence\.*

**Verify the mathematics\.**

</div>
