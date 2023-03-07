# Python Automation Framework 

The intent of this Repository is just to start creating a Brand New Python Automation Framework. 

Because of that, the **PAF 0.1 Version** was launched. Despite the fact there's quite a long Path to walk thru, there's the first quick off though.

I really hope you could enjoy it.
Cheers!

## Set Up
### Python Version
By the time this Framework was created, I started it by using the **Python 3.7** Version. However, you might use any 3.x version you'd prefer. I do recommend not to use 2.x versions though. You can also use the Ven capability.

#### Installing Python
As I mentioned before, you must get a 3.x Python Version installed (python --version to check whether a Python V was installed or not)

#### Installing Selenium
As I mentioned before, you must get a 3.x Python Version installed. All the examples are taking into consideration that you already have PIP installed (```pip --version``` to check it)

```
pip install selenium
```
#### Installing the ChromeDriver
Now we'd need to know if our chrome driver is installed
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

#### Installing Pytest Framework
*pytest* is a framework that makes building simple and scalable tests easy.
In order tu install it, run the following command in your command line:

```
pip install -U pytest
```
Check that you installed the correct version:

```
pytest --version
```
**Important: *pytest* deals with the fact of correctly using relative/absolute Paths. For further details, please refer
to the following >> https://docs.pytest.org/en/3.6.0/writing_plugins.html#conftest-py-plugins

#### Installing Allure Framework
*allure* is a framework to generate reports. Report throws a .xml file which should be 
invoked in order to generate the .html report.
In order to installing it: 
```
brew install allure
```
The **PAF 0.1 Version** is running Pytest. So that, you could install it by using the following command:
```
pip install allure-pytest
```

**First Step**

First of all, the .xml file should be created. As follows:

```
pytest alluredir "Your_Path"
```

**Second Step**

Once .xml files are generated, you should go to **Your_Path** and generate the .html file with all their dependencies. As follows:

```
alluredir generate "Path_of_The_XML_files"
```
**Recommendation:** Generate your reports in the path where the .xml files are
For further information, please refer to >> https://docs.qameta.io/allure/

## Page Object Model (POM)
This framework was built by using the PO concept which is going to be useful for interacting and maintaining the coding in a better way. For further reference, please do take a look at the following url >> https://selenium-python.readthedocs.io/page-objects.html

## Explicit Waits
    This framework was also build by using the Explicit Webdriver Concept which could be investigated further by following this url > https://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
Here you have an example provided for the Python coding

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

ff = webdriver.Firefox()
ff.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
finally:
    ff.quit()
```

## Screenshot

The intent is to get a Screenshot of every Test Case. For that, we would need to get a Module in which our .png files are going to be downloaded.

```
driver.get_screenshot_as_file("Your_path/TC01.png")
```



