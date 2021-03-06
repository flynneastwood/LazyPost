import json
import pyautogui
import os

from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ParsePost import getTitle, getBody, getHashtags, getVideoDesc
from YoutubeUploader import main


driver = webdriver.Chrome('./chromedriver')

with open('ids.json', 'r') as json_file:     #get credentials from json
    data = json.load(json_file)

#Pour utiliser Brave.
#driver = webdriver.Chrome(executable_path ='C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe')
title = getTitle()
body = getBody()
tags = getHashtags()
videoDesc = getVideoDesc()

videoUrl = 'https://www.youtube.com/'

videoMediaList =[]
videoPath = open('./testVidUpload.mp4', 'rb')

videoMediaList.append(str(videoPath))

thumbnail = './thumbnail.jpg'

def main():

    def minds():

        driver.get("https://www.minds.com/")

        #We find the login page and the text input.
        usernameElem = driver.find_element_by_link_text('Login').click()
    
        #Credentials input.
        usernameElem = driver.find_element_by_id('username').send_keys((data['minds']['username']))
        passwordElem = driver.find_element_by_id('password').send_keys((data['minds']['password'], Keys.RETURN))
        

        driver.implicitly_wait(7) #Wait to load the page properly


        # Get text box and add post.txt
        postElem = driver.find_element_by_xpath(
            '/html/body/m-app/m-page/m-body/m-newsfeed'
            '/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster'
            '/div/div/form/m-text-input--autocomplete-container/textarea'
            )

        postElem.send_keys(title)

        postElem.send_keys(Keys.RETURN) #Jump a line in blog text

        postElem.send_keys(body)

        postElem.send_keys(Keys.RETURN) #Jump a line in blog text

        postElem.send_keys(tags)

        postElem.send_keys(Keys.RETURN)
        


        driver.implicitly_wait(5)

        #Submit button
        #driver.find_element_by_xpath('/html/body/m-app/m-page/m-body/m-newsfeed/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster/div/div/form/div/button').click()

    def steemit():

        driver.get("https://www.steemit.com/")

        
        driver.implicitly_wait(7)                                                   #We find the login page and the text input.
        usernameElem = driver.find_element_by_xpath(
            "//*[@id='content']/div/div[2]/div/div/header/nav/div[3]/span[1]/a[1]"
            ).send_keys(Keys.RETURN)

        driver.implicitly_wait(7) #Wait to load the page                             #Username input.
        usernameElem = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/div[1]/input"
            ).send_keys(data['steemit']['username'])
        
        passwordElem = driver.find_element_by_xpath(                                 #Password input.
            '/html/body/div[2]/div/div[2]/div/div/form/div[2]/input'
            ).send_keys(data['steemit']['password'], Keys.RETURN)


        # Get write blog icon and fills each fields using the HTML file.
        
        wait = WebDriverWait(driver, 20)

                                                                                         
        writePost = wait.until(EC.visibility_of_element_located((By.XPATH,             # wait for the button to be available
            "/html/body/div/div/div[2]/div/div/header/nav/div[3]/a"
            )))

        writePost.click()                                                              #click the write blog button
           
        driver.implicitly_wait(5) 

        blogTags = driver.find_element_by_xpath(                                       #Fill in the blog post. This order is the right way so far to 
            "/html/body/div/div/div[3]/div/div[2]/form/div[4]/span/span/input"         #input the post, otherwise, it all goes in the title for some reasons.
            ).send_keys(tags)
        blogTitle = wait.until(EC.visibility_of_element_located((By.XPATH, 
            "/html/body/div/div/div[3]/div/div[2]/form/div[1]/span/input"
            ))).send_keys(title)
        blogBody = wait.until(EC.visibility_of_element_located((By.XPATH, 
            "/html/body/div/div/div[3]/div/div[2]/form/div[2]/span/div/textarea"
            ))).send_keys(body)

       
        return True

    def dTube():
        
        global keyErrorElem

        wait = WebDriverWait(driver, 10)

        def dTube_upload():

            print("Logged In!")
            UploadBtnElem = wait.until(EC.visibility_of_element_located((By.XPATH,     #Get the "upload a video" button
                "/html/body/div/body/div[2]/div/nav[1]/a[3]"
                ))).click()
          
            
            
            srcElem = driver.find_element_by_xpath(                                         #Select from youtube link
                "/html/body/div[1]/body/div[5]/div/main/div/div/div[1]/div[2]/div/input"
                ).click()


            nextElem = driver.find_element_by_xpath(
                "/html/body/div[1]/body/div[5]/div/main/div/div/div[2]/button/div"          #Hit next button
                ).click()

            VideoLinkElem = driver.find_element_by_xpath(                                   #Get link to URL and paste in the youtube link
                "/html/body/div[1]/body/div[5]/div/main/div/div/div[1]/div/input"
                ).send_keys("a youtube url")

            

            pass

        def loginDtube():


            driver.get("https://d.tube/")
with open('postContent.json', 'r') as json_file:     #get credentials from json

            driver.implicitly_wait(7) #Wait to load the page properlywith open('postContent.json', 'r') as json_file:     #get credentials from json


            loginElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Find and click the login button
                "/html/body/div/body/div[1]/div[2]/div[3]/a/div"
                ))).click()
            avalonElem = wait.until(EC.visibility_of_element_located((By.XPATH,             #Select the Dtube authentification
                "/html/body/div/body/div[5]/div/main/div/div[3]"
                ))).click()
            driver.implicitly_wait(5)


            passwordElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input password
                "/html/body/div/body/div[5]/div/main/div/div/form/div/div/div[2]/div/input"
                )))
            for character in (data['dtube']['password']):       #Used to slowdown typing, preventing blocks from bots.
                passwordElem.send_keys(character)


           
            usernameElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
                "/html/body/div/body/div[5]/div/main/div/div/form/div/div/div[1]/div/input"
                ))).send_keys(data['dtube']['username'])



            submitElem = driver.find_element_by_xpath(                                      #Submit information
                "/html/body/div/body/div[5]/div/main/div/div/form/div/div/div[4]/button"
                )


            submitElem.submit()

        loginDtube()


        try:
            LoginSuccess = False
            keyErrorElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Check if login failed
                "/html/body/div[1]/body/div[6]/div/div[2]"
                )))
        except TimeoutException:
            dTube_upload()
            LoginSuccess = True


        #Loop the login process until access
        

        while LoginSuccess == False:    
            if keyErrorElem:
                print('Trying again')
                loginDtube()
                                                    
                
            else:
                     
                print("Success!")
                LoginSuccess = True
                

    def bitchute():
        def loginBitchute():
            driver.get("https://www.bitchute.com/")

            wait = WebDriverWait(driver, 10)

            driver.implicitly_wait(7) #Wait to load the page properly

            loginElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Find and click the login button
                "/html/body/nav/div[1]/div[2]/div[4]/span/a[1]"
                ))).click()

            usernameElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
                "/html/body/div[1]/div/div/div[2]/div/div[1]/form/div[2]/input"
                ))).send_keys(data['bitchute']['username'])

            passwordElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
                "/html/body/div[1]/div/div/div[2]/div/div[1]/form/div[3]/input"
                ))).send_keys(data['bitchute']['password'])

            submitElem = driver.find_element_by_xpath(                                      #Submit information
                "/html/body/div[1]/div/div/div[3]/button[1]"
                ).click()


        def uploadBitchute():

            print("Logged In!")

            wait = WebDriverWait(driver, 10)

            try:

                UploadBtnElem = wait.until(EC.visibility_of_element_located((By.XPATH,     #Get the "upload a video" button
                "/html/body/nav/div[1]/div[2]/div[4]/a"
                    ))).click()

            except TimeoutException:
                print('Not found')

            videoTitleElem = driver.find_element_by_xpath(                                       
            "/html/body/div/div/div/form/div[1]/textarea"         
            ).send_keys(title)

            videoDescElem = wait.until(EC.visibility_of_element_located((By.XPATH, 
            "/html/body/div/div/div/form/div[2]/textarea"
            ))).send_keys(videoDesc)

            uploadVideoElem = wait.until(EC.visibility_of_element_located((By.ID, 
            "video_upload"
            ))).send_keys("C:/Users/Tony Laptop/Documents/GitHub/LazyPost/testVidUpload.mp4")

            uploadThumbnailElem = wait.until(EC.visibility_of_element_located((By.ID, 
            "cover_upload"
            ))).send_keys("C:/Users/Tony Laptop/Documents/GitHub/LazyPost/thumbnail.jpg")

        loginBitchute()
        uploadBitchute()

    def lbry():
        
        def loginLbry():
            driver.get("https://lbry.tv/")

            wait = WebDriverWait(driver, 10)

            driver.implicitly_wait(7) #Wait to load the page properly

            loginElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Find and click the login button
                "/html/body/div/div/header/div/div[2]/div/a[1]/span/span"
                ))).click()

            usernameElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
                "/html/body/div/div/div[1]/main/section/div/div/section/div[2]/div/form/fieldset-section/input"
                ))).send_keys(data['lbry']['username'], Keys.RETURN)

            passwordElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
                "/html/body/div/div/div[1]/main/section/div/div/section/div[2]/form/fieldset-section/input"
                ))).send_keys(data['lbry']['password'], Keys.RETURN)

        def uploadLbry():

            wait = WebDriverWait(driver, 10)

            driver.implicitly_wait(7) #Wait to load the page properly

            uploadBar = wait.until(EC.visibility_of_element_located((By.XPATH,              #Find the top bar
                "/html/body/div/div/header/div/div[2]/button[1]"
                ))).click()
            publishElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Click login Button
                "/html/body/reach-portal/div/div/div[1]"
                ))).click()


            mediaBarElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Upload the file
                "/html/body/div/div/div[1]/main/div/section[1]/div[2]/fieldset-section/input-submit/button"
                ))).click()

            pyautogui.FAILSAFE = True

            pyautogui.PAUSE = 0.5

            #get the directory bar and release keys
            pyautogui.keyDown("altleft")
            pyautogui.keyDown("d")
            pyautogui.keyUp("altleft")
            pyautogui.keyUp("d")

            #Write path and go to directory
            pyautogui.write('C:/Users/Tony Laptop/Documents/GitHub/LazyPost/')
            pyautogui.press('enter')

            pyautogui.write('testVidUpload.mp4')
            pyautogui.press('enter')
            #pyautogui.prompt('This lets the user type in a string and press OK.')

        loginLbry()
        uploadLbry()

    def youtube():
        pass


    def gui():

        window = Tk()

        #Body
        window.title("LazyPost Minds.com")
        window.geometry('400x500')


        lbl = Label(window, text="Send to Minds.com")
        lbl = Label(window, text="Platform", height=2, font=("Helvetica", 16))

        lbl.grid(column=0, row=0)
        lbl.grid(column=2, row=0)

        def clickedMinds():

            minds()

        def clickedSteemit():

            steemit()

        def clickedBitchute():

            bitchute()

        def clickedLBRY():

            lbry()

        def clickedDtube():

            dTube()


        btn01 = Button(window, text="Minds",  width=10, height=3, command=clickedMinds)
        btn02 = Button(window, text="Steemit", width=10, height=3, command=clickedSteemit)
        btn03 = Button(window, text="Bitchute", width=10, height=3, command=clickedBitchute)
        btn04 = Button(window, text="LBRY", width=10, height=3, command=clickedLBRY)
        btn05 = Button(window, text="D.Tube", width=10, height=3, command=clickedDtube)


        btn01.grid(column=0, row=1)
        btn02.grid(column=1, row=1)
        btn03.grid(column=2, row=1)
        btn04.grid(column=3, row=1)
        btn05.grid(column=4, row=1)

        window.mainloop()
    
    lbry()
    #driver.close()
if __name__== "__main__":
  main()

