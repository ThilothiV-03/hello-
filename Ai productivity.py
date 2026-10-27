print("AI PRODUCTIVITY ASSISTANT")
print("-------------------------")

def draft_email(name, subject):
    email = f"""
Dear {name},

I am writing to inform you about {subject}.

Thank you for your time and consideration.

Best regards
"""
    return email

def summarize_text(text):
    sentences = text.split(".")
    return sentences[0].strip() + "." if sentences[0].strip() else ""

print("\n1. Email Drafting")
name = input("Enter recipient name: ")
subject = input("Enter email subject: ")

print(draft_email(name, subject))

print("\n2. Text Summarization")
text = input("Enter a short paragraph: ")

print("Summary:", summarize_text(text))

print("\nProductivity assistant completed!")