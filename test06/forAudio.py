# import pyaudio
# import wave
#
# #定义音频数据参数
# CHUNK = 1024    #块
# FORMAT = pyaudio.paInt16
# CHANNELS = 2   #渠道
# RATE = 44100   #率
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "Recording.wav"
#
# p = pyaudio.PyAudio()
#
# # 打开数据流
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
# print("& Start Recording & :")
#
# frames = []
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("#### done recording ####")
#
# # 停止数据流
# stream.stop_stream()
# stream.close()
#
# # 关闭 PyAudio
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

import pyaudio
import wave
import time
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output1.wav"

p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

time_count = 0
def callback(in_data, frame_count, time_info, status):
    print("~~~~~~~~~~~")
    wf.writeframes(in_data)
    if(time_count < 10):
        return (in_data, pyaudio.paContinue)
    else:
        return (in_data, pyaudio.paComplete)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                stream_callback=callback)

stream.start_stream()
print("* recording")
while stream.is_active():
    time.sleep(1)
    time_count += 1

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
print("* recording done!")


