SigMF Converter README

\## Overview This Python script converts \`.dat\` files containing IQ
samples into the \[SigMF\](https://github.com/gnuradio/sigmf) format,
generating \`.bin\` and \`.json\` files. It is designed for processing
IQ data collected in radio frequency experiments, such as those
involving SDRs (Software-Defined Radios).

\## Features - Converts \`.dat\` files to SigMF-compliant \`.bin\` and
\`.json\` files. - Supports interleaved I/Q samples in \`float32\` or
\`float16\` format. - Generates metadata dynamically for each input file
based on base metadata. - Includes error handling for incomplete or
invalid input files.

\-\--

\## Prerequisites \### Dependencies This script requires the following
Python libraries: - \`numpy\` - \`tqdm\`

You can install these dependencies using: \`\`\`bash pip install numpy
tqdm \`\`\`

\-\--

\## Usage 1. \*\*Setup Input and Output Directories\*\*  - Update the
paths in the script for \`dat_input_path\` and \`sigmf_output_path\` to
point to your \`.dat\` files directory and desired SigMF output
directory, respectively.

2\. \*\*Update Metadata\*\*  - Customize the \`base_metadata\`
dictionary with your recording setup details, such as sample rate,
hardware details, and experiment environment.

3\. \*\*Run the Script\*\*  - Execute the script from the command line
or an IDE: \`\`\`bash python sigmf_converter.py \`\`\`

\-\--

\## Input Requirements - The script processes \`.dat\` files containing
interleaved I/Q samples. - Files must be formatted in either \`float32\`
or \`float16\`. The script will attempt both formats if the first
attempt fails.

\-\--

\## Output For each \`.dat\` file: - A \`.bin\` file is created
containing the I/Q samples. - A \`.json\` file is created containing the
SigMF metadata.

Both files are saved to the directory specified in
\`sigmf_output_path\`.

\-\--

\## Example Metadata Structure The script dynamically updates the
following base metadata for each \`.dat\` file: \`\`\`json { \"global\":
{ \"core:datatype\": \"cf32_le\", \"core:sample_rate\": 23040000,
\"core:version\": \"0.0.1\", \"core:author\": \"ZTX\",
\"core:description\": \"IQ samples from the srsRAN OTA 5G testbed
setup.\" }, \"captures\": { \"core:center_frequency\": 3500000000,
\"core:sample_start\": 0 }, \"annotations\": { \"core:sample_start\": 0,
\"core:sample_count\": 0 } } \`\`\`

\-\--

\## Error Handling - \*\*Incomplete Files:\*\* Skips \`.dat\` files with
an odd number of samples (I/Q pairs must be even). - \*\*Missing
Files:\*\* Prints a warning if no \`.dat\` files are found in the input
directory.

\-\--

\## Example If the input directory contains: \`\`\`
/home/mohammed/ztxdata/iq_samples/file1.dat \`\`\` and the output
directory is set to: \`\`\` /home/mohammed/ztxdata/sigmf_files/ \`\`\`
The script will generate: \`\`\`
/home/mohammed/ztxdata/sigmf_files/file1.bin
/home/mohammed/ztxdata/sigmf_files/file1.json \`\`\`

\-\--

\## Troubleshooting - \*\*No Output Files:\*\* Ensure that the \`.dat\`
files are valid and correctly formatted. - \*\*Metadata Errors:\*\*
Verify the \`base_metadata\` dictionary for accuracy.

\-\--

\## License This script is provided under the MIT License.

Feel free to modify and adapt it for your use.
