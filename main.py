import os
import zipfile


PATH = 'your_saved_zip_path'


def extract(zipFile, dst):
    with zipfile.ZipFile(zipFile) as z:
        z.extractall(dst)


def func(path):
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.zip'):
                if not os.path.exists(pathname + '/' + os.path.splitext(filename)[0]):
                    zipFile = pathname + '/' + filename
                    dst = pathname + '/' + os.path.splitext(filename)[0]
                    extract(zipFile, dst)
                    func(dst)


def main():
    func(PATH)


main()
