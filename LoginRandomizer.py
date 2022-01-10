
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
    domainArray = ["@homtail.com", "@gmail.com", "@icloud.com", "@outlook.com", "@yahoo.com", "@live.com",
                   "@aol.com"]
    firstName = randomFirstName()
    lastName = randomLastName()
    finalEmail = "".join(firstName) + lastName + random.choice(domainArray)
    return finalEmail


def randomFirstName():
    with open("NameFiles/first-names.txt") as f:
        firstNameContents = f.read()
        lines = firstNameContents.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]


def randomLastName():
    with open("NameFiles/middle-names.txt") as f:
        lastNameContents = f.read()
        lines = lastNameContents.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
