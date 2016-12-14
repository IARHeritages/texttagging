# Text-tagging
Crowdsourcing application to tag text for IARH

First you will need to install all the dependencies with the following commands:

```bash

virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

This process will create a virtual environment for hosting all the PYBOSSA required libraries. This will be in a folder named **env** and each time you need to use them, you will have to activate it with the second command (source env/bin/activate).

# Creating the project

In order to create the project in a PYBOSSA server, you have to run the following command:

```
pbs --credentials micropasts create_project
```

**WARNING**: Be sure to have your virtualenv active. Use the source command, when you need it.


**NOTE**: In order to use your credentials, create a file in your home folder named .pybossa.cfg and add there a section like this:

```
[micropasts]
server: http://crowdsourced.micropasts.org
apikey: yourkey

```

## Updating the project

The previous section created the project, but none of the sections like the template, tutorial, long description or result pages have been populated. To do it, just run the following command:

```
pbs --credentials micropasts update_project
```

While this will work every time you run it, you can save a lot of time by telling pbs to watch for changes in any of those files, so it automatically updates the project for you when you save new changes to any of these files:

*  template.html
*  tutorial.html
*  results.html
*  long_description.md

```
pbs --credentials micropasts update_project --watch
```

## Adding tasks to the project from a JSON file

First of all, you will have to run the command **getData.py** as it will scrape a website and get all the articles regarding a query.

Before doing anything, you need to create a settings.py file. Copy the template, settings.py.tmpl, and create the previous file updating
its content. Then, you can run the script like this:

```
scrapy runspider getData.py -o yourquery.json

```

**NOTE**: We are using the Python library [scrapy](https://doc.scrapy.org/). Read the
[docs](https://doc.scrapy.org/) for more information.

The **-o yourquery.json** flag allows you to save your query into different files.

You can see all the available options by using the flag **--help**.

This will create a file with several articles. Be careful, as some searches could be very big.

```
pbs --credentials micropasts add_tasks --tasks-file=yourquery.json --tasks-type=json

```

**NOTE**: You can configure the priority and redundancy also, using the command line, check the help.
