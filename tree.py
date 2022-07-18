import sys
import os

filename = './'


def get_filename(*args):
    if len(sys.argv) > 2:
        print('incompatible use of function')
    global filename
    filename = sys.argv[1]
    return filename  # escape return


def get_files(filename):
    # files = os.listdir(filename)
    for root, dirs, files in os.walk(filename, False, ):
        for name in files:
            # print(os.path.join(root, name))
            print_file(root, name)
            f_out.writelines(fr"{root + name}" + " \n")
        for name in dirs:
            # print(os.path.join(root, name))
            print_dict(root, name)
            f_out.writelines(f"{root + name} \n")
    # close file to clean up
    f_out.close()

    # for item in files:
    #     spec_file = print_dict() + item
    #     if os.path.isdir(spec_file):
    #         get_files(item)
    #     elif os.path.isfile(spec_file):
    #         print(item)
    #     else:
    #         print('unknown filetype')
    # return os.listdir()
    # pass


def print_dict(root, name):
    # return os.getcwd()
    print(os.path.join(root, name))
    # pass


def print_file(root, name):
    # files = [get_files()]
    # print(files)
    print(os.path.join(root, name))
    # return os.path.join(root, name)
    # for expansion, doesnt work


def main(filename):
    # find_dir = input('input directory to print: ')
    # print(str(get_files(filename)))
    # print_dict()
    get_files(filename)
    return


if __name__ == '__main__':
    # filename = sys.argv[0]
    # if filename is None:
    #     filename = '.'
    f_out = open('directory_log.txt', 'w')
    f_out.write('Start of directory list: \n')
    main(filename)
