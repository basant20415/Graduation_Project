# TODO 1: Documentation Varaibles
SUMMARY = "Recipe for main application"
HOMEPAGE = "https://github.com/MariamReda25/MAIN_APP.git"

# TODO 2: License Varaialbes 
LICENSE = "Unknown"
LIC_FILES_CHKSUM =  " "

# TODO 3: Source Vraiables 
SRC_URI = "git://github.com/MariamReda25/MAIN_APP.git;branch=main;protocol=https \
            file://main.service \   
    "
SRCREV = "${AUTOREV}"
S ="${WORKDIR}/git"


# TODO 5: Recipe Tasks
inherit cmake pkgconfig systemd

do_install(){
    
    install -d ${D}${bindir}
    install -m 0755 ${B}/main ${D}${bindir}/main  
    
    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/main.service     ${D}${systemd_system_unitdir}/main.service

} 

# Specify any options you want to pass to cmake using EXTRA_OECMAKE:
EXTRA_OECMAKE = ""

SYSTEMD_SERVICE:${PN} += " main.service "
SYSTEMD_AUTO_ENABLE:${PN} = "enable"
