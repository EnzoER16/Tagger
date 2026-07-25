import flet as ft, os

def main(page: ft.Page):
    page.title = "Tagger"  
    page.window.width = 750
    page.window.height = 500
    page.padding = 15

    async def select_file(e):
        file = await ft.FilePicker().pick_files(
            dialog_title="Select MP3 file",
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["mp3"])
        if file:
            manage_file(file[0].path)

    def manage_file(path: str):
        file_text.value = os.path.basename(path)
        file_text.color = ft.Colors.WHITE

    file_text = ft.Text(
        "No files selected",
        color=ft.Colors.GREY_500)

    select_button = ft.Button(
        "Select file",
        icon=ft.Icons.INSERT_DRIVE_FILE_OUTLINED,
        on_click=select_file)

    page.add(file_text, select_button)

if __name__ == "__main__":
    ft.run(main)