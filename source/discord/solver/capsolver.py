from dataclasses import dataclass
import httpx
import time


@dataclass
class CapSolver:
    task_id: str = "taskId"
    error_id: str = "errorId"


@dataclass
class OPResp:
    ERROR: int = 1
    SUCCESS: int = 0

    READY: str = "ready"
    PROCESSING: str = "processing"


def solve_captcha(api_key: str, ua: str, proxy: str) -> str:
    resp = httpx.post("https://api.capsolver.com/createTask", json={
        "clientKey": api_key,
        "task": {
            "type": "HCaptchaTurboTask",
            "websiteURL": "https://discord.com",
            "websiteKey": "4c672d35-0701-42b2-88c3-78380b0db560",
            "proxy": proxy,
            "userAgent": ua
        }}).json()

    if resp[CapSolver.error_id] == OPResp.SUCCESS:
        print(f"[\033[32m>\033[39m] Created Captcha Task:", resp[CapSolver.task_id])
        while True:
            r = httpx.post("https://api.capsolver.com/getTaskResult", json={
                "clientKey": api_key,
                "taskId": resp[CapSolver.task_id]
            }).json()
            if r["status"] == OPResp.PROCESSING:
                time.sleep(1.5)
                continue
            elif r["status"] == OPResp.READY:
                return r["solution"]["gRecaptchaResponse"]
    else:
        if resp[CapSolver.error_id] == OPResp.ERROR:
            print(f"Failed To Solve: {resp}")
            return ""
        print(f"Something went Wrong: {resp}")
