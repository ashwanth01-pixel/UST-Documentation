# Command Summary (17th July)

- `git config --list` – List all the Git configuration settings.
- `cd desktop` – Navigate to the desktop directory.
- `touch n.txt` – Create a new empty file named n.txt.
- `vim touch n.txt` – Open n.txt with Vim editor.
- `touch m.txt` – Create a new empty file named m.txt.
- `nano m.txt` – Open m.txt with Nano editor.
- `git init` – Initialize a new Git repository.
- `git branch` – List, create, or delete branches.
- `git status` – Show the working directory and staging area status.
- `git add .` – Stage all changes for the next commit.
- `rm -rf .git` – Delete the Git repository metadata.
- `git add m.txt` – Stage m.txt file for commit.
- `git commit -m "first commit"` – Commit staged changes with a message.
- `git diff` – Show changes between working directory and index.
- `git log --oneline` – View commit history in one line per commit.
- `git log` – View detailed commit history.
- `git commit -m "second commit"` – Commit changes with a new message.
- `git commit -am "second"` – Add and commit changes in one step.
- `git reset --hard HEAD~1` – Undo the last commit and discard changes.
- `git restore m.txt` – Restore file from last commit.
- `ls -a` – List all files including hidden ones.
- `ls .git` – List contents of the .git directory.
- `cal` – Display calendar.
- `cal 2024` – Show calendar for the year 2024.
- `bash` – Start a new Bash shell session.
- `clear` – Clear the terminal screen.
- `chmod u+x file.sh` – Make file.sh executable by the user.
- `./file.sh` – Execute the shell script file.sh.
- `echo "ram" >> file.sh` – Append 'ram' to the end of file.sh.
- `cat file.sh` – Display the contents of file.sh.
- `bash --version` – Show the current version of Bash.
- `brew install bash` – Install Bash via Homebrew.
- `openssl rsa -in Ashwanthram.pem -check` – Check and display RSA key.
- `openssl x509 -in Ashwanthram.pem -text -noout` – Display certificate details.
- `chmod 400 Ashwanthram.pem` – Set PEM file permissions to read-only.
- `ssh -i Ashwanthram.pem ubuntu@<public-ip>` – Connect to EC2 instance using PEM file.
- `whoami` – Display the current logged-in username.
- `git remote add origin <url>` – Add remote Git repository.
- `git push -u origin master` – Push commits to the master branch and set upstream.
- `history` – Show command history.
- `ssh-keygen -t ed25519 -C "email"` – Generate SSH key with a comment.
- `eval "$(ssh-agent -s)"` – Start SSH agent.
- `ssh-add <keyfile>` – Add SSH private key to agent.
- `cat <keyfile>.pub` – Display public key.
- `git remote set-url origin <url>` – Change the remote repository URL.