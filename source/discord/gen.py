from source.discord.adapters import anti
from source.discord.solver import capsolver
from source.utils import thread
import random
import httpx
# import websocket


class Creator:

    def __init__(self, instance: thread.Instance) -> None:
        self.name = 'github.com/yaboipy='.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.client = instance.client
        self.instance = instance
        self.client.proxies = instance.proxy
        self.client.cookies = anti.Data.cookie(instance.client)

    def create(self) -> None:
        try:
            # ws = websocket.WebSocket()
            # ws.connect("wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream")
            resp = self.client.post(
                "https://discord.com/api/v9/auth/register",
                headers=anti.Data.header(browser=anti.DiscordData( # TODO create the dataclass inside anti. 
                    xtrack=self.instance.browser.discord.xtrack, version=self.instance.browser.version,
                    useragent=self.instance.browser.useragent, fingerprint=self.instance.browser.discord.fingerprint
                )), json={
                    "captcha_key": capsolver.solve_captcha(
                        self.instance.api_key,
                        self.instance.browser.useragent,
                        self.instance.proxy),
                    "consent": True,
                    "fingerprint": self.instance.browser.discord.fingerprint,
                    "invite": self.instance.browser.discord.invite,
                    "global_name": self.name,
                    "unique_username_registration": True
                })

            # ws.send(payload=anti.Data.ws_header(
            #     agent=self.instance.browser.useragent,
            #     ver=self.instance.browser.version,
            #     token=token
            # ))

            if resp.status_code == httpx.codes.CREATED:
                token = resp.json()["token"]
                if token:
                    req = httpx.get("https://discord.com/api/v9/users/@me/affinities/guilds",
                                    headers={"authorization": token})
                    if req.status_code == httpx.codes.OK:
                        self.instance.file.write(token + "\n")
                        print(f"[\033[32m>\033[39m] Unlocked {token}")
                    else:
                        print(f"[\033[33m/\033[39m] Locked   {token}")
            else:
                print(f"[\033[31mx\033[39m] Failed   {resp.text}")

            return

        except (Exception, ValueError) as err:
            print(err)
            return
