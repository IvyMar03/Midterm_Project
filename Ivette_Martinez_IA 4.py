
import tkinter as tk
from tkinter import ttk

# --- App config ---
BTN_FONT = ("Segoe UI", 14)
DISP_FONT = ("Segoe UI", 20)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Calculator")
        self.resizable(False, False)
        self.configure(padx=10, pady=10)

        # StringVar keeps the UI display synced
        self.expression = tk.StringVar(value="")

        self._build_ui()
        self._bind_keys()

    # ---------- UI ----------
    def _build_ui(self):
        # Display
        self.entry = ttk.Entry(self, textvariable=self.expression, font=DISP_FONT, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=10, pady=(0, 8))

        # Button specs in a grid layout
        buttons = [
            ("C",  1, 0, self.btn_clear),
            ("(",  1, 1, lambda: self.btn_click("(")),
            (")",  1, 2, lambda: self.btn_click(")")),
            ("÷",  1, 3, lambda: self.btn_click("/")),

            ("7",  2, 0, lambda: self.btn_click("7")),
            ("8",  2, 1, lambda: self.btn_click("8")),
            ("9",  2, 2, lambda: self.btn_click("9")),
            ("×",  2, 3, lambda: self.btn_click("*")),

            ("4",  3, 0, lambda: self.btn_click("4")),
            ("5",  3, 1, lambda: self.btn_click("5")),
            ("6",  3, 2, lambda: self.btn_click("6")),
            ("−",  3, 3, lambda: self.btn_click("-")),

            ("1",  4, 0, lambda: self.btn_click("1")),
            ("2",  4, 1, lambda: self.btn_click("2")),
            ("3",  4, 2, lambda: self.btn_click("3")),
            ("+",  4, 3, lambda: self.btn_click("+")),

            ("0",  5, 0, lambda: self.btn_click("0")),
            (".",  5, 1, lambda: self.btn_click(".")),
            ("%",  5, 2, lambda: self.btn_click("%")),
            ("=",  5, 3, self.btn_equal),
        ]

        style = ttk.Style(self)
        style.configure("TButton", font=BTN_FONT, padding=8)
        style.configure("Accent.TButton", font=BTN_FONT, padding=8)

        for (text, r, c, cmd) in buttons:
            style_name = "Accent.TButton" if text == "=" else "TButton"
            btn = ttk.Button(self, text=text, command=cmd, style=style_name)
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        # Expand equally
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def _bind_keys(self):
        # Allow typing numbers/operators; Enter = equals; Escape = clear; Backspace = delete last char
        self.bind("<Return>", lambda e: self.btn_equal())
        self.bind("<KP_Enter>", lambda e: self.btn_equal())
        self.bind("<Escape>", lambda e: self.btn_clear())
        self.bind("<BackSpace>", self._backspace)

        # Generic binding to append any printable key that belongs in our calculator
        allowed = set("0123456789.+-*/%()")
        def handle_key(event):
            ch = event.char
            if ch in allowed:
                self.btn_click(ch)
        self.bind("<Key>", handle_key)

    # ---------- Assignment4 required functions :) ----------
    def btn_click(self, item: str):
        """Append the clicked button's text to the display expression."""
        current = self.expression.get()
        self.expression.set(current + item)

    def btn_clear(self):
        """Clear the display."""
        self.expression.set("")

    def btn_equal(self):
        """
        Evaluate the expression and show the result.
        Uses eval for brevity to match most course demos.
        Includes try/except to catch invalid math like ZeroDivisionError.
        """
        expr = self.expression.get()
        if not expr.strip():
            return
        try:
            # Evaluate in a restricted namespace to avoid access to builtins
            result = eval(expr, {"__builtins__": {}}, {})
            self.expression.set(str(result))
        except ZeroDivisionError:
            self.expression.set("Error: Div by 0")
        except Exception:
            self.expression.set("Error")

    # ---------- Helpers ----------
    def _backspace(self, event=None):
        text = self.expression.get()
        if text:
            self.expression.set(text[:-1])

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
