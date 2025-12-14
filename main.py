import ast
import dis
import inspect
import sys
from fileinput import filename
import mmh3
from traitlets import Integer


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def compile_code(source_code, path):
    code_obj = compile(source_code,filename=path, mode='exec')
    return code_obj



file_content = read_file("test.py")
file_content2 = read_file("test2.py")

code_object = compile_code(file_content, "test.py")
code_object2 = compile_code(file_content2, "test2.py")

def getOpcodes(code_obj):
    opcodes = []

    for instr in dis.get_instructions(code_obj):
        # Dont add print statements
        print(instr)
        opcodes.append(instr.opname)

    return opcodes


def winnowing_algo(arr):
    # Take array and convert into n-grams, lets try with N = 3
    N = 3
    hashArr = []
    left = 0
    right = N - 1
    while right < len(arr):
        hashArr.append(mmh3.hash(arr[left] + "_" + arr[left+1] + "_" + arr[right], 0, False))
        left += 1
        right += 1

    # Create finger prints with winnowing algorithm
    fingerPrints = []
    W_SIZE = 5
    w_left = 0
    w_right = W_SIZE - 1
    last_selected_index = -1
    selected_hashes = set()

    while w_right < len(hashArr):
        min_hash_val = sys.maxsize
        min_hash_index = -1

        for i in range(w_left, w_right + 1):
            current_hash = hashArr[i]

            if current_hash <= min_hash_val:
                min_hash_val = current_hash
                min_hash_index = i

        if min_hash_index != last_selected_index:
            fingerPrints.append(min_hash_val)
            last_selected_index = min_hash_index

        w_left += 1
        w_right += 1

    return fingerPrints


arr = getOpcodes(code_object)
arr2 = getOpcodes(code_object2)

print(winnowing_algo(arr))
print(winnowing_algo(arr2))

