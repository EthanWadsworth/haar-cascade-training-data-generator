import cv2
import os
import config # file for project globals

def save_vid_frames(skip_interval, dirName, videoPath, max_frames=2000):
    """
    Takes video data and saves frames to chosen output directory

    :type skip_interval: int
    :param skip_interval: Amount of frames to skip between each image to be
    saved

    :type dirName: str
    :param dirName: Path in which video frames will be saved

    :type videoPath: str
    :param videoPath: Path to video file

    :type max_frames: int
    :param max_frames: maximum number of frames to save

    rtype: None
    """
    accum = 0
    frame_count = 0
    cap = cv2.VideoCapture(videoPath)
    if (os.path.exists(dirName) == False):
        os.mkdir(dirName)

    if cap.isOpened() == False:
        print("Error opening video file")
        return
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            accum+=1
            if accum % skip_interval == 0 and frame_count < max_frames:
                # switch between show frames and write to output_dir
                # cv2.imwrite(dirName + '/frame' + str(frame_count), frame) 
                cv2.imshow('Frame' + str(frame_count), frame)
                frame_count+=1

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break 
        else:
            break
    
    cap.release()

if __name__ == '__main__':
    # test params
    frame_skip = config.FRAME_SKIP
    save_dir = config.SAVE_DIR
    video_file = config.VIDEO_PATH
    max_saved_frames = config.MAX_FRAMES

    save_vid_frames(frame_skip, save_dir, video_file, max_saved_frames)