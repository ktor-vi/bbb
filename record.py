import time, sys
import urllib.request, urllib.error, urllib.parse
from urllib.request import Request, urlopen


url = "https://cdns-preview-a.dzcdn.net/stream/c-ab6dcd8be2dd2ad84ebe143045cc7c7b-3.mp3"
# url = "https://blinest.com/parties/quiz-general"
# url = "https://server.radiostreaming.com.ar/cp/widgets/player/single/?p=8066#"
# url = "https://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"

print(("Connecting to "+url))

# response = urllib.request.urlopen(url, timeout=10.0) - original one

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/6.0"
    timeout=10.0

opener = AppURLopener()
response = opener.open(url)


fname = "Sample"+str(time.process_time())[2:]+".mp3"
f = open(fname, 'wb')
block_size = 1024
print ("Recording roughly 10 seconds of audio Now - Please wait")
limit = 10
start = time.time()
while time.time() - start < limit:
    try:
        audio = response.read(block_size)
        if not audio:
            break
        f.write(audio)
        sys.stdout.write('.')
        sys.stdout.flush()
    except Exception as e:
        print(("Error "+str(e)))
f.close()
sys.stdout.flush()
print("")
print(("10 seconds from "+url+" have been recorded in "+fname))

#
# here run the finger print test to identify the audio recorded
# using the sample you have downloaded in the file "fname"
#
