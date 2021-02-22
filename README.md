# Find your followers all over the globe!
## A simple web app that works with TwitterAPI and Flask framework.
This project is an example of usage of TwitterAPI and Flask. As a result of running it, the user will get a web-page with a generated HTML-map.
## Usage
This app doesn't require installation, unless you want to clone a project from GitHub for some purposes. To run the app, just click [here](http://vsaliieva.pythonanywhere.com/) and follow the prompts on the screen. Once you click "Submit", map generation will start, and you'll be able to see it, when it's ready.

## main.py
This module contains functions that work with TwitterAPI and process the response. Once the user enters a Twitter nickname, their bearer token, and a number of followers to be checked, the request is sent using TwitterAPI, and the response contains a list of followers. This object is then processed to define locations of those followers, if available, and their coordinates. Finally, an HTML-map is generated and saved to "templates/" folder.

## webapp.py
This module is a web app itself. It accounts for posting a request to a server, getting all the necessary information from user, and returning a web page (a template), which contains a map.

## License
[MIT](https://choosealicense.com/licenses/mit/)

_NOTE: this app requires entering personal information (a bearer token). The app will not store it or use it in any other way, except forming a request with it. Remember to keep this token safe and avoid publishing it.
