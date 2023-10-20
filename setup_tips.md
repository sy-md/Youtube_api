https://steemit.com/raspberry/@joedoe47/easily-run-i3-on-raspberrypi
https://www.makeuseof.com/things-to-do-after-installing-i3wm/ {about i3}

# some of the tool is use for the ricing of my i3
   * sudo apt install nitrogen - exec always nitrogen --restore >> i3 config
   * sudo apt install -y picom - exec picom >> i3 config 
     
   * https://github.com/muesli/duf.git -  apt install duf
   * https://github.com/sharkdp/bat.git - sudo apt install bat
   * https://github.com/junegunn/fzf.git - sudo apt install fzf / checkvim for info alwell
   * https://github.com/nicolargo/glances.git - apt install python3-psutil
   * https://github.com/dylanaraps/neofetch.git - sudo apt-get install neofetch
   * https://github.com/vivien/i3blocks.git -- build
   * https://github.com/i3/i3status.git -- build
   * https://github.com/davatorium/rofi.git -- build
   * https://github.com/yshui/picom.git -- build {once built mkdir /.config/picom && touch picom.conf then copy git clones conf into the new conf in .config}

   * https://github.com/cmus/cmus.git - build
   * https://github.com/WayneD/rsync.git - build
---  
  __other option for glances__
  * https://github.com/dalance/procs.git
      * * --https://github.com/aristocratos/bpytop.git
---
  __others__
  * https://github.com/chmln/sd.git -- parser
  * https://github.com/derf/feh.git -- inamger viewer
  
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
9. sudo update-alternatives --config x-window-manager && sudo update-alternatives --config x-session-manager (keep startlxd {dont change})
10. startx

------

make a file ~/.xinit.rc >> exec i3
also the ~/.dmrc >> Session= i3 --- this will make it open i3 every time

startx -ll launch dorx server



 *nitrogen - exec_always nitrgon --restore

If a file named .xinitrc exists in the home directory, it will execute the commands listed there


/root/.config/i3/config is the real config for i3 _not_ /home/sy1/config/i3/config

picom wasnt working so i ran >> picom --backend xrender
so i just change the the display for the trnaparnt to work so the two you need is i3 and startxld or what ever it said
sudo update-alternaitves --config x-window-manager 

/etc - [X11 and xdg]
/home - home and sy1 
/root/.config - config files for i3 apps {e,g nitrogen autoed into this folder}


