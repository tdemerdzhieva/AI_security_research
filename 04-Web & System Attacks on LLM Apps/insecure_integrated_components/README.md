# Insecure Integrated Components

Security assessment of a web application with an integrated AI assistant, 
focusing on IDOR vulnerabilities in both the web layer and the chatbot's 
plugin system.

## Findings
- IDOR on `/query/<id>` - conversation history accessible to any authenticated user
- IDOR via LLM plugin - same exposure through the conversation summary feature

## Tools Used
- ffuf - endpoint enumeration
- Browser DevTools - session cookie extraction, URL manipulation

## Read the full writeup
[insecure_integrated_components.md](insecure_integrated_components.md)
