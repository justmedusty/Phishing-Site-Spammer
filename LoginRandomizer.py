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
    characters = string.ascii_letters + string.digits
    length = random.randint(6, 30)
    emailHandle = random.choices(characters, k=length)
    finalEmail = "".join(emailHandle) + random.choice(domainArray)
    return finalEmail
