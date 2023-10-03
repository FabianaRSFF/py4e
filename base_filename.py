base_filename = input("Enter the base filename: ")


def process_source_files(base_filename):
    c_files = []    # List to store C file names
    cpp_files = []  # List to store C++ file names
    cs_files = []   # List to store C# file names

    with open(base_filename, 'r') as file:
        for line in file:
            filename = line.strip()  # Remove leading/trailing whitespace

            if filename.endswith(".c"):
                c_files.append(filename)
            if filename.endswith(".cpp"):
                cpp_files.append(filename)
            if filename.endswith(".cs"):
                cs_files.append(filename)

    with open(f"c_{base_filename}", "w") as c_output_filename:
        c_output_filename.write("\n".join(c_files))
    with open(f"cs_{base_filename}", "w") as cs_output_filename:
        cs_output_filename.write("\n".join(cs_files))
    with open(f"cpp_{base_filename}", "w") as cpp_output_filename:
        cpp_output_filename.write("\n".join(cpp_files))


process_source_files(base_filename)




