# This is a sample Python script.
import docker
import time
from containers.utils import stop_container
from containers.utils import get_selenium
from seleniumserver.selenium import get_driver
import atexit
# Variables



container = get_selenium()

atexit.register(stop_container, current_container=container)

# Set up Selenium
time.sleep(2)
driver = get_driver()






