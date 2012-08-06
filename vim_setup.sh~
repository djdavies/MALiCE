#!/bin/bash

# Author:IceAxe 
# Date: 31 May 2012
# Description: Bash script for setup of vim

# Requirements: 'vim', 'exuberant ctags' and 'git'.

#===|Create directories|===#

mkdir -p ~/.vim/autoload 
mkdir -p ~/.vim/bundle
mkdir -p ~/.vim/doc 
mkdir -p ~/.vim/plugin 
mkdir -p ~/.vim/syntax

#===|Download & setup plugins|===#

# Plugin: pathogen 
# Vim 'runtimepath' manager, great for installing plugins. 
git clone git://github.com/tpope/vim-pathogen.git  
cp ./vim-pathogen/autoload/pathogen.vim ~/.vim/autoload/
rm -f -r ./vim-pathogen/

cd ~/.vim/bundle/  

# Plugin: fugitive
# Git wrapper for Vim.
git clone git://github.com/tpope/vim-fugitive.git 

# Plugin: nerdtree
# Sidebar filesystem explorer. 
git clone git://github.com/scrooloose/nerdtree.git  

# Plugin: l9
# l9 is a Vim-script library, which provides some utility functions and
# commands for programming in Vim. 
git clone git://github.com/vim-scripts/L9.git

# Plugin: tagbar
# Sidebar displaying scope-ordered ctags of current file.
# Supports all of the languages that ctags does, i.e. Ant, Assembler, ASP,
# Awk, Basic, BETA, C, C++, C#, COBOL, DosBatch, Eiffel, Erlang, Flex,
# Fortran, HTML, Java, JavaScript, Lisp, Lua, Make, MatLab, OCaml,
# Pascal, Perl, PHP, Python, REXX, Ruby, Scheme, Shell script, SLang, SML,
# SQL, Tcl, Tex, Vera, Verilog, VHDL, Vim and YACC.
git clone git://github.com/majutsushi/tagbar 

# Plugin: tasklist
# Based on the eclipse Task List. It will search the file for FIXME,
# TODO, and XXX.
git clone git://github.com/vim-scripts/TaskList.vim.git 

# Plugin: minibufexpl
# List open buffers as tabs along the top or bottom of your screen.
git clone git://github.com/fholgado/minibufexpl.vim.git 

# Plugin: FuzzyFinder
# Provides convenient ways to quickly reach the
# buffer/file/command/bookmark/tag you want.
git clone git://github.com/vim-scripts/FuzzyFinder.git 

# Plugin: Python-Mode
# Adds refactoring tools inc. pylint, pyflakes, PEP8, rope etc.
git clone git://github.com/klen/python-mode.git
##===|Configure .vim/vimrc|===#

# Create symbolic link to .vimrc
ln -s ~/.vim/vimrc ~/.vimrc

##General

# Run pathogen script on startup.
echo "call pathogen#infect()" >> ~/.vim/vimrc 
echo "call pathogen#helptags()" >> ~/.vim/vimrc

# Enable syntax highlighting.
echo "syntax on" >> ~/.vim/vimrc 

# Enable filetype detection, and loading of plugin and indent files for specific
# filetypes. 
echo "filetype plugin indent on" >> ~/.vim/vimrc

# Enable omnicompletion.
echo "set ofu=syntaxcomplete#Complete" >> ~/.vim/vimrc 

# Set the colour scheme
echo "colorscheme ron" >> ~/.vim/vimrc 

# Enable line numbers
echo "set number" >> ~/.vim/vimrc 

# Set length of history.
echo "set history=700" >> ~/.vim/vimrc

# Enable the WiLd menu
echo "set wildmenu" >> ~/.vim/vimrc 
echo "set wildmode=list:longest,full" >> ~/.vim/vimrc

# Show current position
echo "set ruler" >> ~/.vim/vimrc

# Highlight search results
echo "set hlsearch" >> ~/.vim/vimrc 

# Enable incremental search
echo "set incsearch" >> ~/.vim/vimrc 

# Disable annoying error sound
echo "set noerrorbells" >> ~/.vim/vimrc

# Show matching brackets
echo "set showmatch" >> ~/.vim/vimrc

# Use spaces instead of tabs
echo "set expandtab" >> ~/.vim/vimrc 

# Be smart when using tabs
echo "set smarttab" >> ~/.vim/vimrc 

# 1 tab == 4 spaces
echo "set shiftwidth=4" >> ~/.vim/vimrc 
echo "set tabstop=4" >> ~/.vim/vimrc 

# Show commands that are enetered.
echo "set showcmd" >> ~/.vim/vimrc

## Keyboard mappings

# <,>> = 'leader' key for additional combos.
echo 'let mapleader = ","' >> ~/.vim/vimrc 

# <,>><w>> = fast save.
echo "nmap <leader>w :w!<cr>" >> ~/.vim/vimrc 

# <F2>> = toggle line numbers and fold column for easy copying. 
echo "nnoremap <F2> :set nonumber!<CR>:set foldcolumn=0<CR>" >> ~/.vim/vimrc 

# <space>> = search (/).
echo "map <space> /" >> ~/.vim/vimrc

# <ctrl-space>> = reverse search (?).
echo "map <c-space> ?" >> ~/.vim/vimrc

# <,>><s>><s>> = toggle spellchecker.
echo "map <leaderder>ss :setlocal spell!<cr>" >> ~/.vim/vimrc

# <T>> = tasklist.   
echo "map T :TaskList<CR>" >> ~/.vim/vimrc 

# <P>> = toggle tagbar.
echo "map P :TagbarToggle<CR>" >> ~/.vim/vimrc 

# <[>> = cycle to previosu buffer. 
echo "map [ :MBEbp<CR>" >> ~/.vim/vimrc 

# <]>> = cycle to next buffer. 
echo "map ] :MBEbn<CR>" >> ~/.vim/vimrc
