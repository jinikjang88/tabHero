import cv2
import socket
import pickle
import struct

# 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('127.0.0.1', 8888))

# 비디오 스트리밍 수신 및 표시
while True:
    data, addr = client_socket.recvfrom(65535)

    frame = pickle.loads(data)
    cv2.imshow("Video", frame)

    # 'q' 키를 누르면 비디오 스트리밍 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 클라이언트 소켓 종료
client_socket.close()
cv2.destroyAllWindows()