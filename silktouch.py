import requests
import sys

def main():
    # Minecraft-themed terminal banner
    print("""
 \033[95m┌────────────────────────────────────────────────────────────┐
 │   ✨  S I L K T O U C H  //  U s e r n a m e   O S I N T   │
 │                By Mr.HackerCharlie                         │ 
 └────────────────────────────────────────────────────────────┘\033[0m
    """)
    
    user = input("Enter target username to extract: ").strip()
    if not user:
        print("[-] Username cannot be empty.")
        return

    url = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"
    print(f"\n[*] Mining global matrix for: \033[93m{user}\033[0m...\n")

    try:
        with requests.Session() as session:
            res = session.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            if res.status_code != 200:
                print(f"[-] Failed to fetch database matrix. Status: {res.status_code}")
                return

            sites = res.json().get("sites", [])
            found_count = 0
            
            try:
                for target in sites:
                    name = target.get("name")
                    uri = target.get("uri_check").replace("{account}", user)
                    e_code = target.get("e_code")
                    e_string = target.get("e_string")
                    
                    try:
                        response = session.get(
                            uri, 
                            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}, 
                            timeout=3
                        )

                        if response.status_code == e_code:
                            continue

                        if e_string and e_string in response.text:
                            continue
                            
                        print(f"\033[92m[+] HARVESTED\033[0m | \033[96m{name.upper()}\033[0m -> {uri}")
                        found_count += 1
                        
                    except requests.RequestException:
                        # Silently pass network timeouts or dead websites
                        continue
                        
                print(f"\n\033[95m[*] Scan complete. Successfully extracted {found_count} profile blocks.\033[0m")
                
            except KeyboardInterrupt:
                print("\n\n\033[91m[-] Extraction interrupted by user (Ctrl+C).\033[0m")
                sys.exit(0)

    except Exception as e:
        print(f"[-] Critical Error: {e}")

if __name__ == "__main__":
    main()