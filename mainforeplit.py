'''
if you use VM as replit.com use this code
'''

from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string


def emailgen(email):
    e = email.split('@')
    letters = string.ascii_letters
    numbers = string.digits
    l = ''
    for i in range(5):
        l += ''.join(random.choice(letters).lower())
        l += ''.join(random.choice(numbers))

    return (e[0] + '+' + l + '@' + e[1])


def zalacreation(email, link_newsletter):

    options = Options()
    #options.headless = False  # Use the program in this mode... Headless == True should not work
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    #driver.get('https://www.zalando.it/zalando-newsletter/')
    #driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver = webdriver.Chrome(options=options)
    #driver.set_window_size(200, 200) #You can change the size or comment this command

    t = 60

    driver.get(link_newsletter)

    element = WebDriverWait(driver,t).until(EC.element_to_be_clickable((By.ID,'uc-btn-accept-banner')))
    element.click()

    element = WebDriverWait(driver, t).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="email-input"]')))
    element.send_keys(email)

    element = WebDriverWait(driver, t).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div/div[1]/div/label')))
    element.click()

    element = WebDriverWait(driver, t).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[5]/button')))
    element.click()

def discordbot(token,PATH):
    client = commands.Bot(command_prefix='!')

    @client.event
    async def on_ready():
        print('Bot is ready')

    @client.command()
    @commands.is_owner()
    async def ping(ctx):
        await ctx.send('Bot is online')

    @client.command()
    async def helpzalacode(ctx):
      await ctx.send('Use !generate youremail@domain to receive your codes !')

    @client.command()
    async def mkcodes(ctx,arg):
        await ctx.send('**HEY...CHECK YOUR EMAIL**')

        number_gen=5  #You can change this variable to your liking
        random_emails=[]
        for em in range(number_gen):
            random_emails.append(emailgen(arg))
        print(random_emails)

        for randem in random_emails:
            zalacreation(randem,'https://www.zalando.it/zalando-newsletter/')
             #You can change your link_newsletter for your country


    client.run(token)

if __name__ == '__main__':
    token = 'discord bot token'
    PATH = 'chromedirver Path'

    discordbot(token,PATH)

