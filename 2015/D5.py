naughty = ["ab", "cd", "pq", "xy"]
nice = 0

with open("2015\D5.txt", "r") as file:
    for stringa in file:
        stringa = stringa.strip("\n")

        """vocali = stringa[-1] in "aeiou"
        contieneCoppia = False
        contieneNaughty = True

        for i in range(len(stringa)-1):
            if stringa[i:i+2] in naughty:
                contieneNaughty = False
                break

            if stringa[i:i+2] == stringa[i:i+2][::-1]:
                contieneCoppia = True

            if stringa[i] in "aeiou":
                vocali += 1
            
        if vocali>=3 and contieneCoppia and contieneNaughty:
            nice += 1"""
        
        has_pair = False
        for i in range(len(stringa) - 1):
            pair = stringa[i:i+2]
            if pair in stringa[i+2:]:
                has_pair = True
                break

        # Check for a letter repeating with one letter in between
        has_repeat = any(stringa[i] == stringa[i+2] for i in range(len(stringa) - 2))

        if has_pair and has_repeat:
            nice += 1

print(nice)