def caesar_cipher(text: str, shift: int, encrypt=True) -> str:
    """Encrypts or decrypts a text using the Caesar cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The shift value (0-25).
        encrypt (bool, optional): Whether to encrypt or decrypt. Defaults to True.

    Returns:
        str: The encrypted or decrypted text.
    """

    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift * (1 if encrypt else -1)) % 26 + shift_base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    """Main function for the Caesar cipher program."""

    # Banner art
    banner = """
    ╔══════════════════════════════════════════╗
    ║            Caesar Cipher Tool            ║
    ╚══════════════════════════════════════════╝
    """

    print(banner)

    try:
        # Get user input
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (0-25): "))

        # Validate shift value
        if shift < 0 or shift > 25:
            raise ValueError("Shift must be between 0 and 25 inclusive.")

        # Encrypt or decrypt based on user choice
        choice = input("Do you want to encrypt (e) or decrypt (d)? ").lower()
        if choice == 'e':
            encrypted_text = caesar_cipher(text, shift)
            print(f"Encrypted: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = caesar_cipher(text, shift, encrypt=False)
            print(f"Decrypted: {decrypted_text}")
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()