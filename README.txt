=== MALiCE (My Awesome Linux Coding Environment) ===
"Code with MALiCE :)"

-1. Directory structure

    -1.1 Custom config files                $HOME/etc                   
    -1.2 Custom scripts and binaries        $HOME/bin
    -1.3 Source code                        $HOME/src
    -1.4 Non-shared docs                    $HOME/private
    
0. bash (Bourne again shell)

    0.1 ~/.bashrc -> ~/etc/shellrc

        0.1.1 File deletion
            0.1.1 Safe                      alias delete='\rm'
            0.1.2 Idiot-proof               SafeDelete(){mv $1 ~/.trash/$1--$(date +%Y-%m-%d--%H:%M:%S).trash}
                                            alias rm=SafeDelete
        0.1.2 Bash history       
            0.1.2.1 Eternal                 PROMPT_COMMAND='history 1 >> $HOME/.eternal_history.jim'
            0.1.2.2 Shiny                   export HISTTIMEFORMAT="%F %T "
            0.1.2.3 Long                    export HISTFILESIZE=2000000                   

        0.1.3 Add ~/bin to path             PATH=$PATH:$HOME/bin

        0.1.4 Aliases
        
    0.2 ~/.bash_profile -> ~/etc/shellrc

    0.3 Custom scripts
        0.3.1 backup                        rsync over ssh.
        0.3.2 prog                          Monitor your progress with time-stamped comments.
    
            0.3.2.1 ~/.progrc -> ~/etc/progrc            

        0.3.3 track                         Primitive git for tracking changes via 'diff'.
        0.3.4 vim_setup.sh                  git all the plugins etc.

    0.x COMMANDS
            cd -                            Go to previous directory        

            cat > lol.txt << 'eof'          Here-doc i.e. multi-line input, in the case
             blah blah blah                 to the 'cat' command. The 'eof' signals the
             blah blah blah                 end of the input.
             blah blah blah
             eof

1. GNU screen (terminal multiplexer)

    1.1 ~/.screenrc -> ~/etc/screenrc

    1.x COMMANDS
            screen -ls                      List existing sessions.
            screen -s NEW_SESSION           Create a new session called NEW_SESSION.
            screen -dRR EXISTING_SESSION    Ultimate screen re-attachment to EXISTING_SESSION.
            <ctrl>+a d                      Detach screen.
            <ctrl>+a 0-9                    Switch to window 0-9.

2. vim (powerful text editor) 

    2.1 ~/.vimrc -> ~/etc/vimrc

    2.2 Plugins (via pathogen)
        2.2.1 FuzzyFinder                   Advanced search facility.
        2.2.2 L9                            Libraries needed for other plugins.
        2.2.3 minibufexpl                   Top window - tabbing.
        2.2.4 nerdtree                      Left window - file explorer.
                Bookmarks
                Change working directory
        2.2.5 python-mode                   Python-specific enhancements to vim.
                pylint
                pyflakes
                PEP8
                Run python code
                Code folding
                Vim-Rope
        2.2.6 tagbar                        Right window - code structure via exuberant ctags.
        2.2.7 tasklist                      Top window - lines containing 'TODO' or 'FIXME'.
        2.2.8 vim-fugitive (Git from within vim)

    2.x COMMANDS
            i                               'Insert' mode.
            <esc>                           Leave 'insert' mode.
            :                               Command prompt.
            :w <enter>                      Save buffer ('write').
            :q <enter>                      Quit.
            :q! <enter>                     Force quit.               
            :asc <enter>                    ASCII code of character under the cursor.
            42G                             Goto line 42.
            gg                              Goto start of buffer.
            G                               Goto end of buffer.
            0                               Goto start of line.        
            $                               Goto end of line.
            v                               'Visual' mode (select characters).
            V                               'Visual' mode (select lines).
            o                               Open a new line below.
            O                               Open a new line above.
            /foo bar <enter>                Search buffer for "foo bar".
            x                               Delete character.
            42x                             Delete 42 characters.
            dd                              Delete line.
            42dd                            Delete 42 lines.
            y                               Copy ('yank') selected text.
            p                               Paste ('put') yanked text.
            <ctrl>+w w                      Goto next window.
            <ctrl>+w q                      Close current window.
            q a-z                           Starting recording macro and bind to the 'a-z' key.
            q                               Stop recording macro.
            @ a-z                           Run macro bound to the 'a-z' key.  

3. git (version control system)

    3.x COMMANDS
            git init                        Turn the current directory into a git repository.
            git branch                      List branches.
            git checkout HEFTY              Switch to branch HEFTY.
            git checkout -b HEFTY           Create a new branch called HEFTY and switch to it.
            git add FILENAME                Add FILENAME to the staging area.
            git commit -m 'Something'       Commit files in the staging area and add a meaninful
                                            description about the commit.
            
            git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
                                            Set a remote server as the origin e.g. github.

            git push -u origin master       Send commit to the remote server (origin) e.g. github.

4. ssh (secure shell)

    4.1 ~/ssh/config -> ~/etc/config_ssh

    4.x COMMANDS
            ssh USER@HOST                   Connect to HOST as USER.
            ssh-agent                       Start the ssh agent.
            ssh-add                         Add an identy to the ssh agent to save having to
                                            re-enter the passphrase every time.

5. terminal (virtual terminal)

    5.x COMMANDS
        <ctrl>+<alt>+t                      New terminal window.
        <ctrl>+<alt>+<num-5>                Toggle full screen.
        <ctrl>+<shift>+t                    New terminal tab.
        <ctrl>+<page-up>                    Previous tab.
        <ctrl>+<page-down>                  Next tab.

6. mutt (TUI mail user agent)

    6.1 ~/.muttrc -> ~/etc/muttrc

    6.x COMMANDS
            gi                              Goto inbox
            ga                              Goto 'All mail'
            gs                              Goto 'Sent mail'
            d                               Mark for deletion.
            !                               Mark as spam.
            *                               Star.
            $                               Update inbox / process marked emails.
            m                               New email.
            r                               Reply to email.

7. cmus (TUI music player)

    7.x COMMANDS
            z                               previous
            x                               play
            c                               toggle pause
            v                               stop
            b                               next
            s                               Toggle shuffle
            C                               Toggle continuous play.
            r                               Toggle repeat.
            <space>                         expand item
            <tab>                           Next window
            1                               Artist/song library                               
            2                               List of library files.
            3                               Playlist
            4                               Play queue
            5                               File browser
            6                               Library filters
            7                               Settings
            +/-                             Increase/decrease volume by 10%.
            q                               Quit.
            e                               Appened track to play queue.
            E                               Prepend track to play queue.
            y                               Copy track to playlist.
            :save -p FILE                   Save playlist to 'FILE'

8. irssi (irc client)

    8.x COMMANDS
            /nick superman                  change nick to 'superman'.
            /connect SERV                   connect to server 'SERV' on port 6667.
            /join CHAN                      join channel 'CHAN'
            bob: hi                         say 'hi' to 'bob'.
            <alt>+0-9                       Switch to window 0-9.

9. bitlbee (irc server)

    9.x COMMANDS
            /join &bitlbee                  join the command channel.
            identify                        You want to identify yourself
            /oper                           Password prompt for identifying yourself.
            blist                           Show buddy list.
            rename Tom123 tom               Rename 'Tom123' to 'tom'.

10. srm (secure delete)

11. pgp (OpenPGP encryption and signing tool)
