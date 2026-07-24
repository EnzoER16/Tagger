import flet as ft, os

def main(page: ft.Page):
    page.title = "Tagger"  
    page.window.width = 750
    page.window.height = 500
    page.padding = 15

if __name__ == "__main__":
    ft.run(main)