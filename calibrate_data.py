import numpy as np


def calibrate_data(data_dict, metadata_dict):

    channels = ['1', '2', '11']

    for channel in channels:
        delta_range = float(data_dict[channel]['one_door_range_metres'])
        offset_range = float(data_dict[channel]['offset_range'])
        total_ranges = np.size(data_dict[channel]['DP']['data'][0, :])
        data_dict[channel]['lidar_range'] = np.arange(total_ranges) * delta_range + offset_range

    return data_dict, metadata_dict
