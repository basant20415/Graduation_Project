# Yocto-Image  #

This repository contains code and instructions for building a custom Linux distribution using Yocto Project. The resulting image can be used on embedded devices such as Raspberry Pi 5. It contains recipes for computer vision application like damage detection and C++ Applications. Also, it contains some recipes to install some dependecies that is required by these applications.

## 📌 Pre-Development Stage :

- 1️⃣ Prepare Host Machine with Hardware and Software Requirements: 🔗 (https://docs.yoctoproject.org/ref-manual/system-requirements.html )

- 2️⃣ Choose YOCTO Realese : 🔗 (https://wiki.yoctoproject.org/wiki/Releases )
  
  Release choice decision --> Kirksone ✅
  
   1- Long term support ( request for help for non-common issue

   2- Old since 2022 so it used in development ( search for common issues)

- 3️⃣ Clone Pokey: 🔗(https://github.com/yoctoproject/poky)
  
  ```git clone https://github.com/yoctoproject/poky.git```
  
  ```cd poky```
  
  ```git checkout kirkstone```
  
  ## 📌 Development Stage :

  1️⃣ source "oe-init-build-env" script
 
    ```source oe-init-build-env Graduation_rpi5 ```

  2️⃣ Start integration needed Applications and Packages using Bottom-Up approach:

  ![image](https://github.com/user-attachments/assets/36ca6c7f-c206-46f8-8a98-c9b574222b69)

   
   ## -- ⚙️ Raspberry Pi Board support (BSP layer) --
  
            ``` cd ~/poky ```
  
            ``` git clone -b kirkstone git://git.yoctoproject.org/meta-raspberrypi ``` (this link from 🔗 https://layers.openembedded.org/layerindex/branch/kirkstone/layers/)

            ``` cd Graduation_rpi5 ```

            ``` bitbake-layers add-layer ../meta-raspberrypi ```
  
      📝 Edit Graduation-rpi5/conf/local.conf :

           1- specify machine 

            ``` MACHINE ??= "raspberrypi5" ```

          2- YOCTO Optimization

           📌 make downloads and state-cache shared between different images :
 
              ``` DL_DIR ?= "${TOPDIR}/../shared_yocto_space/downloads" ```

              ``` SSTATE_DIR ?= "${TOPDIR}/../shared_yocto_space/state-cache" ```
  
           📌 bitbake use max.4 Cores to run 4 tasks in same time but not related to each other
  
               ``` BB_NUMBER_THREADS="4" ```

           📌 bitbake use 4 cores when compile to speed up compilation process
  
               ```  PARALLEL_MAKE="-j 4" ```

   ## -- ⚙️ Distribution ( Distro layer ) --

    1- Follow structure of distribution layer (meta-grad-distro/conf/distro/grad.conf)

          Configuration File Structure 📃:
  
              - Distribution Information
  
              - SDK Information
  
              - Distribution Featrures :
  
                    DISTRO_DEFAULT_DISTRO_FEATURES = Values ( SW Layers ‘apps’)
  
                    DISTO_FEATURES = ${DISTRO_DEFAULT_DISTRO_FEATURES}
  
              - Preferred for Package version ( Linux Version )
 
   2- Add systemd as init process :

     - Follow structure ( meta-grad-distro/conf/distro/include/systemd.inc )

     - Require file in grad.conf file

   📝 Return back to Edit Graduation-rpi5/conf/local.conf :

     📌 Specifiy distribution of image 

          ``` DISTRO ?= "grad" ```
   3- Add Layer :

       ``` cd ~/poky/Gradution-rpi5 ```

       ``` bitbake-layers add-layer ../meta-grad-distro ```
  
  ## Build Testing Image for raspberry pi 5 :

      ``` bitbake rpi-test-image ```
 
  ## -- ⚙️ Software Packages - Applications  ( SW layer ) --

   - Integration Nano Editor :

      Follow Layer Strucrure ( meta-features/recipes-cmd/nano )

      ``` recipetool create -o nano_1.0.bb https://www.nano-editor.org/dist/v7/nano-7.2.tar.xz ```
     
      ``` bitbake nano ```
     
  - Integration C++ Applications & Open Streat map scripts

      create new layer : ``` mkdir meta-apps ```   in poky

                        ``` bitbake-layers add-layer ../meta-apps ```  in Gradution_rpi

      create recipes :
    
            - Follow recipe structure :

                    # TODO 1: Documentation Varaibles ( SUMMARY - DESCRIPTION - HOME_PAGE )
    
                    # TODO 2: License Varaialbes      ( LICENSE - LIC_FILES_CHKSUM )
    
                    # TODO 3: Source Vraiables        ( SRC_URI - SRCREV - S )
    
                    # TODO 4 : Resolve dependancy     ( DEPENDS )
    
                    # TODO 5: Recipe Tasks


           1- vehicle to cloud Application recipe  (meta-apps/recipes-v2c/v2c/v2c_1.0.bb)

           2- vehicle to vehicle Application recipe (meta-apps/recipes-v2v/v2v/v2v_1.0.bb)

           3- Main Application recipe (meta-apps/recipes-main/main/main_1.0.bb)

              .
    
              ├── main
    
              │   └── main.service
    
              └── main_1.0.bb

             - Service files ( auto-run script after booting ) : main.service


           4- Rasp-to-arduino Application recipe (meta-apps/recipes-arduino/arduino/arduino_1.0.bb)


           5- Open street Map Scripts recipe  (meta-apps/recipes-osm/osm/osm_1.0.bb)

               .
    
               ├── osm
    
               │   ├── app.py
    
               │   ├── app.service

               │   ├── db.service
    
               │   ├── initialize_db.py
    
               │   ├── request.py
    
               │   └── templates
    
               │       └── map.html
    
               └── openstreetMap_1.0.bb


             - Scripts : app.py - request.py - intialize_db.py
   
             - Service files ( auto-run script after booting ) : db.service - app.service
    
    - Integration AI Model :

       create new layer : ``` mkdir meta-ai ```   in poky

                          ``` bitbake-layers add-layer ../meta-ai ```  in Gradution_rpi
      
       create recipe :

          .
      
          ├── model
      
          │   ├── model.service
      
          │   ├── model_int8_openvino_model_H
    
          │   └── track.py
       
          └── model_1.0.bb

  ## Create Image Recipe for our Customized image:

      Follow image recipe structure (meta-grad-distro/recipes-core/images/grad-test-image.bb)
      
         - Include base image  : ```require recipes-core/images/rpi-test-image.bb ```

         -  Customization Point: IMAGE_INSTALL (supported packages - software applications)

              # Add Aplications
  
              ``` IMAGE_INSTALL += "v2c" ```
  
              ``` IMAGE_INSTALL += "v2v" ```
  
              ``` IMAGE_INSTALL += "osm"  ```
  
              ``` IMAGE_INSTALL += "main" ```
  
              ``` IMAGE_INSTALL += "model" ```
  
              ``` IMAGE_INSTALL += "arduino" ```

             # Add support package for vehicle to cloud
  
             ``` IMAGE_INSTALL += "libssl" ```

             # Add nano & ssh
  
             ``` IMAGE_INSTALL += "nano" ```
  
             ``` IMAGE_INSTALL += "openssh" ```
  
            # Add support packages for AI model & Openstreat map
  
            ``` IMAGE_INSTALL += "python3 python3-core python3-pip python3-setuptools python3-requests python3-flask" ```
  
            ``` IMAGE_INSTALL += "curl" ```
  
            ``` DEPENDS = "sqlite3" ```

         - Add Image Features  : EXTRA_IMAGE_FEATURES
  
   ### Add Needed Configuartions For Hardware (Raspberry pi 5) in local.conf

     1- UART ( Enables extra UART interfaces (UART2, UART3, UART4) on the Pi 5.)
  
        ``` RPI_KERNEL_DEVICETREE_OVERLAYS+= "overlays/uart2-pi5.dtbo" ```
  
        ``` RPI_KERNEL_DEVICETREE_OVERLAYS+= "overlays/uart3-pi5.dtbo" ```
        
        ``` RPI_KERNEL_DEVICETREE_OVERLAYS+= "overlays/uart4-pi5.dtbo" ```

     2- USB Camera :

        # GPU memory (minimal for USB cam)
  
       ``` GPU_MEM = "64" ```

       # Auto-load USB camera driver
  
      ``` KERNEL_MODULE_AUTOLOAD += "uvcvideo" ```

      ```` MACHINE_ESSENTIAL_EXTRA_RECOMMENDS += "kernel-module-uvcvideo" ```
  
    ### Add Needed Packages To Use Camera ( USB Camera ) in image recipe

       #Add support packages for Camera
  
       ``` IMAGE_INSTALL += "ffmpeg" ```
  
       ``` IMAGE_INSTALL += "gstreamer1.0 gstreamer1.0-libav gstreamer1.0-plugins-base gstreamer1.0-meta-base gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-plugins-good" ```
  
       ``` IMAGE_INSTALL += "v4l-utils" ```
  
       ``` IMAGE_INSTALL += "userland" ```

  ### Add Needed Packages To Use wifi in image recipe

      #Add support packages for for network
  
       ``` IMAGE_INSTALL += "wpa-supplicant linux-firmware dhcpcd" ```

  
  ## 📌 Post-Development Stage :
  
    ### Creating and Flashing Image :

       ``` bitbake grad-test-image ``

       ``` mkdir raspi-images ``` # in ~/poky

       ``` cd raspi-images ```

       # create-rpi-image : User-defined Function used to create image (PATH: custome-scripts/flashing.sh)

       ``` create-rpi-image  grad-test-image ```

       # Flahing Image on SD-CARD : User-defined Function used to flash image (PATH: custome-scripts/flashing.sh)

       ``` sdcard-flashing /dev/sdx  <image> ```

     ### After Booting Raspberry pi5  (in config.txt) :

        - Add lines :
  
         ``` dtoverlay=uart2-pi5 ```
  
         ``` dtoverlay=uart3-pi5 ```

         ``` dtoverlay=uart4-pi5 ```

    ### To make wifi auto-connect after booting follow This instructions

      - nano /etc/wpa-supplicatnt.conf File:

        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
       
        update_config=1

        network={
       
           ssid="YOUR_SSID"
       
           psk="YOUR_PASSWORD"
       
           key_mgmt=WPA-PSK
        }
 
    - groupadd netdev    : creates a new group named "netdev" on a Linux system.
 
    -  systemctl enable dhcpcd
   
    -  systemctl start dhcpcd
 
    -  systemctl enable wpa_supplicant
 
    -  systemctl start wpa_supplicant
 
    -  nano /lib/systemd/system/wpa_supplicant.service
 
      [Unit]
      Description=WPA supplicant
      Before=network.target
      After=dbus.service
      Wants=network.target

     [Service]
     Type=dbus
     BusName=fi.w1.wpa_supplicant1
     PermissionsStartOnly=true
     ExecStartPre=-/bin/mkdir -p /var/run/wpa_supplicant
     ExecStartPre=/bin/chown root:netdev /var/run/wpa_supplicant
     ExecStartPre=/bin/chmod 770 /var/run/wpa_supplicant
     ExecStart=/usr/sbin/wpa_supplicant -u -i wlan0 -c /etc/wpa_supplicant.conf
     ExecReload=/bin/kill -HUP $MAINPID

     [Install]
     WantedBy=multi-user.target
     Alias=dbus-fi.w1.wpa_supplicant1.service

  - systemctl disable --now systemd-resolved

  - rm /etc/resolv.conf  # Remove symlink

  - nano /etc/resolv.conf  # Create new file

     nameserver 8.8.8.8
     nameserver 1.1.1.1
    

   ### Testing Commands :

      - Check service status of customized .service files running after booting without errors :
  
       ``` systemctl statusu model ``` 
  
       ``` systemctl status db  ```
  
       ``` systemctl status app ```

       ``` systemctl status main  ``

       - View logs of customized .service files running after booting without errors :
  
       ``` journalctl -u model -f ``` 
  
       ``` journalctl -u db -f ```
  
       ``` journalctl -u app -f ```

       ``` journalctl -u main -f ``

     
      - Test Camera capture photos or videos  :

           # Testing camera photo using gstreamer 
  
       ``` gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=1 !     'video/x-raw,width=640,height=480,framerate=30/1' !     videoconvert ! jpegenc quality=85 ! filesink location=photo.jpg ```

           # Testing camera video using ffmpeg
  
       ``` ffmpeg -f v4l2 -input_format yuyv422 -video_size 1280x720 -i /dev/video0 -c:v copy raw_video.mkv  ```

    - Test wifi :

      ping -I wlan0 google.com
  
    ## ❗️ISSUES occurred while bitbake image :

         🚫 ERROR: boost-1.78.0-r0 do_package: dwarfsrcfiles failed with exit code 1 (cmd was ['dwarfsrcfiles', '/home/ubuntu/EmbeddedLinux/YOCTO/poky/Graduation_rpi5/tmp-glibc/work/cortexa76-oe-linux/boost/1.78.0-r0/package/usr/lib/
                libboost_math_tr1l.a']):

         ✅ SOLVE :

            Disable dwarfsrcfiles : Since dwarfsrcfiles is not mandatory for functionality and mainly used for debugging/source linking, you can disable it safely

            # add in llocal.conf
  
           ``` INHIBIT_PACKAGE_STRIP = "1" ```
  
           ``` INHIBIT_PACKAGE_DEBUG_SPLIT = "1" ```

        🚫  Parsing of 3022 .bb files complete (3019 cached, 3 parsed). 4692 targets, 582 skipped, 0 masked, 0 errors.
  
          === Matching recipes: ===
  
       ffmpeg:
  
       meta-freescale       4.4.1 (skipped: because it has a restricted license 'commercial'. Which is not listed in LICENSE_FLAGS_ACCEPTED)
  
        meta                 5.0.1 (skipped: because it has a restricted license 'commercial'. Which is not listed in LICENSE_FLAGS_ACCEPTED)

       ✅ SOLVE :

           # add in llocal.conf

           ``` LICENSE_FLAGS_ACCEPTED = "commercial" ```


  # Limitations

Requires some familiarity with the Yocto Project and Linux system administration Builds can take a long time on slower hardware Device compatibility may vary depending on the selected options and configurations

    
  

        

       

  

  
  
       

          

    
 

     

     

