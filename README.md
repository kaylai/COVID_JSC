COVID_JSC
=========

A couple of quick scripts to plot up COVID-19 data in a handful of counties across the US.

These plots are designed to emulate some of the data being used by Johnson Space Center to determine when more employees can return to work onsite. Two plots are generated: Daily confirmed cases and Cumulative confirmed cases. In both plots, bars represent daily values and lines represent a 5-day moving average. In the Daily confirmed cases plot, a red or green shaded box covering the previous 14 days of data indicates whether the trend of daily cases is positive (red) or negative (green).

These plots autogenerate daily and can be accessed at http://covid-harris.herokuapp.com/

Data Source
-----------
All data used here are from the Johns Hopkins Whiting School of Engineering Center for Systems Science and Engineering. https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

# Heroku testing and deployment

This app was created on top of python-getting-started. The readme for the original infrastructure is below.

## Test on your local.

Create a virtual environment to test the app on your local machine.
```sh
$ conda create virtualenv -n covid

```

Start up that new env.
```sh
$ conda env export -n covid
$ source activate covid
$ pip install -r requirements.txt
```

Then run the thing...
```sh
$ python manage.py collectstatic
```
(answer yes)

```sh
$ heroku local web
```

Now access the local deployment at http://localhost:5000

If you are having issues getting this to run, your 5000 port may be busy. Kill all processes on that port with:
```sh
$ kill `lsof -i :5000`
```

## Push changes and deploy on Heroku.
```sh
$ git add .
$ git commit -m "commit message"
$ git push heroku master
$ heroku open
```

Done forget to also push to github (here; origin master) where you should definitely also be saving these files:
```sh
$ git add .
$ git commit -m "commit message"
$ git push origin master
```

## The file structure
The file /uploads/core/view.py is where your python code (the actual code being deployed, in this case DensityX.py) lives.

The file /uploads/templates/base.html is the base html file that is essentially your index.html file. All other html files extend base.

The file /uploads/core/templates/core/home.html is where the stuff on your index page is defined.

## Some files you'll need
Use python-getting-started from heroku for an example of a working setup with all required files (readme for original is below)

requirements.txt file - all dependencies and versions go here. To get version: run python, import module, type:
```sh
$ print module.__version__
```

urls.py - list of all the "pages" on the web interface

view.py - where the actual python code gets called and executed. The script to run must be wrapped as a function like:
```sh
def my_python_script(some_thing)
```

# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

## David's setup notes (macOS)

### In local Machine
```
git clone https://github.com/kaylai/DensityX-heroku.git
cd DensityX-heroku
brew install postgresql
conda create virtualenv -n venv
source activate venv
[Switch to Venv Machine]
heroku local web
```

### In Venv Machine
```
pip install -r requirements.txt
python manage.py collectstatic
yes
[Switch to local machine]
```

# Auto-updating and pushing to github
1. Set a webook in heroku so that the heroku server builds and deploys everytime this github is updated
2. Spin up a [DigitalOcean](https://www.digitalocean.com/) droplet running Ubuntu
3. Install the necessary items, including [anaconda](https://www.anaconda.com/products/individual). wget "url" to download the installer .sh file, then follow the instructions [here](https://docs.anaconda.com/anaconda/install/linux/).
4. git clone your github repo into your root folder on the DO server
5. You'll need to store your github credentials so that the DO terminal doesn't ask for a username/pass every time you try to git push. See this [stackexchange](https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git-gitextension) discussion. 
5. Create a cron job to automatically git pull, run fetch.py, git add, git commit, and git push. Also add the output of these commands to log files so that you can debug

## Setting up the cron job
Cron runs in a lightweight environment, so you need to tell it to run in bash or some shell, and you need to provide absolute paths to everything. To edit your crontab, type:

```
crontab -e
```

Then, add this to the first line of your crontab
```
01 00 * * * su -s /bin/sh root -c 'cd /root/COVID_JSC && /usr/bin/git fetch --all && /usr/bin/git reset --hard origin/master && /usr/bin/git pull origin master && /root/anaconda3/bin/python fetch.py | /usr/bin/tee /root/fetchlog.log && /usr/bin/git add * | /usr/bin/tee /root/addstar.log && /usr/bin/git commit -m "Cron autoupdate" | /usr/bin/tee /root/commitlog.log && /usr/bin/git push -u origin master >> /root/gitpushlog.log 2>&1'
```

This tells cron to run this command on the first minute of the 0th hour (midnight) every day of month, every day, every day of week. The `su -s` executes as a super user. The logs get saved into the root folder of the DO server, so you'll have to log into the DO terminal to see them.

## Authors

* **Kayla Iacovino** - [github](https://github.com/kaylai)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
