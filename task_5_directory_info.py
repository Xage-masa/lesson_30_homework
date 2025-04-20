import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

logging.basicConfig(filename='directory_contents.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def collect_info(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path {directory_path} is not a directory.")

    parent_directory = os.path.basename(os.path.abspath(directory_path))

    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        if os.path.isdir(entry_path):
            info = FileInfo(name=entry, extension=None, is_directory=True, parent_directory=parent_directory)
        else:
            name, ext = os.path.splitext(entry)
            info = FileInfo(name=name, extension=ext.lstrip('.'), is_directory=False, parent_directory=parent_directory)

        logging.info(f'{info.name} | {info.extension if info.extension else "N/A"} | ' +
                     f'{"Directory" if info.is_directory else "File"} | {info.parent_directory}')

def main():
    parser = ArgumentParser(description="Analyze directory and log contents.")
    parser.add_argument('directory', type=str, help="Path to the directory")
    args = parser.parse_args()

    try:
        collect_info(args.directory)
        print(f'Information saved to directory_contents.log for "{args.directory}"')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
