# ===============================================================
# SPARTACO / OM337 — INTERFAZ DE AUDITORÍA DETERMINISTA
# Un único archivo de interfaz, siguiendo interfaz_3.py.
# HTML + CSS + JavaScript integrados como cadena multilínea legible.
# Requiere auditor_descarte.py junto a este archivo.
# Copyright (c) 2026 Ilver Villasmil. All rights reserved.
# ===============================================================
from __future__ import annotations
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from auditor_descarte import auditar, verificar_certificado_tana, CertificadoInvalido

CARA = {"id": "SPARTACO_AUDITOR", "nombre": {"es": "Auditor determinista", "en": "Deterministic auditor"}}

HTML = r'''
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SPARTACO / OM337 — Auditor</title>
<style>
/* ===============================================================
 * COLORES Y CAJA
 * Tokens, barra lateral, paneles y marco de luz.
 * =============================================================== */
:root,:root[data-tema="1"]{--bg:#070e1a;--side:#0a1424;--panel:#0f1b2e;--panel2:#0b1626;--border:#2a3d58;--text:#f8fafc;--text2:#c5d4e8;--muted:#8fa0b7;--cyan:#38bdf8;--blue:#2563eb;--green:#22c55e;--red:#ef4444;--amber:#f59e0b;--glass:rgba(15,27,46,.72)}
:root[data-tema="2"]{--bg:#0b0814;--side:#140c1c;--panel:#1a1026;--panel2:#120a1a;--border:#3d2a52;--text:#f8fafc;--text2:#d4c5e8;--muted:#a78fb7;--cyan:#c084fc;--blue:#7c3aed;--green:#22c55e;--red:#ef4444;--amber:#f59e0b;--glass:rgba(26,16,38,.72)}
:root[data-tema="2"] body{background:radial-gradient(circle at 88% -8%,rgba(124,58,237,.22),transparent 40%),var(--bg)}
:root[data-tema="2"] .sidebar{border-right-color:rgba(192,132,252,.18)}
:root[data-tema="2"] .logo{border-radius:50%}
:root[data-tema="2"] .panel,.card,.hero{border-radius:26px}
:root[data-tema="2"] .hbar button{border-radius:12px;padding:8px 14px}
:root[data-tema="2"] .hero{margin-top:18px;min-height:54vh}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(circle at 12% -10%,rgba(37,99,235,.16),transparent 42%),var(--bg);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:.01em}
.layout{display:flex;min-height:100vh}
.sidebar{width:230px;background:var(--side);border-right:1px solid var(--border);padding:20px 14px;position:sticky;top:0;height:100vh;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:10px;padding:4px 8px 20px}
.logo{width:36px;height:36px;border-radius:9px;background:var(--blue);display:grid;place-items:center;font-weight:800}
.brand-name{font-weight:800;letter-spacing:1px}
.languages{display:flex;gap:7px;margin-bottom:12px}
.languages button{appearance:none;-webkit-appearance:none;border:1px solid var(--border);background:#0b1626;color:#c5d4e8;border-radius:7px;padding:5px 11px;cursor:pointer}
.languages button.active{background:#2563eb;border-color:#2563eb;color:#fff}
.hbar{margin:0 0 12px;padding:0;background:transparent;border:0}
#ui3-aviso:empty{display:none}
.sidebar{width:230px;background:var(--side);border-right:1px solid var(--border);padding:20px 14px;position:sticky;top:0;height:100vh;display:flex;flex-direction:column;overflow:hidden}
.ui3-marca{margin:8px 0 0;padding:10px;border:1px solid rgba(56,189,248,.28);border-radius:14px;background:#071018;flex:1;min-height:0;display:flex;flex-direction:column;overflow:hidden}
.ui3-marca p{margin:0;font-size:14px;line-height:1.35;font-weight:750;color:var(--text)}
.ui3-flujo{margin-top:10px;overflow:hidden;flex:1;padding-right:2px;overflow-anchor:none}
.ui3-nodo{opacity:.28;border:1px solid rgba(34,211,238,.16);border-radius:10px;background:#081725;padding:7px 8px;margin:0 0 6px;overflow-anchor:none}
.ui3-nodo.on{opacity:1;border-color:rgba(34,211,238,.45)}
.ui3-nodo.bad.on{border-color:rgba(239,68,68,.55)}
.ui3-nodo .rid{color:#22d3ee;font-size:9px;font-weight:700;letter-spacing:.12em}
.ui3-nodo strong{display:block;font-size:12px;margin-top:2px}
.ui3-nodo span{display:block;color:#8b9bb4;font-size:10px;line-height:1.3}
.ui3-linea{width:1px;height:10px;margin:-2px auto 4px;background:transparent;overflow-anchor:none}
.ui3-linea.on{background:#22d3ee;box-shadow:0 0 6px rgba(34,211,238,.7)}
.ui3-corte{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.nav{display:flex;flex-direction:column;gap:3px}
.nav button{border:0;background:transparent;color:var(--text2);border-radius:8px;padding:11px 12px;text-align:left;cursor:pointer}
.nav button.active,.nav button:hover{background:var(--panel);color:white}
.main{width:calc(100% - 230px);padding:26px 30px 70px;max-width:1400px}
h1{margin:0 0 8px;font-size:30px;line-height:1.25;letter-spacing:.04em;font-weight:800;overflow:visible}
h2{font-size:20px;margin:0 0 10px;line-height:1.3;font-weight:750;overflow:visible}
h3{margin:0 0 10px;color:var(--cyan);font-size:15px;letter-spacing:.04em}
.subtitle{color:var(--muted);margin:0 0 12px;line-height:1.5}
.user-dock{display:none}
.panel,.card,.wizard-step,pre,.obs-pru,.obs-op,.obs-cap,.mod-card{
  position:relative;isolation:isolate;overflow:hidden;
}
.panel{
  background:var(--panel);border:1px solid rgba(34,211,238,.16);
  border-radius:14px;padding:16px;margin-bottom:14px;
}
.card{background:var(--panel2);border:1px solid rgba(34,211,238,.12);border-radius:12px;padding:14px}
.panel::before,.card::before,.mod-card::before,.obs-pru::before,.obs-op::before,.obs-cap::before{
  content:"";position:absolute;inset:-60%;z-index:0;pointer-events:none;
  background:conic-gradient(from 180deg,transparent 0 64%,rgba(34,211,238,0) 70%,rgba(34,211,238,.85) 78%,rgba(37,99,235,.45) 84%,transparent 92% 100%);
  animation:marcoGira 18s linear infinite;
}
.panel::after,.card::after,.mod-card::after,.obs-pru::after,.obs-op::after,.obs-cap::after{
  content:"";position:absolute;inset:1px;z-index:0;pointer-events:none;border-radius:13px;
  background:radial-gradient(circle at 92% 8%,rgba(34,211,238,.07),transparent 42%),var(--panel);
}
.card::after,.mod-card::after{background:radial-gradient(circle at 92% 8%,rgba(34,211,238,.06),transparent 42%),var(--panel2);border-radius:11px}
.panel>*,.card>*,.mod-card>*{position:relative;z-index:1}
@keyframes marcoGira{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){
  .panel::before,.card::before,.mod-card::before,.obs-pru::before,.obs-op::before,.obs-cap::before{animation:none;opacity:.28}
}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.state{font-size:13px;color:var(--muted);margin:6px 0}
.ready{color:var(--green)!important}
.bad{color:var(--red)!important}
.warn{color:var(--amber)!important}
.btn{border:0;border-radius:10px;padding:10px 14px;font-weight:700;letter-spacing:.02em;cursor:pointer;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease,background .16s ease}
.primary{background:linear-gradient(180deg,#3b82f6,#1d4ed8);color:#fff;box-shadow:0 0 0 1px rgba(56,189,248,.28),0 0 18px rgba(37,99,235,.28)}
.primary:hover{transform:translateY(-1px);box-shadow:0 0 0 1px rgba(56,189,248,.5),0 0 22px rgba(56,189,248,.35)}
.secondary{background:rgba(12,22,40,.88);border:1px solid rgba(56,189,248,.28);color:var(--text)}
.secondary:hover{border-color:var(--cyan);color:#fff;box-shadow:0 0 14px rgba(56,189,248,.18)}
.btn:disabled{opacity:.45;cursor:default;transform:none;box-shadow:none}
input[type=file],input[type=text],input[type=number],select,textarea{width:100%;background:rgba(8,18,32,.9);border:1px solid var(--border);border-radius:10px;color:var(--text);padding:10px;transition:border-color .16s ease,box-shadow .16s ease}
input:focus,select:focus,textarea:focus{outline:0;border-color:rgba(56,189,248,.7);box-shadow:0 0 0 3px rgba(56,189,248,.12)}
textarea{min-height:90px;font-family:ui-monospace,monospace}
label{display:block;color:var(--muted);font-size:12px;margin:10px 0 4px}
.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.note{font-size:12px;color:var(--muted);line-height:1.5}
.hidden{display:none!important}
details{margin-top:10px}
summary{cursor:pointer;color:var(--text2);font-weight:650}
pre{background:var(--panel2);border:1px solid var(--border);border-radius:9px;padding:12px;overflow:auto;white-space:pre-wrap;word-break:break-word;font-size:12px}
.mono{font-family:ui-monospace,monospace;color:var(--cyan)}
.pill{display:inline-block;border:1px solid var(--border);background:rgba(12,22,40,.8);border-radius:999px;padding:4px 9px;font-size:11px;font-weight:700;letter-spacing:.04em;color:var(--text2);margin:2px}
.pill-ok{border-color:rgba(34,197,94,.55);color:#4ade80;background:rgba(34,197,94,.08);box-shadow:0 0 10px rgba(34,197,94,.12)}
.pill-warn{border-color:rgba(245,158,11,.55);color:#fbbf24;background:rgba(245,158,11,.08)}
.pill-bad{border-color:rgba(239,68,68,.55);color:#f87171;background:rgba(239,68,68,.08)}
.pill-opt{border-color:rgba(56,189,248,.28);color:#7dd3fc;background:rgba(56,189,248,.06)}
.estado-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:8px}
.estado-score{font-size:28px;font-weight:800;letter-spacing:.04em;color:var(--cyan);line-height:1}
.estado-score span{font-size:14px;color:var(--muted);font-weight:650;margin-left:4px}
.hbar{position:sticky;top:0;background:linear-gradient(180deg,rgba(7,14,26,.96),rgba(7,14,26,.86));border-bottom:0;margin:0 0 6px;padding:8px 0 10px;overflow-x:auto;white-space:nowrap;z-index:5;backdrop-filter:blur(10px)}
.hbar button{border:1px solid rgba(56,189,248,.16);background:rgba(12,22,40,.7);color:var(--text2);border-radius:999px;padding:6px 12px;margin-right:6px;cursor:pointer;font-weight:650;font-size:12px;letter-spacing:.02em;transition:border-color .16s ease,box-shadow .16s ease,background .16s ease}
.hbar button.active{background:rgba(37,99,235,.35);border-color:rgba(56,189,248,.7);color:#fff;box-shadow:0 0 16px rgba(56,189,248,.22)}
.hbar button:hover{color:#fff;border-color:rgba(56,189,248,.45)}
.usersec{display:none}
.usersec.active{display:block}
/* Interfaz 3: proyeccion humana. El backend no cambia. */
.ui3-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:14px}
.ui3-grid-3{grid-template-columns:repeat(3,minmax(0,1fr))}
.ui3-card{background:var(--panel2);border:1px solid rgba(56,189,248,.16);border-radius:12px;padding:14px;min-height:126px}
.ui3-card h3{margin-bottom:8px}
.ui3-k{font-size:11px;letter-spacing:.08em;color:var(--muted);text-transform:uppercase;margin-bottom:6px}
.ui3-v{font-size:18px;font-weight:800;line-height:1.25;word-break:break-word}
.ui3-v.small{font-size:14px;font-weight:700;color:var(--text2)}
.ui3-status{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 0;border-top:1px dashed var(--border)}
.ui3-status:first-child{border-top:0}
.ui3-status .label{color:var(--text2);font-size:13px}
.ui3-status .value{font-size:12px;font-weight:750;text-align:right}
.ui3-section-head{display:flex;justify-content:space-between;gap:16px;align-items:flex-start;flex-wrap:wrap}
.ui3-section-head p{max-width:760px}
.ui3-warning{border-left:3px solid var(--amber);padding:10px 12px;background:rgba(245,158,11,.06);border-radius:8px;color:var(--text2);font-size:12px}
.ui3-good{color:var(--green)}
.ui3-missing{color:var(--amber)}
.ui3-muted{color:var(--muted)}
.ui3-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.ui3-table{width:100%;border-collapse:collapse;font-size:12px}
.ui3-table th,.ui3-table td{padding:9px 8px;border-top:1px solid var(--border);text-align:left;vertical-align:top}
.ui3-table th{color:var(--muted);font-weight:700}
.ui3-table td{color:var(--text2)}
.ui3-history-row{display:grid;grid-template-columns:130px minmax(150px,.7fr) minmax(180px,1fr) 120px;gap:10px;padding:9px 0;border-top:1px dashed var(--border);font-size:12px}
.ui3-history-row:first-child{border-top:0}
.ui3-history-row .when{color:var(--muted);font-family:ui-monospace,monospace}
.ui3-history-row .state{margin:0}
@media(max-width:900px){.ui3-grid,.ui3-grid-3{grid-template-columns:1fr}
.ui3-history-row{grid-template-columns:1fr 1fr}
.ui3-history-row .when{grid-column:1/-1}}
/* Wizard */
.wizard-step{display:grid;grid-template-columns:36px 1fr auto;gap:14px;align-items:center;padding:14px;border:1px solid var(--border);border-radius:10px;background:var(--panel2);margin-bottom:8px}
.wizard-num{width:36px;height:36px;border-radius:50%;background:var(--panel);display:grid;place-items:center;color:var(--cyan);font-weight:700}
.wizard-done .wizard-num{background:var(--green);color:white}
.wizard-todo .wizard-num{background:var(--panel);color:var(--muted)}
.wizard-body h4{margin:0 0 3px;font-size:14px}
.wizard-body .note{margin:0}
/* Ruta clasica */
.route{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px}
.route-step{background:var(--panel2);border:1px solid var(--border);border-radius:10px;padding:12px;min-height:82px}
.route-step strong{display:block;color:var(--cyan);font-size:11px;margin-bottom:5px}
.route-step span{font-size:12px;color:var(--text2)}
.result{margin-top:10px;padding:12px;border-radius:9px;background:var(--panel2);border:1px solid var(--border);font-size:13px}
.cap-row{padding:10px 0;border-top:1px dashed var(--border)}
.cap-row:first-child{border-top:0}
.muelle{margin-top:auto;padding-top:16px;display:flex;flex-direction:column;gap:8px}
.muelle-card{position:relative;isolation:isolate;overflow:hidden;padding:10px 10px 9px;border:1px solid rgba(34,211,238,.16);border-radius:12px;background:var(--panel)}
.muelle-card::before{content:"";position:absolute;inset:-70%;z-index:0;pointer-events:none;background:conic-gradient(from 200deg,transparent 0 70%,rgba(34,211,238,.8) 78%,transparent 88%);animation:marcoGira 22s linear infinite}
.muelle-card::after{content:"";position:absolute;inset:1px;z-index:0;border-radius:11px;background:var(--panel)}
.muelle-card>*{position:relative;z-index:1}
.muelle-k{font-size:9px;letter-spacing:.16em;color:var(--cyan);font-weight:700}
.muelle-v{margin:4px 0 0;font-size:13px;font-weight:700;line-height:1.3}
.muelle-n{margin:3px 0 0;font-size:11px;color:var(--muted);line-height:1.35}
.muelle-btn{width:100%;border:1px solid rgba(34,211,238,.28);background:rgba(37,99,235,.22);color:var(--text);border-radius:9px;padding:8px 10px;font-size:12px;font-weight:650;cursor:pointer;text-align:left}
.muelle-btn:hover{background:var(--blue);border-color:var(--blue);color:#fff}
.statusbar{font-size:11px;color:var(--muted);margin-top:8px}
/* Developer */
.list{display:flex;flex-direction:column;gap:5px}
.list button{border:1px solid rgba(56,189,248,.14);background:rgba(12,22,40,.72);color:var(--text2);padding:8px 10px;border-radius:9px;text-align:left;cursor:pointer}
.list button.active{border-color:var(--cyan);color:var(--cyan);box-shadow:0 0 12px rgba(56,189,248,.16)}
.hero{position:relative;padding:36px 18px 28px;margin:14px 0 18px;min-height:62vh;display:flex;align-items:center;overflow:hidden;border:1px solid var(--border);border-radius:22px;background:radial-gradient(circle at 70% 40%,rgba(34,211,238,.12),transparent 42%),radial-gradient(circle at 20% 80%,rgba(37,99,235,.18),transparent 36%),#071018}
.hero-stage{position:absolute;inset:0;pointer-events:none}
.hero-ring{position:absolute;border:1px solid rgba(34,211,238,.22);border-radius:50%;left:58%;top:46%;transform:translate(-50%,-50%)}
.hero-ring.r1{width:120px;height:120px;animation:spin 28s linear infinite}
.hero-ring.r2{width:210px;height:210px;border-color:rgba(37,99,235,.28);animation:spin 48s linear infinite reverse}
.hero-ring.r3{width:320px;height:320px;border-style:dashed;animation:spin 70s linear infinite}
.hero-core{position:absolute;left:58%;top:46%;width:18px;height:18px;margin:-9px 0 0 -9px;border-radius:50%;background:var(--cyan);box-shadow:0 0 28px rgba(34,211,238,.7)}
.hero-copy{position:relative;z-index:1;max-width:640px}
.hero-kicker{letter-spacing:.18em;font-size:12px;color:var(--cyan);font-weight:700}
.hero h1{font-size:clamp(28px,5vw,44px);line-height:1.2;margin:12px 0 14px;max-width:none}
.hero .lead{font-size:16px;color:var(--text2);max-width:46ch;line-height:1.6}
.portada-block{padding:22px 4px}
.portada-block h2{font-size:26px;line-height:1.2;max-width:22ch;margin:0 0 10px}
.portada-close{text-align:center;padding:48px 16px;border:1px solid var(--border);border-radius:16px;background:#071018}
.portada-close p{font-size:22px;line-height:1.35;max-width:22ch;margin:0 auto 18px}
.mod-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}
.mod-card{background:var(--panel2);border:1px solid var(--border);border-radius:12px;padding:14px}
.mod-card .rid{font-family:ui-monospace,monospace;color:var(--cyan);font-size:11px;letter-spacing:.06em}
@keyframes spin{to{transform:translate(-50%,-50%) rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.hero-ring{animation:none}}
@media(max-width:720px){.hero{min-height:auto;padding:28px 14px}
.hero-ring.r3{display:none}
.hero-core,.hero-ring{left:86%;top:18%}}
.confirm-modal{position:fixed;inset:0;background:rgba(5,10,20,.72);display:flex;align-items:center;justify-content:center;z-index:50;padding:18px}
.confirm-modal.hidden{display:none!important}
.confirm-box{width:min(520px,100%);background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:18px}
.ui3-status-row{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid var(--border)}
.ui3-status-row .value{color:var(--cyan);font-family:ui-monospace,monospace;font-size:12px;white-space:nowrap;overflow-x:auto;max-width:68%;text-align:right}
.result.ok,.result.ready{color:#86efac}


/* Standalone public auditor extension */
.main{max-width:none}
.sidebar{flex-shrink:0}
.ui3-marca{overflow-y:auto}
.ui3-flujo{overflow:visible}
.ui3-nodo{opacity:1}
.ui3-nodo.on{box-shadow:0 0 14px rgba(34,211,238,.12)}
.audit-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
.audit-grid .panel{min-height:270px}
.result-value{font-size:20px;font-weight:800;word-break:break-word}
.audit-header{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.audit-kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.audit-kpis .ui3-card{min-height:85px}
.audit-kpis .ui3-v{font-size:23px;font-weight:800}
.node-list{max-height:420px;overflow:auto}
.node-line{display:grid;grid-template-columns:50px 1fr 90px;gap:12px;align-items:center;padding:10px;border-bottom:1px solid var(--border);font-size:13px}
.node-line b{color:var(--cyan)}
.node-line em{font-style:normal;text-align:right;color:var(--muted)}
.file-caption{overflow-wrap:anywhere;color:var(--text2);font-size:12px;margin-top:8px}
#result-box{min-height:100px}
#status-message{min-height:18px}
.wide{grid-column:1/-1}
@media(max-width:1050px){.audit-grid{grid-template-columns:1fr}}
@media(max-width:720px){.sidebar{height:auto}
.ui3-marca{display:none}
.audit-kpis{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="layout">
<aside class="sidebar">
<div class="brand">
<div class="logo">S</div>
<div class="brand-name">SPARTACO</div>
</div>
<div class="languages">
<button id="lang-es" class="active" onclick="setLang('es')">ES</button>
<button id="lang-en" onclick="setLang('en')">EN</button>
</div>
<div class="ui3-marca">
<p>OM337 · AUDITOR</p>
<div class="ui3-flujo" id="flow">
</div>
</div>
<div class="muelle">
<div class="muelle-card">
<div class="muelle-k">SPARTACO / OM337</div>
<div class="muelle-v" id="side-state">OFFLINE</div>
<div class="muelle-n">DETERMINISTA · 6 VÍAS</div>
</div>
<div class="statusbar">INDEPENDENT MATHEMATICAL VERIFIER</div>
</div>
</aside>
<main class="main">
<div class="audit-header">
<div>
<h1>SPARTACO <span class="mono">/ OM337</span>
</h1>
<p class="subtitle" id="subtitle">Auditor matemático independiente · Sin conexión · Sin motor privado</p>
</div>
<span class="pill pill-ok">OFFLINE · v0.9.1</span>
</div>
<nav id="user-hbar" class="hbar">
<button id="tab-audit" class="active" onclick="showTab('audit')">AUDITORÍA</button>
<button id="tab-chain" onclick="showTab('chain')">CADENA TANA</button>
<button id="tab-about" onclick="showTab('about')">ARQUITECTURA</button>
</nav>
<section id="view-audit">
<div class="audit-grid">
<div class="panel">
<h2 id="num-title">01 / Número entero</h2>
<p class="note" id="num-help">Introduce N. Opcionalmente aporta un divisor o evidencias adicionales. Sin certificado no se declara primo.</p>
<label for="n">N · INTEGER</label>
<textarea id="n" rows="3" spellcheck="false" placeholder="17">
</textarea>
<details>
<summary id="extra-title">Evidencias opcionales</summary>
<div class="two">
<div>
<label>FACTOR</label>
<input id="factor" type="text" placeholder="3">
<label>P (N = 2p + d)</label>
<input id="p" type="text" placeholder="">
</div>
<div>
<label>MÓDULOS (separados por coma)</label>
<input id="modulos" type="text" placeholder="3, 5">
<label>D (N = 2p + d)</label>
<input id="d" type="text" placeholder="">
</div>
</div>
<label>RESTOS / DIVISORES (separados por coma)</label>
<input id="residuos" type="text" placeholder="">
</details>
<div class="actions">
<button class="btn primary" id="btn-audit" onclick="runAudit()">AUDITAR N</button>
<button class="btn secondary" onclick="clearAll()" id="btn-clear">LIMPIAR</button>
</div>
</div>
<div class="panel">
<h2 id="cert-title">02 / Certificado JSON</h2>
<p class="note" id="cert-help">Selecciona un archivo local. La validación TANA se ejecuta una sola vez al pulsar verificar.</p>
<label for="cert-file">CERTIFICADO · .JSON</label>
<input id="cert-file" type="file" accept=".json,application/json" onchange="loadCert(event)">
<div class="file-caption" id="file-info">Ningún archivo seleccionado</div>
<div class="actions">
<button class="btn primary" id="btn-cert" onclick="runCert()" disabled>VERIFICAR CERTIFICADO</button>
<button class="btn secondary" id="btn-example" onclick="loadExample()">EJEMPLO LOCAL</button>
</div>
<p class="note" id="cert-note">El ejemplo local es un certificado pequeño de prueba. El certificado gigante se puede cargar desde disco.</p>
</div>
<div class="panel wide">
<div class="audit-header">
<h2 id="result-title">03 / Dictamen matemático</h2>
<span class="pill pill-opt" id="status-message">EN ESPERA</span>
</div>
<div id="result-box">
<p class="note">El resultado aparecerá aquí después de ejecutar el auditor.</p>
</div>
</div>
</div>
</section>
<section id="view-chain" class="hidden">
<div class="panel">
<h2 id="chain-title">Cadena de certificación TANA</h2>
<p class="note" id="chain-help">Los nodos se muestran como verificados únicamente después de una certificación exitosa.</p>
<div class="audit-kpis" id="chain-kpis">
</div>
<div class="node-list" id="chain-nodes">
<p class="note">Sin cadena verificada.</p>
</div>
</div>
</section>
<section id="view-about" class="hidden">
<div class="panel">
<h2>SPARTACO / OM337</h2>
<p id="about-text">Auditor público independiente. Verifica evidencia matemática sin revelar ni ejecutar el motor privado de descubrimiento.</p>
<div class="ui3-grid">
<div class="ui3-card">
<h3>FACTOR · MÓDULO · RESTO</h3>
<p class="note">Divisibilidad exacta para demostrar composición.</p>
</div>
<div class="ui3-card">
<h3>PINZA · TD · TANA</h3>
<p class="note">Consulta auxiliar, identidad algebraica y certificación determinista de primalidad.</p>
</div>
</div>
<p class="note">AUDITOR_DESCARTE v0.9.1 · VPSI-CONTRACT-1.0 · © 2026 Ilver Villasmil · Uso y redistribución sujetos a licencia.</p>
</div>
</section>
</main>
</div>
<script>
let lang='es',certText=null,verified=null,busy=false;
const $=id=>document.getElementById(id);
const strings={es:{subtitle:'Auditor matemático independiente · Sin conexión · Sin motor privado',num:'01 / Número entero',numHelp:'Introduce N. Opcionalmente aporta un divisor o evidencias adicionales. Sin certificado no se declara primo.',extra:'Evidencias opcionales',cert:'02 / Certificado JSON',certHelp:'Selecciona un archivo local. La validación TANA se ejecuta una sola vez al pulsar verificar.',result:'03 / Dictamen matemático',chain:'Cadena de certificación TANA',chainHelp:'Los nodos se muestran como verificados únicamente después de una certificación exitosa.',audit:'AUDITAR N',verify:'VERIFICAR CERTIFICADO',clear:'LIMPIAR',none:'Ningún archivo seleccionado',wait:'EN ESPERA',example:'EJEMPLO LOCAL'},en:{subtitle:'Independent mathematical auditor · Offline · No private engine',num:'01 / Integer input',numHelp:'Enter N and optional mathematical evidence. Without a certificate, primality is not asserted.',extra:'Optional evidence',cert:'02 / JSON certificate',certHelp:'Select a local file. TANA verification runs exactly once when you press verify.',result:'03 / Mathematical verdict',chain:'TANA certification chain',chainHelp:'Nodes are marked verified only after successful certification.',audit:'AUDIT N',verify:'VERIFY CERTIFICATE',clear:'CLEAR',none:'No file selected',wait:'READY',example:'LOCAL EXAMPLE'}};
function setLang(v){lang=v;for(const l of ['es','en'])$('lang-'+l).classList.toggle('active',l===v);const t=strings[v];for(const [id,key] of Object.entries({'subtitle':'subtitle','num-title':'num','num-help':'numHelp','extra-title':'extra','cert-title':'cert','cert-help':'certHelp','result-title':'result','chain-title':'chain','chain-help':'chainHelp','btn-audit':'audit','btn-cert':'verify','btn-clear':'clear','btn-example':'example'}))$(id).textContent=t[key];}
function showTab(v){for(const x of ['audit','chain','about']){$('view-'+x).classList.toggle('hidden',x!==v);$('tab-'+x).classList.toggle('active',x===v);}}
function renderFlow(){const names=['FACTOR','MÓDULO','PINZA','TD','RESTO','TANA'];$('flow').innerHTML=names.map((x,i)=>'<div class="ui3-nodo on">
<span class="rid">0'+(i+1)+' / EVIDENCE</span>
<strong>'+x+'</strong>
</div>'+(i<5?'<div class="ui3-linea on">
</div>':'' )).join('');}
function safe(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function setBusy(b){busy=b;$('btn-audit').disabled=b;$('btn-cert').disabled=b||!certText;$('status-message').textContent=b?'CALCULANDO…':strings[lang].wait;}
function display(res){const good=res.estado==='PRIMO_POR_DESCARTE',bad=res.estado==='COMPUESTO_VERIFICADO',color=good?'ready':bad?'bad':'warn';$('result-box').innerHTML='<div class="result-value '+color+'">'+safe(res.estado||'ERROR')+'</div>
<p>'+safe(res.justificacion||res.error||'')+'</p>'+(res.bits?'<span class="pill">'+res.bits+' bits</span>':'')+(res.nodos?'<span class="pill">'+res.nodos+' nodos</span>':'');$('status-message').textContent=good?'CERTIFICADO':bad?'COMPUESTO':'REVISAR';}
function renderChain(res){verified=res.estado==='PRIMO_POR_DESCARTE'?res:null;const details=verified?.detalles||[];$('chain-kpis').innerHTML=verified?'<div class="ui3-card">
<div class="ui3-k">BITS</div>
<div class="ui3-v">'+verified.bits+'</div>
</div>
<div class="ui3-card">
<div class="ui3-k">NODOS</div>
<div class="ui3-v">'+details.length+'</div>
</div>
<div class="ui3-card">
<div class="ui3-k">TANA</div>
<div class="ui3-v ready">VALID</div>
</div>':'';$('chain-nodes').innerHTML=details.length?details.map(d=>'<div class="node-line">
<b>#'+String(d.indice+1).padStart(2,'0')+'</b>
<strong>'+safe(d.tipo.toUpperCase())+'</strong>
<em>'+d.bits+' bits ✓</em>
</div>').join(''):'<p class="note">Sin cadena verificada.</p>';}
async function bridge(method,arg){if(!window.pywebview?.api?.[method])throw Error('Desktop Python bridge unavailable. Open with main_auditor.py.');return await window.pywebview.api[method](arg);}
async function runAudit(){if(busy)return;setBusy(true);try{const r=await bridge('auditar_numero',{n:$('n').value,factor:$('factor').value,modulos:$('modulos').value,p:$('p').value,d:$('d').value,residuos:$('residuos').value});display(r);renderChain(r);}catch(e){display({estado:'ERROR',error:String(e)})}finally{setBusy(false)}}
async function runCert(){if(busy||!certText)return;setBusy(true);try{const r=await bridge('verificar_json',certText);display(r);renderChain(r);if(r.estado==='PRIMO_POR_DESCARTE')showTab('chain');}catch(e){display({estado:'ERROR',error:String(e)});renderChain({})}finally{setBusy(false)}}
async function loadCert(ev){const f=ev.target.files?.[0];certText=null;renderChain({});if(!f){$('file-info').textContent=strings[lang].none;$('btn-cert').disabled=true;return}if(f.size>12*1024*1024){display({estado:'ERROR',error:'JSON exceeds 12 MiB input limit'});return}certText=await f.text();$('file-info').textContent=f.name+' · '+(f.size/1024).toFixed(1)+' KiB';$('btn-cert').disabled=false;}
function loadExample(){certText=JSON.stringify({N:'71',bits_N:7,arbol:[{tipo:'pinza',n:'5'},{tipo:'pinza',n:'7'},{tipo:'multi_pock',n:'71',ancestros:[{q:'5',a:'2'},{q:'7',a:'2'}]}]});$('file-info').textContent='example_71.json';$('btn-cert').disabled=false;}
function clearAll(){for(const id of ['n','factor','modulos','p','d','residuos','cert-file'])$(id).value='';certText=null;renderChain({});$('btn-cert').disabled=true;$('file-info').textContent=strings[lang].none;$('result-box').innerHTML='';$('status-message').textContent=strings[lang].wait;showTab('audit');}
renderFlow();
</script>
</body>
</html>
'''


MAX_JSON_BYTES = 12 * 1024 * 1024
MAX_N_DIGITS = 100000
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def parse_int(value, label, optional=False):
    s = str(value if value is not None else "").strip()
    if not s and optional:
        return None
    if not s or len(s.lstrip('+-')) > MAX_N_DIGITS or not s.lstrip('+-').isascii() or not s.lstrip('+-').isdigit():
        raise ValueError(f"{label}: expected a decimal integer (up to {MAX_N_DIGITS} digits)")
    return int(s)


def parse_list(value, label):
    if not str(value or '').strip():
        return []
    parts = str(value).split(',')
    if len(parts) > 1000:
        raise ValueError(f'{label}: too many entries')
    return [parse_int(p, label) for p in parts]


def _verify_cert(raw):
    if not isinstance(raw, str) or len(raw.encode('utf-8')) > MAX_JSON_BYTES:
        raise ValueError('JSON missing or exceeds 12 MiB')
    cert = json.loads(raw)
    # One mathematical verification, no repeated auditar() pass.
    proof = verificar_certificado_tana(cert)
    return {'estado':'PRIMO_POR_DESCARTE','justificacion':'Exact deterministic TANA certificate verified',**proof}


def _audit_numero(payload):
    n = parse_int(payload.get('n'), 'N')
    factor = parse_int(payload.get('factor'), 'factor', True)
    p = parse_int(payload.get('p'), 'p', True)
    d = parse_int(payload.get('d'), 'd', True)
    modulos = parse_list(payload.get('modulos'), 'modulos')
    residuos = parse_list(payload.get('residuos'), 'residuos')
    res = auditar(n, factor=factor, p=p, d=d, modulos=modulos, residuos=residuos)
    return {'estado':res.estado.value,'justificacion':res.justificacion,'bits':n.bit_length()}


class ApiAuditor:
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=2)

    def verificar_json(self, contenido_json):
        try:
            return self.pool.submit(_verify_cert, contenido_json).result()
        except (ValueError, TypeError, OverflowError) as exc:
            return {'estado':'CERTIFICADO_INVALIDO','justificacion':str(exc)}

    def auditar_numero(self, payload):
        try:
            return self.pool.submit(_audit_numero, payload).result()
        except (ValueError, TypeError, OverflowError) as exc:
            return {'estado':'ENTRADA_INVALIDA','justificacion':str(exc)}


def main():
    import webview
    webview.create_window('SPARTACO / OM337 — Auditor Determinista', html=HTML, js_api=ApiAuditor(), width=1280, height=820, min_size=(900,620))
    webview.start(debug=False)

if __name__ == '__main__':
    main()
