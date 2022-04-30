# GNU-Radio-Projects
Projects using GNU Radio with SDRs like USRP X310, USRP B210, LimeSDR USB, LimeSDR Mini and ADALM Pluto SDR.  
I mainly use GNU Radio 3.7 version and hence the instructions would be for the same version.

## GNU Radio
GNU Radio is a software development toolkit to work with software-defined radios like USRP, Lime SDR, Pluto SDR etc.  
Written below is an installation guide for installing GNU Radio (GNU Radio Companion software) and additional suites for different SDRs.

### GNU Radio 3.7 installation

To access the 3.7 released version (legacy), add the gnuradio/gnuradio-releases-3.7 ppa (removing other gnuradio ppas if already configured)

`sudo add-apt-repository ppa:gnuradio/gnuradio-releases-3.7`  
_Note:_ For a different version, change the version number

* Update the apt sources    
`sudo apt-get update`  
* Install gnuradio
`sudo apt install gnuradio`  
_Note:_ This includes USRP (UHD) hardware options.
* Launch GNU Radio Companion using    
`gnuradio-companion`

Install some dependencies for installing other modules:  
`sudo apt install git cmake g++ libboost-all-dev libgmp-dev swig python3-numpy python3-mako python3-sphinx python3-lxml doxygen libfftw3-dev libsdl1.2-dev libgsl-dev libqwt-qt5-dev libqt5opengl5-dev python3-pyqt5 liblog4cpp5-dev libzmq3-dev python3-yaml python3-click python3-click-plugins python3-zmq python3-scipy python3-pip python3-gi-cairo`


### Installing LimeSuite
To use LimeSDR USB, Lime SDR Mini an similar devices, LimeSuite should be added to GNU Radio.  

* cd to home or any directory of your choice. Then enter the following commands:  
`sudo add-apt-repository -y ppa:myriadrf/drivers`  
`sudo apt-get update`  
`sudo apt-get install limesuite liblimesuite-dev limesuite-udev limesuite-images`  
`sudo apt-get install soapysdr-tools soapysdr-module-lms7`

* Download gr-limesdr plugin by typing:  
`git clone https://github.com/myriadrf/gr-limesdr`

* Building and installing gr-limesdr from source:  
To build and install for GNURadio3.7 enter the following commands in terminal:  
    ```
    cd gr-limesdr
    mkdir build
    cd build
    cmake ..
    make
    sudo make install
    sudo ldconfig
    ```

### Installing Pluto SDR
 To use ADALM Pluto SDR which is an IIO based device within GNU Radio, the support is currently provided in an out-of-tree (OOT) module called gr-iio.  
* Download and build libiio. cd to home or any directory of your choice. Then enter the following commands:  
`sudo apt install libxml2 libxml2-dev bison flex cmake git libaio-dev libboost-all-dev libusb-1.0-0-dev libavahi-common-dev libavahi-client-dev`    
    ```
    git clone https://github.com/analogdevicesinc/libiio.git
    cd libiio
    cmake .
    make 
    sudo make install
    cd ..
    ```
* Download and build libad9361-iio  
    ```
    git clone https://github.com/analogdevicesinc/libad9361-iio.git
    cd libad9361-iio
    cmake .
    make 
    sudo make install
    cd ..
    ```
* Finally install gr-iio whih includes Pluto SDR
    ```
    git clone https://github.com/analogdevicesinc/gr-iio.git
    cd gr-iio
    cmake .
    make 
    sudo make install
    cd ..
    sudo ldconfig
    ```