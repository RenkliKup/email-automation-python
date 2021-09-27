from interface import Interface
import threading
s=Interface()

main=threading.Thread(target=s.mailFrame())
main.start()
