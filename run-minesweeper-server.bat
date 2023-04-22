@echo off

REM Stop and remove any existing container
docker rm -f minesweeper-sqlite-server

REM Build the Docker image
docker build -t minesweeper-sqlite-server .

REM Run the Docker container
docker run -d -p 5000:5000 --name minesweeper-sqlite-server minesweeper-sqlite-server
