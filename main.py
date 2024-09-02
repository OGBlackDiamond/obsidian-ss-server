
import asyncio
import websockets.server
from websockets.server import ServerConnection

from util.config_util import ConfigUtil

class Main:

    HOST: str
    PORT: int

    def __init__(self):
        config = ConfigUtil().get_config()

        self.HOST = config.get("host", None)
        self.PORT = config.get("port", None)

        if (self.HOST == None or self.PORT == None) :
            print("Invalid config values!")
            quit()
        

    async def handle_connect(self, connection: ServerConnection):
        pass


    def main(self):
        start_server = websockets.server.serve(self.handle_connect, HOST, PORT, ssl=None, compression=None)  # type: ignore
        print("STARTING SERVER")

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

