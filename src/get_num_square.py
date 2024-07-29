import os

# get the input and convert it to int
num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))
else:
    num = 1

output_env = os.getenv("GITHUB_OUTPUT")

if output_env is None:
    raise OSError("Environment file not found")

with open(output_env, "a") as gh_output:
    gh_output.write(f"NUM_SQUARED={num ** 2}\n")
