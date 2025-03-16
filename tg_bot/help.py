def help_message(message: str) -> str:
    help_dict = {
        "add": (
            "'add <shop_name> <amount>' - оплата картой.\n"
            "'add <shop_name> <amount> cash' - оплата наличными.\n"
            "Например: add lidl 12,45. Разделение 12.45 или 12,45 не имеет значения."
        ),
        "info": "info temp",
        "shop": "shop info <month_number>"
    }

    parts = message.lower().split()
    return help_dict.get(parts[1], "Help") if len(parts) > 1 else "Help <name>\nname: add, shop, info."
