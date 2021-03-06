Contributing
===============

All contributors must abide by the [Code of America Code of Conduct](https://brigade.codeforamerica.org/about/code-of-conduct).

Overview
-----------------
`public-comment` is written in Python using the Django web framework. Postgres is used as a database. The frontend is does not use a single page application JavaScript framework.

There some ancillary services, but knowledge of those is may not be needed to contribute (depending on the part of the code you're working in).

This app tries to keep things simple and use as few frameworks and technologies as possible.

Getting up and running
-----------------
In order to facilitate cross-platform development, Docker is used to build and run the application and database. This means that you don't have to worry about installing Python, app dependencies, or a database on your local machine. All you need to have is Docker.

### What is Docker?
> Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.
 
Source: [https://opensource.com/resources/what-docker](https://opensource.com/resources/what-docker)

### Installing Docker
Download the [Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) or [Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows) installer and follow the installation insturctions.

Note that for Windows, Docker requires 64bit Windows 10 Pro, Enterprise, or Education, and Docker also requires that virtualization be enabled. Check out the [what to know before you install](https://docs.docker.com/docker-for-windows/install/#what-to-know-before-you-install) document for more info. It is completely possible to run votebot without Docker, and we can work on documentation and scripts to make that process easier if we have contributors who can't run Docker. Docker is just handy because it makes it so developers don't have to install or manage installations, and because it mimicks the production environment.

### Running the App
Open a terminal (Terminal on Mac, Git Command Prompt on Windows), navigate to the votebot directory, and run this command: `make begin`.

This command will start the application in debug mode along with a Postgres database instance. Each of these runs in its own container, which you'll see start. `make begin` will also set up the database by running [migrations](https://docs.djangoproject.com/en/2.1/topics/migrations/) and installing [fixtures](https://docs.djangoproject.com/en/2.1/howto/initial-data/#providing-data-with-fixtures).

You can view the site by going to [http://localhost/](http://localhost/) in your browser.

You can log into the admin site by going to [http://localhost/admin/](http://localhost/admin/) and logging in with the username `admin` and the password `pass`.

### Stoping the App
To stop the app, run `make stop`.

### Viewing Logs
To view logs, run `make tail`.
If you want to start the app and automatically show logs, you can combine the `begin` and `tail` commands: `make begin tail`.

Advanced Topics
-----------------
### Running a subset of tests
You can use test labels as described in the [Django testing documentation](https://docs.djangoproject.com/en/2.2/topics/testing/overview/#running-tests) to run a subset of tests.

For example, to run a single test:
`make test labels=noauth.tests.test_views.CodeViewTests.test_validate_and_get_redirect_uri_returns_next_page_from_auth_code`

Or to run all tests in a class:
`make test labels=noauth.tests.test_views.CodeViewTests`

### Debugging via `pdb`
`pdb` is the Python debugger, and it provides a useful way to interact with a running program.

If you need to debug votebot Python code, add the following `breakpoint()` at the point where you would like your breakpoint. The app will stop execution when it reaches this line.

To interact with `pdb`, open a new terminal and run `make attach`.