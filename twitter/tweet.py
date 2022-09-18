from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time,random,os

print('running')

options = Options()  
#options.add_argument("start-maximized")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options.add_argument("--no-sandbox") 
options.add_argument("--remote-debugging-port=9222")  # this
options.add_argument("--headless") 
options.add_argument("--disable-dev-shm-using") 
driver = webdriver.Remote('http://chrome:4444/wd/hub',options=options)

driver.get('https://twitter.com/i/flow/login')
time.sleep(random.randint(10,20))
username=driver.find_element(By.XPATH,'//input')
username.clear()
username.send_keys(os.environ.get('USERNAME'))
username.send_keys(Keys.ENTER)
time.sleep(random.randint(3,6))
password=driver.find_element(By.XPATH,'//input[@name="password"]')
password.send_keys( os.environ.get('PASSWORD'))
time.sleep(random.randint(3,6))
password.send_keys(Keys.ENTER)
time.sleep(random.randint(3,15))

hashtags=['peter obi','Arsenal','obidatti']
## hashtag Trend
count =1
hashtags
while count >= 1:
    print('aaa')
    time.sleep(30)
    print('bba')
    for i in range(1,3):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(random.randint(5,10))

    tweets=driver.find_elements(By.CSS_SELECTOR,'div[data-testid="like"]')
    main_tweet=0
    main_retweet =0
    for tweet in range(len(tweets)-1):
      
        try:
            driver.execute_script('arguments[0].click();',tweets[tweet])
            main_tweet +=1
            time.sleep(random.randint(3,25))
            retweets=(driver.find_elements(By.CSS_SELECTOR,'div[data-testid="retweet"]'))[tweet]
            driver.execute_script('arguments[0].click();',retweets)
            retweet=driver.find_element(By.CSS_SELECTOR,'div[data-testid="retweetConfirm"]')
            driver.execute_script('arguments[0].click();',retweet)
            main_retweet+=1
            time.sleep(random.randint(3,25)) 
            print('completed 1')
        except Exception as e:
            print(e)    
    print(f'{main_tweet} tweet was liked  and {main_retweet} tweet was retweeted ')
        

    

    driver.get('https://twitter.com')
    time.sleep(20)
    n_tweets=0
    n_retweets=0    
    for hashtag in hashtags:

        driver.get(f'https://twitter.com/search?q={hashtag}&src=typed_query')
        time.sleep(4)
        for i in range(1,5):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(random.randint(5,10))

        tweets=driver.find_elements(By.CSS_SELECTOR,'div[data-testid="like"]')

        for tweet in range(len(tweets)-1):
            try:
                driver.execute_script('arguments[0].click();',tweets[tweet])
                n_tweets +=1
                time.sleep(random.randint(3,25))
                retweets=(driver.find_elements(By.CSS_SELECTOR,'div[data-testid="retweet"]'))[tweet]
                driver.execute_script('arguments[0].click();',retweets)
                retweet=driver.find_element(By.CSS_SELECTOR,'div[data-testid="retweetConfirm"]')
                driver.execute_script('arguments[0].click();',retweet)
                n_retweets+=1
                time.sleep(random.randint(3,25)) 
            except Exception as e:
                print(e)    
           

        

        driver.get('https://twitter.com')
        time.sleep(20)
    count +=1
    print(f'{n_tweets} tweet was liked with #{hashtag} and {n_retweets} tweet was retweeted with #{hashtag}')
    print('Total count:',count)
