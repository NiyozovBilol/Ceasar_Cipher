from ceasar_art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def my_function():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
  print(direction)
  if direction != "encode" and direction != "decode":
    print("Incorrect input")
    return
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))
  shift %= 26

  def ceasar(text, shift, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift *= -1
    for letter in text:
      if letter not in alphabet:
        end_text += letter
        continue
      ind = alphabet.index(letter) + shift
      end_text += alphabet[ind]
    print(f"The {direction}ed text is {end_text}")
    answer = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if answer == "yes": my_function()
  ceasar(text, shift, direction)

print(logo)
my_function()



