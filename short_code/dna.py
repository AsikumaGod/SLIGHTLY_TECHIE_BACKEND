sequence = 'AATTGCCGT'
compliment = ''
for char in sequence:
    if char == "A":
        compliment += "T"
    elif char == "T":
        compliment += "A"
    elif char == "C":
        compliment += "G"
    elif char == "G":
        compliment += "C"
print(f"The complimentary Strand of {sequence} is {compliment}")