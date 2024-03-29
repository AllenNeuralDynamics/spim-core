from pathlib import Path
from spim_core.processes.data_transfer import DataTransfer

if __name__ == "__main__":

    source = Path(r'C:\test_dispim\tile_X_0001_Y_0001_Z_0000_cam0.tiff')
    dest = Path(r'Y:\test_dispim\test-ID_2023_02_28\micr\tile_X_0001_Y_0001_Z_0000_cam0.tiff')
    transfer = DataTransfer(source, dest)
    transfer.run()