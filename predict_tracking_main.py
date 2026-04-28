from ultralytics import YOLO
import cv2
import time

if __name__ == "__main__":
    # model path
    model_path = "model/top-down-head.pt"
    track_file = "model/custom_botsort.yaml"
    # load model
    model = YOLO(model_path)

    video_path = 'data/video.mp4'
    # read video
    cap = cv2.VideoCapture(video_path)
    video_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    all_frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    scale_rate = 3
    rw = int(video_w/scale_rate)
    rh = int(video_h/scale_rate)
    while cap.isOpened():
        _, frame = cap.read()
        img = cv2.resize(frame,(rw, rh))
        start = time.time()
        results = model.track(img, conf=0.80, # confidence
                            verbose=False, save=False, persist=True,
                            tracker=track_file)
        time_taken = time.time() - start
        show_fps = int(1. / time_taken)
        boxes = results[0].boxes.xywh.cpu()
        rect_boxes = results[0].boxes.xyxy.cpu()
        if results[0].boxes.id is not None:
            track_ids = results[0].boxes.id.int().cpu().tolist()
            for box, rect_box, track_id in zip(boxes, rect_boxes, track_ids):
                xmin, ymin, xmax, ymax = rect_box
                # draw result
                cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 255, 187), thickness=2)
                cv2.putText(img, str(track_id), (int(xmin), int(ymin)), cv2.FONT_HERSHEY_TRIPLEX, 0.3, (98, 227, 97), 1)
        cv2.putText(img, "FPS: " + str(show_fps), 
                    (10, 20), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (80, 21, 128), 1, cv2.LINE_AA)
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()

