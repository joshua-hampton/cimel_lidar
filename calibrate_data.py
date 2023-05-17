import numpy as np


def calibrate_data(data_dict, metadata_dict):

    channels = ['1', '2', '11']
    bg_low_gate = 1500
    bg_high_gate = 1600

    for channel in channels:
        total_profiles = np.size(data_dict[channel]['DP']['data'][:, 0])
        for profile in range(total_profiles):
            print(profile)
            background = np.mean(data_dict[channel]['DP']['data'][profile, bg_low_gate:bg_high_gate])
            data_dict[channel]['DP']['data'][profile, :] = data_dict[channel]['DP']['data'][profile, :] - background

    return data_dict, metadata_dict
