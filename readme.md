Automated non-ocular artefact removal (ANOAR) 2016, Jeff Hanna
Module works with MNE Python. Globally bad channels are removed by 
calculating a distance-weighted absolute correlation matrix, and identifying 
those that correlate poorly with their neighbours. As for artefact rejection,
the sum of squared deviance from the ERP average is calculated for each trial,
individually for each channel. This results in a matrix of noise measurements,
TxC, where T is the number of trials, and C is the number of channels. Noise
levels laying outside a given threshold of a probability distribution are marked
as bad. Because the values describe both trial and channel, individual channels
can be marked as bad without throwing out the entire trial. The values of these
channels are replaced by interpolation within the trial alone. Trials which have
too many bad channels are marked as bad entirely.
The critical manipulation here that prevents the removal of ocular artefacts 
is that the correlation with the EOG channels for each trial-channel are calculated,
and the noise value for that trial-channel is multiplied by 1-r² from the correlations 
with other channels, this is effect removes the portion of the noise caused by
parts of the signal that correlate with EOG (or any other recorded source of
noise, EKG, etc).
