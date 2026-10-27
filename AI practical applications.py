print("PRACTICAL AI APPLICATIONS")
print("-------------------------")

def chatbot():
    print("\nSimple Chatbot")
    print("Type 'bye' to exit.")

    while True:
        message = input("You: ").lower()

        if message == "bye":
            print("Bot: Goodbye!")
            break
        elif "hello" in message or "hi" in message:
            print("Bot: Hello! How can I help you?")
        elif "name" in message:
            print("Bot: I am a simple Python chatbot.")
        elif "help" in message:
            print("Bot: Tell me what you need help with.")
        else:
            print("Bot: Sorry, I don't understand.")

def calculator():
    print("\nAI Application: Smart Calculator")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid choice.")

chatbot()
calculator()