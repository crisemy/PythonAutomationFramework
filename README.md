# Python Automation Framework (PAF)

The intent of this Repository is just to Learn and start creating a Brand New Python Automation Framework with Python. A cool one actually. 
That's it! 

## Set Up
### Python Version
By the time this Framework was created, I started it by using the **Python 3.7** Version. However, you might user any 3.x version you'd prefer. I do recomment not to use 2.x versions though.

#### Installing Python
As I mentioned before, you must get a 3.x Python Version installed (python --version to check whether a Python V was installed or not)

#### Installing Selenium
As I mentioned before, you must get a 3.x Python Version installed (Try ```python --version``` to check whether a Python V was installed or not). All the examples are taking into consideration you already have PIP installed (```pip --version``` to check it)

```
pip install selenium
```
#### Installing the ChromeDriver
Now we'd need to know if our chrome driver is installed or not
```python``` (The python prompt will be opened up)
```
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
```
**Note**: It will throw an exception if the ChromeDriver is not installed in your Path

Go to chromedriver (Inet) so you could download it >> https://chromedriver.storage.googleapis.com/index.html?path=2.45/

* Download it
* Copy it and run it
* Add your chromedriver into your $PATH >> ```:/usr/local/bin/chromedriver```

## Page Object Model (POM)
This framework was built by using the PO concept which is gonna be useful for interacting an mantaining the coding in a better way. For further reference, please do take a look at the following url > https://selenium-python.readthedocs.io/page-objects.html





