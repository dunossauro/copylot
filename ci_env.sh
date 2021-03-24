install_ubuntu_image_dependencies () {
# based on Ubuntu:18.04
  apt-get update
  apt-get -y install libgstreamer1.0-dev gstreamer1.0-alsa gstreamer1.0-plugins-base \
  libsmpeg-dev libswscale-dev libavformat-dev libavcodec-dev libjpeg-dev libtiff5-dev \
  libx11-dev libmtdev-dev build-essential libgl1-mesa-dev libgles2-mesa-dev xvfb \
  pulseaudio xsel libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev
}

start_xvfb () {
  /sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background \
    --exec /usr/bin/Xvfb -- :99 -screen 0 1280x720x24 -ac +extension GLX
}
