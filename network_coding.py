
import numpy as np

class NetworkCoding:
    def __init__(self, source_data):
        self.source_data = source_data
        self.encoded_data = None

    def encode(self):
        # 符号化の例として、単純なXORを使用
        self.encoded_data = np.bitwise_xor.reduce(self.source_data, axis=0)

    def decode(self, received_data):
        # 符号化データと受信データをXORして元のデータを復元
        return np.bitwise_xor(received_data, self.encoded_data)

# 使用例
if __name__ == "__main__":
    source_data = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 0]])
    nc = NetworkCoding(source_data)
    nc.encode()
    print("Encoded Data:", nc.encoded_data)

    received_data = np.array([1, 1, 1])
    decoded_data = nc.decode(received_data)
    print("Decoded Data:", decoded_data)