#     icsa_values = GetValuesFromIcsa(icsa) # intoarce un dictionar 
#     
#     frame_values = dict(icol_values.items()+icsa_values.items()) #concatenez dictionarele pentru a face un frame
    #frameul o bag intr-o lista o fac json si apoii o scriu intr-un fisier json
    identificator = icol[2:4] 
    secunde = icol[4:6]
    minute = icol[6:8]
    ora = icol [8:10]
    inp_num = [Bits('0x' + icol[i:i+2]).bin for i in range(10,34,2)] # am ramas la 34
    out_num = [Bits('0x' + icol[i:i+2]).bin for i in range(34,46,2)] #44
    
   
    
    mansa_activa_numerice = icol[46:48]
    mansa_activa_forta = icol[48:50]
    mansa_activa_viteza = icol[50:52]
    viteza_impusa = icol[52:54]
    
    u_cat = Bits('0x' + icol[54:56]).uint   
    ucat = PercentValueCustomScale(u_cat, 0,255,0,50) 
    
    u_sa = Bits('0x' + icol[56:58]).uint
    usa = PercentValueCustomScale(u_sa, 0,255,0,777)
     
    i_cat = Bits('0x'+ icol[58:60]).uint
    icat = PercentValueCustomScale(i_cat, 0,255,0,777)
     
    i_tren = Bits('0x'+ icol[60:62]).uint
    itren = PercentValueCustomScale(i_tren, 0,255,0,933) 
    
    i_bat = Bits('0x'+ icol[62:64]).uint
    ibat = PercentValueCustomScale(i_bat, 0,172,-25,25) 
    
    p_cg = Bits('0x'+ icol[64:66]).uint
    p_cg = PercentValueCustomScale(p_cg, 26,255,0,12.72) 
    
    vit1_ls = Bits('0x'+ icol[66:68]).bin
    vit1_ms_last3 = Bits('0x'+ icol[68:70]).bin[-3:]
    vit1 = vit1_ms_last3 + vit1_ls
    vit1 = BitArray(bin=vit1).uint/10.0
    
    vit2_ls = Bits('0x'+ icol[70:72]).bin
    vit2_ms_last3 = Bits('0x'+ icol[72:74]).bin[-3:]
    vit2 = vit2_ms_last3 + vit2_ls
    vit2 = BitArray(bin=vit2).uint/10.0
    
    temp_trafo2 =  Bits('0x'+ icol[74:76]).uint
    temp_trafo2= PercentValueCustomScale(temp_trafo2, 26,134,-50,100)
    
    stare_forta = '0x'+ icol[76:78]
    stare_tractiune = '0x'+ icol[78:80]
    
    turatie_min_trac_ls = Bits('0x'+ icol[80:82]).bin
    turatie_min_trac_ms = Bits('0x'+ icol[82:84]).bin
    turatie_min_trac =  BitArray(bin = turatie_min_trac_ms + turatie_min_trac_ls).uint
    turatie_min_trac = PercentValueCustomScale(turatie_min_trac, 0, 32767, 0, 8000)
    
    turatie_max_trac_ls = Bits('0x'+ icol[84:86]).bin
    turatie_max_trac_ms = Bits('0x'+ icol[86:88]).bin
    turatie_max_trac =  BitArray(bin = turatie_max_trac_ms + turatie_max_trac_ls).uint
    turatie_max_trac = PercentValueCustomScale(turatie_max_trac, 0, 32767, 0, 8000)
    
    turatie_max_notrac_ls = Bits('0x'+ icol[88:90]).bin
    turatie_max_notrac_ms = Bits('0x'+ icol[90:92]).bin
    turatie_max_notrac =  BitArray(bin = turatie_max_notrac_ms + turatie_max_notrac_ls).uint
    turatie_max_notrac = PercentValueCustomScale(turatie_max_notrac, 0, 32767, 0, 8000)
    
    info1 = '0x'+ icol[92:94]
    info2 = '0x'+ icol[94:96]
    
    forta_cda_icol_ls = Bits('0x'+ icol[96:98]).bin
    forta_cda_icol_ms = Bits('0x'+ icol[98:100]).bin
    forta_cda_icol =  BitArray(bin = forta_cda_icol_ms + forta_cda_icol_ls).uint
    forta_cda_icol = PercentValueCustomScale(forta_cda_icol, -2550, 4850, 255, 485)
############################################################################################################
 #                                   S1
############################################################################################################   
    s1_stare_ceta = '0x'+ icol[108:110]
    s1_stare_stare = '0x'+ icol[110:112]
    s1_stare_4qc3ph = '0x' + icol[112:114]
    s1_bloc_soft = '0x' + icol[114:116]
    s1_bloc_hard = '0x' + icol[116:118]
    s1_decon_hard ='0x' + icol[118:120] 
    s1_inp_num = '0x' + icol[120:122]
    s1_tip_ceta = '0x' + icol[122:124]
    
    s1_u_cat =  Bits('0x' + icol[124:126]).uint   
    s1_u_cat = round(PercentValueCustomScale(s1_u_cat, 0,255,0,39.25),2)
        
    s1_irfm__s1_i_in = Bits('0x' + icol[126:128]).uint
    if s1_stare_ceta == "0x40":
        s1_irfm__s1_i_in = round(PercentValueCustomScale(s1_irfm__s1_i_in, 0,255,0,1600),2)
    else:
        s1_irfm__s1_i_in = round(PercentValueCustomScale(s1_irfm__s1_i_in, 0,255,0,2220),2)
    
    s1_u_cc = Bits('0x' + icol[128:130]).uint
    s1_u_cc = round(PercentValueCustomScale(s1_u_cc, 0,255,0,2500),2)
    
    s1_u_sa = Bits('0x' + icol[130:132]).uint
    s1_u_sa = round(PercentValueCustomScale(s1_u_sa, 0,255,0,39.25),2)    
    
    s1_i_out_ls = Bits('0x'+ icol[132:134]).bin
    s1_i_out_ms = Bits('0x'+ icol[134:136]).bin
    s1_i_out =  BitArray(bin = s1_i_out_ms + s1_i_out_ls).uint
    s1_i_out = round(PercentValueCustomScale(s1_i_out, 0,32767,0,4525),2)
    
    s1_v_cda_ls = Bits('0x'+ icol[136:138]).bin
    s1_v_cda_ms = Bits('0x'+ icol[138:140]).bin
    s1_v_cda =  BitArray(bin = s1_v_cda_ms + s1_v_cda_ls).uint
    s1_v_cda = round(PercentValueCustomScale(s1_v_cda, -32767,32767,-100,100),2)
    
    s1_turatie_ls = Bits('0x'+ icol[140:142]).bin
    s1_turatie_ms = Bits('0x'+ icol[142:144]).bin
    s1_turatie =  BitArray(bin = s1_turatie_ms + s1_turatie_ls).uint
    s1_turatie = round(PercentValueCustomScale(s1_turatie, -32767,32767,-8000,8000),2)
    
    s1_forta_cda_ls = Bits('0x'+ icol[144:146]).bin
    s1_forta_cda_ms = Bits('0x'+ icol[146:148]).bin
    s1_forta_cda =  BitArray(bin = s1_forta_cda_ms + s1_forta_cda_ls).uint
    
    if (s1_stare_ceta == "0xe0") or (s1_stare_ceta == "0xf0"):
        s1_cauza_bloc_hard = '0x' + icol[148:150]
        s1_cauza_decon = '0x' + icol[150:152]
        s1_cauza_bloc_soft = '0x' +icol[152:154]
        s1_def_preinc = '0x' + icol[154:156]
    else:
        s1_iq_mas_ls = Bits('0x'+ icol[148:150]).bin
        s1_iq_mas_ms = Bits('0x'+ icol[150:152]).bin
        s1_iq_mas = PercentValueCustomScale(BitArray(bin = s1_iq_mas_ms + s1_iq_mas_ls).uint, -32767,32767, -4525, 4525)
        s1_id_mas_ls = Bits('0x'+ icol[152:154]).bin
        s1_id_mas_ms = Bits('0x'+ icol[154:156]).bin
        s1_id_mas = PercentValueCustomScale(BitArray(bin = s1_id_mas_ms + s1_id_mas_ls).uint, -32767,32767, -4525, 4525)
##############################################################################################
  #                                  S2
##############################################################################################
    s2_stare_ceta = '0x'+ icol[156:158]
    s2_stare_stare = '0x'+ icol[158:160]
    s2_stare_4qc3ph = '0x' + icol[160:162]
    s2_bloc_soft = '0x' + icol[162:164]
    s2_bloc_hard = '0x' + icol[164:166]
    s2_decon_hard ='0x' + icol[166:168] 
    s2_inp_num = '0x' + icol[168:170]
    s2_tip_ceta = '0x' + icol[170:172]
    
    s2_u_cat =  Bits('0x' + icol[172:174]).uint   
    s2_u_cat = round(PercentValueCustomScale(s2_u_cat, 0,255,0,39.25),2)
     
    s2_irfm__s2_i_in = Bits('0x' + icol[174:176]).uint
    if s2_stare_ceta == "0x40":
        s2_irfm__s2_i_in = round(PercentValueCustomScale(s2_irfm__s2_i_in, 0,255,0,1600),2)
    else:
        s2_irfm__s2_i_in = round(PercentValueCustomScale(s2_irfm__s2_i_in, 0,255,0,2220),2)
    
    s2_u_cc = Bits('0x' + icol[176:178]).uint
    s2_u_cc = round(PercentValueCustomScale(s2_u_cc, 0,255,0,2500),2)
    
    s2_u_sa = Bits('0x' + icol[178:180]).uint
    s2_u_sa = round(PercentValueCustomScale(s2_u_sa, 0,255,0,39.25),2)
       
    s2_i_out_ls = Bits('0x'+ icol[180:182]).bin
    s2_i_out_ms = Bits('0x'+ icol[182:184]).bin
    s2_i_out =  BitArray(bin = s2_i_out_ms + s2_i_out_ls).uint
    s2_i_out = round(PercentValueCustomScale(s2_i_out, 0,32767,0,4525),2)
    
    s2_v_cda_ls = Bits('0x'+ icol[184:186]).bin
    s2_v_cda_ms = Bits('0x'+ icol[186:188]).bin
    s2_v_cda =  BitArray(bin = s2_v_cda_ms + s2_v_cda_ls).uint
    s2_v_cda = round(PercentValueCustomScale(s2_v_cda, -32767,32767,-100,100),2)
    
    s2_turatie_ls = Bits('0x'+ icol[188:190]).bin
    s2_turatie_ms = Bits('0x'+ icol[190:192]).bin
    s2_turatie =  BitArray(bin = s2_turatie_ms + s2_turatie_ls).uint
    s2_turatie = round(PercentValueCustomScale(s2_turatie, -32767,32767,-8000,8000),2)
    
    s2_forta_cda_ls = Bits('0x'+ icol[192:194]).bin
    s2_forta_cda_ms = Bits('0x'+ icol[194:196]).bin
    s2_forta_cda =  BitArray(bin = s2_forta_cda_ms + s2_forta_cda_ls).uint
    
    if (s2_stare_ceta == "0xe0") or (s2_stare_ceta == "0xf0"):
        s2_cauza_bloc_hard = '0x' + icol[196:198]
        s2_cauza_decon = '0x' + icol[198:200]
        s2_cauza_bloc_soft = '0x' +icol[200:202]
        s2_def_preinc = '0x' + icol[202:204]
    else:
        s2_iq_mas_ls = Bits('0x'+ icol[196:198]).bin
        s2_iq_mas_ms = Bits('0x'+ icol[198:200]).bin
        s2_iq_mas = PercentValueCustomScale(BitArray(bin = s2_iq_mas_ms + s2_iq_mas_ls).uint, -32767,32767, -4525, 4525)
        s2_id_mas_ls = Bits('0x'+ icol[200:202]).bin
        s2_id_mas_ms = Bits('0x'+ icol[202:204]).bin
        s2_id_mas = PercentValueCustomScale(BitArray(bin = s2_id_mas_ms + s2_id_mas_ls).uint, -32767,32767, -4525, 4525) 
          
###########################################################################################################          
    #                                S3
###########################################################################################################  
    
    s3_stare_ceta = '0x'+ icol[204:206]
    s3_stare_stare = '0x'+ icol[206:208]
    s3_stare_4qc3ph = '0x' + icol[208:210]
    s3_bloc_soft = '0x' + icol[210:212]
    s3_bloc_hard = '0x' + icol[212:214]
    s3_decon_hard ='0x' + icol[214:216] 
    s3_inp_num = '0x' + icol[216:218]
    s3_tip_ceta = '0x' + icol[218:220]
    
    s3_u_cat =  Bits('0x' + icol[220:222]).uint   
    s3_u_cat = round(PercentValueCustomScale(s3_u_cat, 0,255,0,39.25),2)
        
    s3_irfm__s3_i_in = Bits('0x' + icol[222:224]).uint
    if s3_stare_ceta == "0x40":
        s3_irfm__s3_i_in = round(PercentValueCustomScale(s3_irfm__s3_i_in, 0,255,0,1600),2)
    else:
        s3_irfm__s3_i_in = round(PercentValueCustomScale(s3_irfm__s3_i_in, 0,255,0,2220),2)
    
    s3_u_cc = Bits('0x' + icol[224:226]).uint
    s3_u_cc = round(PercentValueCustomScale(s3_u_cc, 0,255,0,2500),2)
    
    s3_u_sa = Bits('0x' + icol[226:228]).uint
    s3_u_sa = round(PercentValueCustomScale(s3_u_sa, 0,255,0,39.25),2)
        
    s3_i_out_ls = Bits('0x'+ icol[228:230]).bin
    s3_i_out_ms = Bits('0x'+ icol[230:232]).bin
    s3_i_out =  BitArray(bin = s3_i_out_ms + s3_i_out_ls).uint
    s3_i_out = round(PercentValueCustomScale(s3_i_out, 0,32767,0,4525),2)
    
    s3_v_cda_ls = Bits('0x'+ icol[232:234]).bin
    s3_v_cda_ms = Bits('0x'+ icol[234:236]).bin
    s3_v_cda =  BitArray(bin = s3_v_cda_ms + s3_v_cda_ls).uint
    s3_v_cda = round(PercentValueCustomScale(s3_v_cda, -32767,32767,-100,100),2)
    
    s3_turatie_ls = Bits('0x'+ icol[236:238]).bin
    s3_turatie_ms = Bits('0x'+ icol[238:240]).bin
    s3_turatie =  BitArray(bin = s3_turatie_ms + s3_turatie_ls).uint
    s3_turatie = round(PercentValueCustomScale(s3_turatie, -32767,32767,-8000,8000),2)
    
    s3_forta_cda_ls = Bits('0x'+ icol[240:242]).bin
    s3_forta_cda_ms = Bits('0x'+ icol[242:244]).bin
    s3_forta_cda =  BitArray(bin = s3_forta_cda_ms + s3_forta_cda_ls).uint
    
    if (s3_stare_ceta == "0xe0") or (s3_stare_ceta == "0xf0"):
        s3_cauza_bloc_hard = '0x' + icol[244:246]
        s3_cauza_decon = '0x' + icol[246:248]
        s3_cauza_bloc_soft = '0x' +icol[248:250]
        s3_def_preinc = '0x' + icol[250:252]
    else:
        s3_iq_mas_ls = Bits('0x'+ icol[244:246]).bin
        s3_iq_mas_ms = Bits('0x'+ icol[246:248]).bin
        s3_iq_mas = PercentValueCustomScale(BitArray(bin = s3_iq_mas_ms + s3_iq_mas_ls).uint, -32767,32767, -4525, 4525)    
        s3_id_mas_ls = Bits('0x'+ icol[248:250]).bin
        s3_id_mas_ms = Bits('0x'+ icol[250:252]).bin
        s3_id_mas = PercentValueCustomScale(BitArray(bin = s3_id_mas_ms + s3_id_mas_ls).uint, -32767,32767, -4525, 4525) 
        
        
#########################################################################################################################3
    #                                                S4
###########################################################################################################################
    s4_stare_ceta = '0x'+ icol[252:254]
    s4_stare_stare = '0x'+ icol[254:256]
    s4_stare_4qc3ph = '0x' + icol[256:258]
    s4_bloc_soft = '0x' + icol[258:260]
    s4_bloc_hard = '0x' + icol[260:262]
    s4_decon_hard ='0x' + icol[262:264] 
    s4_inp_num = '0x' + icol[264:266]
    s4_tip_ceta = '0x' + icol[266:268]
    
    s4_u_cat =  Bits('0x' + icol[268:270]).uint   
    s4_u_cat = round(PercentValueCustomScale(s4_u_cat, 0,255,0,39.25),2)
    
    
     
    s4_irfm__s4_i_in = Bits('0x' + icol[270:272]).uint
    if s4_stare_ceta == "0x40":
        s4_irfm__s4_i_in = round(PercentValueCustomScale(s4_irfm__s4_i_in, 0,255,0,1600),2)
    else:
        s4_irfm__s4_i_in = round(PercentValueCustomScale(s4_irfm__s4_i_in, 0,255,0,2220),2)
    
    s4_u_cc = Bits('0x' + icol[272:274]).uint
    s4_u_cc = round(PercentValueCustomScale(s4_u_cc, 0,255,0,2500),2)
    
    s4_u_sa = Bits('0x' + icol[274:276]).uint
    s4_u_sa = round(PercentValueCustomScale(s4_u_sa, 0,255,0,39.25),2)    
    
    s4_i_out_ls = Bits('0x'+ icol[276:278]).bin
    s4_i_out_ms = Bits('0x'+ icol[278:280]).bin
    s4_i_out =  BitArray(bin = s4_i_out_ms + s4_i_out_ls).uint
    s4_i_out = round(PercentValueCustomScale(s4_i_out, 0,32767,0,4525),2)
    
    s4_v_cda_ls = Bits('0x'+ icol[280:282]).bin
    s4_v_cda_ms = Bits('0x'+ icol[282:284]).bin
    s4_v_cda =  BitArray(bin = s4_v_cda_ms + s4_v_cda_ls).uint
    s4_v_cda = round(PercentValueCustomScale(s4_v_cda, -32767,32767,-100,100),2)
    
    s4_turatie_ls = Bits('0x'+ icol[284:286]).bin
    s4_turatie_ms = Bits('0x'+ icol[286:288]).bin
    s4_turatie =  BitArray(bin = s4_turatie_ms + s4_turatie_ls).uint
    s4_turatie = round(PercentValueCustomScale(s4_turatie, -32767,32767,-8000,8000),2)
    
    s4_forta_cda_ls = Bits('0x'+ icol[288:290]).bin
    s4_forta_cda_ms = Bits('0x'+ icol[290:292]).bin
    s4_forta_cda =  BitArray(bin = s4_forta_cda_ms + s4_forta_cda_ls).uint
    
    if (s4_stare_ceta == "0xe0") or (s4_stare_ceta == "0xf0"):
        s4_cauza_bloc_hard = '0x' + icol[292:294]
        s4_cauza_decon = '0x' + icol[294:296]
        s4_cauza_bloc_soft = '0x' +icol[296:298]
        s4_def_preinc = '0x' + icol[298:230]
    else:
        s4_iq_mas_ls = Bits('0x'+ icol[292:294]).bin
        s4_iq_mas_ms = Bits('0x'+ icol[294:296]).bin
        s4_iq_mas = PercentValueCustomScale(BitArray(bin = s4_iq_mas_ms + s4_iq_mas_ls).uint, -32767,32767, -4525, 4525)
        s4_id_mas_ls = Bits('0x'+ icol[296:298]).bin
        s4_id_mas_ms = Bits('0x'+ icol[298:300]).bin
        s4_id_mas = PercentValueCustomScale(BitArray(bin = s4_id_mas_ms + s4_id_mas_ls).uint, -32767,32767, -4525, 4525)
#####################################################################################################################3
     #                                   S5
######################################################################################################################
    s5_stare_ceta = '0x'+ icol[300:302]
    s5_stare_stare = '0x'+ icol[302:304]
    s5_stare_4qc3ph = '0x' + icol[304:306]
    s5_bloc_soft = '0x' + icol[306:308]
    s5_bloc_hard = '0x' + icol[308:310]
    s5_decon_hard ='0x' + icol[310:312] 
    s5_inp_num = '0x' + icol[312:314]
    s5_tip_ceta = '0x' + icol[314:316]
    
    s5_u_cat =  Bits('0x' + icol[316:318]).uint   
    s5_u_cat = round(PercentValueCustomScale(s5_u_cat, 0,255,0,39.25),2)
    
    
     
    s5_irfm__s5_i_in = Bits('0x' + icol[318:320]).uint
    if s5_stare_ceta == "0x40":
        s5_irfm__s5_i_in = round(PercentValueCustomScale(s5_irfm__s5_i_in, 0,255,0,1600),2)
    else:
        s5_irfm__s5_i_in = round(PercentValueCustomScale(s5_irfm__s5_i_in, 0,255,0,2220),2)
    
    s5_u_cc = Bits('0x' + icol[320:322]).uint
    s5_u_cc = round(PercentValueCustomScale(s5_u_cc, 0,255,0,2500),2)
    
    s5_u_sa = Bits('0x' + icol[322:324]).uint
    s5_u_sa = round(PercentValueCustomScale(s5_u_sa, 0,255,0,39.25),2)
       
    s5_i_out_ls = Bits('0x'+ icol[324:326]).bin
    s5_i_out_ms = Bits('0x'+ icol[326:328]).bin
    s5_i_out =  BitArray(bin = s5_i_out_ms + s5_i_out_ls).uint
    s5_i_out = round(PercentValueCustomScale(s5_i_out, 0,32767,0,4525),2)
    
    s5_v_cda_ls = Bits('0x'+ icol[328:330]).bin
    s5_v_cda_ms = Bits('0x'+ icol[330:332]).bin
    s5_v_cda =  BitArray(bin = s5_v_cda_ms + s5_v_cda_ls).uint
    s5_v_cda = round(PercentValueCustomScale(s5_v_cda, -32767,32767,-100,100),2)
    
    s5_turatie_ls = Bits('0x'+ icol[332:334]).bin
    s5_turatie_ms = Bits('0x'+ icol[334:336]).bin
    s5_turatie =  BitArray(bin = s5_turatie_ms + s5_turatie_ls).uint
    s5_turatie = round(PercentValueCustomScale(s5_turatie, -32767,32767,-8000,8000),2)
    
    s5_forta_cda_ls = Bits('0x'+ icol[336:338]).bin
    s5_forta_cda_ms = Bits('0x'+ icol[338:340]).bin
    s5_forta_cda =  BitArray(bin = s5_forta_cda_ms + s5_forta_cda_ls).uint
    
    if (s5_stare_ceta == "0xe0") or (s5_stare_ceta == "0xf0"):
        s5_cauza_bloc_hard = '0x' + icol[340:342]
        s5_cauza_decon = '0x' + icol[342:344]
        s5_cauza_bloc_soft = '0x' +icol[344:346]
        s5_def_preinc = '0x' + icol[346:348]
    else:
        s5_iq_mas_ls = Bits('0x'+ icol[340:342]).bin
        s5_iq_mas_ms = Bits('0x'+ icol[342:344]).bin
        s5_iq_mas = PercentValueCustomScale(BitArray(bin = s5_iq_mas_ms + s5_iq_mas_ls).uint, -32767,32767, -4525, 4525)
        s5_id_mas_ls = Bits('0x'+ icol[344:346]).bin
        s5_id_mas_ms = Bits('0x'+ icol[346:348]).bin
        s5_id_mas = PercentValueCustomScale(BitArray(bin = s5_id_mas_ms + s5_id_mas_ls).uint, -32767,32767, -4525, 4525)
###########################################################################################################################
      #                                          S6
##########################################################################################################################       
    s6_stare_ceta = '0x'+ icol[348:350]
    s6_stare_stare = '0x'+ icol[350:352]
    s6_stare_4qc3ph = '0x' + icol[352:354]
    s6_bloc_soft = '0x' + icol[354:356]
    s6_bloc_hard = '0x' + icol[356:358]
    s6_decon_hard ='0x' + icol[358:360] 
    s6_inp_num = '0x' + icol[360:362]
    s6_tip_ceta = '0x' + icol[362:364]
    
    s6_u_cat =  Bits('0x' + icol[364:366]).uint   
    s6_u_cat = round(PercentValueCustomScale(s6_u_cat, 0,255,0,39.25),2)
    
    
     
    s6_irfm__s6_i_in = Bits('0x' + icol[366:368]).uint
    if s6_stare_ceta == "0x40":
        s6_irfm__s6_i_in = round(PercentValueCustomScale(s6_irfm__s6_i_in, 0,255,0,1600),2)
    else:
        s6_irfm__s6_i_in = round(PercentValueCustomScale(s6_irfm__s6_i_in, 0,255,0,2220),2)
    
    s6_u_cc = Bits('0x' + icol[368:370]).uint
    s6_u_cc = round(PercentValueCustomScale(s6_u_cc, 0,255,0,2500),2)
    
    s6_u_sa = Bits('0x' + icol[370:372]).uint
    s6_u_sa = round(PercentValueCustomScale(s6_u_sa, 0,255,0,39.25),2)
       
    s6_i_out_ls = Bits('0x'+ icol[372:374]).bin
    s6_i_out_ms = Bits('0x'+ icol[374:376]).bin
    s6_i_out =  BitArray(bin = s6_i_out_ms + s6_i_out_ls).uint
    s6_i_out = round(PercentValueCustomScale(s6_i_out, 0,32767,0,4525),2)
    
    s6_v_cda_ls = Bits('0x'+ icol[376:378]).bin
    s6_v_cda_ms = Bits('0x'+ icol[378:380]).bin
    s6_v_cda =  BitArray(bin = s6_v_cda_ms + s6_v_cda_ls).uint
    s6_v_cda = round(PercentValueCustomScale(s6_v_cda, -32767,32767,-100,100),2)
    
    s6_turatie_ls = Bits('0x'+ icol[380:382]).bin
    s6_turatie_ms = Bits('0x'+ icol[382:384]).bin
    s6_turatie =  BitArray(bin = s6_turatie_ms + s6_turatie_ls).uint
    s6_turatie = round(PercentValueCustomScale(s6_turatie, -32767,32767,-8000,8000),2)
    
    s6_forta_cda_ls = Bits('0x'+ icol[384:386]).bin
    s6_forta_cda_ms = Bits('0x'+ icol[386:388]).bin
    s6_forta_cda =  BitArray(bin = s6_forta_cda_ms + s6_forta_cda_ls).uint
    
    if (s6_stare_ceta == "0xe0") or (s6_stare_ceta == "0xf0"):
        s6_cauza_bloc_hard = '0x' + icol[388:400]
        s6_cauza_decon = '0x' + icol[400:402]
        s6_cauza_bloc_soft = '0x' +icol[402:404]
        s6_def_preinc = '0x' + icol[404:406]
    else:
        s6_iq_mas_ls = Bits('0x'+ icol[406:408]).bin
        s6_iq_mas_ms = Bits('0x'+ icol[408:410]).bin
        s6_iq_mas = PercentValueCustomScale(BitArray(bin = s6_iq_mas_ms + s6_iq_mas_ls).uint, -32767,32767, -4525, 4525)        
        
  
    
    S1, S2, S3, S4, S5, S6 = {}, {}, {}, {}, {}, {}
  
    
    
    
    Ceta = {}
    Ceta['S1'] = S1
    Ceta['S2'] = S2
    Ceta['S3'] = S3
    Ceta['S4'] = S4
    Ceta['S5'] = S5
    Ceta['S6'] = S6
    
    Lente0,Lente1, Lente2, Lente3, Lente4, Lente5 ={}, {}, {}, {}, {}, {}
    
    
    if identificator == "00":
#         S1['def_drv1'] = {'valoare': '0x'+ icol[412:414], 'UM':'gC'} That's the way ahahaha
        S1['def_drv1'] = '0x'+ icol[412:414]
        S1['stare_drv1'] = '0x' + icol[414:416]
        S1['temp_l1'] = PercentValueCustomScale(Bits('0x' + icol[416:418]).uint, -55, 125, -55, 125)
        S1['temp_h1'] = PercentValueCustomScale(Bits('0x' + icol[418:420]).uint, -55, 125, -55, 125)
        
        S1['def_drv2'] = '0x'+ icol[420:422]
        S1['stare_drv2'] = '0x' + icol[422:424]
        S1['temp_l2']= PercentValueCustomScale(Bits('0x' + icol[424:426]).uint, -55, 125, -55, 125)
        S1['temp_h2'] = PercentValueCustomScale(Bits('0x' + icol[426:428]).uint, -55, 125, -55, 125)
        
        S1['def_drv3'] = '0x'+ icol[428:430]
        S1['stare_drv3'] = '0x' + icol[430:432]
        S1['temp_l3'] = PercentValueCustomScale(Bits('0x' + icol[432:434]).uint, -55, 125, -55, 125)
        S1['temp_h3'] = PercentValueCustomScale(Bits('0x' + icol[434:436]).uint, -55, 125, -55, 125)
        
        S1['def_drv4'] = '0x'+ icol[436:438]
        S1['stare_drv4'] = '0x' + icol[438:440]
        S1['temp_l4'] = PercentValueCustomScale(Bits('0x' + icol[440:442]).uint, -55, 125, -55, 125)
        S1['temp_h4'] = PercentValueCustomScale(Bits('0x' + icol[442:444]).uint, -55, 125, -55, 125)
        
        S1['def_drv5'] = '0x'+ icol[444:446]
        S1['stare_drv5'] = '0x' + icol[446:448]
        S1['temp_l5'] = PercentValueCustomScale(Bits('0x' + icol[448:450]).uint, -55, 125, -55, 125)
        S1['temp_h5'] = PercentValueCustomScale(Bits('0x' + icol[450:452]).uint, -55, 125, -55, 125)
        
        S1['def_drv6'] = '0x'+ icol[452:454]
        S1['stare_drv6'] = '0x' + icol[454:456]
        S1['temp_l6'] = PercentValueCustomScale(Bits('0x' + icol[456:458]).uint, -55, 125, -55, 125)
        S1['temp_h6'] = PercentValueCustomScale(Bits('0x' + icol[458:460]).uint, -55, 125, -55, 125)
        
        S1['u_drv'] = '0x'+ icol[460:462]
        S1['dsp_drv'] = '0x'+ icol[462:464]
        S1['trip14'] = '0x'+ icol[464:466]
        S1['trip56'] = '0x'+ icol[466:468]
        S1['stare_mm'] = '0x'+ icol[468:470]
        S1['inp_63'] = '0x'+ icol[470:472]
        S1['defect_can_drv'] = '0x'+ icol[472:474]
        S1['rez_mm1'] = '0x'+ icol[474:476]
        S1['temp_mt2'] =  PercentValueCustomScale(Bits('0x' + icol[476:478]).uint, 0, 255, -50, 205)
        S1['temp_mt1'] =  PercentValueCustomScale(Bits('0x' + icol[478:480]).uint, 0, 255, -50, 205)
        S1['nivel_apa'] =  PercentValueCustomScale(Bits('0x' + icol[480:482]).uint, 0, 255, -50, 205)
        S1['temp_mt3'] =  PercentValueCustomScale(Bits('0x' + icol[482:484]).uint, 0, 255, -50, 205)
        S1['temp_apa_r'] =  PercentValueCustomScale(Bits('0x' + icol[484:486]).uint, 41, 204, 0, 100)
        S1['temp_apa_c'] =  PercentValueCustomScale(Bits('0x' + icol[486:488]).uint, 41, 204, 0, 100)
        
        S1['pres_aer_rad'] =  PercentValueCustomScale(Bits('0x' + icol[488:490]).uint, 13, 204, 0, 50)
        S1['pres_apa'] =  PercentValueCustomScale(Bits('0x' + icol[490:492]).uint, 41, 204, 0, 2.5)
        S1['temp_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[492:494]).uint, 0, 255, 0, 100)
        S1['pres_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[494:496]).uint, 51, 204, 0, 300)
        S1['rez_mm3'] =  '0x' + icol[496:498]
        S1['umid_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[498:500]).uint, 51, 125, 0, 100)
        S1['vibr_Y'] =  PercentValueCustomScale(Bits('0x' + icol[500:502]).uint, 0, 101, 0, 10)
        S1['vibr_X'] =  PercentValueCustomScale(Bits('0x' + icol[502:504]).uint, 0, 101, 0, 10)
        s1_imp_ls =  Bits('0x' + icol[504:506]).bin
        s1_imp_ms =  Bits('0x' + icol[506:508]).bin
        S1['imp'] =  PercentValueCustomScale(BitArray(bin = s1_imp_ms + s1_imp_ls).uint, 0,20460, 0, 100000) 
        
        
        zi =  icol[396:398]
        luna = icol[398:400]
        an =  icol[400:402]
        Lente0['data'] =  zi + '-' + luna + '-' + an
        p_cat_ls = Bits('0x' + icol[402:404]).bin
        p_cat_ms = Bits('0x' + icol[404:406]).bin
        
        Lente0['p_cat'] = PercentValueCustomScale(BitArray(bin = p_cat_ms + p_cat_ls).uint, 0,32767, 0, 49150) 
        
        p_sa_ls = Bits('0x' + icol[406:408]).bin
        p_sa_ms = Bits('0x' + icol[408:410]).bin
        Lente0['p_sa'] = PercentValueCustomScale(BitArray(bin = p_sa_ms + p_sa_ls).uint, 0,32767, 0, 49150) 
        
        temp_trafo = Bits('0x' + icol[410:412]).uint
        Lente0['temp_trafo'] = PercentValueCustomScale(Bits('0x' + icol[370:372]).uint, 26,134, -50, 100) 
        
    elif identificator =='01':
        S2['def_drv1'] = '0x'+ icol[412:414]
        S2['stare_drv1'] = '0x' + icol[414:416]
        S2['temp_l1'] = PercentValueCustomScale(Bits('0x' + icol[416:418]).uint, -55, 125, -55, 125)
        S2['temp_h1'] = PercentValueCustomScale(Bits('0x' + icol[418:420]).uint, -55, 125, -55, 125)
        
        S2['def_drv2'] = '0x'+ icol[420:422]
        S2['stare_drv2'] = '0x' + icol[422:424]
        S2['temp_l2']= PercentValueCustomScale(Bits('0x' + icol[424:426]).uint, -55, 125, -55, 125)
        S2['temp_h2'] = PercentValueCustomScale(Bits('0x' + icol[426:428]).uint, -55, 125, -55, 125)
        
        S2['def_drv3'] = '0x'+ icol[428:430]
        S2['stare_drv3'] = '0x' + icol[430:432]
        S2['temp_l3'] = PercentValueCustomScale(Bits('0x' + icol[432:434]).uint, -55, 125, -55, 125)
        S2['temp_h3'] = PercentValueCustomScale(Bits('0x' + icol[434:436]).uint, -55, 125, -55, 125)
        
        S2['def_drv4'] = '0x'+ icol[436:438]
        S2['stare_drv4'] = '0x' + icol[438:440]
        S2['temp_l4'] = PercentValueCustomScale(Bits('0x' + icol[440:442]).uint, -55, 125, -55, 125)
        S2['temp_h4'] = PercentValueCustomScale(Bits('0x' + icol[442:444]).uint, -55, 125, -55, 125)
        
        S2['def_drv5'] = '0x'+ icol[444:446]
        S2['stare_drv5'] = '0x' + icol[446:448]
        S2['temp_l5'] = PercentValueCustomScale(Bits('0x' + icol[448:450]).uint, -55, 125, -55, 125)
        S2['temp_h5'] = PercentValueCustomScale(Bits('0x' + icol[450:452]).uint, -55, 125, -55, 125)
        
        S2['def_drv6'] = '0x'+ icol[452:454]
        S2['stare_drv6'] = '0x' + icol[454:456]
        S2['temp_l6'] = PercentValueCustomScale(Bits('0x' + icol[456:458]).uint, -55, 125, -55, 125)
        S2['temp_h6'] = PercentValueCustomScale(Bits('0x' + icol[458:460]).uint, -55, 125, -55, 125)
        
        S2['u_drv'] = '0x'+ icol[460:462]
        S2['dsp_drv'] = '0x'+ icol[462:464]
        S2['trip14'] = '0x'+ icol[464:466]
        S2['trip56'] = '0x'+ icol[466:468]
        S2['stare_mm'] = '0x'+ icol[468:470]
        S2['inp_63'] = '0x'+ icol[470:472]
        S2['defect_can_drv'] = '0x'+ icol[472:474]
        S2['rez_mm1'] = '0x'+ icol[474:476]
        S2['temp_mt2'] =  PercentValueCustomScale(Bits('0x' + icol[476:478]).uint, 0, 255, -50, 205)
        S2['temp_mt1'] =  PercentValueCustomScale(Bits('0x' + icol[478:480]).uint, 0, 255, -50, 205)
        S2['nivel_apa'] =  PercentValueCustomScale(Bits('0x' + icol[480:482]).uint, 0, 255, -50, 205)
        S2['temp_mt3'] =  PercentValueCustomScale(Bits('0x' + icol[482:484]).uint, 0, 255, -50, 205)
        S2['temp_apa_r'] =  PercentValueCustomScale(Bits('0x' + icol[484:486]).uint, 41, 204, 0, 100)
        S2['temp_apa_c'] =  PercentValueCustomScale(Bits('0x' + icol[486:488]).uint, 41, 204, 0, 100)
        
        S2['pres_aer_rad'] =  PercentValueCustomScale(Bits('0x' + icol[488:490]).uint, 13, 204, 0, 50)
        S2['pres_apa'] =  PercentValueCustomScale(Bits('0x' + icol[490:492]).uint, 41, 204, 0, 2.5)
        S2['temp_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[492:494]).uint, 0, 255, 0, 100)
        S2['pres_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[494:496]).uint, 51, 204, 0, 300)
        S2['rez_mm3'] =  '0x' + icol[496:498]
        S2['umid_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[498:500]).uint, 51, 125, 0, 100)
        S2['vibr_Y'] =  PercentValueCustomScale(Bits('0x' + icol[500:502]).uint, 0, 101, 0, 10)
        S2['vibr_X'] =  PercentValueCustomScale(Bits('0x' + icol[502:504]).uint, 0, 101, 0, 10)
        S2_imp_ls =  Bits('0x' + icol[504:506]).bin
        S2_imp_ms =  Bits('0x' + icol[506:508]).bin
        S2_imp =  PercentValueCustomScale(BitArray(bin = S2_imp_ms + S2_imp_ls).uint, 0,20460, 0, 100000) 
        
        
        Lente1['mansa1_numerice'] = '0x' + icol[396:398]
        Lente1['mansa1_forta'] = '0x' + icol[398:400]
        Lente1['mansa1_viteza'] = PercentValueCustomScale(Bits('0x' + icol[400:402]).uint, 0, 255, 0, 255)
        Lente1['mansa2_numerice'] = '0x' + icol[402:404]
        Lente1['mansa2_forta'] = '0x' + icol[404:406]
        Lente1['mansa2_viteza'] = PercentValueCustomScale(Bits('0x' + icol[406:408]).uint, 0, 255, 0, 255)
        
        
        
        

    elif identificator =='02':
        S3['def_drv1'] = '0x'+ icol[412:414]
        S3['stare_drv1'] = '0x' + icol[414:416]
        S3['temp_l1'] = PercentValueCustomScale(Bits('0x' + icol[416:418]).uint, -55, 125, -55, 125)
        S3['temp_h1'] = PercentValueCustomScale(Bits('0x' + icol[418:420]).uint, -55, 125, -55, 125)
        
        S3['def_drv2'] = '0x'+ icol[420:422]
        S3['stare_drv2'] = '0x' + icol[422:424]
        S3['temp_l2']= PercentValueCustomScale(Bits('0x' + icol[424:426]).uint, -55, 125, -55, 125)
        S3['temp_h2'] = PercentValueCustomScale(Bits('0x' + icol[426:428]).uint, -55, 125, -55, 125)
        
        S3['def_drv3'] = '0x'+ icol[428:430]
        S3['stare_drv3'] = '0x' + icol[430:432]
        S3['temp_l3'] = PercentValueCustomScale(Bits('0x' + icol[432:434]).uint, -55, 125, -55, 125)
        S3['temp_h3'] = PercentValueCustomScale(Bits('0x' + icol[434:436]).uint, -55, 125, -55, 125)
        
        S3['def_drv4'] = '0x'+ icol[436:438]
        S3['stare_drv4'] = '0x' + icol[438:440]
        S3['temp_l4'] = PercentValueCustomScale(Bits('0x' + icol[440:442]).uint, -55, 125, -55, 125)
        S3['temp_h4'] = PercentValueCustomScale(Bits('0x' + icol[442:444]).uint, -55, 125, -55, 125)
        
        S3['def_drv5'] = '0x'+ icol[444:446]
        S3['stare_drv5'] = '0x' + icol[446:448]
        S3['temp_l5'] = PercentValueCustomScale(Bits('0x' + icol[448:450]).uint, -55, 125, -55, 125)
        S3['temp_h5'] = PercentValueCustomScale(Bits('0x' + icol[450:452]).uint, -55, 125, -55, 125)
        
        S3['def_drv6'] = '0x'+ icol[452:454]
        S3['stare_drv6'] = '0x' + icol[454:456]
        S3['temp_l6'] = PercentValueCustomScale(Bits('0x' + icol[456:458]).uint, -55, 125, -55, 125)
        S3['temp_h6'] = PercentValueCustomScale(Bits('0x' + icol[458:460]).uint, -55, 125, -55, 125)
        S3['u_drv'] = '0x'+ icol[460:462]
        S3['dsp_drv'] = '0x'+ icol[462:464]
        S3['trip14'] = '0x'+ icol[464:466]
        S3['trip56'] = '0x'+ icol[466:468]
        S3['stare_mm'] = '0x'+ icol[468:470]
        S3['inp_63'] = '0x'+ icol[470:472]
        S3['defect_can_drv'] = '0x'+ icol[472:474]
        S3['rez_mm1'] = '0x'+ icol[474:476]
        S3['temp_mt2'] =  PercentValueCustomScale(Bits('0x' + icol[476:478]).uint, 0, 255, -50, 205)
        S3['temp_mt1'] =  PercentValueCustomScale(Bits('0x' + icol[478:480]).uint, 0, 255, -50, 205)
        S3['nivel_apa'] =  PercentValueCustomScale(Bits('0x' + icol[480:482]).uint, 0, 255, -50, 205)
        S3['temp_mt3'] =  PercentValueCustomScale(Bits('0x' + icol[482:484]).uint, 0, 255, -50, 205)
        S3['temp_apa_r'] =  PercentValueCustomScale(Bits('0x' + icol[484:486]).uint, 41, 204, 0, 100)
        S3['temp_apa_c'] =  PercentValueCustomScale(Bits('0x' + icol[486:488]).uint, 41, 204, 0, 100)
        
        S3['pres_aer_rad'] =  PercentValueCustomScale(Bits('0x' + icol[488:490]).uint, 13, 204, 0, 50)
        S3['pres_apa'] =  PercentValueCustomScale(Bits('0x' + icol[490:492]).uint, 41, 204, 0, 2.5)
        S3['temp_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[492:494]).uint, 0, 255, 0, 100)
        S3['pres_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[494:496]).uint, 51, 204, 0, 300)
        S3['rez_mm3'] =  '0x' + icol[496:498]
        S3['umid_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[498:500]).uint, 51, 125, 0, 100)
        S3['vibr_Y'] =  PercentValueCustomScale(Bits('0x' + icol[500:502]).uint, 0, 101, 0, 10)
        S3['vibr_X'] =  PercentValueCustomScale(Bits('0x' + icol[502:504]).uint, 0, 101, 0, 10)
        S3_imp_ls =  Bits('0x' + icol[504:506]).bin
        S3_imp_ms =  Bits('0x' + icol[506:508]).bin
        S3_imp =  PercentValueCustomScale(BitArray(bin = S3_imp_ms + S3_imp_ls).uint, 0,20460, 0, 100000)
        
        
        Lente2['defect0'] =  '0x' + icol[396:398]
        Lente2['defect1'] =  '0x' + icol[398:400]
        Lente2['defect2'] =  '0x' + icol[400:402]
        Lente2['defect3'] =  '0x' + icol[402:404]
        Lente2['defect4'] =  '0x' + icol[404:406]
        Lente2['defect5'] =  '0x' + icol[406:408]
        Lente2['defect7'] =  '0x' + icol[408:410]
        
        

    elif identificator =='03':
        S4['def_drv1'] = '0x'+ icol[412:414]
        S4['stare_drv1'] = '0x' + icol[414:416]
        S4['temp_l1'] = PercentValueCustomScale(Bits('0x' + icol[416:418]).uint, -55, 125, -55, 125)
        S4['temp_h1'] = PercentValueCustomScale(Bits('0x' + icol[418:420]).uint, -55, 125, -55, 125)
        
        S4['def_drv2'] = '0x'+ icol[420:422]
        S4['stare_drv2'] = '0x' + icol[422:424]
        S4['temp_l2']= PercentValueCustomScale(Bits('0x' + icol[424:426]).uint, -55, 125, -55, 125)
        S4['temp_h2'] = PercentValueCustomScale(Bits('0x' + icol[426:428]).uint, -55, 125, -55, 125)
        
        S4['def_drv3'] = '0x'+ icol[428:430]
        S4['stare_drv3'] = '0x' + icol[430:432]
        S4['temp_l3'] = PercentValueCustomScale(Bits('0x' + icol[432:434]).uint, -55, 125, -55, 125)
        S4['temp_h3'] = PercentValueCustomScale(Bits('0x' + icol[434:436]).uint, -55, 125, -55, 125)
        
        S4['def_drv4'] = '0x'+ icol[436:438]
        S4['stare_drv4'] = '0x' + icol[438:440]
        S4['temp_l4'] = PercentValueCustomScale(Bits('0x' + icol[440:442]).uint, -55, 125, -55, 125)
        S4['temp_h4'] = PercentValueCustomScale(Bits('0x' + icol[442:444]).uint, -55, 125, -55, 125)
        
        S4['def_drv5'] = '0x'+ icol[444:446]
        S4['stare_drv5'] = '0x' + icol[446:448]
        S4['temp_l5'] = PercentValueCustomScale(Bits('0x' + icol[448:450]).uint, -55, 125, -55, 125)
        S4['temp_h5'] = PercentValueCustomScale(Bits('0x' + icol[450:452]).uint, -55, 125, -55, 125)
        
        S4['def_drv6'] = '0x'+ icol[452:454]
        S4['stare_drv6'] = '0x' + icol[454:456]
        S4['temp_l6'] = PercentValueCustomScale(Bits('0x' + icol[456:458]).uint, -55, 125, -55, 125)
        S4['temp_h6'] = PercentValueCustomScale(Bits('0x' + icol[458:460]).uint, -55, 125, -55, 125)

        S4['u_drv'] = '0x'+ icol[460:462]
        S4['dsp_drv'] = '0x'+ icol[462:464]
        S4['trip14'] = '0x'+ icol[464:466]
        S4['trip56'] = '0x'+ icol[466:468]
        S4['stare_mm'] = '0x'+ icol[468:470]
        S4['inp_63'] = '0x'+ icol[470:472]
        S4['defect_can_drv'] = '0x'+ icol[472:474]
        S4['rez_mm1'] = '0x'+ icol[474:476]
        S4['temp_mt2'] =  PercentValueCustomScale(Bits('0x' + icol[476:478]).uint, 0, 255, -50, 205)
        S4['temp_mt1'] =  PercentValueCustomScale(Bits('0x' + icol[478:480]).uint, 0, 255, -50, 205)
        S4['nivel_apa'] =  PercentValueCustomScale(Bits('0x' + icol[480:482]).uint, 0, 255, -50, 205)
        S4['temp_mt3'] =  PercentValueCustomScale(Bits('0x' + icol[482:484]).uint, 0, 255, -50, 205)
        S4['temp_apa_r'] =  PercentValueCustomScale(Bits('0x' + icol[484:486]).uint, 41, 204, 0, 100)
        S4['temp_apa_c'] =  PercentValueCustomScale(Bits('0x' + icol[486:488]).uint, 41, 204, 0, 100)
        
        S4['pres_aer_rad'] =  PercentValueCustomScale(Bits('0x' + icol[488:490]).uint, 13, 204, 0, 50)
        S4['pres_apa'] =  PercentValueCustomScale(Bits('0x' + icol[490:492]).uint, 41, 204, 0, 2.5)
        S4['temp_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[492:494]).uint, 0, 255, 0, 100)
        S4['pres_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[494:496]).uint, 51, 204, 0, 300)
        S4['rez_mm3'] =  '0x' + icol[496:498]
        S4['umid_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[498:500]).uint, 51, 125, 0, 100)
        S4['vibr_Y'] =  PercentValueCustomScale(Bits('0x' + icol[500:502]).uint, 0, 101, 0, 10)
        S4['vibr_X'] =  PercentValueCustomScale(Bits('0x' + icol[502:504]).uint, 0, 101, 0, 10)
        S4_imp_ls =  Bits('0x' + icol[504:506]).bin
        S4_imp_ms =  Bits('0x' + icol[506:508]).bin
        S4_imp =  PercentValueCustomScale(BitArray(bin = S4_imp_ms + S4_imp_ls).uint, 0,20460, 0, 100000)
        
        Lente3['defect8'] =  '0x' + icol[396:398]
        Lente3['defect9'] =  '0x' + icol[398:400]
        Lente3['defect10'] =  '0x' + icol[400:402]
        Lente3['defect11'] =  '0x' + icol[402:404]
        Lente3['defect12'] =  '0x' + icol[404:406]
        Lente3['defect13'] =  '0x' + icol[406:408]
        Lente3['defect14'] =  '0x' + icol[408:410]
        Lente3['defect15'] =  '0x' + icol[410:412]

    elif identificator =='04':
        S5['def_drv1'] = '0x'+ icol[412:414]
        S5['stare_drv1'] = '0x' + icol[414:416]
        S5['temp_l1'] = PercentValueCustomScale(Bits('0x' + icol[416:418]).uint, -55, 125, -55, 125)
        S5['temp_h1'] = PercentValueCustomScale(Bits('0x' + icol[418:420]).uint, -55, 125, -55, 125)
        
        S5['def_drv2'] = '0x'+ icol[420:422]
        S5['stare_drv2'] = '0x' + icol[422:424]
        S5['temp_l2']= PercentValueCustomScale(Bits('0x' + icol[424:426]).uint, -55, 125, -55, 125)
        S5['temp_h2'] = PercentValueCustomScale(Bits('0x' + icol[426:428]).uint, -55, 125, -55, 125)
        
        S5['def_drv3'] = '0x'+ icol[428:430]
        S5['stare_drv3'] = '0x' + icol[430:432]
        S5['temp_l3'] = PercentValueCustomScale(Bits('0x' + icol[432:434]).uint, -55, 125, -55, 125)
        S5['temp_h3'] = PercentValueCustomScale(Bits('0x' + icol[434:436]).uint, -55, 125, -55, 125)
        
        S5['def_drv4'] = '0x'+ icol[436:438]
        S5['stare_drv4'] = '0x' + icol[438:440]
        S5['temp_l4'] = PercentValueCustomScale(Bits('0x' + icol[440:442]).uint, -55, 125, -55, 125)
        S5['temp_h4'] = PercentValueCustomScale(Bits('0x' + icol[442:444]).uint, -55, 125, -55, 125)
        
        S5['def_drv5'] = '0x'+ icol[444:446]
        S5['stare_drv5'] = '0x' + icol[446:448]
        S5['temp_l5'] = PercentValueCustomScale(Bits('0x' + icol[448:450]).uint, -55, 125, -55, 125)
        S5['temp_h5'] = PercentValueCustomScale(Bits('0x' + icol[450:452]).uint, -55, 125, -55, 125)
        
        S5['def_drv6'] = '0x'+ icol[452:454]
        S5['stare_drv6'] = '0x' + icol[454:456]
        S5['temp_l6'] = PercentValueCustomScale(Bits('0x' + icol[456:458]).uint, -55, 125, -55, 125)
        S5['temp_h6'] = PercentValueCustomScale(Bits('0x' + icol[458:460]).uint, -55, 125, -55, 125)

        S5['u_drv'] = '0x'+ icol[460:462]
        S5['dsp_drv'] = '0x'+ icol[462:464]
        S5['trip14'] = '0x'+ icol[464:466]
        S5['trip56'] = '0x'+ icol[466:468]
        S5['stare_mm'] = '0x'+ icol[468:470]
        S5['inp_63'] = '0x'+ icol[470:472]
        S5['defect_can_drv'] = '0x'+ icol[472:474]
        S5['rez_mm1'] = '0x'+ icol[474:476]
        S5['temp_mt2'] =  PercentValueCustomScale(Bits('0x' + icol[476:478]).uint, 0, 255, -50, 205)
        S5['temp_mt1'] =  PercentValueCustomScale(Bits('0x' + icol[478:480]).uint, 0, 255, -50, 205)
        S5['nivel_apa'] =  PercentValueCustomScale(Bits('0x' + icol[480:482]).uint, 0, 255, -50, 205)
        S5['temp_mt3'] =  PercentValueCustomScale(Bits('0x' + icol[482:484]).uint, 0, 255, -50, 205)
        S5['temp_apa_r'] =  PercentValueCustomScale(Bits('0x' + icol[484:486]).uint, 41, 204, 0, 100)
        S5['temp_apa_c'] =  PercentValueCustomScale(Bits('0x' + icol[486:488]).uint, 41, 204, 0, 100)
        
        S5['pres_aer_rad'] =  PercentValueCustomScale(Bits('0x' + icol[488:490]).uint, 13, 204, 0, 50)
        S5['pres_apa'] =  PercentValueCustomScale(Bits('0x' + icol[490:492]).uint, 41, 204, 0, 2.5)
        S5['temp_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[492:494]).uint, 0, 255, 0, 100)
        S5['pres_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[494:496]).uint, 51, 204, 0, 300)
        S5['rez_mm3'] =  '0x' + icol[496:498]
        S5['umid_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[498:500]).uint, 51, 125, 0, 100)
        S5['vibr_Y'] =  PercentValueCustomScale(Bits('0x' + icol[500:502]).uint, 0, 101, 0, 10)
        S5['vibr_X'] =  PercentValueCustomScale(Bits('0x' + icol[502:504]).uint, 0, 101, 0, 10)
        S5_imp_ls =  Bits('0x' + icol[504:506]).bin
        S5_imp_ms =  Bits('0x' + icol[506:508]).bin
        S5_imp =  PercentValueCustomScale(BitArray(bin = S5_imp_ms + S5_imp_ls).uint, 0,20460, 0, 100000)
        
        Lente4['defect16'] =  '0x' + icol[396:398]
        Lente4['defect17'] =  '0x' + icol[398:400]
        Lente4['defect18'] =  '0x' + icol[400:402]
        Lente4['defect19'] =  '0x' + icol[402:404]
        Lente4['defect20'] =  '0x' + icol[404:406]
        Lente4['defect21'] =  '0x' + icol[406:408]
        Lente4['defect22'] =  '0x' + icol[408:410] 
        Lente4['defect23'] =  '0x' + icol[410:412]

    elif identificator =='05':
        S6['def_drv1'] = '0x'+ icol[412:414]
        S6['stare_drv1'] = '0x' + icol[414:416]
        S6['temp_l1'] = PercentValueCustomScale(Bits('0x' + icol[416:418]).uint, -55, 125, -55, 125)
        S6['temp_h1'] = PercentValueCustomScale(Bits('0x' + icol[418:420]).uint, -55, 125, -55, 125)
        
        S6['def_drv2'] = '0x'+ icol[420:422]
        S6['stare_drv2'] = '0x' + icol[422:424]
        S6['temp_l2']= PercentValueCustomScale(Bits('0x' + icol[424:426]).uint, -55, 125, -55, 125)
        S6['temp_h2'] = PercentValueCustomScale(Bits('0x' + icol[426:428]).uint, -55, 125, -55, 125)
        
        S6['def_drv3'] = '0x'+ icol[428:430]
        S6['stare_drv3'] = '0x' + icol[430:432]
        S6['temp_l3'] = PercentValueCustomScale(Bits('0x' + icol[432:434]).uint, -55, 125, -55, 125)
        S6['temp_h3'] = PercentValueCustomScale(Bits('0x' + icol[434:436]).uint, -55, 125, -55, 125)
        
        S6['def_drv4'] = '0x'+ icol[436:438]
        S6['stare_drv4'] = '0x' + icol[438:440]
        S6['temp_l4'] = PercentValueCustomScale(Bits('0x' + icol[440:442]).uint, -55, 125, -55, 125)
        S6['temp_h4'] = PercentValueCustomScale(Bits('0x' + icol[442:444]).uint, -55, 125, -55, 125)
        
        S6['def_drv5'] = '0x'+ icol[444:446]
        S6['stare_drv5'] = '0x' + icol[446:448]
        S6['temp_l5'] = PercentValueCustomScale(Bits('0x' + icol[448:450]).uint, -55, 125, -55, 125)
        S6['temp_h5'] = PercentValueCustomScale(Bits('0x' + icol[450:452]).uint, -55, 125, -55, 125)
        
        S6['def_drv6'] = '0x'+ icol[452:454]
        S6['stare_drv6'] = '0x' + icol[454:456]
        S6['temp_l6'] = PercentValueCustomScale(Bits('0x' + icol[456:458]).uint, -55, 125, -55, 125)
        S6['temp_h6'] = PercentValueCustomScale(Bits('0x' + icol[458:460]).uint, -55, 125, -55, 125)
        
        S6['u_drv'] = '0x'+ icol[460:462]
        S6['dsp_drv'] = '0x'+ icol[462:464]
        S6['trip14'] = '0x'+ icol[464:466]
        S6['trip56'] = '0x'+ icol[466:468]
        S6['stare_mm'] = '0x'+ icol[468:470]
        S6['inp_63'] = '0x'+ icol[470:472]
        S6['defect_can_drv'] = '0x'+ icol[472:474]
        S6['rez_mm1'] = '0x'+ icol[474:476]
        S6['temp_mt2'] =  PercentValueCustomScale(Bits('0x' + icol[476:478]).uint, 0, 255, -50, 205)
        S6['temp_mt1'] =  PercentValueCustomScale(Bits('0x' + icol[478:480]).uint, 0, 255, -50, 205)
        S6['nivel_apa'] =  PercentValueCustomScale(Bits('0x' + icol[480:482]).uint, 0, 255, -50, 205)
        S6['temp_mt3'] =  PercentValueCustomScale(Bits('0x' + icol[482:484]).uint, 0, 255, -50, 205)
        S6['temp_apa_r'] =  PercentValueCustomScale(Bits('0x' + icol[484:486]).uint, 41, 204, 0, 100)
        S6['temp_apa_c'] =  PercentValueCustomScale(Bits('0x' + icol[486:488]).uint, 41, 204, 0, 100)
        
        S6['pres_aer_rad'] =  PercentValueCustomScale(Bits('0x' + icol[488:490]).uint, 13, 204, 0, 50)
        S6['pres_apa'] =  PercentValueCustomScale(Bits('0x' + icol[490:492]).uint, 41, 204, 0, 2.5)
        S6['temp_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[492:494]).uint, 0, 255, 0, 100)
        S6['pres_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[494:496]).uint, 51, 204, 0, 300)
        S6['rez_mm3'] =  '0x' + icol[496:498]
        S6['umid_aer_mt'] =  PercentValueCustomScale(Bits('0x' + icol[498:500]).uint, 51, 125, 0, 100)
        S6['vibr_Y'] =  PercentValueCustomScale(Bits('0x' + icol[500:502]).uint, 0, 101, 0, 10)
        S6['vibr_X'] =  PercentValueCustomScale(Bits('0x' + icol[502:504]).uint, 0, 101, 0, 10)
        S6_imp_ls =  Bits('0x' + icol[504:506]).bin
        S6_imp_ms =  Bits('0x' + icol[506:508]).bin
        S6_imp =  PercentValueCustomScale(BitArray(bin = S6_imp_ms + S6_imp_ls).uint, 0,20460, 0, 100000)
        
        Lente5['rezerva'] =  '0x' + icol[396:398]
        Lente5['rezerva'] =  '0x' + icol[398:400]
        Lente5['rezerva'] =  '0x' + icol[400:402]
        Lente5['rezerva'] =  '0x' + icol[402:404]
        Lente5['rezerva'] =  '0x' + icol[404:406]
        Lente5['rezerva'] =  '0x' + icol[406:408]
        Lente5['rezerva'] =  '0x' + icol[408:410] 
        Lente5['rezerva'] =  '0x' + icol[410:412] 
         
        
        