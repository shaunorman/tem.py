import gc
import webrepl

# Used for debugging
import machine  # noqa

# import uos
# uos.dupterm(None, 1) # disable REPL on UART(0)

webrepl.start()
gc.collect()
