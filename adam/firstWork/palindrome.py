# Madam Im Adam
# 1234567654321
# print(restrng)

exitChoice = "Nothing"
while exitChoice != "EXIT":

    strng = input("Enter a Palindrome: ")

    sstrng = ''.join(strng.split())

    restrng = sstrng[::-1]

    if sstrng.lower() == restrng.lower():
        print("Correct that is a palindrome")
    else: 
        print("That is not a palindrome")

    exitChoice = input("Press return to play again, or type EXIT to leave: ")