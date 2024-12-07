
# SigMF Converter

## Overview
This Python script converts `.dat` files containing IQ samples into the [SigMF](https://github.com/gnuradio/sigmf) format, generating `.bin` and `.json` files. It is designed for processing IQ data collected in radio frequency experiments, such as those involving SDRs (Software-Defined Radios).

---

## Features
- Converts `.dat` files to SigMF-compliant `.bin` and `.json` files.  
- Supports interleaved I/Q samples in `float32` or `float16` format.  
- Dynamically generates metadata for each input file based on customizable base metadata.  
- Includes error handling for incomplete or invalid input files.

---

## Prerequisites

### Dependencies
This script requires the following Python libraries:
- `numpy`
- `tqdm`

You can install these dependencies using:
```bash
pip install numpy tqdm
```

---

## Usage

### 1. Setup Input and Output Directories
Update the paths in the script:
- `dat_input_path`: Path to your `.dat` files directory.
- `sigmf_output_path`: Directory where the SigMF files will be saved.

### 2. Customize Metadata
Edit the `base_metadata` dictionary in the script to reflect your experiment setup, such as:
- Sample rate
- Hardware details
- Test environment

### 3. Run the Script
Execute the script with the following command:
```bash
python sigmf_converter.py
```

---

## Input Requirements
- Input files must be `.dat` files containing interleaved I/Q samples.
- Supported data types are `float32` and `float16`.

---

## Output
For each `.dat` file:
- A `.bin` file containing I/Q samples.
- A `.json` file with metadata in SigMF format.

These files are saved in the directory specified by `sigmf_output_path`.

---

## Example

### Input Directory
```plaintext
/home/mohammed/ztxdata/iq_samples/
```

### Output Directory
```plaintext
/home/mohammed/ztxdata/sigmf_files/
```

### Generated Files
For a file named `example.dat`, the output will include:
```plaintext
/home/mohammed/ztxdata/sigmf_files/example.bin
/home/mohammed/ztxdata/sigmf_files/example.json
```

---

## Troubleshooting

### No Output Files
- Verify that the `.dat` files are valid and properly formatted.
- Ensure the files contain interleaved I/Q samples in `float32` or `float16` format.

### Metadata Issues
- Check the `base_metadata` dictionary and update it to match your experimental setup.

---

## Metadata Example
Below is an example of the base metadata structure used in the script:
```json
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
```

---

## License
This project is licensed under the MIT License. Feel free to modify and adapt it to your needs.
