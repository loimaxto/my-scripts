sudo apt update
sudo apt install -y wget gpg apt-transport-https
sudo apt install gnome-tweaks

sudo install -m 0755 -d /etc/apt/keyrings
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/packages.microsoft.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
sudo apt update
sudo apt install -y code
# sudo apt --only-upgrade install code

## Gnome Extension Manager:
sudo apt install gnome-shell-extension-manager -y
# Clipboard Indicator

sudo add-apt-repository -y ppa:jdxcode/mise
sudo apt update -y
sudo apt install -y mise

mise use --global node@26
node -v
# echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
# source ~/.zshrc


# sudo apt update
# sudo apt install -y code


wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
rm google-chrome-stable_current_amd64.deb



PROFILE=$(gsettings get org.gnome.Terminal.ProfilesList default | tr -d "'")s
gsettings set "org.gnome.Terminal.Legacy.Keybindings:/org/gnome/terminal/legacy/keybindings/$PROFILE/" copy '<Primary>c'
gsettings set "org.gnome.Terminal.Legacy.Keybindings:/org/gnome/terminal/legacy/keybindings/$PROFILE/" paste '<Primary>v'


gsettings set org.gnome.desktop.interface screenshot-directory '/dev/null'


git config --global user.email "tranhongquang24@gmail.com"
git config --global user.name "quang"    