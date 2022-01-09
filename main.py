from BotMethods import startBot, inputData
from LoginRandomizer import createLogin, createPassword

startBot("http://microsoftoutlook.in/")

while True:
    inputData(createLogin(), createPassword())
