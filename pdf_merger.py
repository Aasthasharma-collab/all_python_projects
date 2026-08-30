import os
from pypdf import PdfWriter


def merged_file(folder_path, selected_file, output_name, password=None):
    writer = PdfWriter()
    for file in selected_file:
        full_path = os.path.join(folder_path, file)
        if os.path.exists(full_path):
            writer.append(full_path)
            print(f"successfully added {file}")
        else:
            print(f"warning! {file} this file doesn't exist")

    if password:
        writer.encrypt(password)
        print("password applied")

    output_path = os.path.join(folder_path, output_name)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    print(f"\n finished! merged file created at {output_path}")


folder_path = os.path.join(os.path.expanduser("~"), "Downloads")
selected_file = [
    "Sample1.pdf",
    "Sample2.pdf",
]
output_name = input("enter output name: ").strip()
password = input("enter password or enter to skip: ").strip()
if not password:
    password = None

merged_file(folder_path, selected_file, output_name, password)
