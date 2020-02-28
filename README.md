# Find Files
This repo is a python script to recurse a given directory location and return a list of files whose names match a regex.
# Find Files
This is a python script to recurse a given directory location and return a list of files whose names match a regex.
## Usage
Use either 
- `python match_files.py -p <dir_loc> -r <regex> -s <max_size>` from console, or
- Call  `match_files.find_regex(dir_loc, regex, max_size)` from your code to find the files in `dir_loc` that satisfy `regex` pattern or their size are greater than `max_size`.
- `match_files` uses Python Regular Expression from `re` package. Information on `re` package is avaiable at [here](https://developers.google.com/edu/python/regular-expressions) and [here](https://docs.python.org/2/library/re.html).

## Test Cases
 Test cases are in `test` folder. To run test cases, use `python run_test.py`. The following regular expressions are tested:
- sample string: to test if the function has query a nonspecial string
- empty character: to check if the function works with an empty string, the output should be empty
- `_` character: to test if the function works with special characters
- space character: to test if the function works with spaces
- A test case is considered for max_size.

## Run Time
Profiling gives us some insight on runtime of each line of the code. Porfiling was done using [`line_profiler`](https://pypi.org/project/line_profiler/) for two cases:
- a large number of files on a machine using `/` as the root path and `.` as the `regex`, and, 
- a large number of files on a machine using `/` as the root path and a small number (100 bytes) as the `max_size`.

The outputs of profiling are in the profiler folder: `regex_prfile.txt` and `max_size_profile.txt`. Looking at these files, we can see that the main loop with on line 21 with `os.walk` has the time per hit percentage for both queries. The reason is that, `os.walk` is significantly slow as it mentioned in [here](https://github.com/benhoyt/scandir). Therefore, the main improvement would be to replace `os.walk` with a faster module such as [scandir](https://github.com/benhoyt/scandir). Another option is to migrate to C++, which has lower overhead and handles IO and loops faster. 
Another improvement is to remove the function `is_large_file` and directly use it the main loop of `find_regex`. It reduces the overhead for function call but decreases the readability of the code.

