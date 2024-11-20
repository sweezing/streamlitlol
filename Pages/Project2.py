import streamlit as st
import cv2
import tempfile
import numpy as np
from pathlib import Path
from yt_dlp import YoutubeDL
from streamlit_webrtc import webrtc_streamer, WebRtcMode

class Project2:
    def __init__(self):
        pass

    def app(self):
        st.title("we are gonna be streamers, gys!")

        source_option = st.selectbox(
            "Pick up source of the video stream",
            ("mobila", "yt link", "local files", "WEB camera", "RTSP")
        )

        video_url = None
        img_file = None

        if source_option == "mobila" :
            img_file = st.camera_input('take a photo')

        elif source_option == "yt link":
            youtube_url = st.text_input("puta link")
            if youtube_url:
                with st.spinner("videva uploading"):
                    try:
                        ydl_opts = {"format": "best[ext=mp4]/best", "noplaylist": True}
                        with YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(youtube_url, download=False)
                            video_url = info_dict.get("url", None)
                    except Exception as e:
                        st.error(f"there is some problems, bruh: {e}")

                if video_url:
                    st.video(video_url)

        elif source_option == "local files":

            video_file = st.file_uploader("upload videva", type=["mov", "avi", "mp4"])
            if video_file:
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=Path(video_file.name).suffix)
                temp_file.write(video_file.read())
                video_url = temp_file.name
                st.video(video_url)

        elif source_option == "WEB camera":
            st.write("launching the webcam...")
            webrtc_streamer(key="webcam", mode=WebRtcMode.SENDRECV)

        elif source_option == "RTSP":
            rtsp_url = st.text_input("Put in an RTSP link")
            if rtsp_url:
                video_url = rtsp_url

        run_button = st.button("RRUUUUNNN!!!")
        frame_place = st.empty()  # Placeholder for video frames

        if source_option == "mobila" and img_file is not None:
            file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
            frame = cv2.imdecode(file_bytes, flags=1)
            st.image(frame, channels="BGR")

        elif run_button and video_url is not None and source_option in ["local file", "RTSP"]:
            self.cap = cv2.VideoCapture(video_url)

            if not self.cap.isOpened():
                st.error("Error")
            else:
                stop_button = st.button("Stop!")

                while self.cap.isOpened() and not stop_button:
                    ret, frame = self.cap.read()
                    if not ret:
                        st.write('acces is denied')
                        break

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_place.image(frame, channels="RGB")

                    if stop_button:
                        break

                    self.cap.release()
                    cv2.destroyAllWindows()

            