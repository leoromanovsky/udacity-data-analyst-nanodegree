import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data.

    You will want to take the means and run the Mann Whitney U-test on the
    ENTRIESn_hourly column in the turnstile_weather dataframe.

    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain

    You should feel free to use scipy's Mann-Whitney implementation, and you
    might also find it useful to use numpy's mean function.

    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html

    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    with_rain = turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly']
    without_rain = turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']

    with_rain_mean = with_rain.mean()
    without_rain_mean = without_rain.mean()

    r = scipy.stats.mannwhitneyu(with_rain.values, without_rain.values)

    return with_rain_mean, without_rain_mean, r[0], r[1]
