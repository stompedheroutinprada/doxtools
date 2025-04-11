# Camera selector (view cameras)
import cv2

cameras = {
    ".fav 1": "http://72.43.190.171:83/mjpg/video.mjpg",
    ".fav 2": "http://74.142.49.38:8001/mjpg/video.mjpg",
    ".fav 3": "http://87.139.153.80:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".fav 4": "http://168.122.98.2:80/image?speed=0",
    ".fav 5": "http://121.58.129.215:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".fav 6": "http://106.157.4.56:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".fav 7": "http://66.27.116.187:80/mjpg/video.mjpg",
    ".house 1": "http://76.151.170.119:10001/src=%22cam_1.cgi%22",
    ".house 2": "http://73.111.173.193:80/mjpg/video.mjpg",
    ".house 3": "http://204.93.117.45:80/mjpg/video.mjpg",
    ".house 4": "http://166.156.253.4:80/mjpg/video.mjpg",
    ".house 5": "http://72.199.200.5:8080/src=%22cam_1.cgi%22",
    ".house 6": "http://75.149.26.30:1024/src=%22cam_1.cgi%22",
    ".hotel 1": "http://71.249.87.61:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".hotel 2": "http://108.41.24.124:80/mjpg/video.mjpg",
    ".hotel 3": "http://184.74.137.62:84/mjpg/video.mjpg",
    ".elevator 1": "http://72.43.190.171:83/mjpg/video.mjpg",
    ".store 1": "http://76.80.75.130:81/mjpg/video.mjpg",
    ".school 1": "http://131.95.3.178:80/mjpg/video.mjpg",
    ".topview 1": "http://208.76.201.130:80/mjpg/video.mjpg",
    ".topview 2": "http://217.91.145.152:80/mjpg/video.mjpg",
    ".topview 3": "http://80.147.196.243:8888/mjpg/video.mjpg",
    ".topview 4": "http://201.144.24.221:80/mjpg/video.mjpg",
    ".topview 5": "http://168.122.98.2:80/image?speed=0",
    ".topview 6": "http://24.97.151.11:80/mjpg/video.mjpg",
    ".topview 7": "http://118.21.67.254:80/mjpg/video.mjpg",
    ".topview 8": "http://202.213.110.70:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".court 1": "http://50.199.221.39:80/mjpg/video.mjpg",
    ".church 1": "http://74.142.49.38:8001/mjpg/video.mjpg",
    ".church 2": "http://74.142.49.38:8000/mjpg/video.mjpg",
    ".church 3": "http://70.90.194.90:8888/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".out 1": "http://114.179.127.11:8001/mjpg/video.mjpg",
    ".out 2": "http://87.139.153.80:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".out 3": "http://185.137.146.14:80/mjpg/video.mjpg",
    ".out 4": "http://80.66.36.54:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".out 5": "http://213.236.250.78:80/mjpg/video.mjpg",
    ".out 6:": "http://173.255.111.12:80/mjpg/video.mjpg",
    ".out 7": "http://121.58.129.215:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".out 8": "http://106.157.4.56:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".road 1": "http://76.190.79.50:80/mjpg/video.mjpg",
    ".road 2": "http://86.127.212.219:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".road 3": "http://87.139.9.247:80/mjpg/video.mjpg",
    ".road 4": "http://62.242.189.218:80/mjpg/video.mjpg",
    ".road 5": "http://208.193.47.61:80/mjpg/video.mjpg",
    ".road 6": "http://166.252.52.47:83/mjpg/video.mjpg",
    ".road 7": "http://72.24.198.180:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".road 8": "http://50.252.166.122:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".road 9": "http://166.154.166.8:80/mjpg/video.mjpg",
    ".road 10": "http://166.251.9.199:8081/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".road 11": "http://50.246.145.124:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".road 12": "http://124.155.113.18:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".street 1": "http://37.182.240.202:81/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".street 2": "http://129.125.136.20:80/mjpg/video.mjpg",
    ".street 3": "http://66.103.160.160:80/mjpg/video.mjpg",
    ".street 4": "http://108.30.103.58:8082/mjpg/video.mjpg",
    ".street 5": "http://47.44.156.124:8082/mjpg/video.mjpg",
    ".street 6": "http://72.43.190.171:81/mjpg/video.mjpg",
    ".street 7": "http://173.12.209.46:8090/mjpg/video.mjpg",
    ".street 8": "http://66.27.116.187:80/mjpg/video.mjpg",
    ".street 8": "http://206.72.28.209:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".street 9": "http://217.128.94.112:8082/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".work 1": "http://153.156.230.207:8084/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".work 2": "http://153.156.230.207:8081/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".work 3": "http://47.181.86.62:8082/mjpg/video.mjpg",
    ".work 4": "http://61.214.197.204:1024/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".work 5": "http://80.28.135.251:83/mjpg/video.mjpg",
    ".animal 1": "http://66.57.67.108:1024/mjpg/video.mjpg",
    ".animal 2": "http://72.253.153.216:81/mjpg/video.mjpg",
    ".animal 3": "http://76.174.92.213:81/mjpg/video.mjpg",
    ".billboard 1": "http://166.144.239.128:81/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".billboard 2": "http://162.191.224.89:81/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".billboard 3": "http://162.191.6.55:82/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".billboard 4": "http://162.191.12.147:81/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".billboard 5": "http://162.191.198.59:81/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER",
    ".billboard 6": "http://218.219.195.166:8081/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000",
    ".sea 1": "http://50.211.214.94:80/mjpg/video.mjpg",
    ".sea 2": "http://67.53.203.146:8084/mjpg/video.mjpg",
    ".sea 3": "http://71.181.7.91:80/mjpg/video.mjpg",
    ".sea 4": "http://205.215.255.11:80/mjpg/video.mjpg",
    ".gym 1": "http://104.8.103.170:80/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER"
    }

def cameraviewer(camera_id):
    url = cameras.get(camera_id)
    if not url:
        print(f"Camera '{camera_id} not found.")
        return
    
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Failed to connect to the camera stream.")
        return
    
    print(f"Streaming '{camera_id}'... Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.imshow(f"{camera_id} Stream", frame)

        if cv2.waitKey(25 if url.endswith(".mp4") else 1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
