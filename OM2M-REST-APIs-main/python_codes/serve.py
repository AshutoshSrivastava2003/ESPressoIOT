from oneM2M_functions import *

uriCse="http://127.0.0.1:8080/~/in-cse/in-name"

ae="Final_Dt"

create_ae(uriCse,ae)

uriAe=uriCse+'/'+ae
cnt="N1"

create_cnt(uriAe,cnt)