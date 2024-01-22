from harmonization.google.docs import Docs
from harmonization.google.drive import Drive


FILE_ID = '1ybnpb00B2AqOOaWZd3ZrMCEZEH899SjYZFpNcziMRIo'


def main():
    file = Drive(FILE_ID)
    document = Docs(FILE_ID)
    file.get_comments()
    document.get_suggestions()


if __name__ == "__main__":
    main()
