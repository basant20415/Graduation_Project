# Recipe to make AI model auto-run after booting
SUMMARY = "Recipe to make AI model auto-run after booting"
DESCRIPTION = "This recipe installs a YOLOv8 model, its dependencies, and sets it up to run at boot."

# License
LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

# Source files
SRC_URI = " \
    file://track.py \
    file://model_int8_openvino_model_H \
    file://model.service \ 
"

S = "${WORKDIR}"

# Install tasks
do_install() {
    # Install model script and related files
    install -d ${D}${bindir}/Model_deploy

    install -m 0755 ${S}/track.py           ${D}${bindir}/Model_deploy/

    # Copy model folders
    cp -r ${S}/model_int8_openvino_model_H/ ${D}${bindir}/Model_deploy/

    # Install systemd service
    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${S}/model.service      ${D}${systemd_system_unitdir}
}

# Systemd configuration
SYSTEMD_SERVICE:${PN} = "model.service"
SYSTEMD_AUTO_ENABLE:${PN} = "enable"
inherit systemd