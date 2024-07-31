###############################################################################################
# This script automates the process of building, pushing, and running a Docker image
# for the local execution of the oc_lettings_site application.
###############################################################################################

import os
import logging
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
DOCKER_USERNAME = os.getenv("DOCKER_USERNAME")
DOCKER_PASSWORD = os.getenv("DOCKER_PASSWORD")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
DEBUG = os.getenv("DEBUG", "False")
IMAGE_NAME = "oc_lettings_site"
COMMIT_HASH = os.popen("git rev-parse --short HEAD").read().strip()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Function to execute a shell command and capture the output
def run_command(command):
    logger.info(f"Running: {command}")
    result = os.system(f"{command} > command_output.log 2>&1")
    if result != 0:
        with open("command_output.log", "r") as file:
            error_output = file.read()
        logger.error(f"Command failed with exit code {result}")
        logger.error(f"Error output: {error_output.strip()}")
        raise Exception(
            f"Command failed with exit code {result}, error output: {error_output.strip()}"
        )
    return


# Build Docker image
try:
    logger.info("Building Docker image...")
    run_command(
        f"docker build --build-arg AWS_STORAGE_BUCKET_NAME={AWS_STORAGE_BUCKET_NAME} "
        f"--build-arg AWS_ACCESS_KEY_ID={AWS_ACCESS_KEY_ID} "
        f"--build-arg AWS_SECRET_ACCESS_KEY={AWS_SECRET_ACCESS_KEY} "
        f"--build-arg DEBUG={DEBUG} "
        f"-t {DOCKER_USERNAME}/{IMAGE_NAME}:{COMMIT_HASH} ."
    )
except Exception:
    logger.exception("An error occurred while building the Docker image.")
    raise

# Login to Docker Hub
try:
    logger.info("Logging in to Docker Hub...")
    login_command = f"docker login -u {DOCKER_USERNAME} -p {DOCKER_PASSWORD}"
    run_command(login_command)
except Exception:
    logger.exception("An error occurred while logging in to Docker Hub.")
    raise

# Push Docker image to Docker Hub
try:
    logger.info("Pushing Docker image to Docker Hub...")
    run_command(f"docker push {DOCKER_USERNAME}/{IMAGE_NAME}:{COMMIT_HASH}")
except Exception:
    logger.exception("An error occurred while pushing the Docker image to Docker Hub.")
    raise

# Pull Docker image from Docker Hub
try:
    logger.info("Pulling Docker image from Docker Hub...")
    run_command(f"docker pull {DOCKER_USERNAME}/{IMAGE_NAME}:{COMMIT_HASH}")
except Exception:
    logger.exception("An error occurred while pulling the Docker image from Docker Hub.")
    raise

# Run Docker image locally
try:
    logger.info("Running Docker image locally...")
    # Utiliser le chemin absolu pour le répertoire des fichiers statiques
    static_files_path = os.path.abspath("staticfiles")
    run_command(f"docker run -d -p 8000:80 {DOCKER_USERNAME}/{IMAGE_NAME}:{COMMIT_HASH}")
    logger.info("Docker operations completed successfully.")
except Exception as e:
    error_message = str(e)
    if "port is already allocated" in error_message:
        logger.error("Port 8000 is already in use. Please free the port and try again.")
    else:
        logger.exception("An error occurred while running the Docker image locally.")
    raise
