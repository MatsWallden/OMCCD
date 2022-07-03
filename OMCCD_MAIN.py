# %%
# from serial_com.get_port_sequence import get_port_sequence
# from serial_com.get_serial_gwgds1072au import get_serial_gwgds1072au
# from serial_com.get_signal_scale_gwgds1072 import get_signal_scale_gwgds1072
# from serial_com.get_signal_packed_gwgds1072au import get_signal_packed_gwgds1072au
# from serial_com.get_signal_gwgds1072au import get_signal_gwgds1072au
# from serial_com.get_time_scale_acquisition_gwgds1072au import get_time_scale_acquisition_gwgds1072au
# #%%

# the_port_sequence=get_port_sequence()
# the_serial_osc=get_serial_gwgds1072au(a_port_sequence=the_port_sequence)

# # %%
# the_scale=get_signal_scale_gwgds1072(a_serial=the_serial_osc,a_channel_id="1")

# # %%

# the_signal_packed=get_signal_packed_gwgds1072au(a_serial=the_serial_osc,a_channel_id="1")

# the_signal=get_signal_gwgds1072au(a_signal_packed=the_signal_packed,a_scale=1.0)

# the_time_scale=get_time_scale_acquisition_gwgds1072au(a_signal_packed=the_signal_packed)


from SINEDEFINE.SINE_DEFINE_MAIN import do_sinedefine
import sys
sys.path.insert(1, "/home/pi/OMCCD/SINEDEFINE")

do_sinedefine()

# N = 1000 # number of data points
# t = np.linspace(0, 4*np.pi, N)
# f = 1.15247 # Optional!! Advised not to use
# data = the_signal # create artificial data with noise

# guess_mean = np.mean(data)
# guess_std = 3*np.std(data)/(2**0.5)/(2**0.5)
# guess_phase = 0
# guess_freq = 1
# guess_amp = 1

# # we'll use this to plot our first estimate. This might already be good enough for you
# data_first_guess = guess_std*np.sin(t+guess_phase) + guess_mean

# # Define the function to optimize, in this case, we want to minimize the difference
# # between the actual data and our "guessed" parameters
# optimize_func = lambda x: x[0]*np.sin(x[1]*t+x[2]) + x[3] - data
# est_amp, est_freq, est_phase, est_mean = leastsq(optimize_func, [guess_amp, guess_freq, guess_phase, guess_mean])[0]

# # recreate the fitted curve using the optimized parameters
# data_fit = est_amp*np.sin(est_freq*t+est_phase) + est_mean

# # recreate the fitted curve using the optimized parameters

# fine_t = np.arange(0,max(t),0.1)
# data_fit=est_amp*np.sin(est_freq*fine_t+est_phase)+est_mean

# plt.plot(t, data, '.')
# plt.plot(t, data_first_guess, label='first guess')
# plt.plot(fine_t, data_fit, label='after fitting')
# plt.legend()
# plt.show()
