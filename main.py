import json
from typing import Any

from bafang_api_responses import Spoofed
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
            spoof(flow, Spoofed.login)

        elif flow.request.path == "/client/1/auth/detail":
            spoof(flow, Spoofed.auth)

        elif flow.request.path == "/client/1/vehicle/report-list-of-org":
            spoof(flow, Spoofed.report_list_of_org)

        elif flow.request.path == "/client/1/org/all-junior-partner-list":
            spoof(flow, Spoofed.all_junior_partner_list)

        elif flow.request.path == "/client/1/stat/brand/item-stat":
            spoof(flow, Spoofed.item_stat)

        elif flow.request.path == "/client/1/stat/brand/item-sales":
            spoof(flow, Spoofed.item_sales)

        elif flow.request.path == "/client/1/stat/brand/dealer-sales-list":
            spoof(flow, Spoofed.dealer_sales_list)

        elif flow.request.path == "/client/1/stat/brand/dealer-sales":
            spoof(flow, Spoofed.dealer_sales)

        elif flow.request.path == "/client/1/stat/brand/after-sales-stat":
            spoof(flow, Spoofed.after_sales_stat)

        elif flow.request.path == "/client/1/stat/brand/assembler-stat":
            spoof(flow, Spoofed.assembler_stat)

        elif flow.request.path == "/client/1/object-record/list-for-brand":
            spoof(flow, Spoofed.list_for_brand)

        elif flow.request.path in [
            "/client/1/stat/brand/item-sales-list",
            "/client/1/stat/brand/after-sales-stat-list",
            "/client/1/stat/brand/assembler-stat-list",
        ]:
            spoof(flow, Spoofed.sales_stat_list),

        else:
            spoof(flow, Spoofed.generic)

    # Disable update check
    if flow.request.method == "GET":
        if flow.request.pretty_url.__contains__("update/latest.yml"):
            flow.response = http.Response.make(status_code=404)
        if flow.request.pretty_url.__contains__("hacked.jpg"):
            flow.response = http.Response.make(status_code=404)
