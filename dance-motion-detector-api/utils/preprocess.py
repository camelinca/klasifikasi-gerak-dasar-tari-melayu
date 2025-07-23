import cv2
import numpy as np

def preprocess_video(video_path, num_frames=30, frame_size=224):
    cap = cv2.VideoCapture(video_path)
    frames = []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_step = max(total_frames // num_frames, 1)

    frame_count = 0
    while len(frames) < num_frames:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_step == 0:
            frame = cv2.resize(frame, (frame_size, frame_size))
            frame = frame.astype('float32') / 255.0
            frames.append(frame)

        frame_count += 1

    cap.release()

    # ❗ Ganti padding menggunakan frame terakhir (bukan zeros)
    while len(frames) < num_frames:
        frames.append(frames[-1])

    return np.expand_dims(np.array(frames, dtype='float32'), axis=0)
