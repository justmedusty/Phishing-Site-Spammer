# Phishing-Site-Spammer
sends large amounts of fake logins to phishing websites to muddy up their database

To begin you must have the url of the website in question , then you must inspect element for both the email and password textboxes and if required the submit button
and plug those into the BotMethods file. The url will be given in main.py , the CSS tags/id/classes are given under the inputData method in the BotMethods file.

You must download chromedriver from https://chromedriver.chromium.org/downloads and it MUST match your current chrome version. Change the chromedriver path in once you have downloaded it
