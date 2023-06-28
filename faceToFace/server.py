import cv2
import socket
import pickle
import struct

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 8888))

# 클라이언트 연결 대기
print("서버가 시작되었습니다. 클라이언트 연결을 기다리는 중...")

while True:
    data, addr = server_socket.recvfrom(65535)

    # 비디오 스트리밍 시작
    capture = cv2.VideoCapture(0)

    while True:
        # 프레임 읽기
        ret, frame = capture.read()

        # 프레임을 직렬화하여 전송
        data = pickle.dumps(frame)
        server_socket.sendto(data, addr)

        # 'q' 키를 누르면 비디오 스트리밍 종료
        if cv2.waitKey(1) == ord('q'):
            break

    # 클라이언트 소켓 종료
    capture.release()

# 서버 소켓 종료
server_socket.close()