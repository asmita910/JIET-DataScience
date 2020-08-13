def play_music(mood):
    list = ['sad','happy','angry','surprised','neutral','disgusted','fearful']
    import random
    d = {'happy':['happy+music+indian','party+song','dance+music','rock+music','pop+music','pop+dance']
         'sad':['top+heart+broken+hindi+sad+songs','fix+you','dooriyan','sad+heart+touching+song','hindi sad song']
         'angry':['angry+songs','dushman+na+kare+dost+ne+woh+kam+kiya+hai','jab+bhi+jee+chahe+nai+duniya+basa','before+he+cheats','the+kill','the+way+i+am','gives+you+hell','angry+again']
         'disgusted':['dushman+na+kare+dost+ne+woh+kam+kiya+hai','jab+bhi+jee+chahe+nai+duniya+basa','before+he+cheats','the+kill','the+way+i+am','gives+you+hell']
         'neutral':['pop+songs','indian love songs','hindi songs','make+you+feel+my+love','i+will','love+me+like+you+do','taylor+swift+songs','coldplay+songs']
         'fearful'['the+breakup+song','fear+is+a+liar','no+longer+slaves',+'fear+is+the+sky','scared+of+lonely']
         }
    
    query = d['mood'][random.randint(0, len(d['mood'])-1)]
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    
    driver = webdriver.Chrome()
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located

    # Navigate to url with video being appended to search_query
    driver.get('https://www.youtube.com/results?search_query='+query)
    
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
