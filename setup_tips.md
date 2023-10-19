https://steemit.com/raspberry/@joedoe47/easily-run-i3-on-raspberrypi

# some of the tool is use for the ricing of my i3
   * i3status / i3blocks
   * rofi
   * picom
   * https://github.com/muesli/duf.git
   * https://github.com/sharkdp/bat.git
   * https://github.com/junegunn/fzf.git
   * https://github.com/dalance/procs.git
      * * --https://github.com/aristocratos/bpytop.git--
   * https://github.com/WayneD/rsync.git
      * * --https://github.com/chmln/sd.git--
   * https://github.com/nicolargo/glances.git
   * https://github.com/cmus/cmus.git
   * https://github.com/dylanaraps/neofetch.git

# THIS HELP I3 BE VISABLE ON WINDOES MANGER
sudo apt install i3 dmenu suckless-tools
cd into the downloads

1. git clone https://github.com/Airblader/i3.wiki.git i3
2. mkdir build && cd build
3. sudo apt install meson && meson ..
4. ninja
5. sudo ninja install
6. two file ect/lxsesssion/ldxp-pi {desktop = i3 or comment out}
7. i3-config-wizard
8. sudo apt-get install lightdm
9. sudo update-alternatives --config x-window-manager && sudo update-alternatives --config x-session-manager
10. startx

------

make a file ~/.xinit.rc >> exec i3
also the ~/.dmrc >> Session= i3 --- this will make it open i3 every time

startx -ll launch dory server



 *nitrogen - exec_always nitrgon --restore

If a file named .xinitrc exists in the home directory, it will execute the commands listed there

