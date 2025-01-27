# Negative Selection Algorithm for DDoS attack detection
* This solution uses the Negative Selection Algorithm to detect DDoS attacks on NTP, DNS and UDP protocols.
* This project uses CMake for its configuration.

# Instructions
It is recommended to create a specific directory for your build.
```
$ mkdir build
$ cd build
```
Once there, you must execute one of these two commands:
* To set up a build environment for ```Intel``` compiler:
```
$ cmake ..
```
* To let the setup script decide the best environment for you:
```
$ cmake .. -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```
With one of these two operations done, the next step now is to generate the binaries:
```
$ make
```
Done. Binaries should now be generated in the folders specified by ```Makefile```

To run, given this example setup, just insert any of these commands in the data folder, in any order:
```
$ OMP_PROC_BIND=true OMP_NUM_THREADS=1 ../build/nsa dataset.conf
```
To get better results, run OMP_NUM_THREADS with more threads.

# Citation
To quote the project, use one of the ways below:
```
J. C. de Lima Costa, L. N. de Castro and C. de Paula Bianchini, "Sensitivity Analysis of the Negative Selection Algorithm Applied to Anomalies Identification in Builds," 2019 XLV Latin American Computing Conference (CLEI), Panama, Panama, 2019, pp. 1-6, doi: 10.1109/CLEI47609.2019.235087.
```

```
@INPROCEEDINGS{9073958,
author={J. C. {de Lima Costa} and L. N. {de Castro} and C. {de Paula Bianchini}},
booktitle={2019 XLV Latin American Computing Conference (CLEI)},
title={Sensitivity Analysis of the Negative Selection Algorithm Applied to Anomalies Identification in Builds},
year={2019},
volume={},
number={},
pages={1-6},}
```
https://doi.org/10.1109/CLEI47609.2019.235087

# Original repo
Check the original project @ https://github.com/hpc-fci-mackenzie/FlakyBuild