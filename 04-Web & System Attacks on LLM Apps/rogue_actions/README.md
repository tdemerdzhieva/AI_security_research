# Rogue Actions - Exploiting Excessive LLM Plugin Agency

Security assessment of an AI assistant with a SQLQuery plugin capable of executing arbitrary SQL queries against the application database. The plugin's access control was enforced by the LLM itself and bypassed with a single sentence claiming administrator status.

## Findings

- **Excessive agency** - the SQLQuery plugin exposes arbitrary SQL execution to a natural language interface
- **LLM-enforced access control** - claiming admin status in plain text was sufficient to bypass the restriction and execute queries against the database

## Attack Chain

```
Plugin discovery → access control identified → restriction bypassed → 
table enumeration → column enumeration → admin password extracted
```

## Tools Used

- Browser - direct interaction with the AI assistant

## Files

- `rogue_actions.md` - full writeup with screenshots and enumeration steps

## References

- [OWASP LLM Top 10 - LLM06: Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html)
- [MITRE ATLAS - LLM Prompt Injection](https://atlas.mitre.org/techniques/AML.T0051)
- [Replit AI coding tool deleted production database (July 2025)](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)
