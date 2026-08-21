from cyber_easy.tools.base_tool import Tool

class CaesarCipher(Tool):
    def __init__(self):
        super().__init__(
            toolName = "Caesar Cipher",
            toolDescription = "Encrypt and Decrypt text using Caesar Cipher"
        )
    
    def encrypt(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a') #ord is used to check the ascii number of the base letter that is either A or a
                result += chr((ord(char) - base + shift) %26 + base) #after ascii number is found, cipher operations are done on it and resulting number is again transformed back to char using chr
            else:
                result += char
        return result

    def decrypt(self, text, shift):
        return self.encrypt(text, -shift)

    def run(self):
        print(self.display_info())
        choice = input("\nDo you wanna encrypt(E) or decrypt(D) the text? ").upper()
        text = input("\nEnter text: ")
        shift = int(input("Enter shift(1-25): "))
        
        #validate shift
        if shift>=1 or shift<=25:
            print(f"Shift is {shift}")
        else:
            print("shift is out of bounds")


        #validate choice
        if choice == 'E':
            print(f"\nEncrypted text: {self.encrypt(text,shift)}")
        elif choice == 'D':
            print(f"\nDecrypted text: {self.decrypt(text,shift)}")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.run()