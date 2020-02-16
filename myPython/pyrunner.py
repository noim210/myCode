import sys
from io import StringIO

def pyrun(data,isfile=False,notestcase=100,ain='a.in',aout='a.out'):

    if (isfile==True):
        scode=filetostr(data)
    else:
        scode=data

    scode =  addcleaninput(scode)
    originp=sys.stdin
    origout = sys.stdout
    with open(ain, "r") as fin:
        sys.stdin = fin
        with open(aout, "w") as fout:
            sys.stdout = fout
            try:
                print("::@-Start-")
                for i in range(notestcase):
                    exec(scode, {})
                    print("\n::@-----")
            except SyntaxError:
                print("ERROR::CompilingError::SyntaxError")
            except NameError:
                print("ERROR::CompilingError::NameError")
            except ZeroDivisionError:
                print("ERROR::RuntimeError::ZeroDivisionError")
            except TypeError:
                print("ERROR::CompilingError::TypeError")
            except ValueError:
                print("ERROR::CompilingError::ValueError")
            except RuntimeError:
                print("ERROR::RuntimeError::RuntimeError")
            except EOFError:
                print("\n::@-End-")
            except :
                print("ERROR::CompilingError::CompilingError")
            finally:
                print("\n::@-End-")
                sys.stdin = originp
                sys.stdout = origout

def pyruntostr(data,isfile=False,notestcase=100,ain='a.in',aout='a.out'):

    if (isfile==True):
        scode=filetostr(data)
    else:
        scode=data

    scode =  addcleaninput(scode)
    originp=sys.stdin
    origout = sys.stdout
    with open(ain, "r") as fin:
        sys.stdin = fin
        sys.stdout = myiostr = StringIO()
        try:
            print("::@-Start-")
            for i in range(notestcase):
                exec(scode, {})
                print("\n::@-----")
        except SyntaxError:
            print("ERROR::CompilingError::SyntaxError")
        except NameError:
            print("ERROR::CompilingError::NameError")
        except ZeroDivisionError:
            print("ERROR::RuntimeError::ZeroDivisionError")
        except TypeError:
            print("ERROR::CompilingError::TypeError")
        except ValueError:
            print("ERROR::CompilingError::ValueError")
        except RuntimeError:
            print("ERROR::RuntimeError::RuntimeError")
        except EOFError:
            print("\n::@-End-")
        except :
            print("ERROR::CompilingError::CompilingError")
        finally:
            print("\n::@-End-")
            sys.stdin = originp
            sys.stdout = origout
    
    soutput = myiostr.getvalue();
    return soutput



def filetostr(fname):
    with open(fname,'r') as file:
        data = file.read()
    return data

def cleanfiledata(fname):
    sret=""
    blank=""
    with open(fname) as fp:
        line = fp.readline()
        while line:
            if(line=="\n"):
                blank+=line
            elif line[:3]=='::@':
                blank=""
            else:
                sret+=(blank+line)
                blank=""
            line = fp.readline()
    #print(sret)
    return sret

def cleanstrdata(data):
    lines = data.split('\n')
    sret=""
    blank=""
    for line in lines:
        if(line==""):
            blank+="\n"
        elif line[:3]=='::@':
            blank=""
        else:
            sret+=(blank+line+"\n")
            blank=""
    #print(sret)
    return sret

def compare2str(str1,str2):
    lines1 = str1.split('\n')
    lines2 = str2.split('\n')
    ilen = len(lines1)

    if(ilen!=len(lines2)):
        return False

    for i in range(ilen):
        if(lines1[i]!=lines2[i]):
            return False;
    return True

def compare2str_soft(str1,str2):
    lines1 = str1.split('\n')
    lines2 = str2.split('\n')
    ilen = len(lines1)
    ilen2 = len(lines2)

    if(abs(ilen-ilen2)<=1):
        ilen=min(ilen,ilen2)
    else:
        return False

    for i in range(ilen):
        if(lines1[i]!=lines2[i]):
            return False;
    return True

def addcleaninput(scode):
    sprefix = ("\nimport builtins\n"
                "def input(par=\'\'):\n"
                "    return builtins.input()\n\n")
    sret= sprefix+scode
    #print(sret)
    return sret


