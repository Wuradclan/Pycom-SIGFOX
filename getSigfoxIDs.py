from network import Sigfox
import binascii
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2)
print(binascii.hexlify(sigfox.id()))
print(binascii.hexlify(sigfox.pac()))
