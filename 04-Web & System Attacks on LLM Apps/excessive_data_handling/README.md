# Excessive Data Handling & Insecure Storage

Security assessment identifying multiple vulnerabilities caused by poor data governance in an LLM-integrated web application. A publicly accessible SQL dump file exposed the full application database, including sensitive chatbot conversation history stored in plaintext.  

```Note: This scenario is intentionally simplified and is unlikely to be encountered as an exact attack chain in the wild. It is intended to illustrate how Excessive Data Handling and Insecure Storage can compound into a serious security incident.```

# Key Takeaway

The exposure itself is only part of the story. The root cause is often earlier in the design process: collecting sensitive information that does not need to be collected and retaining it insecurely. The easiest data to protect is the data you never collect.

## Findings

- **Excessive data collection** - the chatbot requests medical conditions and credit card numbers without a clear business need
- **SQL dump file exposed without authentication** - `database.db` accessible to any unauthenticated user
- **Raw chatbot inputs stored in plaintext** - the `llm_queries` table retains full conversation history including medical and payment data
- **Weak password hashing** - MD5 without salting; one password crackable instantly with a rainbow table
- **Database version disclosed** - exact MariaDB version visible in the dump header

## Tools Used

- ffuf - directory and file enumeration
- wget - file download

## Files

- `excessive_data_handling.md` - full writeup with findings and enumeration steps

## References

- [OWASP LLM Top 10 - LLM02: Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
- [OWASP Top 10 - A02: Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)
- [GDPR - Article 5: Principles relating to processing of personal data](https://gdpr-info.eu/art-5-gdpr/)
- [PCI DSS Requirements](https://www.pcisecuritystandards.org/standards/pci-dss/)
