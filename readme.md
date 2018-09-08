# Perlite.io 

### You'll need
- git: https://git-scm.com/downloads
- docker: https://www.docker.com/get-started
## Installation
- Clone this repo `git clone https://github.com/awarebayes/perliteio`
- Build docker environment using `docker-compose build`, it will take a while
- Run built container: `docker-compose up -d`
- Get a list of currently running detached containers: `docker ps`
- Get a console instance of the container `docker exec -i -t perliteio_web_1 /bin/bash`. Note: if it doesn't work, change `perliteio_web_1` to the listed above
- `cd src/backend && python manage.py migrate && celery -A perliteio worker --loglevel=info`
- Get another console instance `docker exec -i -t perliteio_web_1 /bin/bash`
- Deploy the server: `python manage.py runserver 0.0.0.0:8000`
- Open `http://localhost:8000/` and have fun with winning the lottery
- If you want to delete all tickets: `http://localhost:8000/delete/`
- Now you can change the code. Docker-compose file system is shared with yours and all changes will be applied instantly
## Tips

- No need to build you container over and over. Changing `Dockerfile` or `docker-compose.yml` doesn't require that
- Changing the port in code (or cmd) is not enough. Also check `port` in docker-compose
- Docker console is a **shithole**. Need to think of something else.

## Some copyright shit
Copyright (c) 2018 **dotapetro**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
### That seems to be all. For a while... For now...
