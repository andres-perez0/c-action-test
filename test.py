import os, subprocess

# settings 
TEST_DIR = '/tests'
CODE_FILE = 'main.c'
COMPILER_TIMEOUT = 10.0 # always good to have timeouts for security purposes
RUN_TIMEOUT = 10.0

# create absolute paths
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

print("Building...")
try: 
    ret = subprocess.run(['gcc', code_path, '-o', app_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, 
                         timeout=COMPILER_TIMEOUT
                         )
except Exception as e:
    print("Error: Compilation failed.", str(e))
    exit(1)

# Parse Output
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stdout.decode('utf-8')
print(output)

# Check to see if the program compiled successfully
if ret.returncode != 0:
    print("Compilation failed.")
    exit(1)

# run  the compiled program 
print("running...")
try: 
    ret = subprocess.run([app_path], 
                         stdout=subprocess.PIPE,
                         timeout=RUN_TIMEOUT
                         )
except Exception as e:
    print("ERROR: Runtime failed.", str(e))
    exit(1)

# Parse Ouput
output = ret.stdout.decode('utf-8')
print("output: ", output)

# all tests passed! Exit gracefully
print("all tests passed!")
exit(0)