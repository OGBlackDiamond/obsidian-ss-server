
import asyncio
import websockets.server
from websockets.sync.server import ServerConnection

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
        print("Connection Established")
        test = await connection.recv()
        print(test)
        await connection.send("test")
        await connection.close()


    def main(self):
        start_server = websockets.server.serve(self.handle_connect, self.HOST, self.PORT, ssl=None, compression=None)  # type: ignore
        print("STARTING SERVER")

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

main = Main()
main.main()

