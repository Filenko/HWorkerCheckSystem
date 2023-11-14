import asyncio
from .server import serve
from .loader import Loader
from .container_manager import ContainerManager

if __name__ == "__main__":
    asyncio.run(serve())
    # containerManager = ContainerManager()
    # containerManager.RunContainers(5)
    # container = containerManager.RunContainer()
    # print(container)
    print(55)