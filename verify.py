import board
import busio
from adafruit_pn532.i2c import PN532_I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532= PN532_I2C(i2c)
ic, ver, rev, support = pn532.firmware_version

print(f&quot;successs! Found PN532 with Fireware: {ver}.{rev}&quot;)
print(&quot;Place your blue fob or white card on the red board...&quot;)
while True:
uid= pn532.read_passive_target(timeout=0.5)
if uid is not None:
print(f&quot;Found Tag! ID is : {[hex(i) for i in uid]}&quot;)
