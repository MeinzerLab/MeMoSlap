
# Git-Hub

- to use github you have to install the git command
- on Ubuntu, open a terminal an typ in

```bash
sudo apt install git
```

## Clone the repository

- You can easily get all the instruction by cloning the repository
- therefore go to a folder in which you want to have the repository
- open a terminal and type in
  
```bash
git clone https://github.com/MeinzerLab/MeMoSlap 
```

- the repository should be now in your path as folder

## Change and push the repository

- if you want to make changes, say in the GitHub.md you have to commit these changes and then push the repository back to github

### git credential manager (gcm)

- for an easier use you can install the [git-credential-manager](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)

#### download and install the newest gcm

- [dowonload the newest gcm](https://github.com/git-ecosystem/git-credential-manager/releases)
- for ubuntu choose the one ending with *.deb
- install via terminal
- go to path where *.deb is saved

```bash
sudo dpkg -i name_of_file.deb
```

- [configure after installation](https://www.baeldung.com/ops/git-configure-credentials)

```bash
git-credential-manager configure
```

#### use gcm

- to generate a key needed for pulling in gitub open a terminal and type in  

```bash
gpg --gen-key
```

- and follow the prompts (you must have an github account for that)
- remember user and mail for later
- a key is given, copy paste the key from the terminal by mark and copy (strg+shift+c)
- pass the key (strg+shift+v)

```bash
pass init <gpg-id>
```

run

```bash
git config --global credential.credentialStore gpg
```

- add user as global user

```bash
git config --global user.email "git hub mail adress"
git config --global user.name "user name"
```

## commit changes

- to track changes in file, say "title is changed in file", let's say in GiHub.md

```bash
git commit fmriprep.md -m "title is changed in file"
```

- If you changed many files you can use also

```bash
git commit -a -m "whatever you have done"
```
  
- push the modified repository

```bash
git push
```

### Add file to repositor which was not there befor

- create a new file and change director to file path
-create a new file say GitHub.md and add it to repository via

```bash
git add Github.md
```
