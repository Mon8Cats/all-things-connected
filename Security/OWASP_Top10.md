# OWASP

The OWASP Top 10 is a standard awareness document for developers and web application security professionals. It represents a consensus regarding the most critical security risks to web applications.

Here is the list from the latest major release, OWASP Top 10: 2021, along with a brief explanation for each category:

Rank	Risk Category	Explanation
A01	Broken Access Control	Occurs when an application fails to properly enforce user permissions. Attackers can exploit these flaws to access sensitive data, view unauthorized user accounts, or perform administrative functions.
A02	Cryptographic Failures	Relates to the inadequate protection of sensitive data at rest and in transit. This often stems from weak encryption algorithms, improper key management, storing data in clear text, or not encrypting data that requires protection (previously known as Sensitive Data Exposure).
A03	Injection	Occurs when untrusted data is sent to an interpreter as part of a command or query. This malicious data can trick the interpreter into executing unintended commands or accessing data without proper authorization. Common examples include SQL, NoSQL, and Command Injection.
A04	Insecure Design	A new category that focuses on risks related to fundamental flaws in the architecture and design of an application. It emphasizes the need for threat modeling, secure design patterns, and establishing adequate security controls at the design stage, rather than just fixing implementation defects.
A05	Security Misconfiguration	This is a broad category covering vulnerabilities that arise from insecure default configurations, incomplete configuration, open cloud storage, misconfigured HTTP headers, verbose error messages that reveal system information, or unpatched and unsecure systems.
A06	Vulnerable and Outdated Components	Using libraries, frameworks, and other third-party software components with known vulnerabilities. These components run with the same privileges as the application itself, and exploiting a vulnerability in one of them can lead to severe data loss or server takeover.
A07	Identification and Authentication Failures	Flaws related to user identity, authentication, and session management. This includes poor password policies, weak or missing multi-factor authentication, allowing brute-force attacks, or insecure handling of session tokens (previously known as Broken Authentication).
A08	Software and Data Integrity Failures	A new category for 2021 that focuses on making assumptions about the integrity of software updates, critical data, and CI/CD pipelines without proper verification. This includes risks from insecure deserialization and failure to validate the integrity of data being processed.
A09	Security Logging and Monitoring Failures	Inadequate logging and ineffective monitoring can prevent timely detection and response to security incidents. This risk includes failures to log security-relevant events, weak alert thresholds, and logs that are not properly stored or secured.
A10	Server-Side Request Forgery (SSRF)	This flaw allows an attacker to cause the server-side application to make an unintended request to any domain the server can access, including internal resources. This can be used to scan internal networks, access metadata services, or interact with other services.


The OWASP Top 10 is a standard awareness document for developers and web application security professionals. It represents a consensus regarding the most critical security risks to web applications.

Here is the list from the latest major release, OWASP Top 10: 2021, along with a brief explanation for each category:

Rank	Risk Category	Explanation
A01	Broken Access Control	Occurs when an application fails to properly enforce user permissions. Attackers can exploit these flaws to access sensitive data, view unauthorized user accounts, or perform administrative functions.
A02	Cryptographic Failures	Relates to the inadequate protection of sensitive data at rest and in transit. This often stems from weak encryption algorithms, improper key management, storing data in clear text, or not encrypting data that requires protection (previously known as Sensitive Data Exposure).
A03	Injection	Occurs when untrusted data is sent to an interpreter as part of a command or query. This malicious data can trick the interpreter into executing unintended commands or accessing data without proper authorization. Common examples include SQL, NoSQL, and Command Injection.
A04	Insecure Design	A new category that focuses on risks related to fundamental flaws in the architecture and design of an application. It emphasizes the need for threat modeling, secure design patterns, and establishing adequate security controls at the design stage, rather than just fixing implementation defects.
A05	Security Misconfiguration	This is a broad category covering vulnerabilities that arise from insecure default configurations, incomplete configuration, open cloud storage, misconfigured HTTP headers, verbose error messages that reveal system information, or unpatched and unsecure systems.
A06	Vulnerable and Outdated Components	Using libraries, frameworks, and other third-party software components with known vulnerabilities. These components run with the same privileges as the application itself, and exploiting a vulnerability in one of them can lead to severe data loss or server takeover.
A07	Identification and Authentication Failures	Flaws related to user identity, authentication, and session management. This includes poor password policies, weak or missing multi-factor authentication, allowing brute-force attacks, or insecure handling of session tokens (previously known as Broken Authentication).
A08	Software and Data Integrity Failures	A new category for 2021 that focuses on making assumptions about the integrity of software updates, critical data, and CI/CD pipelines without proper verification. This includes risks from insecure deserialization and failure to validate the integrity of data being processed.
A09	Security Logging and Monitoring Failures	Inadequate logging and ineffective monitoring can prevent timely detection and response to security incidents. This risk includes failures to log security-relevant events, weak alert thresholds, and logs that are not properly stored or secured.
A10	Server-Side Request Forgery (SSRF)	This flaw allows an attacker to cause the server-side application to make an unintended request to any domain the server can access, including internal resources. This can be used to scan internal networks, access metadata services, or interact with other services.

Export to Sheets
Why is the OWASP Top 10 Important?
The OWASP Top 10 is crucial because:

Awareness: It provides a list of the most critical risks that development teams and security teams should be aware of.

Prioritization: It helps organizations prioritize their security efforts by focusing resources on the most prevalent and high-impact threats.

Standardization: It serves as a baseline for security requirements, testing methodologies, and vendor tool comparisons.