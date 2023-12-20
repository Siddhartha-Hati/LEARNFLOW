import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        
        self.amount_var = tk.DoubleVar()
        amount_label = tk.Label(root, text="Enter Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10)
        amount_entry = tk.Entry(root, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        from_currency_label = tk.Label(root, text="From Currency:")
        from_currency_label.grid(row=1, column=0, padx=10, pady=10)
        from_currency_menu = tk.OptionMenu(root, self.from_currency_var, *CurrencyConverter.get_currency_list())
        from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

        to_currency_label = tk.Label(root, text="To Currency:")
        to_currency_label.grid(row=2, column=0, padx=10, pady=10)
        to_currency_menu = tk.OptionMenu(root, self.to_currency_var, *CurrencyConverter.get_currency_list())
        to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

        
        self.result_var = tk.StringVar()
        result_label = tk.Label(root, text="Result:")
        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_display = tk.Label(root, textvariable=self.result_var)
        result_display.grid(row=3, column=1, padx=10, pady=10)

        
        convert_button = tk.Button(root, text="Convert", command=self.convert)
        convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    def convert(self):
        try:
            amount = self.amount_var.get()
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            
            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)

            
            result = amount * rate

            
            self.result_var.set(f"{amount} {from_currency} = {result:.2f} {to_currency}")

        except Exception as e:
            self.result_var.set("Error: " + str(e))

    @staticmethod
    def get_currency_list():
        c = CurrencyRates()
        currencies = c.get_rates('USD')
        return list(currencies.keys())

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()