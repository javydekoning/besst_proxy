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
        "user": {
            "status": 6,
            "name": "hacked",
            "org": {"id": 1340, "type": 6, "name":"hacked", "avatar": "hacked.jpg"}
        },
        "token": fake.md5(),
    },
}

# GET http://static.besst.bafang-service.com/besst/img/hacked.jpg HTTP/1.1

spoofed_auth: dict[str, Any] = {
    "code": 0,
    "data": {
        "auth": [
            "account.delete",
            "account.menu",
            "auth_material",
            "brand.add",
            "brand.delete",
            "brand.edit",
            "brand.menu",
            "dealer.delete",
            "dealer.invitation",
            "dealer.menu",
            "diagnose.menu",
            "error_shooting.menu",
            "file.error.add",
            "file.error.delete",
            "file.error.detail",
            "file.error.edit",
            "file.error",
            "item.add",
            "item.bom.delete",
            "item.bom.edit",
            "item.copy",
            "item.delete",
            "item.edit",
            "item.menu",
            "object.delete",
            "object.menu",
            "object.replace",
            "oem.delete",
            "oem.invitation",
            "oem.menu",
            "order.add",
            "order.delete",
            "order.edit",
            "order.menu",
            "order.replace",
            "product_secondary_battery",
            "product_secondary_charger",
            "product_secondary_connector",
            "product_secondary_controller",
            "product_secondary_hmi",
            "product_secondary_motor",
            "product_secondary_sensor",
            "product_secondary_tool",
            "product.edit_category",
            "product.menu",
            "product.part",
            "product.product.add",
            "product.product.bom.delete",
            "product.product.bom.edit",
            "product.product.bom.view",
            "product.product.delete",
            "product.product.edit",
            "product.product.training.delete",
            "product.product.training.edit",
            "product.training",
            "production.add",
            "production.delete",
            "production.edit",
            "production.menu",
            "production.produce",
            "production.report",
            "ticket.complaint",
            "ticket.delete",
            "ticket.menu",
            "ticket.service_center.add",
            "ticket.service_center.edit",
            "ticket.service_center",
            "ticket.task",
            "tool.menu",
        ]
    },
}

# /client/1/vehicle/report-list-of-org
spoofed_report_list_of_org = {
    "code": 0,
    "data": {
        "count": 0,
        "report_list": []
    }
}

# /client/1/org/all-junior-partner-list
all_junior_partner_list = {
    "code": 0,
    "data": {
        "org_list": []
    }
}

# /client/1/stat/brand/item-stat
spoofed_item_stat = {
    "code": 0,
    "data": {
        "brand": 0,
        "item": 0
    }
}

# /client/1/stat/brand/item-sales
spoofed_item_sales = {
    "code": 0,
    "data": {
        "list": {
            "data": {
                "2023/08/13": 0,
                "2023/08/14": 0,
                "2023/08/15": 0
            },
            "total": 0
        }
    }
}

# /client/1/stat/brand/dealer-sales-list
dealer_sales_list = {
    "code": 0,
    "data": {
        "list": []
    }
}

# /client/1/stat/brand/item-sales-list
# /client/1/stat/brand/after-sales-stat-list
# /client/1/stat/brand/assembler-stat-list
spoofed_sales_stat_list = {
    "code": 0,
    "data": {
        "list": [],
        "total": 0
    }
}

# /client/1/stat/brand/dealer-sales
dealer_sales = {
    "code": 0,
    "data": {
        "data": {
            "2023/08/13": 0,
            "2023/08/14": 0,
            "2023/08/15": 0
        },
        "total": 0
    }
}

# /client/1/stat/brand/after-sales-stat
after_sales_stat = {
    "code": 0,
    "data": {
        "stat": {
            "Battery": 0,
            "Hmi": 0,
            "Light": 0,
            "Motor": 0,
            "Other": 0,
            "Sensor": 0,
            "Vehicle": 0,
            "controller": 0
        }
    }
}

# /client/1/stat/brand/assembler-stat
assembler_stat = {
    "code": 0,
    "data": {
        "stat": {}
    }
}

# /client/1/object-record/list-for-brand
spoofed_list_for_brand = {
    "code": 0,
    "data": {
        "count": 0,
        "record_list": []
    }
}