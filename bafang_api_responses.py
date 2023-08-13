from typing import Any

from faker import Faker

fake = Faker()
Faker.seed(0)

spoofed: dict[str, Any] = {
    "code": 0,
    "data": {},
}

spoofed_login: dict[str, Any] = {
    "code": 0,
    "data": {
        "account_type": [1, 2, 3, 6, 7],
        "user": {"status": 6, "name": "hacked", "org": {"id": 1340, "type": 6}},
        "token": fake.md5(),
    },
}

spoofed_auth: dict[str, Any] = {
    "code": 0,
    "data": {
        "auth": [
            "product.menu",
            "product.part",
            "product.training",
            "product.edit_category",
            "product.product.add",
            "product.product.edit",
            "product.product.delete",
            "product.product.bom.view",
            "product.product.bom.edit",
            "product.product.bom.delete",
            "product.product.training.edit",
            "product.product.training.delete",
            "product_secondary_motor",
            "product_secondary_hmi",
            "product_secondary_battery",
            "product_secondary_sensor",
            "product_secondary_controller",
            "product_secondary_connector",
            "product_secondary_charger",
            "product_secondary_tool",
            "production.menu",
            "production.add",
            "production.edit",
            "production.delete",
            "production.produce",
            "production.report",
            "order.menu",
            "order.add",
            "order.edit",
            "order.delete",
            "order.replace",
            "item.menu",
            "item.add",
            "item.edit",
            "item.delete",
            "item.copy",
            "item.bom.edit",
            "item.bom.delete",
            "account.menu",
            "account.delete",
            "ticket.menu",
            "ticket.delete",
            "ticket.service_center",
            "ticket.service_center.add",
            "ticket.service_center.edit",
            "ticket.complaint",
            "ticket.task",
            "brand.menu",
            "brand.add",
            "brand.edit",
            "brand.delete",
            "object.menu",
            "object.delete",
            "object.replace",
            "tool.menu",
            "diagnose.menu",
            "error_shooting.menu",
            "dealer.menu",
            "dealer.delete",
            "dealer.invitation",
            "oem.menu",
            "oem.delete",
            "oem.invitation",
            "file.error",
            "file.error.delete",
            "file.error.detail",
            "file.error.add",
            "file.error.edit",
            "auth_material",
        ]
    },
}
