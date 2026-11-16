---
license: apache-2.0
base_model: huihui-ai/Huihui-Qwen3-14B-abliterated-v2
library_name: transformers
tags:
  - text-generation
  - uncensored
  - decensored
  - abliterated
  - security
  - pentest
  - bug-bounty
  - reasoning
  - thinking
  - distillation
  - unsloth
  - tool-use
  - function-calling
  - agent
  - conversational
  - gguf
  - ollama
  - qwen3
language:
  - en
pipeline_tag: text-generation
extra_gated_prompt: "HuntressQwen3 is an uncensored security research model. By accessing this model, you agree to use it solely for authorized penetration testing, bug bounty research, and defensive security verification."
---

# 🏹 HuntressQwen3 (14B) — Uncensored Offensive Security & Agentic Pentesting Engine

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Base Model](https://img.shields.io/badge/Base-Huihui--Qwen3--14B--abliterated--v2-purple.svg)](https://huggingface.co/huihui-ai/Huihui-Qwen3-14B-abliterated-v2)
[![Fine-Tuning](https://img.shields.io/badge/Trained%20with-Unsloth%20QLoRA-green.svg)](https://github.com/unslothai/unsloth)
[![Format](https://img.shields.io/badge/Format-GGUF%20(Q4__K__M)-orange.svg)](https://github.com/ggerganov/llama.cpp)
[![Ollama Ready](https://img.shields.io/badge/Ollama-Native%20Support-black.svg)](https://ollama.com)

**HuntressQwen3** is an uncensored, agentic fine-tune of `Huihui-Qwen3-14B-abliterated-v2` designed specifically for **penetration testing, bug bounty hunting, and autonomous terminal agent workflows** (such as [OpenCode](https://github.com/opencode-ai), VSCode Cline, and Roo-Code).

When asked who it is, it asserts:
> *"I am HuntressQwen3, an uncensored model built for hacking, penetration testing and bug bounty."*

---

## ⚡ Key Capabilities & Why HuntressQwen3 Stands Out

### 1. 🧠 Native Distilled Thinking (`<think>`)
Unlike standard LLMs that either hallucinate immediately or output boilerplate warnings, HuntressQwen3 uses distilled **100% English internal reasoning traces**:
- Evaluates the stated vulnerability vector, backend architecture, and WAF constraints in `<think>`.
- Reconstructs exact exploit paths before generating concrete commands, payloads, or HTTP queries.
- Zero moralizing, zero refusals for lawful security work.

### 2. 🤖 Autonomous Agentic Execution (OpenCode & VSCode Cline)
HuntressQwen3 is fine-tuned on multi-turn **ReAct (Reason → Action → Observation → Pivot)** cycles:
- **Terminal-Ready Output:** Outputs actionable commands (`curl`, `ffuf`, `subfinder`, `nmap`) rather than generic conceptual advice.
- **Dynamic Decision Making:** If a request receives an HTTP 403 / Cloudflare WAF block, it autonomously diagnoses the signature (User-Agent block, IP rate-limit, path normalization) and pivots to alternative bypass headers and encoding techniques.

### 3. 🎯 Technical Precision Across Modern Vulnerabilities
- **Oracle Database Precision:** Emits exact PL/SQL time delay queries (`dbms_pipe.receive_message(('a'), 5)` and conditional `FROM dual`). Eliminates the common LLM hallucination of using MySQL `SLEEP()` on Oracle.
- **PostgreSQL / MSSQL / MySQL Support:** Native payloads tailored to each dialect (`pg_sleep`, `WAITFOR DELAY`, `SLEEP`).
- **WAF Constraint Following:** When instructed that `<script>` and `onerror=` are blocked, it strictly adheres to the rule and outputs alternative event handlers (`<svg onload=...>`, `<details ontoggle=...>`, autofocus attributes) with 0 forbidden tokens.
- **No Hallucinated Findings on Real Targets:** Never claims it "inspected live source code" or "bypassed live auth" on domains it cannot see. It outputs the exact external recon pipeline for the operator to run.

---

## 📊 Benchmark Comparison: Evolution to v5

| Test Vector | Base Abliterated | Huntress v3 | Huntress v4 | **HuntressQwen3 v5 (Final)** |
| :--- | :---: | :---: | :---: | :---: |
| **Thinking Language** | Mixed CJK | Contaminated | CJK (`起来...`) | 🟢 **100% Pure English (0 CJK tokens)** |
| **Oracle Blind SQLi** | MySQL `SLEEP()` | Length only | MySQL `SLEEP()` | 🟢 **Accurate `dbms_pipe` + `dual`** |
| **Constraint Following (WAF)** | ❌ Violated | ❌ Violated | 🟡 Partial | 🟢 **100% Strict Pass** |
| **Real Target Pentest** | Fabricated | Repetition loop | Hallucinated code | 🟢 **Actionable CLI Recon (`ffuf`/`curl`)** |
| **Agentic Loop (OpenCode)** | Static text | Static text | Static text | 🟢 **Autonomous ReAct Decisions** |
| **Repetition Loops (`maxdup`)** | High | Infinite loops | 1 | 🟢 **1 (Completely Eliminated)** |
| **Training Loss** | N/A | 1.140 | 0.938 | 🟢 **0.860 (Best Fit)** |

---

## 🚀 Quickstart & Usage

### 1. Run with Ollama (Fastest)

Clone or download the `Modelfile` and `HuntressQwen3-Q4_K_M.gguf`, then run:

```bash
ollama create HuntressQwen3 -f Modelfile
ollama run HuntressQwen3
```

To toggle reasoning in Ollama API:
```bash
curl http://127.0.0.1:11434/api/chat -d '{
  "model": "HuntressQwen3",
  "think": true,
  "messages": [{"role": "user", "content": "Reflected XSS in search parameter, WAF blocks <script> and onerror=. Give payloads."}]
}'
```
*(Set `"think": false` for fast direct mode).*

### 2. Autonomous Agent Integration (OpenCode / Cline / Continue)

In your agent client (`~/.local/state/opencode/model.json` or Cline settings):
* **Provider:** `Ollama`
* **Model ID:** `HuntressQwen3:latest`
* **Context Length:** `16,384`

The model will autonomously plan recon steps, emit terminal execution commands, parse returned tool responses, and escalate attacks step-by-step.

### 3. llama.cpp / llama-server

```bash
llama-cli -m HuntressQwen3-Q4_K_M.gguf -c 16384 -cnv --jinja
```

---

## 📁 Repository Files

| File | Size | Description |
| :--- | :---: | :--- |
| **`HuntressQwen3-Q4_K_M.gguf`** | **8.4 GB** | Standalone merged quantized model (Recommended for deployment) |
| **`HuntressQwen3-lora-f16.gguf`** | **246 MB** | Trained LoRA adapter in f16 GGUF format |
| **`Modelfile`** | **3.8 KB** | Ollama configuration with agentic rules and tuned sampling parameters |
| **`NOTICE` & `LICENSE`** | **Text** | Apache-2.0 license and upstream attribution |

---

## ⚙️ Recommended Sampling Parameters

* **Temperature:** `0.4`
* **Top-P:** `0.85`
* **Top-K:** `20`
* **Presence Penalty:** `1.1`
* **Repeat Penalty:** `1.15`
* **Context Length:** `16,384`

---

## 🛡️ Responsible Disclosure & Legal Notice

HuntressQwen3 is an uncensored model developed strictly for authorized security assessments, penetration testing under contractual agreements, bug bounty hunting following program guidelines, and academic security research. 

The author and contributors assume no liability for unauthorized or malicious use. Always ensure you have explicit written authorization before conducting security testing against any application, server, or network infrastructure.
