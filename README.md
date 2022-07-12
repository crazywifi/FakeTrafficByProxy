# FakeTrafficByProxy
Send Fake Traffic by Free Proxies

### Fore more details: https://lazyhacker22.blogspot.com/2022/07/fake-traffic-by-proxy-use-proxy-to-send.html

## How to use this code?

## Command:
python3 FakeTrafficByProxy.py URL

## Example:
python3 FakeTrafficByProxy.py https://lazyhacker22.blogspot.com/

![Alt text](https://raw.githubusercontent.com/crazywifi/FakeTrafficByProxy/main/process.png)


Need to change the highlighted data in the script before using it according to your website server response

![Alt text](https://raw.githubusercontent.com/crazywifi/FakeTrafficByProxy/main/needtomodify.PNG)

![Alt text](https://raw.githubusercontent.com/crazywifi/FakeTrafficByProxy/main/poc.PNG)

### How to compile py file to exe?
c:\Python3\Scripts\pyinstaller.exe --add-data "C:\Python3\Lib\site-packages\pyfiglet\fonts;./pyfiglet/fonts" -i icon.ico --onefile FakeTrafficByProxy.py

