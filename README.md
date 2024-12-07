# SigMF Converter README

\\## Overview  
This Python script converts \`.dat\` files containing IQ samples into the \[SigMF\](https://github.com/gnuradio/sigmf) format, generating \`.bin\` and \`.json\` files. It is designed for processing IQ data collected in radio frequency experiments, such as those involving SDRs (Software-Defined Radios).

\\## Features  
- Converts \`.dat\` files to SigMF-compliant \`.bin\` and \`.json\` files.  
- Supports interleaved I/Q samples in \`float32\` or \`float16\` format.  
- Generates metadata dynamically for each input file based on base metadata.  
- Includes error handling for incomplete or invalid input files.

\\---

\\## Prerequisites  
\\### Dependencies  
This script requires the following Python libraries:  
- \`numpy\`  
- \`tqdm\`  

You can install these dependencies using:  
\`\`\`bash  
pip install numpy tqdm  
\`\`\`

\\---

\\## Usage  

1. \\\*\\\*Setup Input and Output Directories\\\*\\\*  
   - Update the paths in the script for \`dat_input_path\` and \`sigmf_output_path\` to point to your \`.dat\` files directory and desired SigMF output directory, respectively.

2. \\\*\\\*Customize Metadata\\\*\\\*  
   - Edit the \`base_metadata\` dictionary in the script to match your experiment details (e.g., sample rate, hardware details, and environment).

3. \\\*\\\*Run the Script\\\*\\\*  
   Execute the script with:  
   \`\`\`bash  
   python sigmf_converter.py  
   \`\`\`

\\---

\\## Input Requirements  
- The \`.dat\` files must contain interleaved I/Q samples.  
- Supported data types are \`float32\` and \`float16\`.

\\---

\\## Output  
For each \`.dat\` file:  
- A \`.bin\` file containing I/Q samples.  
- A \`.json\` file with metadata in SigMF format.  

These files are saved in the directory specified by \`sigmf_output_path\`.

\\---

\\## Example  
\\### Input Directory  
\`/home/mohammed/ztxdata/iq_samples/\`

\\### Output Directory  
\`/home/mohammed/ztxdata/sigmf_files/\`

\\### Generated Files  
\`/home/mohammed/ztxdata/sigmf_files/example.bin\`  
\`/home/mohammed/ztxdata/sigmf_files/example.json\`

\\---

\\## Troubleshooting  
- **No Output Files**: Ensure \`.dat\` files are valid and properly formatted.  
- **Metadata Issues**: Verify and update the \`base_metadata\` dictionary for accuracy.

\\---

\\## Metadata Example  
Below is an example of the base metadata structure in the script:  
\`\`\`json  
{
    "global": {
        "core:datatype": "cf32_le",
        "core:sample_rate": 23040000,
        "core:version": "0.0.1",
        "core:author": "ZTX",
        "core:description": "IQ samples from the srsRAN OTA 5G testbed setup."
    },
    "captures": {
        "core:center_frequency": 3500000000,
        "core:sample_start": 0
    },
    "annotations": {
        "core:sample_start": 0,
        "core:sample_count": 0
    }
}
\`\`\`

\\---

\\## License  
This project is licensed under the MIT License. Feel free to modify and adapt it to your needs.
