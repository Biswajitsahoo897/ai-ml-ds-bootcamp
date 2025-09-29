def madlibs():
    print("Welcome to the Madlibs game!")
    print("Fill in the blanks with appropriate words to create a fun story.\n")

    A_1 = input("Enter an adjective: ")
    A_2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun_plural = input("Enter a plural noun: ")
    profession = input("Enter a profession: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")


    story = (f"\nOnce upon a time, there was a {A_1} {noun1} who lived in a {A_2} {place}. "
                f"This {noun1} loved to {verb} every day. One day, a group of {noun_plural} approached the {noun1} "
                f"and asked if it wanted to become a {profession}. The {noun1} thought for a moment and decided to "
                f"pursue its dreams of becoming the best {profession} in the whole {place}. "
                f"It worked hard, practiced daily, and soon everyone knew about the {noun2} who turned into a successful {profession}.\n")

    print(story)
madlibs()
