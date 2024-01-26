# PA Media and Design High School Competition 2024 Project Entry

Recommender (undecided name) is a cross-platform app built using Kivy and Python, giving recommendations to users that use it in a vast variety of topics.

## Installation:

### Windows:

#### Using virtualenv (recommended to use virtual environments)
- Install [Python](python.org/downloads/windows/) if you haven't already
- Install virtualenv using ```pip install virtualenv```
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Get Python executable location by executing ```where python```
- Create virtualenv environment by executing ```virtualenv --python <Python executable location> venv```, replacing `<Python executable location>` with the path outputted by running the previous command.
- Activate virtualenv environment by executing ```.\venv\Scripts\activate```
- Install all required modules by executing ```pip -r requirements.txt```
- Run the program by executing ```python Funnies.py```

#### Using conda (recommended to use virtual environments)
- Install [Python](python.org/downloads/windows/) if you haven't already
- Install [Anaconda](anaconda.com/download) or [Miniconda](docs.conda.io/projects/conda/en/stable] if you haven't already
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Create a new conda environment by executing ```conda create -n Recommender```
- Activate conda environment by executing ```conda activate Recommender```
- Install all required modules by executing ```pip -r requirements.txt```
- Run the program by executing ```python Funnies.py```

#### Without using virtual environments (not recommended)
- Install [Python](python.org/downloads/windows/) if you haven't already
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Install all required modules by executing ```pip -r requirements.txt```
- Run the program by executing ```python Funnies.py```


### Linux:
#### Install Python if you haven't already by:
- Debian-/Ubuntu-based: ```sudo apt install python3```
- Arch-based: ```sudo pacman -S python3```
- RHEL-/Fedora-based: ```sudo dnf install python3```
- SUSE-/OpenSUSE-based: ```sudo zypper install python3```
- NixOS (Note: there are separate instructions for installing on NixOS):
  - Add ```python3``` to environment.systemPackages = [];
  - Or install imperatively by ```nix-env -iA python3```

### Using virtualenv (recommended to use virtual environments)
- Install virtualenv by:
  - Debian-/Ubuntu-based: ```sudo apt install python3-venv virtualenv python3-virtualenv```
  - Arch-based: ```sudo pacman -S python-virtualenv```
  - RHEL-/Fedora-based: ```sudo dnf install python3-virtualenv```
  - SUSE-/OpenSUSE-based: ```sudo zypper install python3-virtualenv```
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Create virtualenv environment by executing ```virtualenv venv```
- Activate virtualenv environment by executing ```source venv/bin/activate```
- Install all required modules by executing ```pip -r requirements.txt```
- Run the program by executing ```python Funnies.py```

#### Using conda (recommended to use virtual environments)
- Install conda by:
  - Debian-/Ubuntu-based: Follow instructions on [https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
  - Arch-based: ```sudo pacman -S python-conda```
  - RHEL-/Fedora-based: Follow instructions on [https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
  - SUSE-/OpenSUSE-based: Follow instructions on [https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Create a new conda environment by executing ```conda create -n Recommender```
- Activate conda environment by executing ```conda activate Recommender```
- Install all required modules by executing ```pip -r requirements.txt```
- Run the program by executing ```python Funnies.py```

### Using Nix-shell (Only for NixOS)
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Run ```nix-shell```
- Run the program by executing ```python Funnies.py```

#### Without using virtual environments (not recommended) (differs on distro so not properly documented)
- Clone this repo by executing ```git clone https://github.com/nulladmin1/PA-Media-and-Design-High-School-Competition-2024-Project-Entry.git```
- Go into the clones repo by executing ```cd PA-Media-and-Design-High-School-Competition-2024-Project-Entry```
- Install all required modules by executing ```pip -r requirements.txt```
- Run the program by executing ```python Funnies.py```

