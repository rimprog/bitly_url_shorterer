# Bitly url shorterer

This script use bitly api and short your link or give total clicks statistics by your short link. Just give positional argument "link" in your command line.

More info: python3 main.py -h

Comand line EXAMPLE 1:
```
In:
python3 main.py https://examplesite.com/
Out:
http://bit.ly/2XXX59g
```

Comand line EXAMPLE 2:
In:
python3 main.py http://bit.ly/2XXX59g
Out:
По вашей ссылке прошли 2 раз(а)

### How to install

You need create bitly token. Choose GENERIC ACCESS TOKEN. You can create it here: https://bitly.com/a/oauth_apps
After create TOKEN, create .env file in root project folder and place TOKEN in BITLY_TOKEN variable.

Example .env:
BITLY_TOKEN = YOUR_BITLY_TOKEN

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
