import flet as ft, flet_dropzone as ftd, os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

def main(page: ft.Page):
    page.title = "Tagger"  
    page.window.width = 750
    page.window.height = 500
    page.window.resizable = False
    page.window.maximizable = False
    page.padding = 15

    metadata = {
        "TIT2": "Title",
        "TIT3": "Subtitle",
        "TPE1": "Artist",
        "TPE2": "Album Artist",
        "TALB": "Album",
        "TCON": "Genre",
        "TRCK": "Track",
        "TDRC": "Year",
        "COMM": "Comment",
        "POPM": "Rating",
        "APIC": "Image"}

    # file selection

    async def select_file():
        file = await ft.FilePicker().pick_files(
            dialog_title="Select MP3 file",
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["mp3"])
        if file:
            file_text.value = os.path.basename(file[0].path)
            file_text.color = ft.Colors.WHITE
            read_metadata(file[0].path)

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
            read_metadata(file)
        else:
            file_text.value = "Only mp3 files are allowed"
            file_text.color = ft.Colors.RED

        file_text.update()

    # metadata

    def read_metadata(path):
        data_column.controls.clear()
        audio = MP3(path, ID3=ID3)

        for key, value in audio.tags.items():
            label = metadata.get(key[:4], key)

            if key.startswith("APIC"):
                cover = ft.Image(
                    src=value.data,
                    width=200,
                    height=200)
                data_column.controls.append(cover)
            else:
                data_column.controls.append(
                    ft.TextField(label=label, value=str(value)))

        save_button.disabled = False

    # controls

    file_text = ft.Text(
        "No file selected",
        color=ft.Colors.GREY_500,
        expand=True)

    select_button = ft.Button(
        "Select file",
        icon=ft.Icons.INSERT_DRIVE_FILE_OUTLINED,
        on_click=select_file)

    save_button = ft.Button(
        "Save changes",
        icon=ft.Icons.SAVE,
        disabled=True)

    buttons_row = ft.Container(
        content=ft.Row(
            controls=[
                file_text, select_button, save_button]))

    metadata_container = ft.Container(
        data_column:=ft.Column())

    main_container = ft.Container(
        ft.Column([buttons_row, metadata_container]))

    dropzone = ftd.Dropzone(
        expand=True,
        on_dropped=on_drop)

    page.add(
        ft.Stack(
            [dropzone, main_container],
            expand=True))

if __name__ == "__main__":
    ft.run(main)