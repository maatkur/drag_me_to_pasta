from tkinter import messagebox


class Dialogs:

    @staticmethod
    def success_dialog() -> None:
        messagebox.showinfo("Aviso", "Seu XML foi enviado para a pasta correta\nAgora é só imprimir a NF :-)")

    @staticmethod
    def fail_dialog(text: str) -> None:
        messagebox.showinfo("Aviso", f"{text}")
