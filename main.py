from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import random, os

os.makedirs('samples', exist_ok=True)
os.makedirs('result', exist_ok=True)

string = '안녕! 나는 귀염둥이 숟가락 스푼이야! 오늘은 이 에버랜드에 유명한 음식축제 ‘스프링 온 스푼’ 을 한다고 해서 초청 받았어 내 이름이 들어가서라나 뭐라나?! 특별히 나 스푼이가 에버랜드에 왔으니 내 위에 봄을 얹어보러 가자!'
'
random_factor = 0.35

result_sound = None

for i, letter in enumerate(string):
    if letter == ' ':
        new_sound = letter_sound._spawn(b'\x00' * (44100 // 3), overrides={'frame_rate': 44100})
        new_sound = new_sound.set_frame_rate(44100)
    else:
        if not os.path.isfile('samples/%s.mp3' % letter):
            tts = gTTS(letter, lang='ko')
            tts.save('samples/%s.mp3' % letter)

        letter_sound = AudioSegment.from_mp3('samples/%s.mp3' % letter)

        raw = letter_sound.raw_data[5000:-5000]

        octaves = 2.0 + random.random() * random_factor
        frame_rate = int(letter_sound.frame_rate * (2.0 ** octaves))
        print('%s - octaves: %.2f, fr: %.d' % (letter, octaves, frame_rate))

        new_sound = letter_sound._spawn(raw, overrides={'frame_rate': frame_rate})
        new_sound = new_sound.set_frame_rate(44100)

    result_sound = new_sound if result_sound is None else result_sound + new_sound

play(result_sound)
result_sound.export('result/%s.mp3' % string, format='mp3')
