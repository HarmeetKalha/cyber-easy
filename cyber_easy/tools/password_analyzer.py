import re
from cyber_easy.tools.base_tool import Tool

class PasswordAnalyzer(Tool):
    def __init__(self):
        super().__init__(
            toolName = "Password Analyzer",
            toolDescription = "A tool made for analyzing password strength and provide feedback"
        )
    def analyze(self, password):
        score = 0
        feedback = []

            #check password length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use atleast 8 characters")

            #check uppercase
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Use an uppercase letter")
            
            #check lowercase
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Use a lowercase letter")

            #check for number
        if re.search(r'\d',password):
            score += 1
        else: 
            feedback.append("Add a number")

            #check for special characters
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Add special characters")

        levels = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
        return score, levels[score], feedback
    
   #def display_info(self):
     #   self.display_info()

    def run(self):
        print(self.display_info()) 
        password = input("\n Enter password to analyze: ")
        score,level,feedback = self.analyze(password)
        print(f"\nStrength: {level}")   
        if feedback:
            print("suggestions:")
            for tip in feedback:
                print(f"{tip} ")
    

if __name__ == "__main__":
    analyzer = PasswordAnalyzer()
    analyzer.run()      