import os
import re
import pprint
import argparse

# @profile
def find_regex(dir_loc, regex, max_size=0):
    """
    Find all the files which name matches the regex or their size is
        larger than max_size

    :param dir_loc: the root path
    :param regex: the search string
    :param max_size: file size (in bytes) should be larger than this
    :return: return a list of files which match either of regex or
        larger than max_size, each file's directory is added before filename
    """
    assert isinstance(max_size, int), "Error: max_size should be integer"
    match_files = []
    try:
        for root, dirs, files in os.walk(dir_loc):
            for f in files:
                if regex and re.search(regex, f):
                    match_files.append(os.path.join(root, f))
                elif max_size:
                    fname = os.path.join(root, f)
                    if is_large_file(fname, max_size):
                        match_files.append(fname)
    except re.error as e:
        raise e
    return match_files

# @profile
def is_large_file(fname, max_size):
    try:
        return os.path.getsize(fname) > max_size
    except Exception as e:
        # print ('Warning in checking file {}: {}'.format(fname, e))
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", required=True,
                        dest="root_dir",
                        help="path to the root directory")
    parser.add_argument("-r", default="",
                        dest="reg_exp",
                        help="regular expression for search")
    parser.add_argument("-s", type=int, default=0,
                        dest="max_size",
                        help="find files greater than max_size in bytes")

    args = parser.parse_args()
    assert (args.reg_exp or args.max_size), \
        "search regex or max_size is required!, pass regex using -r parameter or max_size using -s parameter"

    try:
        results = find_regex(args.root_dir, args.reg_exp, args.max_size)
        pprint.pprint(results)
    except re.error as e:
        raise Exception("RegEx Error: {}".format(e))