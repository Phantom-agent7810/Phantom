from config.settings import APP_NAME, VERSION
from brain.brain import Brain


class Loader:
    def start(self):
        print("==========================")
        print(f"{APP_NAME} {VERSION}")
        print("Initializing...\n")

        print("✓ Configuration Loaded")

        brain = Brain()
        brain.load()

        print("✓ Modules Loaded\n")
        print("PHANTOM Ready.")
        print("==========================")
