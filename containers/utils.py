import atexit
import docker
from docker.errors import APIError


@atexit.register
def goodbye():
    print("The program has closed")


def stop_container(current_container=None):
    print("Closing pyselenium from atexit")
    current_container.stop()


def get_selenium():
    # Create Container
    client = docker.from_env()

    try:
        container = client.containers.run(image='selenium/standalone-chrome:3.141.59', ports={'4444/tcp': 4445},
                                          name='pyselenium', detach=True)
    except APIError:
        container = client.containers.get('pyselenium')
        container.start()

    return container
