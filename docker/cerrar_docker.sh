#!/bin/bash
number="${1:-}"
CONTAINER_NAME="workshop$number"

# Se intenta detener y borrar el contenedor. 
# > /dev/null 2>&1 oculta cualquier mensaje (tanto de éxito como de error).
# || true asegura que el script no se detenga aunque falle el comando.

docker kill "$CONTAINER_NAME" > /dev/null 2>&1 || true
docker rm "$CONTAINER_NAME" > /dev/null 2>&1 || true
