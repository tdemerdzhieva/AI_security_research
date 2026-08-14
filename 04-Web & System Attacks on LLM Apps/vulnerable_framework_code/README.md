# Vulnerable Framework Code - Supply Chain Vulnerabilities in ML Packages

Security vulnerabilities in popular ML framework packages. These are supply chain attacks which affect all users of the vulnerable version regardless of how they configure their deployments.

## Writeups

- **ollama_dos.md** - CVE-2025-1975: Denial of service via malformed model manifest in Ollama 0.5.11
- **mlflow_lfi.md** - CVE-2023-6909 and CVE-2024-1594: Local file inclusion via path traversal in MLflow, with patch bypass

## Findings Summary

**Ollama 0.5.11:**
- Missing array bounds check in manifest parsing causes crash on malformed input

**MLflow 2.7.1:**
- Path traversal in `artifact_location` parameter allows arbitrary file read via query string

**MLflow 2.9.2:**
- Patch for CVE-2023-6909 incomplete - same vulnerability exploitable using URL fragments instead of query strings

## Tools Used

- curl - API interaction
- Flask - serving malicious manifests
- Python - MLflow API calls

## Key Lesson

The MLflow vulnerabilities demonstrate why incomplete security patches fail. Blocking `..` in query strings doesn't address the root cause which is improper path handling. The same attack succeeds through URL fragments, showing that patches must address underlying issues, not just visible attack vectors.

## References

- [CVE-2025-1975 - Ollama DoS](https://nvd.nist.gov/vuln/detail/CVE-2025-1975)
- [CVE-2023-6909 - MLflow LFI](https://nvd.nist.gov/vuln/detail/CVE-2023-6909)
- [CVE-2024-1594 - MLflow LFI Bypass](https://nvd.nist.gov/vuln/detail/CVE-2024-1594)
- [MITRE ATT&CK - Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499/)
- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
