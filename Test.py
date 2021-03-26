import pyppeteer
import time

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://www.rbc.ru/')
    n = int(input("Введите количество скриншотов "))
    t = int(input("Введите задержку "))
    for i in range(n):
        s = "rbk" + str(i) + ".jpg"
        await page.screenshot({'path': s})
        time.sleep(t)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
