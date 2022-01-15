from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

invites_file = 'invites.xlsx'
output_file = 'output.xlsx'

invites = []
df = pd.read_excel(invites_file)
invites.append(df.columns.values[0])
invites.extend(df.iloc[:, 0].tolist())

driver = webdriver.Chrome('./chromedriver')

raw_data = []

for inv in range(len(invites)):
  metadata = []
  driver.get(invites[inv])
  if driver.current_url[:26] == 'https://discord.com/invite':
    try:
      count = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'span')))
      metadata.append(invites[inv])
      for num in count:
        val = num.get_attribute("innerText").split(" ")
        metadata.append(val[0])
      raw_data.append(metadata)
    except:
      print(invites[inv], ": Invalid invite link")
      raw_data.append(
          [invites[inv], 'INVALID INVITE LINK', 'INVALID INVITE LINK'])
  else:
      print(invites[inv], ": Not a server invite link")
  time.sleep(3)

df1 = pd.DataFrame(raw_data, columns=['Invite Link', 'Online', 'Offline'])
df1.to_excel(output_file)
