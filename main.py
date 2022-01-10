from BotMethods import startBot, inputData
from LoginRandomizer import createLogin, createPassword

count = 0
startBot("http://microsoftoutlook.in/")

while True:

    inputData(createLogin(), createPassword())
    count += 1
    print(count)
