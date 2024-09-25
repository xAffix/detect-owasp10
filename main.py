import argparse
from scanner import sql_injection, broken_auth, xss
from scanner.utils import validate_url
import sys

def main():
    parser = argparse.ArgumentParser(description="OWASP Top 10 Vulnerability Scanner")
    parser.add_argument("url", help="The URL of the website to scan")
    parser.add_argument("--all", action="store_true", help="Run all available scans")
    parser.add_argument("--sql", action="store_true", help="Run SQL Injection scan")
    parser.add_argument("--auth", action="store_true", help="Run Broken Authentication scan")
    parser.add_argument("--xss", action="store_true", help="Run Cross-Site Scripting (XSS) scan")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()
    
    url = validate_url(args.url)
    if not url:
        print("Invalid URL provided. Please check and try again.")
        return

    vulnerable = False

    try:
        if args.all or args.sql:
            print("Running SQL Injection scan...")
            if sql_injection.scan(url):
                vulnerable = True
    except Exception as e:
        print(f"Error during SQL Injection scan: {e}")

    try:
        if args.all or args.auth:
            print("Running Broken Authentication scan...")
            if broken_auth.scan(url):
                vulnerable = True
    except Exception as e:
        print(f"Error during Broken Authentication scan: {e}")

    try:
        if args.all or args.xss:
            print("Running XSS scan...")
            if xss.scan(url):
                vulnerable = True
    except Exception as e:
        print(f"Error during XSS scan: {e}")

    print("\nScan Summary:")
    print(f"SQL Injection: {'Vulnerable' if args.sql and vulnerable else 'Safe'}")
    print(f"Broken Authentication: {'Vulnerable' if args.auth and vulnerable else 'Safe'}")
    print(f"XSS: {'Vulnerable' if args.xss and vulnerable else 'Safe'}")

    if vulnerable:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
