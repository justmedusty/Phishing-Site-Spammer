import random
import string


# creates a random password containing numbers , letters , and punctuation (between 6 and 128 chars)
def createPassword():
    length = random.randint(6, 128)
    letters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation
    all = letters + numbers + punctuation

    temp = random.choices(all, k=length)
    finalPass = "".join(temp)
    return finalPass


# creates a random email from a short list of popular domains
def createLogin():
    domainArray = ["@hotmail.com", "@gmail.com", "@icloud.com", "@outlook.com", "@yahoo.com", "@live.com",
                   "@aol.com"]
    firstName = randomName("first-names.txt")
    lastName = randomName("middle-names.txt")
    randomNumber = random.randint(0, 400)
    finalEmail = "".join(firstName) + lastName + str(randomNumber) + random.choice(domainArray)
    print(finalEmail)
    return finalEmail


def randomName(filename):
    with open("NameFiles/" + filename) as f:
        nameContents = f.read()
        lines = nameContents.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
