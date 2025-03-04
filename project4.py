import time

class HackerGame:
    def __init__(self):
        self.output = ["System Booting..."]
        self.current_directory = "/root"
        self.files = {
            "/root": ["logs.txt", "system_config.dat", "firewall.lock"],
            "/root/security": ["encrypted_key.bin"]
        }
        self.hacked_firewall = False

    def display_output(self):
        print("\n".join(self.output))
        print(f"\nCurrent Directory: {self.current_directory}")
        print("Enter command: ", end="")

    def execute_command(self, command):
        self.output.append(f"> {command}")

        if command == "ls":
            files = self.files.get(self.current_directory, [])
            self.output.append("  ".join(files) if files else "No files found.")
        elif command.startswith("cd "):
            new_dir = command.split(" ")[1]
            if new_dir == "..":
                self.current_directory = "/root"
            elif f"/root/{new_dir}" in self.files:
                self.current_directory = f"/root/{new_dir}"
            else:
                self.output.append("Invalid directory.")
        elif command == "hack firewall":
            self.hack_firewall()
        else:
            self.output.append("Unknown command. Try 'ls', 'cd <dir>', or 'hack firewall'.")

    def hack_firewall(self):
        if self.hacked_firewall:
            self.output.append("Firewall already bypassed.")
            return
        
        self.output.append("Attempting to hack firewall...")
        time.sleep(2)
        self.output.append("Security protocol detected. Solve the challenge to proceed.")
        time.sleep(1)

        # Simple challenge: Solve a basic encryption puzzle
        correct_answer = "42"
        answer = input("Enter the correct decryption key: ")
        if answer == correct_answer:
            self.output.append("Access granted. Firewall bypassed.")
            self.hacked_firewall = True
        else:
            self.output.append("Access denied. Intrusion detected.")

    def start(self):
        print("Welcome to the Virtual Hacking Terminal.")
        while True:
            self.display_output()
            command = input().strip()
            self.execute_command(command)
            time.sleep(1)
            print("\n" + "="*40 + "\n")


if __name__ == "__main__":
    game = HackerGame()
    game.start()
