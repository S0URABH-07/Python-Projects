class Credential:
    def __init__(self, website, username, password):
        self.website = website.strip().lower()  # Normalize website keys (e.g., GitHub.com -> github.com)
        self.username = username.strip()
        self.password = password.strip()

    def update_password(self, new_password):
        if len(new_password.strip()) == 0:
            print("Error: Password field cannot be completely empty!")
            return False
            
        self.password = new_password.strip()
        print(f"Password updated successfully for {self.website}.")
        return True

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

    def __str__(self):
        return f"Site: {self.website:<20} | User: {self.username:<25} | Pass: {'*'*len(self.password)} ({self.password})"