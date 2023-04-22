# minesweeper-server

# Setup docker
docker build -t minesweeper-sqlite-server .

# Run docker
docker run -d -p 5000:5000 --name minesweeper-sqlite-server minesweeper-sqlite-server

# Install
poetry install

# Run docker
Bat script: ./run-minesweeper-server.bat

# Run tests
poetry run python test_db.py

# maybe use heroku to deploy for free
 gpt-3 guide
Deploying the server on your local PC is a good option for development and testing purposes, but if you want to make the server accessible from the internet, you will need to deploy it on a hosting provider.

There are many cloud hosting providers that offer a variety of services for hosting web applications, such as AWS, Azure, Google Cloud, and DigitalOcean.

If you are looking for a simple and cost-effective solution, you could consider using a Platform as a Service (PaaS) provider like Heroku, which offers a free plan that includes a small database and limited resources.

To deploy your Flask application on Heroku, you can follow these general steps:

Create a Heroku account and install the Heroku CLI on your local PC.
Create a new Heroku app and connect it to your Git repository where the Flask application code is stored.
Configure your Flask application to run on Heroku by creating a Procfile that specifies the commands to run the server.
Create a new PostgreSQL database on Heroku and add the database URL as an environment variable in your Flask application.
Deploy your Flask application to Heroku by pushing your Git repository to the Heroku remote.
For more detailed instructions on how to deploy a Flask application on Heroku, you can refer to the official Heroku documentation.
