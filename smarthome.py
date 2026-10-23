import random


class WelcomeScreen:
    def play(self):
        print("\n--- SMART HOME SYSTEM ---")
        print("Welcome home!")
        print("Your smart devices are ready.")
        print("-------------------------\n")


class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.actions = ["TURN ON", "TURN OFF", "CHECK STATUS"]

    def run_device(self):
        action = random.choice(self.actions)
        print(f"{self.name}: {action}")
        if action == "TURN ON":
            print(f"{self.name} is now ON.")
        elif action == "TURN OFF":
            print(f"{self.name} is now OFF.")
        else:
            print(f"{self.name} is working normally.")
        print("-" * 25)


class SmartHome:
    def __init__(self):
        self.welcome = WelcomeScreen()
        self.devices = [
            SmartDevice("Living Room Light"),
            SmartDevice("Smart Fan"),
            SmartDevice("Front Door Lock")
        ]

    def start_simulation(self):
        self.welcome.play()
        device = random.choice(self.devices)
        print(f"Selected device: {device.name}\n")
        device.run_device()


home = SmartHome()
home.start_simulation()
