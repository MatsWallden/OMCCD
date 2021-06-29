#%%
import time
from serial_com.get_port_sequence import get_port_sequence
from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
from serial_com.get_signal_scale_gwgds1072 import get_signal_scale_gwgds1072
from serial_com.get_signal_packed_gwgds1072au import get_signal_packed_gwgds1072au
from serial_com.get_signal_gwgds1072au import get_signal_gwgds1072au
from serial_com.get_time_scale_acquisition_gwgds1072au import get_time_scale_acquisition_gwgds1072au
#%%
the_file_name="./store_buffer.txt"

the_file=open(the_file_name,'a')

the_port_sequence=get_port_sequence()

the_serial_osc=get_serial_gwgds1072au(a_port_sequence=the_port_sequence)
# %%
#the_scale=get_signal_scale_gwgds1072(a_serial=the_serial_osc,a_channel_id="1")
# %%
# %%
    
#the_signal=get_signal_gwgds1072au(a_signal_packed=the_signal_packed,a_scale=1.0)
# %%
#the_time_scale=get_time_scale_acquisition_gwgds1072au(a_signal_packed=the_signal_packed)

#the_signal_packed=get_signal_packed_gwgds1072au(a_serial=the_serial_osc,a_channel_id="1")

#the_file.write(str(the_signal_packed))

#%%

iter_max=10
iter=0

while True and not iter >=iter_max :

    the_scale=get_signal_scale_gwgds1072(a_serial=the_serial_osc,a_channel_id="1")
    the_signal_packed=get_signal_packed_gwgds1072au(a_serial=the_serial_osc,a_channel_id="1")
    #the_time_scale=get_time_scale_acquisition_gwgds1072au(a_signal_packed=the_signal_packed)
    the_signal=get_signal_gwgds1072au(a_signal_packed=the_signal_packed,a_scale=the_scale)
    the_file.write(str(time.time()))
    the_file.write(str(the_signal))
    print(the_signal)
    iter+=1

# %%
