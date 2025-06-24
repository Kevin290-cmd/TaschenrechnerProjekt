import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]  # wenn ich mehr buttons adden möchte, muss ich hier was ändern
# das tutorial wollte das ich "√" selber hinzufüge

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]  # die Symbole die oben sind

row_count = len(button_values)  # wird gezählt wie viele Zeilen es gibt
column_count = len(button_values[0])
# also in der ersten zeile ["AC", "+/-", "%", "÷"] werden die 4 strings gezählt


# die farben habe ich auf https://www.schemecolor.com gefunden
color_dark_black = "#0C1A46"
color_sweet_beige = "#F5E0C3"
color_deep_carrot_orange = "#A18477"
color_sandy_brown = "#F1A062"
color_white = "white"

# jz kommt der windows setup>>>>
window = tkinter.Tk()  # erschafft das Fenster/Window
window.title("Taschenrechner")  # Titel des Fensters
# Fenster kann nicht verändert werden (länger gezogen werden)
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_dark_black,
                      # anchor e --> text geht nach rechts
                      foreground=color_white, anchor="e", width=column_count)
# sticky="we" bedeutet, dass der Text in der Label von links nach rechts gestreckt wird
# width=column_count sorgt dafür das die buttons nicht unendlich lang werden wenn man viele Zahlen eingibt
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,  # für die Größe der Buttons
                                # wenn ich auf Button klicke soll (funktion) ausgeführt werden
                                command=lambda value=value: button_clicked(value))
        if value == "√":
            button.config(foreground=color_dark_black, background=color_white)
        elif value in top_symbols:
            button.config(foreground=color_dark_black,  # farben einstellen
                          background=color_sweet_beige)
        elif value in right_symbols:
            button.config(foreground=color_dark_black,
                          background=color_sandy_brown)
            button.config(foreground=color_white,
                          background=color_deep_carrot_orange)
        else:
            button.config(foreground=color_dark_black, background=color_white)
        button.grid(row=row + 1, column=column)
frame.pack()

# A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None


def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None


def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    # global Variablen, damit sie in der Funktion benutzt werden können
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()  # nach der Berechnung werden die Variablen zurückgesetzt

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                operator = value
                label["text"] = "0"
            else:
                B = "0"

            operator = value
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        elif value == "√":
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


# das fenster auf einen bestimmten Ort setzen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# das format des fensters "(w) x (h) + (x) + (y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# das Fenster wird in der Mitte des Bildschirms geöffnet

window.mainloop()  # hält das Fenster aktiv ansonsten würde es sofort schließen
