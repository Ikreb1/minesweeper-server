# minesweeper-server
probably need to add port 5000 to whitelist on windows firewall to be able to test it

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

# deployment
git push heroku develop
* Note: shit dies when heroku dies RIP use postgres if we want this to survive