from ai.manager import AIManager


def main():
    print("========================")
    print("PHANTOM v1\n")

    ai = AIManager()

    print(f"Provider: {ai.provider.__class__.__name__}\n")

    try:
        response = ai.generate("Say hello to Yug.")
        print(response)
    except Exception as e:
        print(f"Error: {e}")

    print("\n========================")


if __name__ == "__main__":
    main()
