import cv2
import config

def cascade_detect_img(test_img, cascade_data, scaleFactor, minNeighbors):
    img = cv2.imread(test_img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    robot_cascade = cv2.CascadeClassifier(cascade_data)
    robots = robot_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)

    for (x, y, w, h) in robots:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    # choose between showing and saving img result
    cv2.imshow(img)
    # cv2.imwrite('cascade_img_result', img)


def cascade_detect_video(vid_src, cascade_data, scaleFactor, minNeighbors):
    cap = cv2.VideoCapture(vid_src)
    robot_cascade = cv2.CascadeClassifier(cascade_data)

    if(cap.isOpened() == False):
        print('Error opening video file')
        return 
    
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_gray = cv2.cvtColor(frame, cv2.cvtColor_BGR2GRAY)
            robots = robot_cascade.detectMultiScale(frame_gray, scaleFactor, minNeighbors)

            for (x, y, w, h) in robots:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
            
            cv2.imshow('Detect', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        else:
            break
    
    cap.release()


if __name__ == '__main__':
    scale = 1.3
    min_neighbors = 5
    video = config.TEST_VIDEO
    cascade_data = config.TRAINING_DATA
    test_img = config.POS_SAMPLE
    if config.USING_VIDEO:
        cascade_detect_video(video, cascade_data, scale, min_neighbors)
    else:
        cascade_detect_img(test_img, cascade_data, scale, min_neighbors)

