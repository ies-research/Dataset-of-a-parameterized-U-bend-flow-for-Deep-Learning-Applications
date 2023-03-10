
from math import cos, sin, pi
import sys

class export_blockmesh_file:
    def __init__(self, params, path):
        self.CAX =  2*params[0] -1
        self.CAY =  2*params[1] -1
        self.DAX =  2*params[2] -1
        self.DAY =  2*params[3] -1
        self.EAX =  2*params[4] -1
        self.EAY =  2*params[5] -1
        self.CMX =    params[6] 
        self.CMY =  2*params[7] -1 
        self.DMX =  2*params[8] -1
        self.DMY =    params[9] 
        self.EMX =    params[10] 
        self.EMY =  2*params[11] -1
        self.BCAAY =  params[12]
        self.BCBAY =  params[13]
        self.CDAAY =  params[14]
        self.CDBAX =  params[15]
        self.DEAAX =  params[16]
        self.DEBAY =  params[17]
        self.EFAAY =  params[18]
        self.EFBAY =  params[19]
        self.BCAMY =  params[20]
        self.BCBMY =  params[21]
        self.CDAMY =  params[22]
        self.CDBMX =  params[23]
        self.DEAMX =  params[24]
        self.DEBMY =  params[25]
        self.EFAMY =  params[26]
        self.EFBMY =  params[27]
        self.path = path
        self.calc_params()

    def calc_params(self):
        diameter=0.075
        r=0.5*diameter
        t=0.05*diameter
        L=10.0*diameter

        H1=0.13*diameter
        H2=0.26*diameter
        H3=1.26*diameter

        L1=0.5*diameter
        L2=1*diameter
        L3=2*diameter

        aix=-H1
        aiy=L

        bix=-H1
        biy=L3

        cix=-H1
        ciy=0

        dix= 0
        diy=-H1

        eix=H1
        eiy=0

        fix=H1
        fiy=L3

        gix=H1
        giy=L

        amx=-H2
        amy=L

        bmx=-H2
        bmy=L3

        cmx=-H2-0.25*diameter*self.CMX
        cmy=0.25*diameter*self.CMY

        bcAmx=bmx
        bcAmy=bmy+(cmy-bmy)* self.BCAMY

        bcBmx=cmx
        bcBmy=cmy+(bmy-cmy)*self.BCBMY

        dmx=0.5*H2*self.DMX
        dmy=-H2-0.5*H2*self.DMY

        cdAmx=cmx
        cdAmy=0.55228475*dmy+(dmy-0.55228475*dmy)*self.CDAMY

        cdBmx=0.55228475*cmx+(cmx-0.55228475*cmx)*self.CDBMX
        cdBmy=dmy

        emx=H2+0.25*diameter*self.EMX
        emy=0.25*diameter*self.EMY

        deAmx=0.55228475*emx+(emx-0.55228475*emx)*self.DEAMX
        deAmy=dmy

        deBmx=emx
        deBmy=0.55228475*dmy+(dmy-0.55228475*dmy)*self.DEBMY

        fmx=H2
        fmy=L3

        efAmx=emx
        efAmy=emy+(fmy-emy)*self.EFAMY

        efBmx=fmx
        efBmy=fmy+(emy-fmy)*self.EFBMY

        gmx=H2
        gmy=L

        aax=-H3
        aay=L

        bax=bmx-diameter
        bay=L3

        cax=cmx-diameter-self.CAX*0.375*diameter
        cay=0.375*diameter*self.CAY

        bcAax=bax
        bcAay=bay+(cay-bay)*self.BCAAY

        bcBax=cax
        bcBay=cay+(bay-cay)*self.BCBAY

        dax=self.DAX*0.375*diameter
        day=dmy-diameter-self.DAY*0.375*diameter

        cdAax=cax
        cdAay=cay+(day-cay)*self.CDAAY

        cdBax=dax+(cax-dax)*self.CDBAX
        cdBay=day

        eax=emx+diameter+self.EAX*0.375*diameter
        eay=0.375*diameter*self.EAY

        deAax=dax+(eax-dax)*self.DEAAX
        deAay=day

        deBax=eax
        deBay=eay+(day-eay)*self.DEBAY

        fax=fmx+diameter
        fay=L3

        efAax=eax
        efAay=eay+(fay-eay)*self.EFAAY

        efBax=fax
        efBay=fay+(eay-fay)*self.EFBAY

        gax=H3
        gay=L

        abAix=aix
        abAiy=amy/3

        abBix=aix
        abBiy=2*amy/3

        abAmx=amx
        abAmy=abAiy

        abBmx=amx
        abBmy=abBiy

        abAax=aax
        abAay=abAiy

        abBax=aax
        abBay=abBiy

        bcAix=aix
        bcAiy=efAmy
        bcBix=aix
        bcBiy=efBmy

        fgAix=gix
        fgAiy=gmy/3

        fgBix=gix
        fgBiy=2*gmy/3

        fgAmx=gmx
        fgAmy=fgAiy

        fgBmx=gmx
        fgBmy=fgBiy

        fgAax=gax
        fgAay=fgAiy

        fgBax=gax
        fgBay=fgBiy

        efAix=gix
        efAiy=efAmy
        efBix=gix
        efBiy=efBmy

        r1=sin(pi/4)*H1
        r11=-r1

        f = open(f"{self.path}/para.in", "w")
        f.write("diameter " +str(diameter) + ";"+"\n")
        f.write("r        " +str(r       ) + ";"+"\n")
        f.write("t        " +str(t       ) + ";"+"\n")
        f.write("L        " +str(L       ) + ";"+"\n")
        f.write("H1       " +str(H1      ) + ";"+"\n")
        f.write("H2       " +str(H2      ) + ";"+"\n")
        f.write("H3       " +str(H3      ) + ";"+"\n")
        f.write("L1       " +str(L1      ) + ";"+"\n")
        f.write("L2       " +str(L2      ) + ";"+"\n")
        f.write("L3       " +str(L3      ) + ";"+"\n")
        f.write("r1       " +str(r1      ) + ";"+"\n")
        f.write("r11      " +str(r11     ) + ";"+"\n")
        f.write("aix      " +str(aix     ) + ";"+"\n")
        f.write("aiy      " +str(aiy     ) + ";"+"\n")
        f.write("bix      " +str(bix     ) + ";"+"\n")
        f.write("biy      " +str(biy     ) + ";"+"\n")
        f.write("cix      " +str(cix     ) + ";"+"\n")
        f.write("ciy      " +str(ciy     ) + ";"+"\n")
        f.write("dix      " +str(dix     ) + ";"+"\n")
        f.write("diy      " +str(diy     ) + ";"+"\n")
        f.write("eix      " +str(eix     ) + ";"+"\n")
        f.write("eiy      " +str(eiy     ) + ";"+"\n")
        f.write("fix      " +str(fix     ) + ";"+"\n")
        f.write("fiy      " +str(fiy     ) + ";"+"\n")
        f.write("gix      " +str(gix     ) + ";"+"\n")
        f.write("giy      " +str(giy     ) + ";"+"\n")
        f.write("amx      " +str(amx     ) + ";"+"\n")
        f.write("amy      " +str(amy     ) + ";"+"\n")
        f.write("bmx      " +str(bmx     ) + ";"+"\n")
        f.write("bmy      " +str(bmy     ) + ";"+"\n")
        f.write("cmx      " +str(cmx     ) + ";"+"\n")
        f.write("cmy      " +str(cmy     ) + ";"+"\n")
        f.write("dmx      " +str(dmx     ) + ";"+"\n")
        f.write("dmy      " +str(dmy     ) + ";"+"\n")
        f.write("emx      " +str(emx     ) + ";"+"\n")
        f.write("emy      " +str(emy     ) + ";"+"\n")
        f.write("fmx      " +str(fmx     ) + ";"+"\n")
        f.write("fmy      " +str(fmy     ) + ";"+"\n")
        f.write("gmx      " +str(gmx     ) + ";"+"\n")
        f.write("gmy      " +str(gmy     ) + ";"+"\n")
        f.write("fgAmx      " +str(fgAmx     ) + ";"+"\n")
        f.write("fgAmy      " +str(fgAmy     ) + ";"+"\n")
        f.write("fgBmx      " +str(fgBmx     ) + ";"+"\n")
        f.write("fgBmy      " +str(fgBmy     ) + ";"+"\n")
        f.write("aax      " +str(aax     ) + ";"+"\n")
        f.write("aay      " +str(aay     ) + ";"+"\n")
        f.write("bax      " +str(bax     ) + ";"+"\n")
        f.write("bay      " +str(bay     ) + ";"+"\n")
        f.write("cax      " +str(cax     ) + ";"+"\n")
        f.write("cay      " +str(cay     ) + ";"+"\n")
        f.write("dax      " +str(dax     ) + ";"+"\n")
        f.write("day      " +str(day     ) + ";"+"\n")
        f.write("eax      " +str(eax     ) + ";"+"\n")
        f.write("eay      " +str(eay     ) + ";"+"\n")
        f.write("fax      " +str(fax     ) + ";"+"\n")
        f.write("fay      " +str(fay     ) + ";"+"\n")
        f.write("gax      " +str(gax     ) + ";"+"\n")
        f.write("gay      " +str(gay     ) + ";"+"\n")
        f.write("fgAax      " +str(fgAax     ) + ";"+"\n")
        f.write("fgAay      " +str(fgAay     ) + ";"+"\n")
        f.write("fgBax      " +str(fgBax     ) + ";"+"\n")
        f.write("fgBay      " +str(fgBay     ) + ";"+"\n")
        f.write("bcAax      " +str(bcAax     ) + ";"+"\n")
        f.write("bcAay      " +str(bcAay     ) + ";"+"\n")
        f.write("bcBax      " +str(bcBax     ) + ";"+"\n")
        f.write("bcBay      " +str(bcBay     ) + ";"+"\n")
        f.write("bcAmx      " +str(bcAmx     ) + ";"+"\n")
        f.write("bcAmy      " +str(bcAmy     ) + ";"+"\n")
        f.write("bcBmx      " +str(bcBmx     ) + ";"+"\n")
        f.write("bcBmy      " +str(bcBmy     ) + ";"+"\n")
        f.write("cdAax      " +str(cdAax     ) + ";"+"\n")
        f.write("cdAay      " +str(cdAay     ) + ";"+"\n")
        f.write("cdBax      " +str(cdBax     ) + ";"+"\n")
        f.write("cdBay      " +str(cdBay     ) + ";"+"\n")
        f.write("cdAmx      " +str(cdAmx     ) + ";"+"\n")
        f.write("cdAmy      " +str(cdAmy     ) + ";"+"\n")
        f.write("cdBmx      " +str(cdBmx     ) + ";"+"\n")
        f.write("cdBmy      " +str(cdBmy     ) + ";"+"\n")
        f.write("deAax      " +str(deAax     ) + ";"+"\n")
        f.write("deAay      " +str(deAay     ) + ";"+"\n")
        f.write("deBax      " +str(deBax     ) + ";"+"\n")
        f.write("deBay      " +str(deBay     ) + ";"+"\n")
        f.write("deAmx      " +str(deAmx     ) + ";"+"\n")
        f.write("deAmy      " +str(deAmy     ) + ";"+"\n")
        f.write("deBmx      " +str(deBmx     ) + ";"+"\n")
        f.write("deBmy      " +str(deBmy     ) + ";"+"\n")
        f.write("efAax      " +str(efAax     ) + ";"+"\n")
        f.write("efAay      " +str(efAay     ) + ";"+"\n")
        f.write("efBax      " +str(efBax     ) + ";"+"\n")
        f.write("efBay      " +str(efBay     ) + ";"+"\n")
        f.write("efAmx      " +str(efAmx     ) + ";"+"\n")
        f.write("efAmy      " +str(efAmy     ) + ";"+"\n")
        f.write("efBmx      " +str(efBmx     ) + ";"+"\n")
        f.write("efBmy      " +str(efBmy     ) + ";"+"\n")
        f.write("fgAix      " +str(fgAix     ) + ";"+"\n")
        f.write("fgAiy      " +str(fgAiy     ) + ";"+"\n")
        f.write("fgBix      " +str(fgBix     ) + ";"+"\n")
        f.write("fgBiy      " +str(fgBiy     ) + ";"+"\n")
        f.write("abAix      " +str(abAix     ) + ";"+"\n")
        f.write("abAiy      " +str(abAiy     ) + ";"+"\n")
        f.write("abBix      " +str(abBix     ) + ";"+"\n")
        f.write("abBiy      " +str(abBiy     ) + ";"+"\n")
        f.write("abAmx      " +str(abAmx     ) + ";"+"\n")
        f.write("abAmy      " +str(abAmy     ) + ";"+"\n")
        f.write("abBmx      " +str(abBmx     ) + ";"+"\n")
        f.write("abBmy      " +str(abBmy     ) + ";"+"\n")
        f.write("abAax      " +str(abAax     ) + ";"+"\n")
        f.write("abAay      " +str(abAay     ) + ";"+"\n")
        f.write("abBax      " +str(abBax     ) + ";"+"\n")
        f.write("abBay      " +str(abBay     ) + ";"+"\n")
        f.write("bcAix      " +str(bcAix     ) + ";"+"\n")
        f.write("bcAiy      " +str(bcAiy     ) + ";"+"\n")
        f.write("bcBix      " +str(bcBix     ) + ";"+"\n")
        f.write("bcBiy      " +str(bcBiy     ) + ";"+"\n")
        f.write("efAix      " +str(efAix     ) + ";"+"\n")
        f.write("efAiy      " +str(efAiy     ) + ";"+"\n")
        f.write("efBix      " +str(efBix     ) + ";"+"\n")
        f.write("efBiy      " +str(efBiy     ) +";")
        f.close()

        g = open(f"{self.path}/params.in", "w")
        g.write(str(self.CAX)+"\n")
        g.write(str(self.CAY)+"\n")
        g.write(str(self.DAX)+"\n")
        g.write(str(self.DAY)+"\n")
        g.write(str(self.EAX)+"\n")
        g.write(str(self.EAY)+"\n")
        g.write(str(self.CMX)+"\n")
        g.write(str(self.CMY)+"\n")
        g.write(str(self.DMX)+"\n")
        g.write(str(self.DMY)+"\n")
        g.write(str(self.EMX)+"\n")
        g.write(str(self.EMY)+"\n")
        g.write(str(self.BCAAY)+"\n")
        g.write(str(self.BCBAY)+"\n")
        g.write(str(self.CDAAY)+"\n")
        g.write(str(self.CDBAX)+"\n")
        g.write(str(self.DEAAX)+"\n")
        g.write(str(self.DEBAY)+"\n")
        g.write(str(self.EFAAY)+"\n")
        g.write(str(self.EFBAY)+"\n")
        g.write(str(self.BCAMY)+"\n")
        g.write(str(self.BCBMY)+"\n")
        g.write(str(self.CDAMY)+"\n")
        g.write(str(self.CDBMX)+"\n")
        g.write(str(self.DEAMX)+"\n")
        g.write(str(self.DEBMY)+"\n")
        g.write(str(self.EFAMY)+"\n")
        g.write(str(self.EFBMY))
        g.close()


