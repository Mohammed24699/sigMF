import numpy as np
import os
import glob
import json
from tqdm import tqdm

def convert_dat_to_sigmf(dat_path, sigmf_path, metadata, dtype='float32'):
    """
    Converts .dat files containing IQ samples to SigMF format.

    Parameters:
        dat_path (str): Directory containing .dat files.
        sigmf_path (str): Directory to save SigMF .bin and .json files.
        metadata (dict): Base metadata for SigMF files.
        dtype (str): Data type of IQ samples in .dat files ('float16' or 'float32').
    """
    # Ensure the output directory exists
    if not os.path.isdir(sigmf_path):
        os.mkdir(sigmf_path)

    # Get all .dat files in the input directory
    dat_files = glob.glob(os.path.join(dat_path, "*.dat"))

    if not dat_files:
        print("No .dat files found in the specified directory.")
        return

    for dat_file in tqdm(dat_files):
        try:
            # Read the .dat file
            iq_samples = np.fromfile(dat_file, dtype=dtype)

            # Ensure the number of samples is even (I/Q interleaved)
            if len(iq_samples) % 2 != 0:
                raise ValueError(f"File {dat_file} contains an odd number of samples, indicating incomplete data.")

            # Save binary IQ samples as a .bin file
            bin_filename = os.path.basename(dat_file).replace('.dat', '.bin')
            bin_filepath = os.path.join(sigmf_path, bin_filename)
            iq_samples.tofile(bin_filepath)

            # Prepare SigMF metadata
            file_metadata = metadata.copy()
            file_metadata['global']['core:description'] = f"SigMF file generated from {os.path.basename(dat_file)}"
            file_metadata['annotations']['core:sample_count'] = len(iq_samples) // 2  # I/Q pairs
            file_metadata['captures']['core:file_name'] = bin_filename

            # Save metadata as a .json file
            json_filename = os.path.basename(dat_file).replace('.dat', '.json')
            json_filepath = os.path.join(sigmf_path, json_filename)
            with open(json_filepath, 'w') as json_file:
                json.dump(file_metadata, json_file, indent=4)

            print(f"Converted {dat_file} to SigMF format.")

        except Exception as e:
            print(f"Error processing {dat_file}: {e}")


# Example usage
if __name__ == "__main__":
    dat_input_path = "/home/mohammed/ztxdata/iq_samples"  # Replace with your .dat files directory
    sigmf_output_path = "/home/mohammed/ztxdata/sigmf_files"  # Replace with your desired SigMF output directory

    # Base metadata for SigMF files
    base_metadata = {
        'global': {                      # Contains how the signals were recorded and by whom
            'core:datatype': 'cf32_le',  # Use 'cf16_le' for float16 samples
            'core:sample_rate': 23.04e6,  # Replace with your actual sample rate
            'core:version': '0.0.1',
            'core:author': 'ZTX',
            'core:description': 'IQ samples from the srsRAN OTA 5G testbed setup.',
            'hardware': {
                'usrp_model': 'USRP B210',
                'frequency_range': '70 MHz to 6 GHz',
                #'attenuator': '20 dB inline attenuator',
                'clock_source': 'CDA-2990 external clock'
            },
            'software': {
                'srsran_version': 'v24.04',
                'open5gs_version': 'v2.7.0',
                'uhd_version': 'Latest compatible',
                #'libzmq_version': 'Latest compatible',
                #'czmq_version': 'Latest compatible',
                #'iperf3_version': 'Latest compatible',
                'operating_system': 'Ubuntu 22.04',
                'computer_specs': {
                    'ue1': {'cpu': 'AMD Ryzen 7 7745HX', 'ram': '16GB'},
                    'ue2': {'cpu': 'Intel Core i9-11900K', 'ram': '16GB'},
                    'gnb': {'cpu': 'Intel Core i9-11900K', 'ram': '16GB'}
                }
            }
        },
        'captures': {
            'core:sample_start': 0,
            'core:center_frequency': 3500000000,  # Set center frequency to 3.5 GHz
            'core:file_name': '',  # This will be dynamically updated for each file
            'measurement_setup': {
                'distance_from_source': '1 meter',
                'environment': 'Open Air Experiment',
                'source_signal': 'USRP Tx using srsRAN',
                'subcarrier_spacing': '15 kHz',
                'bandwidth': '10 MHz',
                'gain_settings': {
                    'tx_gain': 60,
                    'rx_gain': 40
                }
            }
        },
        'annotations': {
            'core:sample_start': 0,
            'core:sample_count': 0,  # This will be dynamically updated for each file
            'core:environment': 'Laboratory setup for OTA 5G testbed testing',
            'notes': 'Collected from srsRAN 5G OTA testbed using Open5GS and USRP B210.'
        }
    }

    # Attempt conversion with float32
    print("Attempting conversion with float32 data type...")
    convert_dat_to_sigmf(dat_input_path, sigmf_output_path, base_metadata, dtype='float32')

    # If float32 fails, try float16
    if not glob.glob(os.path.join(sigmf_output_path, "*.bin")):
        print("No valid output files with float32. Retrying with float16...")
        base_metadata['global']['core:datatype'] = 'cf16_le'  # Update metadata for float16
        convert_dat_to_sigmf(dat_input_path, sigmf_output_path, base_metadata, dtype='float16')

