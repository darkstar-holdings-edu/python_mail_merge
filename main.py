from mail_merge import Template, MergeData

LETTER_PATH = "Input/Letters/starting_letter.txt"
DATA_PATH = "Input/Names/invited_names.txt"
OUTPUT_DIR = "Output/ReadyToSend"
REPLACE_TOKEN = "[input]"


def main() -> None:
    template = Template(LETTER_PATH)
    merge_data = MergeData(DATA_PATH)

    for name in merge_data.data:
        letter = template.merge(token=REPLACE_TOKEN, value=name)

        path = "/".join([OUTPUT_DIR, f"letter_for_{name}"])
        with open(path, mode="w") as file:
            file.write(letter)


if __name__ == "__main__":
    main()
