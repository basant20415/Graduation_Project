# TODO 1: Documentation Varaibles
SUMMARY = "Recipe for v2v application"
HOMEPAGE = "https://github.com/MariamReda25/UART-APP.git"

# TODO 2: License Varaialbes 
LICENSE = "Unknown"
LIC_FILES_CHKSUM =  " "

# TODO 3: Source Vraiables 
SRC_URI = "git://github.com/MariamReda25/UART-APP.git;branch=main;protocol=https"
SRCREV = "${AUTOREV}"
S ="${WORKDIR}/git"

# TODO 5: Recipe Tasks
inherit cmake pkgconfig

# Specify any options you want to pass to cmake using EXTRA_OECMAKE:
EXTRA_OECMAKE = ""
