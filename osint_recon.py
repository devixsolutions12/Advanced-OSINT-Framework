import dns.resolver
import requests
import json
import socket

class OSINTRecon:
    def __init__(self, target):
        self.target = target

    def get_dns_records(self):
        print(f"[*] Enumerating DNS records for {self.target}...")
        records = ['A', 'AAAA', 'MX', 'NS', 'TXT']
        results = {}
        for qtype in records:
            try:
                answers = dns.resolver.resolve(self.target, qtype)
                results[qtype] = [rdata.to_text() for rdata in answers]
            except Exception:
                pass
        return results

    def run(self):
        print(f"--- ADVANCED OSINT RECON: {self.target} ---")
        dns_data = self.get_dns_records()
        print(json.dumps(dns_data, indent=4))
        
if __name__ == "__main__":
    target = input("Enter target domain: ")
    recon = OSINTRecon(target)
    recon.run()
