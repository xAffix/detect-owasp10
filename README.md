# Detect OWASP Top 10 Vulnerabilities

This repository contains a tool designed to detect and report common vulnerabilities as defined by the [OWASP Top 10](https://owasp.org/www-project-top-ten/) list. The OWASP Top 10 represents the most critical security risks to web applications. This tool provides detection mechanisms for some of the most prevalent issues, helping developers and security professionals secure their applications.

## Features

- **SQL Injection Detection**: Scans for vulnerabilities that allow attackers to execute arbitrary SQL queries.
- **Broken Authentication**: Detects weak or missing authentication mechanisms that may lead to account compromise.
- **Cross-Site Scripting (XSS) Detection**: Identifies spots where user input is improperly sanitized, potentially leading to XSS attacks.
- **Broken Access Control**: Checks for improper access control mechanisms, ensuring that users cannot escalate privileges or access unauthorized data.

## Modules

1. **SQL Injection**
    - Detects basic and advanced SQL injection attempts.
    - Scans query parameters and form inputs for potential vulnerabilities.
    
2. **Broken Authentication**
    - Ensures that proper session management and password protections are in place.
    - Identifies weak password storage mechanisms.

3. **Cross-Site Scripting (XSS)**
    - Identifies areas where untrusted input is being reflected in a response without proper sanitization.
    - Scans for stored, reflected, and DOM-based XSS vulnerabilities.

4. **Broken Access Control**
    - Examines access control rules for improper configuration or bypassable mechanisms.
    - Detects common misconfigurations that could lead to unauthorized access.

## Usage

### Prerequisites
- Python 3.x
- Required libraries from `requirements.txt
