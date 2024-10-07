def format_time(seconds):
    SECONDS_IN_A_MINUTE = 60
    SECONDS_IN_AN_HOUR = 60 * SECONDS_IN_A_MINUTE
    SECONDS_IN_A_DAY = 24 * SECONDS_IN_AN_HOUR


    days, seconds = divmod(seconds, SECONDS_IN_A_DAY)
    hours, seconds = divmod(seconds, SECONDS_IN_AN_HOUR)
    minutes, seconds = divmod(seconds, SECONDS_IN_A_MINUTE)
    day_word = "днів" if days != 1 else "день"
    return f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


user_input = int(input("Введіть кількість секунд (0 ≤ число < 8640000): "))
if 0 <= user_input < 8640000:
    result = format_time(user_input)
    print(result)
else:
    print("Число повинно бути більше або дорівнювати 0 та менше ніж 8640000.")
