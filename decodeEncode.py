import random

# Persistent storage for encoded message
LastMessage = ""

def generate_random_words():
    chars = "qwertyuiopasdfghjklzxcvbnm"
    return ''.join(random.choice(chars) for _ in range(3))

def encoded(separate_words):
    encoded_words = []
    for word in separate_words:
        if len(word) <= 3:
            encoded_words.append(word[::-1])
        else:
            random_front = generate_random_words()
            random_back = generate_random_words()
            swapped = word[-1] + word[1:-1] + word[0]
            encoded_words.append(random_front + swapped + random_back)
    return ' '.join(encoded_words)

def decode(separate_words):
    decoded_words = []
    for word in separate_words:
        if len(word) <= 3:
            decoded_words.append(word[::-1])
        else:
            trimmed = word[3:-3]
            if len(trimmed) >= 2:
                swapped_back = trimmed[-1] + trimmed[1:-1] + trimmed[0]
            else:
                swapped_back = trimmed
            decoded_words.append(swapped_back)
    return ' '.join(decoded_words)

def start_program():
    global LastMessage
    print("Welcome to the Encode and Decode program")
    while True:
        try:
            option = int(input("\nChoose an option:\n1. Encode Message\n2. Decode Message\n3. Exit\nEnter your option: "))
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue

        if option == 1:
            message = input("Enter the message you want to encode: ")
            words = message.split(" ")
            LastMessage = encoded(words)
            print("Encoded Message:", LastMessage)
        elif option == 2:
            if LastMessage == "":
                print("❗ No message to decode yet.")
            else:
                words = LastMessage.split(" ")
                decoded_message = decode(words)
                print("Decoded Message:", decoded_message)
        elif option == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
start_program()
