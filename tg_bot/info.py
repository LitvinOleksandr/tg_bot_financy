COMMANDS = {
    "temp": lambda: get_a_core_temp(),
    "help": lambda: get_help()
}

def get_help() -> str:
    # Здесь можно добавить более подробное описание каждой команды
    return """
    Доступные команды:
    - temp: Показывает температуру процессора
    - help: Показывает список доступных команд
    """

def get_a_core_temp() -> str:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temperature = int(file.read().strip()) / 1000
    return f"Температура процессора: {temperature:.2f}°C"

def info_manager(message: str):
    text = message.lower()
    for command, func in COMMANDS.items():
        if command in text:
            return func()
    return "Проверьте правильность написания команды."
