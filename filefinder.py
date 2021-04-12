import os
'''
parameters:
root=root folder to search from
substr=substring for file, can be extensions as well e.g. '.png'
exception=optional argument to esxclude files located in specific subpaths (e.g. 'bkp' will escludes files located anywhere with 'bkp' in the filepath from root)
'''
def filefinder(root,substr,exception=''):
    filelst=[]
    for i in os.walk(root):
        for j in i[2]:
            if substr in j and exception!='' and exception not in i[0]:
                filelst.append(i[0]+os.sep+j)
    return filelst
