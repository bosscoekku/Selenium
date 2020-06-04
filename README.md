## วิธีติดตั้ง

ขอเกริ่นแปป ก่อนหน้านี้เคยใช้ beautiful soup ในการดึงข้อมูล ปัญหาคือเวลาไปเจอเว็บไซต์ที่เป็น NodeJS หรือเว็บไซต์ทั่วไปแต่ตรงที่เราต้องการมันเป็น javascript แล้วมันดึงยาก หรือดึงไม่ได้เลย เพราะมันวิ่งเข้าไปไม่ถึง T_T อยู่ดีๆก็เลยไปเจอเครื่องมือใหม่ ชื่อว่า Selenium ที่มีพลังดูดมหาศาล ดูดได้ทุกอย่างที่ตาเห็นบนเว็บไซต์ และมันกรอกข้อมูลให้เราด้วย เขียนให้คลิกได้ด้วย และที่สำคัญมันใช้ง่าย อิหลี :)

ปล.อิหลี อิสมีน จริงๆ


**selenium** เป็น Tool ชนิดหนึ่งใช้ในการเขียนทดสอบเว็บไซต์ เพราะเราสามารถสั่งให้คลิกหรือกรอกข้อมูลเองได้ 
หรือใช้ดึงข้อมูลบนเว็บไซต์ได้ เพราะมันสามารถดึงผ่าน XPath แบบง่ายมากกกกกกกกกกกกกกก และยังรองรับอีกหลายภาษา
สำหรับบทความนี้ เราจะมาสอนวิธีติดตั้ง และใช้งานเบื้องต้น



1. ติดตั้ง selenium
  ```shell
     pip install selenium
```
2. ติดตั้ง driver (เราสามารถเลือกได้ตามที่ถนัด แต่บทความนี้จะใช้ Chrome :D )
Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

3. เมื่อแตกไฟล์ driver เสร็จแล้วจะได้ตามรูป

[![](https://i.imgur.com/jXEhjHO.png)](https://i.imgur.com/jXEhjHO.png)

4. สร้างไฟล์ python ชื่อ app.py
  ```shell
     touch app.py
```
code app.py
```python
from selenium import webdriver # Import package
driver = webdriver.Chrome('chromedriver')  # Call Driver
driver.get("https://www.google.com/") # Get url: www.gooogle.com
print (driver.title) # Print title is : Google
```
output app.py
[![app.py](https://i.imgur.com/eZR7GuP.png "app.py")](https://i.imgur.com/eZR7GuP.png "app.py")
5. ต่อไปเราจะให้ selenium ช่วยกรอกข้อมูลในช่องค้นหาให้

	**หลักการง่ายๆคือ**
		 หาตำแหน่งที่ต้องการจะคีย์ข้อมูลลงไป
		 ใส่ข้อความเข้าไป
[![](https://i.imgur.com/EBRahBs.png)](https://i.imgur.com/EBRahBs.png)
```python
from selenium import webdriver # Import package
driver = webdriver.Chrome('chromedriver')  # Call Driver
driver.get("https://www.google.com/") # Get url: www.gooogle.com
print (driver.title) # Print title is : Google

 search = driver.find_element_by_name('q') # Seach element name "q"
 search.clear()                                                # Clear
 search.send_keys("selenium")                      # Insert string with send_keys()
```
[![](https://i.imgur.com/gpDWzZL.gif)](https://i.imgur.com/gpDWzZL.gif)


ถ้าต้องการให้คลิกปุ่มค้นหาด้วย เพิ่มโค้ดอีกนิดหน่อย

```python
from selenium import webdriver # Import package
driver = webdriver.Chrome('chromedriver')  # Call Driver
driver.get("https://www.google.com/") # Get url: www.gooogle.com
print (driver.title) # Print title is : Google

 search = driver.find_element_by_name('q') # Seach element name "q"
 search.clear()                                                # Clear
 search.send_keys("selenium")                      # Insert string with send_keys()
 search.send_keys(Keys.RETURN)                  # Keys.RETURN is Special Keys
```
[![](https://i.imgur.com/EGZjMSH.gif)](https://i.imgur.com/EGZjMSH.gif)





