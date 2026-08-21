import hashlib
from cyber_easy.tools.base_tool import Tool

class HashGenerator(Tool):
    def __init__(self):
        super().__init__(
            toolName = "Hash Generator",
            toolDescription = "Generates MD5, SHA256 and SHA512 hashes for any text"
        )
    
    def generate(self,text,choice):
        encoded = text.encode()
        
        if choice == "MD5":
            return {"MD5": hashlib.md5(encoded).hexdigest()}
        elif choice == "SHA256":
            return{"SHA256": hashlib.sha256(encoded).hexdigest()}
        elif choice == "SHA512":
            return{"SHA512": hashlib.sha512(encoded).hexdigest()}
        else:
            print("choose the correct hashing algorithm")
            return None

    def run(self):
        print(f"\n{self.display_info()}")
        text = input("\nEnter text to hash: ")
        choice = input("\nChoose a hashing algorithm (MD5/SHA256/SHA512): ").upper()
        hashes = self.generate(text,choice)
        if hashes is None:
            return
        for algo,value in hashes.items():
            print(f"{algo}: {value}")


if __name__ == "__main__":
    hash = HashGenerator()
    hash.run()