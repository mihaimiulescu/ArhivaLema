import csv
import json

class Point:
    pass



list_of_Points = []
locomotive = []



with open('/home/mihai/ArhivaDateLema/somedata/temp/temp_Mt1_Panda_Std_Report.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader, None)
    f = lambda x : locomotive.index(x)

    
    for row in spamreader:

        p = Point()
        if spamreader.line_num % 8 == 2:# locomotiva noua
            means = []
            counts = []
            stds = []
            maxs = []
            mins = []
            locomotiva = row[0]
            if locomotiva not in locomotive:
                locomotive.append(locomotiva)
                
            p.x = f(locomotiva)

            for i in xrange(2, len(row)):
                counts.append(row[i])
        elif  spamreader.line_num % 8 == 3:

            locomotiva = row[0]
            for i in xrange(2, len(row)):
                means.append(row[i])
                
        elif  spamreader.line_num % 8 == 4:
            locomotiva = row[0]
            for i in xrange(2, len(row)):
                stds.append(row[i])
        
        elif  spamreader.line_num % 8 == 5:
            locomotiva = row[0]
            for i in xrange(2, len(row)):
                mins.append(row[i])
                
        elif  spamreader.line_num % 8 == 1:
            #construct de points
            for i in xrange(2, len(row)):
                maxs.append(row[i])
            
            locomotiva = row[0]
            if locomotiva not in locomotive:
                locomotive.append(locomotiva)
            x = len(locomotive) - 1 # indicele pe harts incepe de la 0
            for cnt in xrange(len(stds)):
                p = Point()
                p.x = x
                p.y = cnt
                p.value = means[cnt][:6]
                p.counter = counts[cnt][:1]
                p.std = stds[cnt][:4]
                p.min = mins[cnt][:5]
                p.max = maxs[cnt][:5]
                p.locomotiva = locomotiva
                list_of_Points.append(p)
for point in list_of_Points:
    print point.x, point.y, point.counter, point.std, point.value, point.locomotiva, point.min, point.max
json_string = json.dumps([ob.__dict__ for ob in list_of_Points])


with open('/home/mihai/ArhivaDateLema/somedata/temp/temp_Mt1_Panda_Std_Report.json', 'wb') as jsonfile:
    jsonfile.write(json_string)
            
            

                
 
            

                    

        

    
            
            
            
        
                

            
            
            
            
             

        
        
        