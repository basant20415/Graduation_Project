# TODO: 1. Documentation Variables “meta-data" about recipe
SUMMARY = "Recipe to make AI model auto-run after booting"
DESCRIPTION = "This recipe installs a YOLOv8 model, its dependencies, and sets it up to run at boot."

# TODO: 2. License Variable 
LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

# TODO: 3. Source code Variables
SRC_URI = " \
    file://app.py \
    file://initialize_db.py \
    file://request.py \
    file://app.service \
    file://db.service \
    file://templates/ \
"

S = "${WORKDIR}"

# TODO: 4. Tasks executed by bitbake

do_install() {
    # Install model script and related files
    install -d ${D}${bindir}/OSM

    install -m 0755 ${WORKDIR}/app.py                ${D}${bindir}/OSM/
    install -m 0644 ${WORKDIR}/initialize_db.py      ${D}${bindir}/OSM/
    install -m 0644 ${WORKDIR}/request.py            ${D}${bindir}/OSM/

    # Copy model folders
    cp -r ${WORKDIR}/templates                      ${D}${bindir}/OSM/

    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/app.service ${D}${systemd_system_unitdir}/app.service
    install -m 0644 ${WORKDIR}/db.service      ${D}${systemd_system_unitdir}/db.service

} 

SYSTEMD_SERVICE:${PN} += " db.service app.service "
SYSTEMD_AUTO_ENABLE:${PN} = "enable"
inherit systemd