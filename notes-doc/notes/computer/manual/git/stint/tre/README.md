{{c1::  Sets the name attached to your commit transaction }}  {{c2::   git config --global user.name "[name]" }} ~
{{c1::  Set the email attached to your commit transactions }}  {{c2::   git config --global user.email "[email address]" }} ~
{{c1::  Enables colorization of command line output }}  {{c2::   git config --global color.ui auto }} ~

{{c1::  Turn an existing directory into a git repository }}  {{c2::   git init }} ~
{{c1::  Clone (download) a repository that already exists, including all of the files, branches, and commits from url }}  {{c2::   git clone [url]  }} ~
{{c1::  Clone (download) a repository that already exists, including all of the files, branches, and commits from ssh path }}  {{c2::   git clone   [user@host:/path] }} ~

{{c1::  Create a new branch }}  {{c2::   git branch [branch-name] }} ~
{{c1::  Switches to the specified branch and updates the working directory }}  {{c2::   git checkout [branch-name] }} ~
{{c1::  Combines the specified branch’s history into the current branch. }}  {{c2::   git merge [branch] }} ~
{{c1::  Deletes the specified branch }}  {{c2::   git branch -d [branch-name] }} ~
{{c1::  Push branch to remote repository }}  {{c2::   git push origin [branch] }} ~

{{c1::  Downloads all history from the remote tracking branches }}  {{c2::   git fetch }} ~
{{c1::  Combines remote tracking branch into current local branch }}  {{c2::   git merge }} ~
{{c1::  Uploads all local branch commits to GitHub }}  {{c2::   git push }} ~
{{c1::  Updates your current local working branch with all new commits from the remote branch }}  {{c2::   git pull }} ~

{{c1::  List version history for the current branch }}  {{c2::   git log }} ~
{{c1::  List version history for a file }}  {{c2::   git log --follow [file] }} ~
{{c1::  Show content differences between two branches }}  {{c2::   git diff [branch-1]…[branch-2] }} ~
{{c1::  Output metadata and content changes of a commit }}  {{c2::   git show [commit] }} ~
{{c1::  Snapshots a file in preparation for versioning }}  {{c2::   git add [file] }} ~
{{c1::  Remove a git file from a repository }}  {{c2::   git rm [file] }} ~
{{c1::  Record file snapshot in permanent version history }}  {{c2::   git commit -m “[description text]” }} ~

{{c1::  Undo all commits after the specified commit, except changes locally }}  {{c2::   git reset [commit] }} ~
{{c1::  Discard all history & changes back to commit }}  {{c2::   git reset --hard [commit] }} ~
{{c1::  Replace working copy with latest from HEAD }}  {{c2::   git checkout --[file] }} ~


Git is an open source, distributed {{c1:: version-control system}} ~
Commit is a Git {{c1::object}}  a {{c1::snapshot}}  of your entire repository compressed into a {{c1::SHA}}   ~
Branch is a lightweight movable {{c1::pointer}}  to a {{c1::commit}}  ~
Clone is a {{c1::local}}  version of a {{c1::repository}} , including all {{c1::commits}}  and {{c1::branches}}  ~
Remote is a common {{c1::repository}}  that is used to exchange their changes ~
Fork is a {{c1::copy}}  of a {{c1::repository}}  on GitHub owned by a different user ~
Pull request is a place to compare and discuss the differences introduced on a {{c1::branch}}  with reviews, comments, integrated tests, and more ~
HEAD represents your current {{c1::working directory}} , the HEAD pointer can be moved to different branches, tags, or commits when using git checkout ~

