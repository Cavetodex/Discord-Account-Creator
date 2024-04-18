from source.discord.adapters import anti
from dataclasses import dataclass
from typing import Any, Union
import concurrent.futures
import tls_client
import random


@dataclass
class Discord:
    xtrack: str
    invite: str
    fingerprint: str


@dataclass
class Browser:
    version: int
    useragent: str
    discord: Discord


@dataclass
class Instance:
    file: any
    proxy: str
    api_key: str
    browser: Browser
    client: tls_client.Session


class Start:
    @staticmethod
    def create(instance: Instance):
        from source.discord.gen import Creator
        Creator(instance).create()


def create_threads(cfg: Union[Any], proxies: list[str]) -> None:
    instances: list[Instance] = []
    tokens: list[str] = []

    inv = input("discord.gg/")
    fil = open("tokens.txt", "a")
    ver = random.randint(110, 115)

    def create_instance(proxy: str) -> Instance:
        instance = Instance(
            file=fil,
            api_key=cfg["ApiKey"],
            proxy=f"http://{proxy}",
            client=tls_client.Session(
                client_identifier=f"chrome_{str(ver)}",
                random_tls_extension_order=True
            ),
            browser=Browser(
                version=ver,
                useragent=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(ver)}.0.0.0 Safari/537.36",
                discord=Discord(
                    invite=inv,
                    xtrack=anti.Data.xtrack(ver),
                    fingerprint=anti.Data.fingerprint()
                )
            )
        )
        return instance

    with concurrent.futures.ThreadPoolExecutor(max_workers=int(cfg["MaxWorkers"] or len(proxies))) as ex:
        for f in concurrent.futures.as_completed(
                [ex.submit(create_instance, value) for value in proxies]):
            instances.append(f.result())
        for ins in instances:
            tokens.append(ex.submit(Start.create, ins))
    return
