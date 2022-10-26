# ------------------------------------------ Shiva Saurabh ----------------------------------- #
def caeser(text, shift, direction):
    while shift > 46:
        shift = shift % 26
    final_text = ""
    if direction == "decode":
        shift *= -1
    for letters in text:
        if letters in alphabets:
            position = alphabets.index(letters)
            new_position = position + shift
            final_text += alphabets[new_position]
        else:
            final_text += letters
    print(f"The {direction} text is: {final_text}\n")


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
should_run = True
while should_run:
    direction = input("""Type "Encode" for Encrypt and "Decode" to Decrypt: """).lower()
    user_input = input("enter your text: ")
    user_shift = int(input("shift amount: "))
    caeser(user_input, user_shift, direction)
    result = input("""type "yes" to go again or "no" to quit: """).lower()
    if result == "no":
        should_run = False
        print("goodbye!!")
