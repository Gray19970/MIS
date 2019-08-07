import json


adict_information={}
adict_stuid={  }      #用id作为开头的列表



def use_input():                        #用户录入学生信息
    adict_information = {}
    adict_stuid = {}
    cho=True
    while cho:

        id=input('请输入ID:')
        if not id.isdigit():
            print('你输入的不是数字')

            continue

        id=int(id)

        name=input('请输入名字:')
        adict_information.setdefault('名字',name)


        english=input('输入英语成绩:')
        if not english.isdigit():
            print('你输入的不是数字')

            continue
        else:
            english = int(english)

            adict_information.setdefault('英语成绩', english)

        python=input('请输入python成绩:')
        if not python.isdigit():
            print('你输入的不是数字')

            continue
        else:
            python = int(python)

            adict_information.setdefault('python成绩', python)

        cplus=input('请输入C语言成绩:')

        if not cplus.isdigit():
            print('你输入的不是数字')

            continue
        else:
            cplus = int(cplus)

            adict_information.setdefault('c语言成绩', cplus)

        sum_l=cplus+python+english
        adict_information.setdefault('总成绩',sum_l)
        adict_stuid.setdefault(id, adict_information)




        choice_l=input('是否继续添加？（y/n）:')
        if choice_l=='n':
            print(adict_stuid)
            with open('haha.json','w',encoding='utf-8') as f :
                json.dump(adict_stuid,f)


            break
        elif choice_l=='y' :
            adict_information = {}
            continue
        else:
            print('你别乱按！！！')
            continue



def use_get():
    with open('haha.json','r') as f:
        adict_stuid=json.load(f)
        print(adict_stuid)


    fblit_l=True
    while fblit_l:

        get_choice=input('按ID查找输入1；按姓名查找输入2：')

        if not get_choice.isdigit():
            print('请输入数字')
            continue

        if get_choice == '1':
          while True:
                stu_id=input('请输入学生ID:')
                if not stu_id.isdigit():
                   print('你输入的不是id格式')
                   continue



                if stu_id  in  adict_stuid.keys():

                    for i in adict_stuid[stu_id].keys():
                        print('{:>8}'.format(i),end='  ')
                    print('\n')
                    for i in adict_stuid[stu_id].values():
                        print('{:>8}'.format(i), end='  ')
                    fblit_l=False
                    break
                else:
                    print('(o@.@o) 无数据信息 (o@.@o)')
                    fblit_l = False
                    break


        if get_choice == '2':
            fblit_l = True

            while fblit_l:
                flog=0
                name = input('请输入学生姓名:')

                for i in adict_stuid.values():    #判断名字在不在
                    flog+=1
                    if name==i.get('名字'):
                      for j in i.keys():
                          print('{:*^8}'.format(j), end='  ')
                      print('\n')
                      for k in i.values():
                          print('{:*^8}'.format(k), end='  ')

                      fblit_l = False
                      break

                    if flog==len(adict_stuid.values()):
                        print('(o@.@o) 无数据信息 (o@.@o)')
                    else:
                        continue






def use_remove():                #用户删除学生信息
    with open('haha.json','r') as f:
        adict_stuid=json.load(f)

    choice_l=input('请输入要删除的学生ID:')

    del  adict_stuid[choice_l]
    print('ID为%s的学生信息已经被删除。。。'%choice_l)
    print(adict_stuid)
    with open('haha.json','w') as f:
        json.dump(adict_stuid, f)



def use_correct():                            #用户修改信息
    with open('haha.json','r') as f:
        adict_stuid=json.load(f)
        print(adict_stuid)
           #读出字典

    adict_information = {}                     #建立一个字典用来存用户的信息
    while True:
        stu_id = input('请输入学生ID:')
        if not stu_id.isdigit():
            print('你输入的不是id格式')
            continue

        if stu_id in adict_stuid.keys():         #如果id在字典里





            name = input('请输入名字:')
            adict_information.setdefault('名字', name)            #更新姓名

            english = input('输入英语成绩:')
            if not english.isdigit():
                print('你输入的不是数字')

                adict_information.clear()
                continue
            else:
                english = int(english)

                adict_information.setdefault('英语成绩', english)  #更新英语成绩

            python = input('请输入python成绩:')
            if not python.isdigit():
                print('你输入的不是数字')
                adict_information.clear()
                continue
            else:
                python = int(python)

                adict_information.setdefault('python成绩', python)    #更新python成绩

            cplus = input('请输入C语言成绩:')

            if not cplus.isdigit():
                print('你输入的不是数字')
                adict_information.clear()
                continue
            else:
                cplus = int(cplus)

                adict_information.setdefault('c语言成绩', cplus)     #更新c语言成绩
                sum_l = cplus + python + english

                adict_information.setdefault('总成绩', sum_l)
                adict_stuid[stu_id]=adict_information

            print('修改成功')
            choice_l = input('是否继续添加？（y/n）:')
            if choice_l == 'n':
                print(adict_stuid)


                with open('haha.json', 'w', encoding='utf-8') as f:
                    json.dump(adict_stuid, f)
                fblit_l = False
                break
            elif choice_l == 'y':
                continue
            else:
                print('你别乱按！！！')
                continue




        else:
            print('(o@.@o) 无数据信息 (o@.@o)')

            break





def use_sort():                   #用户排序
    gdx=True
    with open('haha.json', 'r') as f:
        adict_stuid = json.load(f)

    print('{:<8}{:<8}{:<8}{:<10}{:<8}{:<8}'.format('ID', '姓名', '英语成绩', 'python成绩', 'c语言成绩', '总成绩'))
    for j in adict_stuid:
        print('{: <8}'.format(j), end=' ')

        for i in adict_stuid[j].values():
            print('{: <8}'.format(i), end='   ')

        print('\n')


    while gdx:



        user_choice1=input   ('请选择排序方式（1 按英语成绩排序，  2 按照python成绩排序，3按照c语言成绩排序，0按总成绩排序）')


        if not user_choice1.isdigit():

            print('请输入数字')

            continue



        user_choice1=int(user_choice1)

        if int(user_choice1)>3  or   int(user_choice1)<0:
            print('你输入的数字不对')
            continue

        else:

            while True:
                list_l = ['总成绩','英语成绩',  'python成绩','c语言成绩']
                user_choice2=input('请选择（0升序，1降序）')




                if not user_choice2.isdigit():

                    print('你输入的不是数字')
                    continue
                elif user_choice2=='0':



                    adict_stuid = sorted(adict_stuid.items(), key=lambda  x: x[1].get(list_l[user_choice1]), reverse=False)
                    print('{:<8}{:<8}{:<8}{:<10}{:<8}{:<8}'.format('ID', '姓名', '英语成绩', 'python成绩', 'c语言成绩', '总成绩'))
                    adict_stuid=dict(adict_stuid)
                    for j in adict_stuid:
                        print('{: <8}'.format(j), end=' ')

                        for i in adict_stuid[j].values():
                            print('{: <8}'.format(i), end='   ')

                        print('\n')




                    gdx=False
                    break
                elif user_choice2=='1':


                    adict_stuid = sorted(adict_stuid.items(), key=lambda x: x[1].get(list_l[user_choice1]), reverse=True)
                    adict_stuid = dict(adict_stuid)
                    for j in adict_stuid:
                        print('{: <8}'.format(j), end=' ')

                        for i in adict_stuid[j].values():
                            print('{: <8}'.format(i), end='   ')

                        print('\n')
                    gdx=False
                    break

                else :

                    print('你的输入有误！重新输入')

                    continue




















def use_sun():                   #用户统计学生总人数
    with open('haha.json','r') as f:
        adict_stuid= json.load(f)

    i=0
    for  j  in adict_stuid:
        i+=1
    print('一共有%d名学生'%i)



def use_inforfind():
    with open('haha.json', 'r') as f:
        adict_stuid = json.load(f)

    print('{:<8}{:<8}{:<8}{:<10}{:<8}{:<8}'.format( 'ID',    '姓名',   '英语成绩' ,  'python成绩',  'c语言成绩',  '总成绩'))
    for j in adict_stuid:
        print('{: <8}'.format(j),  end=' ')

        for i in adict_stuid[j].values():
            print('{: <8}'.format(i), end='   ')

        print('\n')


while True:

    print('''
       ╔———————学生信息管理系统————————╗
       │                                              
       │   ========== 功能菜单 =====  
       │                                              
       │   1 录入学生信息                              
       │   2 查找学生信息                              
       │   3 删除学生信息                                
       │   4 修改学生信息                               
       │   5 排序                                      
       │   6 统计学生总人数                              
       │   7 显示所有学生信息                      
       │   0 退出系统                            
       │  ========================     
       │        
       ╚——————————————————————————————╝
       ''')
    use_choice=input('请选择:')
    if not use_choice.isdigit():
        print('输入错误')

        continue
    use_choice=int(use_choice)
    if use_choice>7 or use_choice<0:
        print('输入错误')
        continue
    if use_choice==1:
        use_input()
    if use_choice==2:
        use_get()
    if use_choice==3:
        use_remove()
    if use_choice==4:
        use_correct()
    if use_choice==5:
        use_sort()
    if use_choice==6:
        use_sun()
    if use_choice==7:

        use_inforfind()
    if use_choice==0:
        exit(0)