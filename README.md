# Content profiling

+ Subject: Content profiling for a data repository
+ Year of creation: 2023
+ Author: Valentin Schnabl & Tuvshin Selenge
+ ORCID: https://orcid.org/0000-0001-6367-3403 (Valentin Schnabl)
+ ORCID: https://orcid.org/0009-0001-3293-2959 (Tuvshin Selenge)

---
**Overview**

Operating a data repository comes with the crucial task of understanding its contents. In this project, we aim to utilize digital preservation tools for content profiling. 
Our goal is to analyse and visualise the types of files within the repository, gaining valuable insights into their characteristics and formats. This information will guide us in making informed decisions regarding storage, preservation strategies, and data management practices, ensuring responsible repository operation.

---

**Key Topics**

- Procedure
- Code
- Overview of the data samples
- Brief analysis
- Conclusion
--- 

**Procedure**

In this project, we utilize FITS <sup>[1](#fits)</sup> (File Information Tool Set) for file format identification and validation, as well as C3PO <sup>[2](#c3po)</sup> for content profiling and conflict resolution. The analysis process is automated using a Python script. C3PO is deployed as a Docker image, enabling metadata analysis of digital collections. To run the analysis, use the command `docker run -it -p **port**:9000 -v **dir**/output:/data/FITS artourkin/c3po:latest`.

The analysis results are processed in PowerBI. PowerBI provides a platform for data visualization and exploration. Through visual outputs, we gain insights into file types and quantities. Additionally, based on the interpretation of the results, decisions can be made regarding the need for digital preservation actions.

---

**Code**

The code requires the following packages to be imported:

- sys: This package provides access to system-specific parameters and functions.
- os: This package provides a way to interact with the operating system, allowing file and directory operations.
- subprocess: This package allows the creation of new processes, enabling the execution of external commands or scripts.
- zipfile: This package provides tools for creating, reading, and extracting files from ZIP archives.

These packages are part of the Python standard library, so no additional external dependencies or installations are required to execute the code.

The script starts by setting the path to the FITS tool (fits.bat) in the pathToFits variable. Make sure to adjust this path to match the actual location of the FITS tool on your system.

Next, the script retrieves the directory path from the command-line argument passed to the script (`sys.argv[1]`), which specifies the directory where the data repository is located. It ensures that only one command-line argument is provided; otherwise, it prints an error message and exits.

The script attempts to create an output directory named "output" inside the specified directory. If the directory already exists, it prints an error message.

Then, it retrieves the list of files and directories within the specified directory using `os.listdir(dir)`.

The script iterates over the entries in the directory and checks if any of them have a ".zip" file extension. If a ZIP file is found, it extracts its contents into the specified directory using the ZipFile module.

The code uses the subprocess.Popen function to execute the fits.bat command-line tool. It passes the appropriate arguments, including the input directory (dir) and the output directory (dir/output/). The cwd parameter is set to the pathToFits directory to ensure the correct execution context. The shell=True argument enables running the command as a shell command.

The script captures the standard output and error from the executed process using `p.communicate()`, storing them in the stdout and stderr variables, respectively.

In summary, this code automates the analysis of files within a data repository using the FITS command-line tool. It sets up the execution environment, extracts ZIP files if present, and runs the FITS tool on the specified directory, generating the output in the "output" directory. This script provides a convenient way to automate the analysis of file contents within a data repository using FITS.

---
**Overview of the data samples**

Our dataset, derived from C3PO, was transformed from a 651 KB raw CSV file into a filtered XLSX file with a reduced size of 93 KB. During the conversion, we retained essential information for our PowerBI analysis, including Author, Pagecount, File Extension, Font, Content Type, and Checksum.

Furthermore, our analysis focused on exploring the distribution of mimetypes within the dataset, providing insights into the variety of file types present. Additionally, we examined the creation year of certain files, revealing trends and patterns in their origins.

By optimizing the dataset and considering these factors, we enabled efficient data exploration and informed decision-making in PowerBI.

---
**Brief analysis**

In our PowerBI analysis, we filtered and cleaned data from C3PO. Unnecessary columns were removed to focus on relevant information. We created three visualizations: a table overview, showing important details; a visualization of mimetype frequency; and a visualization of file creation years. We found out that most commen mimetype were text/plain and image/png. Preservation plans should be considered for formats like JPG and PNG. Evaluation of preservation costs and benefits is crucial for future access and visualisation.

---

**Conclusion**

To summarize our findings, our analysis in PowerBI provided valuable insights into the dataset obtained from C3PO. By filtering and cleaning the data, we obtained a clear view of important information. We created visualizations to explore file types, mimetypes, and creation years. Preservation plans should be considered for non-plain text formats. Careful evaluation of preservation costs and benefits is necessary for informed decision-making. Overall, this analysis enhances our understanding of the dataset and highlights the importance of preservation for long-term access and visualization.

<a name="fits">1</a>: https://projects.iq.harvard.edu/fits/home
<a name="c3po">2</a>: http://ifs.tuwien.ac.at/imp/c3po
