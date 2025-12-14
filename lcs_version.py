import ast
import dis
import inspect
from fileinput import filename

code = """
def greet(name):
    print(f"Hello, {name}!")
    for i in range(0,10):
        print("YOO")

greet("World")
"""

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def compile_code(source_code, path):
    code_obj = compile(source_code,filename=path, mode='exec')
    return code_obj

def longestCommonSubsequence(code1, code2):
    dp = [[0 for j in range(len(code2) + 1)] for i in range(len(code1) + 1)]
    for i in range(len(code1)-1, -1 ,-1):
        for j in range(len(code2) -1, -1, -1):
            if code1[i] == code2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    return dp[0][0]



def normalizeFile(code):
    new_code = ""
    arr = list(code.split("\n"))

    for statement in arr:
        if statement.strip().startswith("print") or statement.strip().startswith("#"):
            continue
        else:
            new_code += statement
            new_code += "\n"

    return code


file_content = read_file("test.py")
file_content2 = read_file("test2.py")

code_object = compile_code(normalizeFile(file_content), "test.py")
code_object2 = compile_code(file_content2, "test2.py")

def normalizeOpCodes(opcodelst):
    pass



def getOpcodes(code_obj):
    opcodes = []

    for instr in dis.get_instructions(code_obj):
        # Dont add print statements
        print(instr)
        opcodes.append(instr.opname)

    return opcodes

# Convert array into strings
c1 = "".join(str(x) for x in getOpcodes(code_object))
c2 = "".join(str(x) for x in getOpcodes(code_object2))

# Dice similarity coefficient
score = (2 * longestCommonSubsequence(c1, c2)) / (len(c1) + len(c2))
print(score)