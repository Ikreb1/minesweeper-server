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