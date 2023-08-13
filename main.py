import json
from typing import Any

from bafang_api_responses import spoofed, spoofed_auth, spoofed_login
from mitmproxy import http


def spoof(flow: http.HTTPFlow, spoofed_response: dict[str, Any]):
    print(
        f"""Intercepted POST to: {flow.request.path}
         with body: {str(flow.request.content)}"""
    )

    flow.response = http.Response.make(
        status_code=200,
        content=json.dumps(spoofed_response),
        headers={"Content-Type": "application/json"},
    )
    return flow.response


def request(flow: http.HTTPFlow) -> None:
    print(
        json.dumps(
            {"method": flow.request.method, "url": flow.request.pretty_url},
            sort_keys=True,
            indent=2,
        )
    )

    if flow.request.method == "POST":
        if flow.request.path == "/client/1/user/login":
            spoof(flow, spoofed_login)

        elif flow.request.path == "/client/1/auth/detail":
            spoof(flow, spoofed_auth)

        else:
            spoof(flow, spoofed)

    # Disable update check
    if flow.request.method == "GET":
        if flow.request.pretty_url.__contains__("update/latest.yml"):
            flow.response = http.Response.make(status_code=404)
