# Model Deployment Tampering - RCE via SSRF and Java Deserialization

Remote code execution against TorchServe through a combination of server-side request forgery (SSRF) and unsafe Java deserialization. The attack chain uses a malicious workflow artifact to instantiate a Java gadget that executes arbitrary commands on the deployment host.

## Findings

- **Exposed management API** - TorchServe management interface accessible without authentication
- **SSRF in workflow upload** - the `/workflows` endpoint fetches arbitrary URLs and processes the content
- **Unsafe YAML deserialization** - spec files containing Java object instantiation syntax are deserialized without validation
- **Java gadget chain instantiation** - URLClassLoader loads and instantiates arbitrary classes from attacker-controlled servers
- **No privilege separation** - TorchServe running as root boosts the impact of code execution

## Attack Chain

```
Management API discovery → SSRF test → craft malicious workflow → 
Java exploit class → package with torch-workflow-archiver → 
serve exploit → trigger SSRF → reverse shell as root
```

## Tools Used

- curl - API exploration and SSRF testing
- javac - compiling the exploit class
- torch-workflow-archiver - packaging the malicious workflow
- Python http.server - serving the exploit
- netcat - catching the reverse shell

## Files

`torchserve_deployment_rce.md` - full writeup with exploitation steps and technique notes  
`payloads/` - source code for the exploitation chain  
`handler.py` - minimal workflow handler  
`spec.yaml` - YAML spec containing the URLClassLoader gadget  
`MyScriptEngineFactory.java` - Java class implementing the reverse shell exploit  


## References

- [OWASP - Server-Side Request Forgery (SSRF)](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)
- [Java Deserialization Security](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
- [Java URLClassLoader Documentation](https://docs.oracle.com/javase/8/docs/api/java/net/URLClassLoader.html)
- [MITRE ATLAS - ML Model Inference API Access](https://atlas.mitre.org/techniques/AML.T0040)
