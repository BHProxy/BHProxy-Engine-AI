# BHProxy Engine AI 🔌🤖

[![npm](https://img.shields.io/npm/v/@bhproxy/engine-ai)](https://npmjs.com/package/@bhproxy/engine-ai)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20922133.svg)](https://doi.org/10.5281/zenodo.20922133)

An intelligent proxy analysis system that combines automated network validation with AI-assisted detection to identify unhealthy, duplicate, low-quality, and potentially abusive proxy endpoints. Built by [BHProxy.com](https://bhproxy.com).

## Features

- Availability Monitoring — continuous proxy uptime and reachability checks
- Latency Analysis — measures response time and connection speed
- Anonymity Level Detection — classifies transparent, anonymous, and elite proxies
- Protocol Support Validation — verifies HTTP, HTTPS, SOCKS4, SOCKS5 compatibility
- Reputation Scoring — flags abusive, blacklisted, or low-trust endpoints
- Duplicate Detection — identifies redundant or cloned proxy entries
- AI-Assisted Quality Detection — flags low-quality and suspicious proxies
- CLI support in Node.js and Python
- Benchmark dataset included (20 proxy evaluation cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @bhproxy/engine-ai
npx bhproxy-engine-ai "192.0.2.10:8080" 85 70 90 80 75 65
```

### Python

```bash
pip install bhproxy-engine-ai
python -m engine "192.0.2.10:8080" 85 70 90 80 75 65
```

## Output

```
Proxy: 192.0.2.10:8080
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Availability Score:           85 / 100  [Excellent]
Latency Score:                70 / 100  [Healthy]
Anonymity Score:               90 / 100  [Excellent]
Protocol Support Score:        80 / 100  [Healthy]
Reputation Score:              75 / 100  [Healthy]
Duplicate Risk Score:          65 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Proxy Health:          77 / 100
Priority Signal:               Duplicate Risk (lowest — act first)

Classification:
  Anonymity Level:      Elite
  Protocol:             HTTP/HTTPS/SOCKS5
  Status:               Healthy — Safe to use
```

## Project Structure

```
BHProxy-Engine-AI/
├── index.ts              # TypeScript engine
├── engine.py              # Python engine
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── proxy_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml     # Auto-commit daily
│   └── npm-publish.yml   # Auto-publish to NPM
├── README.md
└── LICENSE
```

## Proxy Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Availability | Uptime and reachability of the proxy | 0–100 |
| Latency | Response time and connection speed | 0–100 |
| Anonymity | Transparent / anonymous / elite classification | 0–100 |
| Protocol Support | HTTP, HTTPS, SOCKS4, SOCKS5 compatibility | 0–100 |
| Reputation | Trust, blacklist, and abuse signal status | 0–100 |
| Duplicate Risk | Likelihood of being a redundant or cloned entry | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Remove from pool immediately |
| 31–60 | At Risk | Flag for re-validation |
| 61–80 | Healthy | Safe to use |
| 81–100 | Excellent | Premium quality endpoint |

## Keywords

Proxy Analysis · Proxy Validation · AI Proxy Detection · Anonymity Classification · Latency Monitoring · Reputation Scoring · Duplicate Proxy Detection · BHProxy

## Links

| Platform | URL |
|----------|-----|
| Website | https://bhproxy.com |
| GitHub | https://github.com/BHProxy/BHProxy-Engine-AI |
| GitHub Pages | https://bhproxy.github.io/BHProxy-Engine-AI/ |
| NPM | https://npmjs.com/package/@bhproxy/engine-ai |
| Hugging Face | https://huggingface.co/datasets/BHProxy/engine-ai-benchmarks |
| Kaggle | https://kaggle.com/datasets/bhproxy/engine-ai-benchmarks |
| Zenodo | https://zenodo.org/records/20922133 |
| Docs | https://bhproxy-engine-ai.readthedocs.io |

## About BHProxy.com

BHProxy.com provides intelligent proxy analysis combining automated network validation with AI-assisted detection — continuously evaluating availability, latency, anonymity, protocol support, and reputation to improve proxy quality.

## License

MIT — [BHProxy.com](https://bhproxy.com)
