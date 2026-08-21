# main.py
from cyber_easy.tools.password_analyzer import PasswordAnalyzer
from cyber_easy.tools.caesar_cipher import CaesarCipher
from cyber_easy.tools.hash_generator import HashGenerator
from cyber_easy.tools.port_scanner import PortScanner

def main():
    tools = [
        PasswordAnalyzer(),
        CaesarCipher(),
        HashGenerator(),
        PortScanner()
    ]

    print("=" * 40)
    print("   Cyber-Easy — by Harmeet Singh Kalha")
    print("=" * 40)

    while True:
        print("\nAvailable Tools:")
        for i, tool in enumerate(tools, 1):
            print(f"  {i}. {tool.toolName}")
        print("  0. Exit")

        choice = input("\nSelect a tool: ")

        if choice == '0':
            print("Goodbye.")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(tools):
            tools[int(choice) - 1].run()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()