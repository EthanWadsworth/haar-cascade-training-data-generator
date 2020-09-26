# Shared configuration constants
POS_SAMPLE = '<path_to_positive_sample_img>'   # path to the positive image sample

# Configuration constants for video_frame_reader.py
FRAME_SKIP = 10     # Number of frames to skip in-between each saved frame
MAX_FRAMES = 2000   # maximum number of frames to save
SAVE_DIR = ''       # name of directory to save video frames
VIDEO_PATH = '<path_to_video_src>'     # Path to video file

# Configuration constants for cascade_training_data.py
NEG_IMG_DIR_PATH = 'seg_train'   # Path to negative image samples
CASCADE_NEG_OUT_DIR = 'neg_cascade_training_imgs'  # Path to negative image output directory

# Configuration constants for cascades.py
TEST_VIDEO = ''  # path to video file to test cascade training results
TRAINING_DATA = 'data/cascade.xml'  # path to created cascade training data
USING_VIDEO = False  # set to true if a video source is being used to visualize cascade results
