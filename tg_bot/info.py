def info_computer(mess: str):
    mess = mess.lower().split()
    if len(mess) == 2 and mess[1] == "temp":
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temperature = int(file.read().strip()) / 1000
        return f"Температура процессора: {temperature:.2f}°C"
    return "Неизвестная команда"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(info_computer(" ".join(sys.argv[1:])))