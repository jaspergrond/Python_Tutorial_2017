import numpy as np

def findpeaks(data, spacing=1, limit=None):
    """Finds peaks in `data` which are of `spacing` width and >=`limit`.
    :param data: values
    :param spacing: minimum spacing to the next peak (should be 1 or more)
    :param limit: peaks should have value greater or equal
    :return:
    """
    len = data.size
    x = np.zeros(len+2*spacing)
    x[:spacing] = data[0]-1.e-6
    x[-spacing:] = data[-1]-1.e-6
    x[spacing:spacing+len] = data
    peak_candidate = np.zeros(len)
    peak_candidate[:] = True
    for s in range(spacing):
        start = spacing - s - 1
        h_b = x[start : start + len]  # before
        start = spacing
        h_c = x[start : start + len]  # central
        start = spacing + s + 1
        h_a = x[start : start + len]  # after
        peak_candidate = np.logical_and(peak_candidate, np.logical_and(h_c > h_b, h_c > h_a))

    ind = np.argwhere(peak_candidate)
    ind = ind.reshape(ind.size)
    if limit is not None:
        ind = ind[data[ind] > limit]
    return ind

def fmtUncty(value, error, LaTeX = False):
	"""Round and format, in plain text or "LaTeX", the uncertainty on the "value" based on most significant digit in the "error".
	:param value: value to be formatted
	:param error: error of said value, also to be formatted
	:param LaTeX: turns LaTeX formatting on (True) and off (False)
	:return:
	"""
    	power = np.log10(np.fabs(error))
    	if power < 0:
    	    rndErr = np.round(error,int(-1*power+1))
    	    rndVal = np.round(value,int(-1*power+1))
    	else:
    	    rndErr = np.round(error, int(-1*power))
    	    rndVal = np.round(value,int(-1*power))
        
    	if LaTeX:
    	    return str(rndVal) + ' $\pm$ ' + str(rndErr)
    	else:
    	    return str(rndVal) + ' +/- ' + str(rndErr)	
