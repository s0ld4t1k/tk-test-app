import os
stri=''
def studentData(file):
    student=str(file.decode()).split('/')
    student=student[len(student)-1][:-4]
    res=[]
    print(student.center(30,'*'))
    students.append({"name": student, "id": 1, "info": "info", })
    global stri
    stri+=student.center(30,'*')
    print()
    stri+='\n'
    try:
        with open(file,'rb') as fl:
            for line in fl.readlines():
                ln=line.decode().strip().split(':')
                
                if len(ln)==1 and len(ln[0])>0:
                    lesson=ln[0]
                    res.append([lesson,0,0,0,{}])
                    themes={}
                    themesCor={}
                
                elif len(ln)>1:
                    res[len(res)-1][1]+=1
                    res[len(res)-1][2]+=int(ln[2])
                    res[len(res)-1][3]=(100*res[len(res)-1][2])/res[len(res)-1][1]
                    try:
                        themes[ln[1]]+=1
                        themesCor[ln[1]]+=int(ln[2])
                    except:
                        themes[ln[1]]=1
                        themesCor[ln[1]]=int(ln[2])
                    res[len(res)-1][4][ln[1]]=(100*themesCor[ln[1]])/themes[ln[1]]
                    # print(lesson)
                # print(ln.striip())
    except Exception as e:
        print(f'error  {e}')
    res=sorted(res, key=lambda item: item[3],reverse=True)
    results=[]
    k=0
    # print(res)
    for rs in res:
        k+=1
        rs[4]=sorted(rs[4].items(),key=lambda item: item[1],reverse=False)[0]
        talyp=student
        sapak=rs[0]
        baha=rs[3]
        worst=rs[4][0]
        print(f'{k}.{sapak}',f'{baha}%',worst,sep=' \t ')
        stri+=f'{k}.{sapak} {baha}% {worst}'
        results.append({
            'talyp':talyp,
            'sapak':sapak,
            'baha':baha,
            'worst':worst
        })
    print()
    stri+='\n'
    print(' * ', f'gowy bilyan sapagy {res[0][0]}.')
    print(f'{(res[0][0]).title()} shu dersin shu {res[0][4][0]} temadan yetishiginiz pes, has gowy tayyarlanmagynyzy maslahat beryaris.')
    print(f'{(res[0][0]).title()} shu sapagy siz gowy bilyarsiniz we siz bu sapakdan kamilleship durli ders basleshiklerine hem gatnashyp bilersiniz.')
    print()
    stri+='\n'
    print(' * ', f'erbet bilyan sapagy {res[len(res)-1][0]}.')
    stri+=f'erbet bilyan sapagy {res[len(res)-1][0]}.\n'
    print(f'{(res[len(res)-1][0]).title()} dersinden yetishiginiz pes, shu sapakdan gowy tayyarlyk gormegini we esaslaryny(bazalaryny) owrenmeginizi maslahat beryaris.')
    stri+=f'{(res[len(res)-1][0]).title()} dersinden yetishiginiz pes, shu sapakdan gowy tayyarlyk gormegini we esaslaryny(bazalaryny) owrenmeginizi maslahat beryaris.\n'
    return results

def fetch(dir,stri):
    print()
    stri+='\n'
    for root,_,files in os.walk(dir):
        for file in files:
            file=os.path.join(root, file)
            studentData(file)
            print()
            stri+='\n'
            print(''.center(50,'-'))
            stri+=''.center(50,'-')
            print()
            stri+='\n'
    try:
        with open('./result.html','w')as html:
            html.write(f'''
                    <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Test</title>
                        </head>
                        <body>
                            {stri}
                        </body>
                        </html>
                    ''')
    except:
        print('gen html')
            

dir=b'./test/'
fetch(dir,stri)
