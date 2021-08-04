# VIM tutorial
[distrotube youtube link](https://youtu.be/tExTz7GnpdQ)

## Moving The Cursor
- **h**: left

- **j**: down

- **k**: up

- **l**: right

> visual line movement j, k where there is 2 lines used for certain lines: **gj** and **gk**

## Quiting
- ':wq'

- ':q', ':exit', ZZ


## Modes
### Normal Mode
> navigation and some copy paste type of actions

> hjkl works for the cursor movement

gg: first line

G (shift+g): end of line

0: first word of the line

{number}G(shift+g): goes to the {number} line.

x: delete key, delete the char behind the cursor.

u: undo whatever you just did.

ctrl+R: for redo

dw: deletes a word on the cursor.

dd: delete line.

d$: cursor to end of the line delete. (~$ means 'to the end of the line') usually do **'D'** instead of this.

{number}dd: delete {number} of lines.

w: navigate to next word in the first character.

e: navigate through end of word.

b: navigate backwords.

{number}(w,b,h,j,k,l): navigate through {number} of words forward or backward (or character direction for hjkl)

p: paste

W,E,B: navigates through the file but excludes special characters

f{character}: **forward** to a character, i.e. ft will bring cursor to the first 't'.

F{character}: **backwards** to the character and cursor on the character.

t,T will do similar, but something -1 or +1 depending on the position (until the cursor encounters)

#### finding symbols

% will find a parenthesis in that line 

#### searching

/: search forward

?: search backwards; but usually not use it

n: searches for the next

Ctrl+o: takes me where I was backwards

Ctrl+i: go back to where I was forwards

#### replacing strings

:%s/oldstring/newstring/g  : replace 'oldstring' with 'newstring' in every instance

:3,9s/oldstring/newstring/g : replace 'oldstring' with 'newstring' in lines 3,9

:%s/oldstring/newstring/gc : this will ask if you want to replace

#### running terminal commands inside vim and then come back to vim.

:!{command}: bash commands works and comes back to vim.

:w+(ctrl+d): will let you know most of commands on linux you can run inside vim that starts with the 'w' character.

#### cut and paste
> delete and go to line 17 and paste

dd 17G p

#### copy paste

yw: copy word

y$: copy cursor to end of the line

yy: copy whole line

and then **'p'** for paste.

### Insert Mode 'i' in normal mode
You can start writing.

esc to go back to normal mode.

**'I'** brings you to the first character in the line and turns on insert mode.
 
**'A'** brings you to the end of the line and turns on insert mode. (**append mode** some say)

**'s'** will delete the character on the cursor and enters the insert mode

**'S'** will delete the line of cursor and enters the insert mode

**'o'** will make a new line under the cursor and enters the insert mode

**'O'** will make a new line above the cursor and enters the insert mode

**'c'** deletes character and enters the insert mode; can be used with the '$' for '~to the end of the line'

**'C'** deletes cursor to end of the line and enters the insert mode

### visual mode
highlight text by navigating.
