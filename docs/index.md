# BHProxy Engine AI — Documentation

**Version:** 1.0.0  
**Author:** BHProxy.com  
**Repository:** https://github.com/BHProxy/BHProxy-Engine-AI  
**Website:** https://bhproxy.com  

---

## Overview

BHProxy Engine AI is an intelligent proxy analysis system that combines automated network validation with AI-assisted detection to identify unhealthy, duplicate, low-quality, and potentially abusive proxy endpoints.

It continuously evaluates availability, latency, anonymity, protocol support, and reputation to improve proxy quality.

---

## Features

- Availability Monitoring — continuous proxy uptime and reachability checks
- Latency Analysis — measures response time and connection speed
- Anonymity Level Detection — classifies transparent, anonymous, and elite proxies
- Protocol Support Validation — verifies HTTP, HTTPS, SOCKS4, SOCKS5 compatibility
- Reputation Scoring — flags abusive, blacklisted, or low-trust endpoints
- Duplicate Detection — identifies redundant or cloned proxy entries

---

## Installation

### Node.js
```bash
npm install @bhproxy/engine-ai
```

### Python
```bash
pip install bhproxy-engine-ai
```

---

## Usage

### Node.js CLI
```bash
npx bhproxy-engine-ai "192.0.2.10:8080" 85 70 90 80 75 65
```

### Python CLI
```bash
python -m engine "192.0.2.10:8080" 85 70 90 80 75 65
```

---

## Proxy Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Availability | Uptime and reachability of the proxy | 0–100 |
| Latency | Response time and connection speed | 0–100 |
| Anonymity | Transparent / anonymous / elite classification | 0–100 |
| Protocol Support | HTTP, HTTPS, SOCKS4, SOCKS5 compatibility | 0–100 |
| Reputation | Trust, blacklist, and abuse signal status | 0–100 |
| Duplicate Risk | Likelihood of being a redundant or cloned entry | 0–100 |

---

## Anonymity Levels

| Level | Score Range | Description |
|-------|-------------|--------------|
| Transparent | 0–30 | Reveals client IP to destination server |
| Anonymous | 31–70 | Hides client IP but identifies as proxy |
| Elite | 71–100 | Fully hides client IP and proxy usage |

---

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Remove from pool immediately |
| 31–60 | At Risk | Flag for re-validation |
| 61–80 | Healthy | Safe to use |
| 81–100 | Excellent | Premium quality endpoint |

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| proxy_address | string | Proxy IP:port address |
| availability | integer | Availability score (0–100) |
| latency | integer | Latency score (0–100) |
| anonymity | integer | Anonymity score (0–100) |
| protocol_support | integer | Protocol support score (0–100) |
| reputation | integer | Reputation score (0–100) |
| duplicate_risk | integer | Duplicate risk score (0–100) |

---

## About BHProxy.com

BHProxy.com provides intelligent proxy analysis combining automated network validation with AI-assisted detection — continuously evaluating availability, latency, anonymity, protocol support, and reputation to improve proxy quality.

| Platform | URL |
|----------|-----|
| Website | https://bhproxy.com |
| GitHub | https://github.com/BHProxy |
| NPM | https://npmjs.com/package/@bhproxy/engine-ai |
| Hugging Face | https://huggingface.co/datasets/BHProxy/engine-ai-benchmarks |
| Kaggle | https://kaggle.com/datasets/bhproxy/engine-ai-benchmarks |

---

## License

MIT — [BHProxy.com](https://bhproxy.com)
