execute pathogen#infect()

set nocompatible
syntax on
filetype plugin indent on


set ignorecase
set smartcase
set backspace=indent,eol,start
set ruler
set laststatus=2
set confirm
set visualbell
set cmdheight=2

set shiftwidth=2
set softtabstop=2
set expandtab


map Y y$

let g:slime_target = "screen"
let g:slime_python_ipython = 1

xmap <leader>d <Plug>SlimeRegionSend
nmap <leader>d <Plug>SlimeLineSend


:imap qq <Esc>


set list
set listchars=tab:>-

let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_math = 1

let g:ale_python_pylint_options = '--disable=E0401,C0114,E1111,W0311'
let g:ale_virtualtext_cursor = 'current'

