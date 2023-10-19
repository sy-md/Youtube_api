https://steemit.com/raspberry/@joedoe47/easily-run-i3-on-raspberrypi

# some of the tool is use for the ricing of my i3
   * i3status / i3blocks
   * rofi
   * picom
   * https://github.com/muesli/duf.git
   * https://github.com/sharkdp/bat.git
   * https://github.com/junegunn/fzf.git
   * https://github.com/dalance/procs.git
      * --https://github.com/aristocratos/bpytop.git--
   * https://github.com/WayneD/rsync.git
      * --https://github.com/chmln/sd.git--
   * https://github.com/nicolargo/glances.git
   * https://github.com/cmus/cmus.git
   * https://github.com/dylanaraps/neofetch.git





# THIS HELP I3 BE VISABLE ON WINDOES MANGER
sudo apt install i3 dmenu suckless-tools

>> git clone 
>> # get all depenpeces from wiki/github
>> mkdir build && cd build
>> sudo apt install meson && meson ..
>> ninja
>> sudo ninja install
>> two file ect/lxsesssion/ldxp-pi {desktop = i3 or comment out}
>> i3-config-wizard
>> sudo apt-get install lightdm 
>> sudo update-alternatives --config x-window-manager && sudo update-alternatives --config x-session-manager 
>> startx

make a file ~/.xinit.rc >> exec i3
also the ~/.dmrc >> Session= i3 --- this will make it open i3 every time

startx -ll launch dory server



 *nitrogen - exec_always nitrgon --restore

If a file named .xinitrc exists in the home directory, it will execute the commands listed there

