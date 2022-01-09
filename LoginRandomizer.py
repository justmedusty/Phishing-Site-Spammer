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
    length = random.randint(6, 25)
    letters = string.ascii_letters
    numbers = string.digits
    all = letters + numbers
    emailHandle = random.choices(all, k=length)
    finalEmail = "".join(emailHandle) + random.choice(domainArray)
    return finalEmail

