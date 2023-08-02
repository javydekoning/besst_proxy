from mitmproxy import http
from bafang_api_responses import *
import json

def request(flow: http.HTTPFlow) -> None:
    print(
        json.dumps(
            {"method": flow.request.method, "url": flow.request.pretty_url},
            sort_keys=True,
            indent=2,
        )
    )

    if (
        flow.request.pretty_url.__contains__("/client/1/user/login")
        and flow.request.method == "POST"
    ):
        print("Intercepted login")
        flow.response = http.Response.make(
            status_code=200,
            content=json.dumps(spoofed_login),
            headers={"Content-Type": "application/json"},
        )

    elif (
        flow.request.pretty_url.__contains__("/client/1/auth/detail")
        and flow.request.method == "POST"
    ):
        print("Intercepted auth")
        flow.response = http.Response.make(
            status_code=200,
            content=json.dumps(spoofed_auth),
            headers={"Content-Type": "application/json"},
        )
    
    elif (
        flow.request.method == "POST"
    ):
        print("Intercepted generic POST")
        flow.response = http.Response.make(
            status_code=200,
            content=json.dumps(spoofed),
            headers={"Content-Type": "application/json"},
        )