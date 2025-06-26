# TODO 1: Documentation Varaibles
SUMMARY = "Recipe for v2c application"
HOMEPAGE = "https://github.com/basant20415/new_aws_app.git"

# TODO 2: License Varaialbes 
LICENSE = "Unknown"
LIC_FILES_CHKSUM =  " "

# TODO 3: Source Vraiables 
SRC_URI = "git://github.com/basant20415/new_aws_app.git;branch=main;protocol=https"
SRCREV = "${AUTOREV}"
S ="${WORKDIR}/git"

# TODO 4 : Resolve dependancy 
DEPENDS = "paho-mqtt-cpp"

# TODO 5: Recipe Tasks
inherit cmake pkgconfig

# Specify any options you want to pass to cmake using EXTRA_OECMAKE:
EXTRA_OECMAKE = ""

