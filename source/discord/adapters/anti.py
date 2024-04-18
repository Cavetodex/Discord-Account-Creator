from dataclasses import dataclass
import base64
import json
import httpx
import tls_client


@dataclass
class DiscordData:
    xtrack: str
    version: int
    useragent: str
    fingerprint: str


class Data:
    @staticmethod
    def fingerprint() -> str:
        while not (fp := httpx.get("https://discord.com/api/v9/experiments").json().get("fingerprint", "")):
            continue
        return fp

    @staticmethod
    def xtrack(ver: int) -> str:
        return base64.b64encode(json.dumps({
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "en-US",
            "browser_user_agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(ver)}.0.0.0 Safari/537.36",
            "browser_version": f"{str(ver)}.0.0.0",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 9999,
            "client_event_source": None
        }).encode("utf-8")).decode("utf-8")

    @staticmethod
    def header(browser: DiscordData) -> dict:
        return {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/',
            'sec-ch-ua': f'"Not.A/Brand";v="8", "Chromium";v="{str(browser.version)}", "Google Chrome";v="{str(browser.version)}"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': browser.useragent,
            'x-fingerprint': browser.fingerprint,
            'x-track': browser.xtrack,
        }

    @staticmethod
    def cookie(client: tls_client.sessions):
        return client.post("https://discord.com/register").cookies

    # @staticmethod
    # def ws_header(ver: int, token: str, agent: str) -> str:
    #     return json.dumps({
    #         "op": 2,
    #         "d": {
    #             "token": token,
    #             "capabilities": 16381,
    #             "properties": {
    #                 "os": "Windows",
    #                 "browser": "Chrome",
    #                 "device": "",
    #                 "system_locale": "en-GB",
    #                 "browser_user_agent": agent,
    #                 "browser_version": f"{str(ver)}.0.0.0",
    #                 "os_version": "10",
    #                 "referrer": "",
    #                 "referring_domain": "",
    #                 "referrer_current": "",
    #                 "referring_domain_current": "",
    #                 "release_channel": "stable",
    #                 "client_build_number": 225093,
    #                 "client_event_source": None
    #             },
    #             "presence": {
    #                 "status": "online",
    #                 "since": 0,
    #                 "activities": [],
    #                 "afk": False
    #             },
    #             "compress": False,
    #             "client_state": {
    #                 "guild_versions": {},
    #                 "highest_last_message_id": "0",
    #                 "read_state_version": 0,
    #                 "user_guild_settings_version": -1,
    #                 "user_settings_version": -1,
    #                 "private_channels_version": "0",
    #                 "api_code_version": 0
    #             }
    #         }
    #     })
