#!/usr/bin/python
import os
import re
import pathlib
import argparse
import subprocess
from py_anki import AnkiApi

fnroot="/home/chrome/notes/"
fname = "README.md"
anki = AnkiApi()

parse = argparse.ArgumentParser(allow_abbrev=True)
parse.add_argument('--topic', type=str, required=True)
parse.add_argument('--stopic', type=str, required=True)
parse.add_argument('--element', type=str, required=True)
parse.add_argument('--mode', type=str, required=True)
args = parse.parse_args()


def mkdir(froot):
    if not os.path.exists(froot): 
        os.makedirs(froot)


def inputent(fnroot, topic, stopic, element, mstr, mode, fname, commit):
    fmpath = os.path.join(fnroot,topic,stopic,element,mstr,mode)
    fnpath = os.path.join(fmpath,fname)
    mkdir(fmpath)
    if  not os.path.exists(fnpath):
        pathlib.Path(fnpath).touch()
    subprocess.run(["nvim", fnpath])
    subprocess.run(["git", "add", fnpath])
    subprocess.run(["git", "commit", "-m", commit])
    
def adrv(fnroot,topic,stopic,element,mstr,mode,fname,dckhie,memcit):
    file = open(os.path.join(fnroot,topic,stopic,element,mstr,mode,fname))
    lines = file.readlines()
    linect = []
    linefr = []
    parabr = []
    strbra = """ """

    for index,value in enumerate(lines):
        if ":" in value:
            linect.append(index)
            linefr.append(re.sub(':',' ',value))
   
    for index,value in enumerate(linect):
        strcra = """ """
        if value == linect[-1] : break
        strlst = lines[value+1:linect[index+1]-1]
        for value in strlst:
            strcra = strcra + value
        parabr.append(strcra)

    for value in range(linect[-1]+1,len(lines)):
        strbra = strbra + lines[value]
    parabr.append(strbra) 

    file.close()
    model = "Basic"
    deck = "pool" + "::" + topic + "::" + stopic + "::" + element + "::" + mstr + "::" + mode
    tags = [topic,stopic,element,element+mstr,element+mode]
    query = anki.create_deck(deck)
    try:
        anki.exec(query)
    except Exception:
        pass
    for index,value in enumerate(linefr):
        try:
            note = anki.create_note([memcit[0] + value + " in " + memcit[1] ,parabr[index]],deck,model,tags=tags)
            anki.exec(note)
        except Exception:
            pass


def aexp(fnroot,topic,stopic,element,mstr,mode,fname,dckhie,memcit):
    file = open(os.path.join(fnroot,topic,stopic,element,mstr,mode,fname))
    lines = file.readlines()
    cardfr = []
    cardbr = []

    for index in lines:
        if ':' not in index : continue
        charst = index.find(':')
        cardfr.append(index[0:charst])
        cardbr.append(index[charst+1:-1])
    
    file.close()

    model = "Basic"
    deck = "pool" + "::" + topic + "::" + stopic + "::" + element + "::" + mstr + "::" + mode
    tags = [topic,stopic,element,element+mstr,element+mode]
    query = anki.create_deck(deck)
    try:
        anki.exec(query)
    except Exception:
        pass
    for index,value in enumerate(cardfr):
        try:
            note = anki.create_note([memcit[0] + value + " in " + memcit[1],cardbr[index]],deck,model,tags=tags)
            anki.exec(note)
        except Exception:
            pass


def ahmemcit(fnroot,topic,stopic,element,mstr,mode,fname,dckhie,memcit):
    file = open(os.path.join(fnroot,topic,stopic,element,mstr,mode,fname))
    lines = file.readlines()
    linect = []
    linefr = []
    parabr = []
    strbra = """ """

    for index,value in enumerate(lines):
        if ":" in value:
            linect.append(index)
            linefr.append(re.sub(':',' ',value))
   
    for index,value in enumerate(linect):
        strcra = """ """
        if value == linect[-1] : break
        strlst = lines[value+1:linect[index+1]-1]
        for value in strlst:
            strcra = strcra + value
        parabr.append(strcra)

    for value in range(linect[-1]+1,len(lines)):
        strbra = strbra + lines[value]
    parabr.append(strbra) 

    file.close()
    model = "Basic"
    deck = "pool" + "::" + topic + "::" + stopic + "::" + element + "::" + mstr + "::" + mode
    tags = [topic,stopic,element,element+mstr,element+mode]
    try:
        query = anki.create_deck(deck)
    except Exception:
        pass
    anki.exec(query)
    for index,value in enumerate(linefr):
        try:
            note = anki.create_note([value + " in " + memcit[0] ,parabr[index]],deck,model,tags=tags)
            anki.exec(note)
        except Exception:
            pass


def apst(fnroot,topic,stopic,element,mstr,mode,fname,dckhie,memcit):
    file = open(os.path.join(fnroot,topic,stopic,element,mstr,mode,fname))
    lines = file.readlines()
    linect = []
    linefr = []
    parabr = []
    strbra = """ """

    for index,value in enumerate(lines):
        if ":" in value:
            linect.append(index)
            linefr.append(re.sub(':',' ',value))
   
    for index,value in enumerate(linect):
        strcra = """ """
        if value == linect[-1] : break
        strlst = lines[value+1:linect[index+1]-1]
        for value in strlst:
            strcra = strcra + value
        parabr.append(strcra)

    for value in range(linect[-1]+1,len(lines)):
        strbra = strbra + lines[value]
    parabr.append(strbra) 

    file.close()
    model = "Basic"
    deck = "pst" + "::" + topic + "::" + stopic + "::" + element + "::" + mstr + "::" + mode
    tags = [topic,stopic,element,element+mstr,element+mode]
    query = anki.create_deck(deck)
    try:
        anki.exec(query)
    except Exception:
        pass
    for index,value in enumerate(linefr):
        try:
            note = anki.create_note([memcit[0] + value + " in " + memcit[1] ,parabr[index]],deck,model,tags=tags)
            anki.exec(note)
        except Exception:
            pass



if __name__ == '__main__':
    if args.mode == "drv":
        commit = "Add derivations for " + args.element + " in " + args.stopic 
        memcit = ["How to derive the expression of ", args.element, args.stopic] 
        dckhie = [args.topic, args.stopic, args.element, "mchar", "drv"]
        inputent(fnroot, args.topic, args.stopic, args.element, "mchar", args.mode, fname ,commit)
        adrv(fnroot,args.topic,args.stopic,args.element,"mchar",args.mode,fname,dckhie,memcit)

    if args.mode == "exp":
        commit = "Add expressions for " + args.element + " in " + args.stopic 
        memcit = ["What is the expression of  ", args.element, args.stopic] 
        dckhie = [args.topic, args.stopic, args.element, "mchar", "exp"]
        inputent(fnroot, args.topic, args.stopic, args.element, "mchar", args.mode, fname ,commit)
        aexp(fnroot,args.topic,args.stopic,args.element,"mchar",args.mode,fname,dckhie,memcit)


    if args.mode == "pst":
        commit = "Add problem set entries for " + args.element + " in " + args.stopic
        memcit = [ "Review problem for ", args.element, args.stopic ]
        dckhie = [args.topic, args.stopic, args.element, "mchar", "pst"]
        inputent(fnroot, args.topic, args.stopic, args.element, "mchar", args.mode, fname ,commit)
        apst(fnroot,args.topic,args.stopic,args.element,"mchar",args.mode,fname,dckhie,memcit)


    if args.mode == "pss":
        commit = "Add problem solving stat for " + args.element + " in " + args.stopic 
        memcit = ["What is the general strategy to ", args.element, args.stopic] 
        dckhie = [args.topic, args.stopic, args.element, "mchar", "pss"]
        inputent(fnroot, args.topic, args.stopic, args.element, "mchar", args.mode, fname ,commit)
        adrv(fnroot,args.topic,args.stopic,args.element,"mchar",args.mode,fname,dckhie,memcit)


    if args.mode == "fct":
        commit = "Add fact as " + args.element + " in " + args.stopic 
        memcit = ["What is the ", args.element, args.stopic] 
        dckhie = [args.topic, args.stopic, args.element, "stint", "fct"]
        inputent(fnroot, args.topic, args.stopic, args.element, "stint", args.mode, fname, commit )
        aexp(fnroot,args.topic,args.stopic,args.element,"stint",args.mode,fname,dckhie,memcit)


    if args.mode == "trm":
        commit = "Add terms for " + args.element + " in " + args.stopic 
        memcit = ["What do you mean by ", args.element, args.stopic] 
        dckhie = [args.topic, args.stopic, args.element, "stint", "trm"]
        inputent(fnroot, args.topic, args.stopic, args.element, "stint", args.mode, fname, commit )
        aexp(fnroot,args.topic,args.stopic,args.element,"stint",args.mode,fname,dckhie,memcit)


    if args.mode == "tre":
        commit = "Add term surrogate for " + args.element + " in " + args.stopic 
        memcit = [args.element, args.stopic]
        dckhie = [args.topic, args.stopic, args.element, "stint", "tre"]
        inputent(fnroot, args.topic, args.stopic, args.element, "stint", args.mode, fname, commit )
        ahmemcit(fnroot,args.topic,args.stopic,args.element,"stint",args.mode,fname,dckhie,memcit)


    if args.mode == "mll":
        commit = "Add multi lines for " + args.element + " in " + args.stopic 
        memcit = [args.element, args.stopic]
        dckhie = [args.topic, args.stopic, args.element, "stint", "mll"]
        inputent(fnroot, args.topic, args.stopic, args.element, "stint", args.mode, fname, commit )
        ahmemcit(fnroot,args.topic,args.stopic,args.element,"stint",args.mode,fname,dckhie,memcit)


    if args.mode == "res":
        commit = "Add reasons for " + args.element + " in " + args.stopic 
        memcit = [args.element, args.stopic]
        dckhie = [args.topic, args.stopic, args.element, "stint", "res"]
        inputent(fnroot, args.topic, args.stopic, args.element, "stint", args.mode, fname, commit )
        ahmemcit(fnroot,args.topic,args.stopic,args.element,"stint",args.mode,fname,dckhie,memcit)






