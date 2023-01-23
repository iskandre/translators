import time
import translators as ts

start_time = time.time()
ts.translate_text('hello','google','en','fr',is_async = True)
time0 = time.time()
print('took %s'%(time0 - start_time))
ts.translate_text('how are you?','google','en','fr',is_async = True)
print('took %s'%(time.time() - time0))