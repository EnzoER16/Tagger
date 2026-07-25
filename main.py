import flet as ft, flet_dropzone as ftd, os

def main(page: ft.Page):
    page.title = "Tagger"  
    page.window.width = 750
    page.window.height = 500
    page.padding = 15

    async def select_file():
        file = await ft.FilePicker().pick_files(
            dialog_title="Select MP3 file",
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["mp3"])
        if file:
            manage_file(file[0].path)

    def on_drop(event: ftd.DropzoneEvent):
        files_dropped = event.files

        if len(files_dropped) != 1:
            file_text.value = "One file allowed at a time"
            file_text.color = ft.Colors.RED
            file_text.update()
            return

        file = files_dropped[0]

        if file.lower().endswith(".mp3"):
            file_text.value = os.path.basename(file)
            file_text.color = ft.Colors.WHITE
        else:
            file_text.value = "Only mp3 files are allowed"
            file_text.color = ft.Colors.RED

        file_text.update()

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

    main_container = ft.Container(
        ft.Column(
            [file_text, select_button]))

    dropzone = ftd.Dropzone(
        expand=True,
        on_dropped=on_drop)

    page.add(
        ft.Stack(
            [dropzone, main_container],
            expand=True))

if __name__ == "__main__":
    ft.run(main)