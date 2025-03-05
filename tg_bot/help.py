def help_message(message: str) -> str:
    message = message.split()
    if len(message) < 2:
        return "Help <name>\nname: add, auto, poket, shop."
    if message[1] == "add":
        return (f"'add <shop_name> <amount>' - оплата картой."
                f"\n'add <shop_name> <amount> cash' - оплата наличными."
                f"\nНапример: add lidl 12,45. Разделение . или , не имеет значения.")
    if message[1] == "auto":
        return "Help auto"
    if message[1] == "shop":
        return "shop info <month_number>\nshop total <month_number>"
    return "Help"