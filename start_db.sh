#!/bin/bash
# This script starts the database server for the SPPS project.

podman run --name neon_db -p 5432:5432 -e POSTGRES_PASSWORD=root -v /opt/data/neon_db -e POSTGRES_USER=root -e DRIVER=serverless --replace f49abb9855df&
