from optparse import OptionParser
import os
import subprocess


def add_enviorment_variables():
    cur_path = os.getcwd()

    config_path = cur_path + r"\z88dk\lib\config"
    os.environ["ZCCCFG"] = config_path

    lib_path = cur_path + r"\z88dk\bin"
    os.environ["Path"] = os.environ["Path"] + lib_path


def parse_command_line_arguments():
    parser = OptionParser("usage: %prog -s")
    parser.add_option("-i", dest="input_file", help="input .txt file")
    (options, args) = parser.parse_args()
    if not options.input_file:
        print "input file missing!"
        exit(1)
    return options.input_file



def write_c_line(line):
    line = line.strip()
    return "    printf(\"" + line + "\\n\"" + ");" + "\n"


def compile_tap():
    subprocess.check_output(r"zcc +zx -lndos -create-app -o out in.c")


def compile_wav():
    subprocess.check_output(r"appmake +zx --dumb --audio -b out.tap")


def create_c_file(in_path):
    lines = []
    with open(in_path, "r") as file:
        for line in file:
            lines.append(line)

    with open("in.c", "w") as c_file:
        c_file.write("main(){\n")
        for line in lines:
            c_file.write(write_c_line(line))
        c_file.write("}")
        c_file.write("\r\n")


if __name__ == '__main__':
    in_path = parse_command_line_arguments()
    add_enviorment_variables()
    create_c_file(in_path)
    compile_tap()
    compile_wav()

