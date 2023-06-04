
# --> DOI missing
# Content profiling

+ Group 6
+ Subject: Content profiling for a data repository
+ Year of creation: 2023
+ Author: Valentin Schnabl & Tuvshin Selenge
+ ORCID: https://orcid.org/0000-0001-6367-3403 (Valentin Schnabl)
+ ORCID: https://orcid.org/0009-0001-3293-2959 (Tuvshin Selenge)

---
**Overview**

Operating a data repository comes with the crucial task of understanding its contents. In this project, we aim to utilize digital preservation tools for content profiling. 
Our goal is to analyze and visualize the types of files within the repository, gaining valuable insights into their characteristics and formats. This information will guide us in making informed decisions regarding storage, preservation strategies, and data management practices, ensuring responsible repository operation.

---

**Key Topics**

- Procedure
- Code
- Overview of the data samples
- Brief analysis
- Conclusion
--- 

**Procedure**

In this project, we leverage FITS (File Information Tool Set) for file format identification and validation, as well as C3PO for content profiling and conflict resolution. Through a Python script, we automate the analysis process. C3PO is deployed as a Docker image, allowing metadata analysis of digital collections. The analysis results are processed in a Jupyter notebook, generating visual outputs that provide insights into file types and quantities. Additionally, data samples are produced, and based on the interpretation of the results, decisions can be made regarding the need for digital preservation actions.

---

**Code**

The provided code requires the following packages to be imported:

- sys: This package provides access to system-specific parameters and functions.
- os: This package provides a way to interact with the operating system, allowing file and directory operations.
- subprocess: This package allows the creation of new processes, enabling the execution of external commands or scripts.
- zipfile: This package provides tools for creating, reading, and extracting files from ZIP archives.

These packages are part of the Python standard library, which means they should be available by default when running Python. No additional external dependencies or installations are required to execute the code.

Our code is a Python script that automates the process of analyzing files within a data repository using the FITS (File Information Tool Set) command-line tool. The script begins by setting the path to the FITS tool (`fits.bat`) in the `pathToFits` variable, which should be adjusted based on the actual location of the tool on your system.

Next, it retrieves the directory path from the command-line argument passed to the script (`sys.argv[1]`), which specifies the directory where the data repository is located. If more than one command-line argument is provided, it prints an error message and exits.

The script attempts to create an output directory named "output" inside the specified directory. If the directory already exists, it prints an error message.

It then retrieves the list of files and directories within the specified directory using `os.listdir(dir)`.

The script iterates over the entries in the directory and checks if any of them have a ".zip" file extension. If a ZIP file is found, it extracts its contents into the specified directory using the `ZipFile` module.

The code then uses the `subprocess.Popen` function to execute the `fits.bat` command-line tool. It passes the appropriate arguments, including the input directory (`dir`) and the output directory (`dir/output/`). The `cwd` parameter is set to the `pathToFits` directory to ensure the correct execution context. The `shell=True` argument enables running the command as a shell command.

The script captures the standard output and error from the executed process using `p.communicate()`, storing them in the `stdout` and `stderr` variables, respectively.

In summary, this code sets up the execution environment for the FITS command-line tool, extracts any ZIP files found in the specified directory, and then runs the FITS tool on the directory, generating the output in the "output" directory. The script provides a convenient way to automate the analysis of file contents within a data repository using FITS.

---
**Overview of the data samples**

---
**Brief analysis**

---

**Conclusion**

# docker run -it -p **port**:9000 -v **dir**\output:/data/FITS artourkin/c3po:latest
