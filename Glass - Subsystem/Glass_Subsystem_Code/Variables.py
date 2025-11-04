hashed_pass2 = []
hashed_pass3 = []
hashed_char = []
vocabp = []
memp = []
vocablines = []
memlines = []
clogp = []
illegal_chars = []
ver = "Rusk_Botv1.10"
updates1 = "Re-Added all pre-v1.9 features"
updates2 = "Added new features"
updates3 = "Chatbot is not fully analytical"
updates4 = "Chatbot is now coded in subsystems"


ter_dict = {

    "<cmd:ter>", "<cmd:teron>", "<cmd:teroff>"

}

help_dict = {

    "<cmd:help>", "<cmd:help-teron>", "<cmd:help-teroff>",
    "<cmd:help-ter>", "<cmd:help->", "<cmd:help-help>",
    "<cmd:help-verbose>", "<cmd:help-ulog>", "<cmd:help-ver>",
    "<cmd:help-tutor>", "<cmd:help-clearc>", "<cmd:help-clearm>",
    "<cmd:help-clog>", "<cmd:help-cmem>", "<cmd:help-perm>",
    "<cmd:help-py>"

}


abtbot_dict = {

    "<cmd:ver>", "<cmd:ulog>"

}

mem_dict = {

    "<cmd:cmem>", "<cmd:clearm>"

}

chatlog_dict = {

    "<cmd:clog>", "<cmd:clearc>"

}

cls_dict = {

    "<cmd:cls>"

}


pyexe_dict = {

    "<cmd:py>"

}

perm_dict = {

    "<cmd:vc --y>", "<cmd:allowpy --y>",
    "<cmd:allowpyexe --y>", "<cmd:vc --n>",
    "<cmd:allowpy --n>", "<cmd:allowpyexe --n>"

}

all_cmds = {

    "<cmd:ter>", "<cmd:teron>", "<cmd:teroff>",
    "<cmd:help>", "<cmd:help-teron>", "<cmd:help-teroff>",
    "<cmd:help-ter>", "<cmd:help->", "<cmd:help-help>",
    "<cmd:help-verbose>", "<cmd:help-ulog>", "<cmd:help-ver>",
    "<cmd:help-tutor>", "<cmd:help-clearc>", "<cmd:help-clearm>",
    "<cmd:help-clog>", "<cmd:help-cmem>", "<cmd:help-perm>",
    "<cmd:help-py>", "<cmd:ver>", "<cmd:ulog>",
    "<cmd:cmem>", "<cmd:clearm>", "<cmd:clog>",
    "<cmd:clearc>", "<cmd:py>", "<cmd:vc --y>",
    "<cmd:allowpy --y>", "<cmd:allowpyexe --y>","<cmd:vc --n>",
    "<cmd:allowpy --n>", "<cmd:allowpyexe --n>", "<cmd:cls>"
    
}

#Total lines (Variables.py + Glass.py)
# = 955 (In copy)
# IDK if there are any bugs in
# this, but THIS TOOK 36 PAGES.
# In laptop, it took 757 lines, AND IN BOTH COPY AND BOOK, IT IS THE LONGEST PROGRAM I HAVE EVER WRITTEN.
# AND IT IS STILL JUST A SUBSYSTEM.