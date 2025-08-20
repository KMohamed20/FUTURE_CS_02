# 🛑 OWASP Top 10 2025 Analysis

| Risque | Relevé dans notre projet |
|--------|--------------------------|
| **A01: Broken Access Control** | Détecté via accès multiples à `/admin` |
| **A03: Injection** | Détecté via `union select`, `<script>` |
| **A05: Security Misconfiguration** | Logs non chiffrés détectés |
| **A10: Server-Side Request Forgery** | Tentatives de SSRF détectées |
