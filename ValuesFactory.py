from bitstring import *
from  MathHelperFunctions import *
from itertools import *
from collections import *

def InitializeBox3_Box8():
    Box3 = {}
    
    Box3['def_drv1'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box3['stare_drv1'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box3['temp_l1'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box3['temp_h1'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box3['def_drv2'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box3['stare_drv2'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box3['temp_l2'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box3['temp_h2'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box4 = {}
    Box4['def_drv3'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box4['stare_drv3'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box4['temp_l3'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box4['temp_h3'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box4['def_drv4'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box4['stare_drv4'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box4['temp_l4'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box4['temp_h4'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box5 = {}
    Box5['def_drv5'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box5['stare_drv5'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box5['temp_l5'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box5['temp_h5'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box5['def_drv6'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box5['stare_drv6'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box5['temp_l6'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box5['temp_h6'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box6 = {}
    Box6['u_drv'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['dsp_drv'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['trip14'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['trip56'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['stare_mm'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['inp_63'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['defect_can_drv'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['stare_abs'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box6['rez_mm1'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    
    Box7 = {}
    Box7['temp_mt2'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box7['temp_mt1'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box7['nivel_apa'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box7['temp_mt3'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box7['temp_apa_r'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box7['temp_apa_c'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box7['pres_aer_rad'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'mm'}
    Box7['pres_apa'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'bar'}
    Box8 = {}
    Box8['temp_aer_mt'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    Box8['pres_aer_mt'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'mm'}
    Box8['inp_num_ABS'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None}
    Box8['umid_aer_mt'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'%'}
    Box8['vibr_Y'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'m/s2'}
    Box8['vibr_X'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'m/s2'}
    Box8['ipm'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'mA'}
    Box8['rez_mm3'] = {'S1':None,'S2':None, 'S3':None, 'S4':None, 'S5':None, 'S6':None, 'UM':'gC'}
    
    return (Box3, Box4, Box5, Box6, Box7, Box8)
       
    
def GetValuesFromIcol(icol, Boxuri, type_of_file_out = "json"):
    """ 
        Intoarce un dictionar de forma "{marime1:{'val':<valoare>, 'UM':<UM>},.... }
        unde <valoare poate fi:
           - un array (pot fi si valori binare inp_num etc, )
           - o valoare unitara
           - un nou dictionar de forma {S1:<val_S1>, S2:<val_S2, ...}
             
    """
    icol_return = {}
    
    Box3 = Boxuri[0]   
    Box4 = Boxuri[1]
    Box5 = Boxuri[2]
    Box6 = Boxuri[3]
    Box7 = Boxuri[4]
    Box8 = Boxuri[5]
    
    
    identificator = icol[2:4] 

    
    secunde = icol[4:6]
    minute = icol[6:8]
    ora = icol [8:10]
    
    inp_num = [Bits('0x' + icol[i:i+2]).bin for i in range(10,34,2)] # am ramas la 34
    out_num = [Bits('0x' + icol[i:i+2]).bin for i in range(34,46,2)] #44
    
    inp_num = {'val': inp_num, 'UM':'hex'}
    icol_return['inp_num']=inp_num
    out_num = {'val': out_num, 'UM':'hex'}
    icol_return['out_num'] = out_num
    
    
    icol_return['mansa_activa_numerice'] ={'val' :'0x' +  icol[46:48], 'UM':'hex'}

    stare_ceta_array = ['0x'+ icol[i:i+2] for i in range(108,396,48)]
   
    stare_ceta = {'val':stare_ceta_array, 'UM':'hex'}
    icol_return['stare_ceta'] = stare_ceta
    
    stare_stare_array = ['0x'+ icol[i:i+2] for i in range(110,398,48)]
    stare_stare = {'val':stare_stare_array, 'UM':'hex'}
    icol_return['stare_stare'] = stare_stare
        
    icol_return['mansa_activa_forta'] = {'val':'0x' + icol[48:50], 'UM':'hex'}
    icol_return['mansa_activa_viteza'] = {'val': icol[50:52], 'UM':'kmh'}
    icol_return['viteza_impusa'] ={'val': icol[52:54], 'UM':'kmh'}
    
    u_cat =  Bits('0x' + icol[54:56]).uint   
    icol_return['u_cat_icol'] = {'val':PercentValueCustomScale(u_cat, 0,255,0,50), 'UM':'kV'} 
    
    usa = Bits('0x' + icol[56:58]).uint
    icol_return['u_sa_icol'] = {'val':PercentValueCustomScale(usa, 0,255,0,777), 'UM':'V'}
     
    icat = Bits('0x'+ icol[58:60]).uint
    icol_return['i_cat'] = {'val':PercentValueCustomScale(icat, 0,255,0,777),'UM':'A'}
     
    itren = Bits('0x'+ icol[60:62]).uint
    icol_return['i_tren'] = {'val':PercentValueCustomScale(itren, 0,255,0,933),'UM':'A'} 
    
    ibat = Bits('0x'+ icol[62:64]).uint
    icol_return['i_bat'] = {'val':PercentValueCustomScale(ibat, 0,172,-25,25),'UM':'A'} 
    
    pcg = Bits('0x'+ icol[64:66]).uint
    icol_return['p_cg'] = {'val':PercentValueCustomScale(pcg, 26,255,0,12.72),'UM':'bar'} 
    
    vit1_ls = Bits('0x'+ icol[66:68]).bin
    vit1_ms_last3 = Bits('0x'+ icol[68:70]).bin[-3:]
    vit_1 = vit1_ms_last3 + vit1_ls
    icol_return['vit1'] = {'val':BitArray(bin=vit_1).uint/10.0, 'UM':'kmh'}
    
    vit2_ls = Bits('0x'+ icol[70:72]).bin
    vit2_ms_last3 = Bits('0x'+ icol[72:74]).bin[-3:]
    vit_2 = vit2_ms_last3 + vit2_ls
    icol_return['vit2'] = {'val':BitArray(bin=vit_2).uint/10.0,'UM':'kmh'}
    
    temp_trafo2 =  Bits('0x'+ icol[74:76]).uint
    icol_return['temp_trafo2']= {'val':PercentValueCustomScale(temp_trafo2, 26,134,-50,100), 'UM':'gC'}
    
    icol_return['stare_forta'] = {'val':'0x'+ icol[76:78], 'UM':'hex'}
    icol_return['stare_tractiune'] = {'val':'0x'+ icol[78:80], 'UM':'hex'}
    
    turatie_min_trac_ls = Bits('0x'+ icol[80:82]).bin
    turatie_min_trac_ms = Bits('0x'+ icol[82:84]).bin
    turatie_min_trac =  BitArray(bin = turatie_min_trac_ms + turatie_min_trac_ls).uint
    icol_return['turatie_min_trac'] = {'val':PercentValueCustomScale(turatie_min_trac, 0, 32767, 0, 8000), 'UM':'rpm'}
    
    turatie_max_trac_ls = Bits('0x'+ icol[84:86]).bin
    turatie_max_trac_ms = Bits('0x'+ icol[86:88]).bin
    turatie_max_trac =  BitArray(bin = turatie_max_trac_ms + turatie_max_trac_ls).uint
    icol_return['turatie_max_trac'] = {'val':PercentValueCustomScale(turatie_max_trac, 0, 32767, 0, 8000), 'UM':'rpm'}
    
    turatie_max_notrac_ls = Bits('0x'+ icol[88:90]).bin
    turatie_max_notrac_ms = Bits('0x'+ icol[90:92]).bin
    turatie_max_notrac =  BitArray(bin = turatie_max_notrac_ms + turatie_max_notrac_ls).uint
    icol_return['turatie_max_notrac'] = {'val':PercentValueCustomScale(turatie_max_notrac, 0, 32767, 0, 8000), 'UM':'rpm'}
    
    icol_return['info1'] = {'val':'0x'+ icol[92:94], 'UM':'hex'}
    icol_return['info2'] = {'val':'0x'+ icol[94:96], 'UM':'hex'}
    
    forta_cda_icol_ls = Bits('0x'+ icol[96:98]).bin
    forta_cda_icol_ms = Bits('0x'+ icol[98:100]).bin
    forta_cda_icol =  BitArray(bin = forta_cda_icol_ms + forta_cda_icol_ls).uint
    icol_return['forta_cda_icol'] = {'val':PercentValueCustomScale(forta_cda_icol, -2550, 4850, 255, 485), 'UM':'KN'}

    stare_4qc3ph_array = ['0x'+ icol[i:i+2] for i in range(112,400,48)]
    icol_return['stare_4qc3ph'] = {'val':stare_4qc3ph_array, 'UM':'hex'}
    
    bloc_soft_array = ['0x' + icol[i:i+2] for i in range(114,402,48)]
    icol_return['bloc_soft'] = {'val':bloc_soft_array, 'UM':'hex'}
    
    bloc_hard_array = ['0x' + icol[i:i+2] for i in range(116,404,48)]
    icol_return['bloc_hard'] = {'val':bloc_hard_array, 'UM':'hex'}
    
    decon_hard_array = ['0x' + icol[i:i+2] for i in range(118,406,48)]
    icol_return['decon_hard'] = {'val':decon_hard_array, 'UM':'hex'}
    
    inp_num_blocuri_array = ['0x' + icol[i:i+2] for i in range(120,408,48)]
    icol_return['inp_num_blocuri'] = {'val':inp_num_blocuri_array, 'UM':'hex'}
    
    tip_ceta_array = ['0x' + icol[i:i+2] for i in range(122,410,48)]
    icol_return['inp_num_blocuri'] = {'val':inp_num_blocuri_array, 'UM':'hex'}
    
    u_cat_array = [round(PercentValueCustomScale(Bits('0x' + icol[i:i+2]).uint,0,255,0,39.25),2)  for i in range(124,412,48)]
    icol_return['u_cat'] = {'val': u_cat_array, 'UM':'KVef'}

        
    irfm__i_in_array = [Bits('0x' + icol[i:i+2]).uint for i in range(126,414,48)]
    
    for k  in range(6):
        if stare_ceta_array[k] =="0x40":
            irfm__i_in_array[k] = round(PercentValueCustomScale(irfm__i_in_array[k], 0,255,0,2200),2)
            um = 'Aef'
        else:
            irfm__i_in_array[k] = round(PercentValueCustomScale(irfm__i_in_array[k], 0,255,0,1600),2)
            um = 'A'
    
    icol_return['irfm__i_in'] = {'val':irfm__i_in_array, 'UM':um}
        
    u_cc_array = [round(PercentValueCustomScale(Bits('0x' + icol[i:i+2]).uint, 0,255,0,2500),2)  for i in range(128,416,48)]
    icol_return['u_cc'] = {'val':u_cc_array, 'UM':'V'}
    
    u_sa_array = [round(PercentValueCustomScale(Bits('0x' + icol[i:i+2]).uint, 0,255,0,2500),2)  for i in range(130,418,48)]
    icol_return['u_sa'] = {'val':u_sa_array, 'UM':'V'}   
 
 
    
    def make_value_from_ms_and_ls(valori, min1,max1,min2,max2):
        if (valori[0] != '-') or (valori[1] != '-'): #este pusa pentru iq_mas si id_mas care pot prelua valori nule in cazul in care stare_ceta este 0xfe sau 0xe0 in blocul respectiv
            concat = BitArray(bin = valori[0] + valori[1]).uint
            return round(PercentValueCustomScale(concat,min1,max1,min2,max2),2)
       
    i_out_ls_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(132,420,48)]
    i_out_ms_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(134,422,48)]
    combined = zip(i_out_ms_array,i_out_ls_array)
    i_out_array = [make_value_from_ms_and_ls(combined[i], 0,32767,0,4525) for i in range(6)]
    icol_return['i_out'] = {'val': i_out_array, 'UM':'A'}
       
    v_cda_ls_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(136,424,48)]
    v_cda_ms_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(138,426,48)]
    combined = zip(v_cda_ms_array, v_cda_ls_array) 
    v_cda_array = [make_value_from_ms_and_ls(combined[i], -32767, 32767, -100, 100) for i in range(6)]
    icol_return['v_cda'] = {'val':v_cda_array, 'UM':'%'}

    turatie_ls_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(140,428,48)]
    turatie_ms_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(142,430,48)]
    combined = zip(turatie_ms_array, turatie_ls_array) 
    turatie_array = [make_value_from_ms_and_ls(combined[i], -32767, 32767, -8000, 8000) for i in range(6)]
    icol_return['turatie'] = {'val':turatie_array, 'UM':'rpm'}
   
    forta_cda_ls_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(144,432,48)]
    forta_cda_ms_array = [Bits('0x'+ icol[i:i+2]).bin for i in range(146,434,48)]
    combined = zip(forta_cda_ms_array, forta_cda_ls_array) 
    forta_cda_array = [BitArray(bin = combined[i][0] + combined[i][1]).uint for i in range(6)]
    icol_return['forta_cda'] = {'val':forta_cda_array, 'UM':'rpm'}    
    
    
    def face_valori_cauza(start_reading):         
        return_set = []
        for i in range(6):
            if (stare_ceta_array[i] == "0xe0") or (stare_ceta_array[i] == "0xf0"):
                item= '0x' + icol[start_reading + i*48 : start_reading + i*48 + 2]           
            else:
                item = '-'
            return_set.append(item)

        return return_set
  
                
    iq_mas_ls_array = [Bits('0x'+ icol[148 + i*48 : 148 + i*48 + 2]).bin  if (stare_ceta_array[i] != "0xe0") and (stare_ceta_array[i] != "0xf0") else '-' for i in range(6) ]
    iq_mas_ms_array = [Bits('0x'+ icol[150 + i*48 : 150 + i*48 + 2]).bin  if (stare_ceta_array[i] != "0xe0") and (stare_ceta_array[i] != "0xf0") else '-' for i in range(6) ]
    combined = zip(iq_mas_ms_array, iq_mas_ls_array) 
    iq_mas_array = [make_value_from_ms_and_ls(combined[i], -32767, 32767, -4525, 4525) for i in range(6)]
    
    id_mas_ls_array = [Bits('0x'+ icol[152 + i*48 : 152 + i*48 + 2]).bin  if (stare_ceta_array[i] != "0xe0") and (stare_ceta_array[i] != "0xf0") else '-' for i in range(6) ]
    id_mas_ms_array = [Bits('0x'+ icol[154 + i*48 : 154 + i*48 + 2]).bin  if (stare_ceta_array[i] != "0xe0") and (stare_ceta_array[i] != "0xf0") else '-' for i in range(6) ]
    combined = zip(id_mas_ms_array, id_mas_ls_array) 
    id_mas_array = [make_value_from_ms_and_ls(combined[i], -32767, 32767, -4525, 4525) for i in range(6)]
       
    cauza_bloc_hard = face_valori_cauza(148)
    cauza_decon  = face_valori_cauza(150)
    cauza_bloc_soft = face_valori_cauza(152)
    cauza_def_preinc = face_valori_cauza(154)
    
    icol_return['cauza_bloc_hard'] = {'val':cauza_bloc_hard, 'UM':"hex"}    
    icol_return['cauza_decon'] = {'val':cauza_decon, 'UM':"hex"}
    icol_return['cauza_bloc_soft'] = {'val':cauza_bloc_soft, 'UM':"hex"}
    icol_return['cauza_def_preinc'] = {'val':cauza_def_preinc , 'UM':"hex"}
    
    icol_return['iq_mas'] = {'val':iq_mas_array, 'UM':'hex'}
    icol_return['id_mas'] = {'val':id_mas_array, 'UM':'hex'}

    
    S1, S2, S3, S4, S5, S6 = {}, {}, {}, {}, {}, {}
  
    
    
    Ceta = {}
    Ceta['S1'] = S1
    Ceta['S2'] = S2
    Ceta['S3'] = S3
    Ceta['S4'] = S4
    Ceta['S5'] = S5
    Ceta['S6'] = S6
    
    Lente0,Lente1, Lente2, Lente3, Lente4, Lente5 ={}, {}, {}, {}, {}, {}
    
    legend = {'00':'S1', '01':'S2', '02':'S3', '03':'S4', '04':'S5', '05':'S6'}
    marimi_hexa_Box3 = {'def_drv1':412,'stare_drv1': 414, 'def_drv2':420, 'stare_drv2':422 }
    marimi_numerice_Box3 = {'temp_l1':{'start':416, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_h1':{'start':418, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_l2':{'start':424, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_h2':{'start':426, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125}}
    
    marimi_hexa_Box4 = {'def_drv3':428,'stare_drv3': 430, 'def_drv4':436, 'stare_drv4':438 }
    marimi_numerice_Box4 = {'temp_l3':{'start':432, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_h3':{'start':434, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_l4':{'start':440, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_h4':{'start':442, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125}}
    
    marimi_hexa_Box5 = {'def_drv5':444,'stare_drv5': 446, 'def_drv6':452, 'stare_drv6':454 }
    marimi_numerice_Box5 = {'temp_l5':{'start':448, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_h5':{'start':450, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_l6':{'start':456, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125},
                            'temp_h6':{'start':458, 'min1':-55, 'max1':125, 'min2':-55, 'max2':125}}
    
    marimi_hexa_Box6 = {'u_drv':460, 'dsp_drv':462, 'trip14':464, 'trip56':466, 
                        'stare_mm':468, 'inp_63':470, 'defect_can_drv':472, 'rez_mm1':474 }
    
    marimi_numerice_Box7 = {'temp_mt2':{'start':476, 'min1':0, 'max1':255, 'min2':-50, 'max2':205},
                            'temp_mt1':{'start':478, 'min1':0, 'max1':255, 'min2':-50, 'max2':205},
                            'nivel_apa':{'start':480, 'min1':41, 'max1':204, 'min2':0, 'max2':100},
                            'temp_mt3':{'start':482, 'min1':41, 'max1':204, 'min2':-50, 'max2':205},
                            'temp_apa_r':{'start':484, 'min1':41, 'max1':204, 'min2':0, 'max2':100},
                            'temp_apa_c':{'start':486, 'min1':41, 'max1':204, 'min2':0, 'max2':100},
                            'pres_aer_rad':{'start':488, 'min1':13, 'max1':204, 'min2':0, 'max2':50},
                            'pres_apa':{'start':490, 'min1':41, 'max1':204, 'min2':0, 'max2':2.5}}
    
    marimi_numerice_Box8 = {'temp_aer_mt':{'start':492, 'min1':0, 'max1':255, 'min2':0, 'max2':100},
                            'pres_aer_mt':{'start':494, 'min1':51, 'max1':204, 'min2':0, 'max2':300},
                            'umid_aer_mt':{'start':498, 'min1':51, 'max1':152, 'min2':0, 'max2':100},
                            'vibr_Y':{'start':500, 'min1':0, 'max1':101, 'min2':0, 'max2':10},
                            'vibr_X':{'start':502, 'min1':0, 'max1':101, 'min2':0, 'max2':10} }
    marimi_hexa_Box8 = {'rez_mm3':496}

        
    for k,v in marimi_hexa_Box3.iteritems():
        Box3[k][legend[identificator]] = '0x' + icol[v:v+2]
        icol_return[k] = Box3[k]
    
    for k,v in marimi_numerice_Box3.iteritems():
        Box3[k][legend[identificator]] =  PercentValueCustomScale(Bits('0x' + icol[v['start']:v['start']+2]).uint, v['min1'], v['max1'], v['min2'], v['max2'])
        icol_return[k] = Box3[k]
    
    for k,v in marimi_hexa_Box4.iteritems():
        Box4[k][legend[identificator]] = '0x' + icol[v:v+2]
        icol_return[k] = Box4[k]
    
    for k,v in marimi_numerice_Box4.iteritems():
        Box4[k][legend[identificator]] =  PercentValueCustomScale(Bits('0x' + icol[v['start']:v['start']+2]).uint, v['min1'], v['max1'], v['min2'], v['max2'])
        icol_return[k] = Box4[k]
    
    for k,v in marimi_hexa_Box5.iteritems():
        Box5[k][legend[identificator]] = '0x' + icol[v:v+2]
        icol_return[k] = Box5[k]
    
    for k,v in marimi_numerice_Box5.iteritems():
        Box5[k][legend[identificator]] =  PercentValueCustomScale(Bits('0x' + icol[v['start']:v['start']+2]).uint, v['min1'], v['max1'], v['min2'], v['max2'])
        icol_return[k] = Box5[k]
    
    for k,v in marimi_hexa_Box6.iteritems():
        Box6[k][legend[identificator]] = '0x' + icol[v:v+2]
        icol_return[k] = Box6[k] 
         
    for k,v in marimi_numerice_Box7.iteritems():
        Box7[k][legend[identificator]] =  PercentValueCustomScale(Bits('0x' + icol[v['start']:v['start']+2]).uint, v['min1'], v['max1'], v['min2'], v['max2'])
        icol_return[k] = Box7[k]
    
    for k,v in marimi_numerice_Box8.iteritems():
        Box8[k][legend[identificator]] =  PercentValueCustomScale(Bits('0x' + icol[v['start']:v['start']+2]).uint, v['min1'], v['max1'], v['min2'], v['max2'])
        icol_return[k] = Box8[k] 
    
    for k,v in marimi_hexa_Box8.iteritems():
        Box8[k][legend[identificator]] = '0x' + icol[v:v+2]
        icol_return[k] = Box8[k]  

    
    ipm_ls = Bits('0x'+ icol[504:506]).bin 
    ipm_ms = Bits('0x'+ icol[506:508]).bin
    concat = BitArray(bin = ipm_ms + ipm_ls).uint
    Box8['ipm'][legend[identificator]] = round(PercentValueCustomScale(concat,0,20460, 0,100000),2)
    

    
    marimi_functie_de_identificator = ['rezerva_lente','p_cat','p_sa', 'data_lente', 'temp_trafo', 'mansa1_numerice', 'mansa1_forta',\
                                        'mansa1_viteza', 'mansa2_numerice', 'mansa2_forta','mansa2_viteza','defect0_lente', \
                                        'defect1_lente','defect2_lente','defect3_lente','defect4_lente','defect5_lente','defect6_lente', 'defect7_lente', 'defect8_lente',\
                                         'defect9_lente', 'defect10_lente', 'defect11_lente', 'defect12_lente', 'defect13_lente',\
                                        'defect14_lente', 'defect15_lente','defect16_lente', 'defect17_lente', 'defect18_lente', 'defect19_lente', 'defect20_lente', \
                                        'defect21_lente', 'defect22_lente', 'defect23_lente']
    for marime in marimi_functie_de_identificator:
        icol_return[marime] = {'val':'-', 'UM':'-'}
         
    if identificator == "00":
      
        zi =  icol[396:398]
        luna = icol[398:400]
        an =  icol[400:402]
        Lente0['data'] =  zi + '-' + luna + '-' + an
       
        icol_return['data_lente'] =   {'val':Lente0['data'],'UM':'Date'} 
        
        p_cat_ls = Bits('0x' + icol[402:404]).bin
        p_cat_ms = Bits('0x' + icol[404:406]).bin
        
        Lente0['p_cat'] = PercentValueCustomScale(BitArray(bin = p_cat_ms + p_cat_ls).uint, 0,32767, 0, 49150) 
        icol_return['p_cat'] = {'val':Lente0['p_cat'],'UM':'kW'} 
      
        
        
        p_sa_ls = Bits('0x' + icol[406:408]).bin
        p_sa_ms = Bits('0x' + icol[408:410]).bin
        icol_return['p_sa'] = {'val': PercentValueCustomScale(BitArray(bin = p_sa_ms + p_sa_ls).uint, 0,32767, 0, 49150), 'UM':'kW' }
        
        temp_trafo = Bits('0x' + icol[410:412]).uint
        icol_return['temp_trafo'] = {'val': PercentValueCustomScale(Bits('0x' + icol[370:372]).uint, 26,134, -50, 100) , 'UM':'gC'}
    
    elif identificator =='01':       
        icol_return['mansa1_numerice'] = {'val':'0x' + icol[396:398], 'UM':'hex'}
        icol_return['mansa1_forta'] = {'val':'0x' + icol[398:400], 'UM':'hex'}
        icol_return['mansa1_viteza'] = {'val':PercentValueCustomScale(Bits('0x' + icol[400:402]).uint, 0, 255, 0, 255), 'UM':'kmh'}
        icol_return['mansa2_numerice'] = {'val':'0x' + icol[402:404], 'UM':'hex'}
        icol_return['mansa2_forta'] = {'val':'0x' + icol[404:406], 'UM':'hex'}
        icol_return['mansa2_viteza'] = {'val':PercentValueCustomScale(Bits('0x' + icol[406:408]).uint, 0, 255, 0, 255),'UM':'kmh'}

    elif identificator =='02':
      
        icol_return['defect0_lente'] =  {'val':'0x' + icol[396:398],'UM':'hex'}
        icol_return['defect1_lente'] =  {'val':'0x' + icol[398:400], 'UM':'hex'}
        icol_return['defect2_lente'] =  {'val':'0x' + icol[400:402], 'UM':'hex'}
        icol_return['defect3_lente'] =  {'val':'0x' + icol[402:404], 'UM':'hex'}
        icol_return['defect4_lente'] =  {'val':'0x' + icol[404:406], 'UM':'hex'}
        icol_return['defect5_lente'] =  {'val':'0x' + icol[406:408], 'UM':'hex'}
        icol_return['defect7_lente'] =  {'val':'0x' + icol[408:410], 'UM':'hex'}

    elif identificator =='03':

        
        icol_return['defect8_lente'] =  {'val':'0x' + icol[396:398], 'UM':'hex'}
        icol_return['defect9_lente'] =  {'val':'0x' + icol[398:400], 'UM':'hex'}
        icol_return['defect10_lente'] = {'val': '0x' + icol[400:402], 'UM':'hex'}
        icol_return['defect11_lente'] = {'val': '0x' + icol[402:404], 'UM':'hex'}
        icol_return['defect12_lente'] = {'val': '0x' + icol[404:406], 'UM':'hex'}
        icol_return['defect13_lente'] = {'val': '0x' + icol[406:408], 'UM':'hex'}
        icol_return['defect14_lente'] =  {'val':'0x' + icol[408:410], 'UM':'hex'}
        icol_return['defect15_lente'] =  {'val':'0x' + icol[410:412], 'UM':'hex'}

    elif identificator =='04':

        
        icol_return['defect16_lente'] =  {'val':'0x' + icol[396:398], 'UM':'hex'}
        icol_return['defect17_lente'] =  {'val':'0x' + icol[398:400], 'UM':'hex'}
        icol_return['defect18_lente'] =  {'val':'0x' + icol[400:402], 'UM':'hex'}
        icol_return['defect19_lente'] =  {'val':'0x' + icol[402:404], 'UM':'hex'}
        icol_return['defect20_lente'] =  {'val':'0x' + icol[404:406], 'UM':'hex'}
        icol_return['defect21_lente'] =  {'val':'0x' + icol[406:408], 'UM':'hex'}
        icol_return['defect22_lente'] =  {'val':'0x' + icol[408:410], 'UM':'hex'} 
        icol_return['defect23_lente'] =  {'val':'0x' + icol[410:412], 'UM':'hex'}

    elif identificator =='05':

        
        icol_return['rezerva_lente'] =  {'val':'0x' + icol[396:398], 'UM':'hex'}
#         Lente5['rezerva'] =  '0x' + icol[398:400]
#         Lente5['rezerva'] =  '0x' + icol[400:402]
#         Lente5['rezerva'] =  '0x' + icol[402:404]
#         Lente5['rezerva'] =  '0x' + icol[404:406]
#         Lente5['rezerva'] =  '0x' + icol[406:408]
#         Lente5['rezerva'] =  '0x' + icol[408:410] 
#         Lente5['rezerva'] =  '0x' + icol[410:412] 
         
  
    return icol_return

def GetValuesFromGPS(gps, type_of_file_out = "json"):
    
    gps_return = {}

    
    sec = str(gps[0:2])  
    min = str(gps[2:4])  
    ora = str(gps[4:6])  
    zi = str(gps[6:8])  
    luna = str(gps[8:10])  
    an = "20"+str(gps[10:12])  
    
    data = zi + "-" + luna + '-' + an + " " + ora + ":" + min + ":"+ sec
    gps_return['data_gps'] = data
    
    grad_lat = str(gps[12:14])
    min_lat =  str(gps[14:16])
    sutimi_min_lat  = str(gps[16:18])
    zecimi_miimi_min_lat = str(gps[18:20])
    
    latitudine = grad_lat + 'grd' + min_lat + '.' + sutimi_min_lat + zecimi_miimi_min_lat
    
    grad_long = str(gps[22:24])
    min_long =  str( gps[24:26])
    sutimi_min_long  = str(gps[26:28])
    zecimi_miimi_min_long = str(gps[28:30])
    
    longitudine = grad_long + 'grd' + min_long + '.' + sutimi_min_long + zecimi_miimi_min_long
    gps_return['latitudine'] = latitudine
    gps_return['longitudine'] = longitudine
    
    sute_alt = float(str(gps[30:32]))
    unit_alt = float(str(gps[32:34]))    
    altitudine = sute_alt *100  + unit_alt
    gps_return['altitudine'] = altitudine
    
    zeci_curs =  str(gps[34:36])
    zecimi_curs =  str(gps[36:38])
    curs = zeci_curs + '.' + zecimi_curs
    gps_return['curs'] = curs
    
    
    zeci_viteza = float(str(gps[38:40]))
    zecimi_viteza = float(str(gps[40:42]))   
    viteza = zeci_viteza*10 + zecimi_viteza/10.0
    gps_return['viteza_gps'] = viteza
        
    return gps_return
    
    
    
    